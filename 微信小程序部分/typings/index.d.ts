/// <reference path="./types/index.d.ts" />

interface IAppOption {
  globalData: {
    phoneNumber: string,  // 存储用户手机号
    uid: string,  // 存储用户唯一标识
    userInfo?: WechatMiniprogram.UserInfo,
    baseurl: string,
    token: string,
  }
  userInfoReadyCallback?: WechatMiniprogram.GetUserInfoSuccessCallback,
  checkPhoneNumber(): void,  // 自定义方法声明
  queryPhoneNumberFromServer: () => void, // 自定义方法
  requestPhoneNumberAuthorization: () => void, // 自定义方法
  navigateToHome: () => void,  // 自定义方法
  getToken:  () => void
}