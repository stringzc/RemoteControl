Page({
  data: {
    phoneNumber: '',  // 用于保存用户输入的手机号码
  },

  /**
   * 处理用户输入的手机号码
   */
  onInputPhoneNumber(e: WechatMiniprogram.BaseEvent): void {
    this.setData({
      phoneNumber: e.detail.value,  // 更新 phoneNumber 数据
    });
  },

  /**
   * 提交手机号码
   */
  submitPhoneNumber(): void {
    const phoneNumber = this.data.phoneNumber;  // 获取用户输入的手机号码
    // 校验手机号码是否为空
    if (!phoneNumber) {
      wx.showToast({
        title: '请输入手机号码',
        icon: 'none',
      });
      return;
    }

    // 校验手机号码格式（简单示例，您可以根据需要增加更严格的验证）
    const phoneRegex = /^[1][3-9][0-9]{9}$/;
    if (!phoneRegex.test(phoneNumber)) {
      wx.showToast({
        title: '请输入有效的手机号码',
        icon: 'none',
      });
      return;
    }

    // 将手机号和 uid 发送到后端
    const token: TokenType = wx.getStorageSync('token');
    wx.request({
      url: getApp().globalData.baseurl +  'Login/savePhoneNumber/',  // 替换为实际的服务器 URL
      method: 'POST',
      header: {
        'Authorization': `Bearer ${token}` // 将 Token 放入请求头
      },
      data: {
        phoneNumber:phoneNumber,
      },
      success: (response) => {
        if (response.data && response.data.result === "success") {
          // 手机号保存成功
          getApp().globalData.phoneNumber = phoneNumber
          wx.reLaunch({
            url: '/pages/index/index',  // 跳转到主页
          });
        } else {
          wx.showToast({
            title: '保存手机号失败，请重试',
            icon: 'none',
          });
        }
      },
      fail: (err) => {
        wx.showToast({
          title: '请求失败，请稍后再试',
          icon: 'none',
        });
        console.error('保存手机号失败:', err);
      }
    });
  }
});
