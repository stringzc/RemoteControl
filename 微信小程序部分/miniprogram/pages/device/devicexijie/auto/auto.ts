// 获取应用实例
const app = getApp<IAppOption>()

interface RecordItem {
  startTime: string;
  endTime: string;
}

Page({
  data: {
    startTime: '',        // 起始时间
    endTime: '',          // 结束时间
    records: [] as RecordItem[],  // 记录列表，指定为 RecordItem 类型数组
    maxRecords: 4,        // 最大记录数
    errorMessage: '',      // 错误提示
    token: String,
    PlanId: String
  },

  // 页面加载时加载已有记录
  onLoad(PlanId: any) {
    this.setData(
      {
        token:wx.getStorageSync('token'),
        PlanId:PlanId.id
      }
    )
    this.loadRecords(PlanId);
  },

  // 加载已有记录（从本地存储或后台获取）
  loadRecords(PlanId: any) {
    // 从云端获取
    wx.request({
      url: getApp().globalData.baseurl + 'Plan/getAutoTimeWithPlanID/', // 
      method: 'POST',
      header: {
        'Authorization': `Bearer ${this.data.token}` // 将 Token 放入请求头
      },
      data: { PlanId: PlanId.id },
      success: res => {
        // 处理服务器返回的数据
        if (res.data.result === 'success') {
          // 转换字段名：start_time → startTime，end_time → endTime
          const records = res.data.data.map(item => ({
            startTime: item.start_time,
            endTime: item.end_time
          }));
          this.setData({ records });
          wx.setStorageSync('records', records); // 可选缓存
        } else if( res.data.result ==='fail'){
          wx.showToast({ title: '当前没有设置自动启停时间', icon: 'none' });
        }else{
          wx.showToast({ title: '错误', icon: 'error' });
        }
      },
      fail: err => {
        console.error('获取设备信息失败:', err);
        wx.showToast({
          title: '设备信息获取失败',
          icon: 'none'
        });
      },
      complete: () => {
        wx.hideLoading();
      }
    });
    // const records = wx.getStorageSync('records') || [];
    // this.setData({
    //   records: records
    // });
  },

  // 设置起始时间
  setStartTime(e: any) {
    this.setData({
      startTime: e.detail.value
    });
  },

  // 设置结束时间
  setEndTime(e: any) {
    this.setData({
      endTime: e.detail.value
    });
  },

  // 创建新记录
  createRecord() {
    if (this.data.records.length >= this.data.maxRecords) {
      this.setData({
        errorMessage: '最多只能创建四条记录！'
      });
      return;
    }

    if (!this.data.startTime || !this.data.endTime) {
      this.setData({
        errorMessage: '起始时间和结束时间不能为空！'
      });
      return;
    }

    if (this.data.startTime >= this.data.endTime) {
      this.setData({
        errorMessage: '起始时间不能晚于结束时间！'
      });
      return;
    }

    const newRecord: RecordItem = {
      startTime: this.data.startTime,
      endTime: this.data.endTime
    };

    const updatedRecords = [...this.data.records, newRecord];
    
    // 根据起始时间排序记录
    updatedRecords.sort((a, b) => a.startTime.localeCompare(b.startTime));

    this.setData({
      records: updatedRecords,
      startTime: '',
      endTime: '',
      errorMessage: ''
    });

    wx.setStorageSync('records', updatedRecords); // 更新本地存储
  },

  // 删除记录
  // deleteRecord(e: any) {
  //   const index = e.currentTarget.dataset.index;
  //   const records = this.data.records;
  //   records.splice(index, 1); // 删除记录
  //   this.setData({
  //     records: records
  //   });
  //   wx.setStorageSync('records', records); // 更新本地存储
  // },
  // 删除记录
deleteRecord(e: any) {
  const index = e.currentTarget.dataset.index;
  
  wx.showModal({
    title: "确认删除",
    content: "确定要删除这条记录吗？",
    success: (res) => {
      if (res.confirm) {
        // 用户点击确定后执行删除
        const records = [...this.data.records]; // 创建新数组避免污染原数据
        records.splice(index, 1);
        
        this.setData({
          records: records
        });

      }
    }
  });
},

  // 保存记录
  saveRecords() {
  //   wx.setStorageSync('records', this.data.records);
    wx.request({
      url: getApp().globalData.baseurl +  'Plan/SaveAutoRecords/', // 
      method: 'POST',
      header: {
        'Authorization': `Bearer ${this.data.token}` // 将 Token 放入请求头
      },
      data: { records: this.data.records ,
          PlanId: this.data.PlanId
      },
      success: res => {
        // 处理服务器返回的数据
        if (res.data.result === 'success') {
          console.log(res)
        } else {
          wx.showToast({
            title: '设备信息获取失败',
            icon: 'none'
          });
        }
      },
      fail: err => {
        console.error('获取设备信息失败:', err);
        wx.showToast({
          title: '设备信息获取失败',
          icon: 'none'
        });
      },
      complete: () => {
        wx.hideLoading();
      }
    });
    wx.showToast({
      title: '记录已保存',
      icon: 'success'
    });
  },

  // 退出页面
  exitPage() {
    wx.showModal({
      title: "确认退出",
      content: "确定要退出吗？",
      success: (res) => {
        if (res.confirm) {
          wx.navigateBack(); // 返回上一页
        }
      }
    });
  }
});
