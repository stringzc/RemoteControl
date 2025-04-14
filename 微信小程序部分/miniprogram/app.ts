// app.ts
type TokenType = string;
App<IAppOption>({
  globalData: {
    phoneNumber: '',  // 存储用户手机号
    uid: '',  // 存储用户唯一标识
    baseurl:`https://www.aurage.cn/wx/`,
    token: '',
  },
  
  onLaunch() {
    // 登录并获取用户 uid
    const token: TokenType = wx.getStorageSync('token');
    if (token) {
      wx.request({
        url: this.globalData.baseurl + 'Login/UserProfileView',
        header: {
          'Authorization': `Bearer ${token}` // 将 Token 放入请求头
        },
        success: (res) => {
          // 这里获取用户资料（如昵称、头像）
          if (res.statusCode >= 200 && res.statusCode < 300)
          {
            this.globalData.uid = res.data.openid;
            this.checkPhoneNumber();
          }else{
            wx.showToast({
              title: 'token过期',
              icon: 'none'
            });
            this.getToken()
          }
        },
        fail: (err) => {
          wx.showToast({
            title: '网络错误',
            icon: 'error'
          });
        } 
      });
    } else {
      this.getToken()
    }
  },
  /**
   * 获取token
   */
  getToken(){
    wx.login({
      success: res => {
        // 假设从后台获取 uid
        wx.request({
          url: this.globalData.baseurl + `Login/getUid`, // 替换为实际的服务器 URL
          method: 'GET',
          data: { code: res.code },
          success: (response:any) => {
            const token = response.data.token;
            wx.setStorageSync('token', token);  // 存储Token
            this.checkPhoneNumber();
          }
        });
      }
    });
  },
  /**
   * 检查是否已存储手机号
   */
  checkPhoneNumber() {
    this.queryPhoneNumberFromServer();
  },

  /**
   * 从服务器查询手机号
   */
  queryPhoneNumberFromServer() {
    const token: TokenType = wx.getStorageSync('token');
    wx.request({
      url: this.globalData.baseurl + 'Login/getPhoneNumber', // 替换为实际的服务器 URL
      method: 'GET',
      header: {
        'Authorization': `Bearer ${token}` // 将 Token 放入请求头
      },
      success: (response) => {
        const data = response.data as { phoneNumber: string }; 
        if (data.phoneNumber) {
          this.globalData.phoneNumber = data.phoneNumber;
          this.navigateToHome();
        } else {
          this.requestPhoneNumberAuthorization();
        }
      },
      fail: (err) => {
        wx.showToast({
          title: '网络错误',
          icon: 'error'
        });
      }
    });
  },

  /**
   * 请求用户授权手机号
   */
  requestPhoneNumberAuthorization() {
    wx.redirectTo({
      url: '/pages/login/login',  // 跳转到获取手机号的页面
    });
  },

  /**
   * 跳转到主页面
   */
  navigateToHome() {
    wx.reLaunch({
      url: '/pages/index/index',  // 跳转到主页面
    });
  },

})