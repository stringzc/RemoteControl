// pages/index/index.ts
Page({
  data: {
    currentSwiper: 0,
    bannerList: [
      {
        id: 1,
        imageUrl: "https://i2.3conline.com/images/piclib/201203/22/batch/1/130539/1332349654033obqessjgay.jpg",
        link: "/pages/detail/detail?id=1",
        title: "智能家居新时代",
        description: "体验全屋智能联动"
      },
      {
        id: 2,
        imageUrl: "https://ts1.cn.mm.bing.net/th/id/R-C.51136df0b742cdadabac92f88ba989a1?rik=Gq5BvhSCaT0NhQ&riu=http%3a%2f%2fimg.pconline.com.cn%2fimages%2fupload%2fupc%2ftx%2fwallpaper%2f1211%2f23%2fc2%2f16013920_1353654565612.jpg&ehk=QlYeWMk3KcFlzHLEp0xY8yOi0Uc1S03XwjlVmU7Nk5o%3d&risl=&pid=ImgRaw&r=0",
        link: "/pages/detail/detail?id=2",
        title: "安全防护系统",
        description: "24小时智能安防监控"
      },
      {
        id: 3,
        imageUrl: "https://pic1.zhimg.com/v2-202ef5254b6dcbd45053b42f81d12f2a_r.jpg?source=1940ef5c",
        link: "/pages/about/about",
        title: "环境智能调节",
        description: "温湿度自动控制系统"
      }
    ]
  },
  onSwiperChange(e: { detail: { current: number } }) {
    this.setData({
      currentSwiper: e.detail.current
    })
  },
  onBannerTap(e: { currentTarget: { dataset: { id: number } } }) {
    const bannerId = e.currentTarget.dataset.id;
    const banner = this.data.bannerList.find(item => item.id === bannerId);
    if (banner) {
      wx.navigateTo({
        url: banner.link
      });
    }
  }
});