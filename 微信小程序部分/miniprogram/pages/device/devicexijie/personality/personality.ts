// pages/device/devicexijie/personality/personality.ts
Page({

  /**
   * 页面的初始数据
   */
data: {
  list: [],
  activeId: null, // 当前激活的ID
  selectedItem: null, // 当前选中的项
  token: String
},
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad(PlanId: any) {
    this.setData(
      {
        token:wx.getStorageSync('token')
      }
    )
    // 从云端获取每个模式的内容 获取模式内容
    wx.request({
      url: getApp().globalData.baseurl +  'Plan/getModelInfoWithPlanID/', // 
      method: 'POST',
      header: {
        'Authorization': `Bearer ${this.data.token}` // 将 Token 放入请求头
      },
      data: { PlanId: PlanId },
      success: res => {
        // 处理服务器返回的数据
        if (res) {
          console.log(res)
          this.setData({
            list:res.data.data 
          })
          
        } else {
          wx.showToast({
            title: '模式信息获取失败',
            icon: 'none'
          });
        }
      },
      fail: err => {
        console.error('模式信息获取失败:', err);
        wx.showToast({
          title: '模式信息获取失败',
          icon: 'error'
        });
      },
    });
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
   
 // 处理按钮点击事件
 onButtonClick(e: any) {
  wx.showModal({
    title: "点击确认",
    content: "确定点击该按钮吗",
    success: (res) => {
      if (res.confirm) {
        const clickedId = e.currentTarget.dataset.id; // 获取当前点击行的ID
        this.setData({
          activeId: this.data.activeId === clickedId ? null : clickedId // 切换激活状态
        });
        
      }
    }
  });
},

// 处理点击行显示详情
onRowClick(e: any) {
  const selectedItem = this.data.list.find(item => item.id === e.currentTarget.dataset.id);
  this.setData({
    selectedItem: selectedItem || null // 设置选中的项数据，确保为null时不会报错
  });
}
})