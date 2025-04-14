// pages/device/devicexijie/xijie.ts
Page({

  /**
   * 页面的初始数据
   */
  data: {
      id: String,
      url: String,
      token: String
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad(options: { data?: string }) {
    this.setData(
      {
        token:wx.getStorageSync('token')
      }
    )
    if (options.data) {
      const decodedData = JSON.parse(decodeURIComponent(options.data));
      this.setData({
        url: decodedData['url'],
        id: decodedData['id']
      });
    }
   
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
  handleAutomation(){
    console.log(1)
    wx.navigateTo({
      url: `/pages/device/devicexijie/auto/auto?id=${this.data.id}`
    });
  },
  handleCustom(){
    console.log(2)
    wx.navigateTo({
      url: `/pages/device/devicexijie/personality/personality?id=${this.data.id}`
    });
  },

  
  handleActmation(){
    wx.request({
      url: getApp().globalData.baseurl +  'Plan/PlanAct/', // 替换为实际的服务器 URL
      method: 'POST',
      header: {
        'Authorization': `Bearer ${this.data.token}` // 将 Token 放入请求头
      },
      data: { PlanId: this.data.id},
      success: res => {
        // 处理服务器返回的数据
        const status = res.data.status;
        if (status == 0){
          wx.showToast({
            title: '启动成功',
            icon: 'success'
          });
        }else if( status == 1){
          wx.showToast({
            title: '正在执行请勿重复',
            icon: 'loading'
          });
        }else if(status == 2){
          wx.showToast({
            title: '请一分钟后重试',
            icon: 'loading'
          });
        }else{
          wx.showToast({
            title: '404',
            icon: 'error'
          });
        }
      },
      fail: err => {
        wx.showToast({
          title: '启动失败',
          icon: 'error'
        });
      },
    });
  },
  handleCancelmation(){
    wx.request({
      url: getApp().globalData.baseurl +  'Plan/CancelAct/', // 替换为实际的服务器 URL
      method: 'POST',
      header: {
        'Authorization': `Bearer ${this.data.token}` // 将 Token 放入请求头
      },
      data: { PlanId: this.data.id,
      },
      success: res => {
        // 处理服务器返回的数据
        const status = res.data.status;
        if (status == 0){
          wx.showToast({
            title: '取消成功',
            icon: 'success'
          });
        }else if( status == 1){
          wx.showToast({
            title: '无任务在执行',
            icon: 'error'
          });
        }else if (status == 2){
          wx.showToast({
            title: '点击过于频繁',
            icon: 'loading'
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
          title: '取消失败',
          icon: 'error'
        });
      },
    });
  }
})