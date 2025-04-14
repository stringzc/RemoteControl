// pages/device/device.ts
interface Device {
  id: number;
  name: string;
  status: '已连接' | '未响应' | '离线';
  updateTime: string;
  active: boolean;
  icon: string;
}

Page({

  data: {
    deviceList: [] as Device[]
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad() {
    this.loadRealDeviceData();
  },
  /**
   * 从后端API获取真实设备数据
   */
  loadRealDeviceData() {
    const token: TokenType = wx.getStorageSync('token');
    wx.showLoading({ title: '加载设备...' });
    wx.request({
      url: getApp().globalData.baseurl + 'Plan/getPlanInfoWithID/',
      method: 'GET',
      header: {
        'Authorization': `Bearer ${token}` // 将 Token 放入请求头
      },
      success: (res) => {
        if (res.statusCode === 200) {
          const data = res.data
          if (data.result === 'success'){
            this.processApiData(data.devices);
          }else if(data.result === 'fail'){
            this.handleDataError('错误')
          }else{
            this.handleDataError('错误')
          }
          
        } else {
          this.handleDataError('数据格式异常');
        }
      },
      fail: (err) => {
        this.handleDataError('网络连接异常');
      },
      complete: () => wx.hideLoading()
    });
  },

  /**
   * 处理API返回的真实数据
   */
  processApiData(apiData: any[]) {
    const validatedData = apiData
      .filter(item => this.validateDeviceData(item))
      .map(item => ({
        id: item.id,
        name: item.name,
        status: this.mapDeviceStatus(item.active),
        updateTime: this.formatTimestamp(item.updateTime),
        active: Boolean(item.active),
        icon: this.getDeviceIcon(item.icon)
      }))
      .sort((a, b) => (a.active === b.active ? 0 : a.active ? -1 : 1));
      this.setData({
        deviceList: [...this.data.deviceList, ...validatedData]
      });
  },

  /**
   * 数据验证（示例）
   */
  validateDeviceData(item: any): boolean {
    const requiredFields = ['id', 'name', 'active', 'updateTime'];
    return requiredFields.every(field => item[field] !== undefined);
  },

  /**
   * 状态码映射（根据实际API调整）
   */
  mapDeviceStatus(statusCode: number): Device['status'] {
    const statusMap: Record<number, Device['status']> = {
      0: '离线',
      1: '已连接',
      2: '未响应'
    };
    return statusMap[statusCode] || '离线';
  },

  /**
   * 时间戳格式化
   */
  formatTimestamp(timestamp: number): string {
    const date = new Date(timestamp);
    return `${date.toLocaleDateString()} ${date.toLocaleTimeString()}`;
  },

  /**
   * 获取设备图标（根据实际类型映射）
   */
  getDeviceIcon(deviceType: string): string {
    const iconMap: Record<string, string> = {
      'GG': '/images/w/default.png',
    };
    return iconMap[deviceType] || '/images/w/default.png';
  },

  /**
   * 错误统一处理
   */
  handleDataError(message: string) {
    wx.showToast({
      title: `设备加载失败: ${message}`,
      icon: 'none',
      duration: 3000
    });
    
    // 失败时降级显示空状态
    this.setData({ deviceList: [] });
  },
  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady() {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow() {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide() {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload() {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh() {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom() {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage() {

  },
  handleScan() {
    wx.scanCode({
      success: res => this.handleScanSuccess(res.result),
      fail: err => this.handleScanError(err)
    });
  },
  /**
   * 扫码成功处理
   */
  handleScanSuccess(code: string) {
    this.fetchDeviceInfo(code);
  },
   /**
   * 扫码错误处理
   */
  handleScanError(err: WechatMiniprogram.GeneralCallbackResult) {

    wx.showToast({
      title: '扫码失败',
      icon: 'none'
    });
  },
/**
 * 获取设备信息
 * 通过设备编码访问服务器，获取设备的详细信息
 */
fetchDeviceInfo(code: string) {
  wx.showLoading({ title: '加载设备信息...' });
  const token: TokenType = wx.getStorageSync('token');
  wx.request({
    url: getApp().globalData.baseurl +  'Plan/AddPlanInfoWithID/', // 替换为实际的服务器 URL
    method: 'POST',
    header: {
      'Authorization': `Bearer ${token}` // 将 Token 放入请求头
    },
    data: { deviceCode: code },
    success: res => {
      // 处理服务器返回的数据
      const data = res.data
      if (data.result === 'success') {
        this.handleDeviceData(res.data.device);
      } else if (data.result === 'fail') {
        wx.showToast({
          title: '不存在该设备',
          icon: 'none'
        });
      }else if(data.result === 'have')
      {
        wx.showToast({
          title: '已经添加该设备',
          icon: 'none'
        });
      }else if(data.result === 'no'){
        wx.showToast({
          title: '已经添加该设备',
          icon: 'none'
        });
      }else{
        wx.showToast({
          title: '错误',
          icon: 'error'
        });
      }
    },
    fail: err => {
      wx.showToast({
        title: '设备信息获取失败',
        icon: 'none'
      });
    },
    complete: () => {
      wx.hideLoading();
    }
  });
},
/**
 * 处理设备数据
 * 获取设备信息后，创建新的设备对象并添加到设备列表
 */
handleDeviceData(deviceData:any) {
  this.processApiData(deviceData)
  wx.showToast({
    title: '设备添加成功',
    icon: 'success'
  });
},

  /**
   * 设备点击事件（需要在WXML中绑定）
   */
  onDeviceTap(e: WechatMiniprogram.TouchEvent) {
    const deviceId = e.currentTarget.dataset.id as number;
    const device = this.data.deviceList.find(d => d.id === deviceId);
    const NewDate = {"id": deviceId, "url" : device.icon}
    const ND  = encodeURIComponent(JSON.stringify(NewDate))
    if (device) {
      wx.navigateTo({
        url: `/pages/device/devicexijie/xijie?data=${ND}`
      });
    }
  }

})