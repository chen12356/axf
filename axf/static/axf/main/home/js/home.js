$(function () {
    var mySwiper = new Swiper("#topSwiper", {
        loop: true,
        autoplay: 3000,
        pagination: '.swiper-pagination', autoplayDisableOnInteraction: false,
    });
    var mySwiper1 = new Swiper("#swiperMenu",{
        slidesPerView:4,
    })
});