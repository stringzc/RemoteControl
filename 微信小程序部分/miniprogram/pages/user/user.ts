// pages/user/user.ts
interface UserInfo {
  avatar: string;
  nickname: string;
  bio?: string;
}

Page({
  data: {
    userInfo: {
      avatar: 'https://www.aurage.cn/static/userhead.png',
      nickname: '智能农业用户',
      bio: '🏠 智能农业爱好者'
    } as UserInfo
  },

  // 更换头像
  changeAvatar() {
    wx.chooseMedia({
      count: 1,
      mediaType: ['image'],
      success: (res) => {
        const tempPath = res.tempFiles[0].tempFilePath
        this.setData({
          'userInfo.avatar': tempPath
        })
        // 实际开发中需上传至服务器
      }
    })
  },

  // 跳转编辑资料
  navigateToEditProfile() {
    wx.navigateTo({
      url: '/pages/edit-profile/edit-profile'
    })
  },

  // 显示添加设备面板
  showAddDevicePanel() {
    wx.showActionSheet({
      itemList: ['扫码添加设备', '手动输入设备码'],
      success: (res) => {
        if (res.tapIndex === 0) {
          this.scanToAddDevice()
        } else {
          this.inputDeviceCode()
        }
      }
    })
  },

scanToAddDevice() {
    wx.scanCode({
      success: (res) => {
        console.log('扫描结果:', res.result)
        wx.showToast({ title: '设备添加成功' })
      }
    })
  },

 inputDeviceCode() {
    wx.showModal({
      title: '输入设备码',
      content: '',
      editable: true,
      success: (res) => {
        if (res.confirm && res.content) {
          console.log('输入设备码:', res.content)
        }
      }
    })
  }
})