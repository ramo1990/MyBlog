document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll('.agenda-carousel-container').forEach(container => {
    const swiperEl = container.querySelector('.mySwiper');
    const nextBtn = container.querySelector('.swiper-button-next');
    const prevBtn = container.querySelector('.swiper-button-prev');
    
    const swiper = new Swiper(swiperEl, {
      slidesPerView: 1.1,
      spaceBetween: 5,
      centeredSlides: true,
      loop: false,
      watchOverflow: true,

      navigation: {
        nextEl: nextBtn,
        prevEl: prevBtn,
      },

      breakpoints: {
        576: {
          slidesPerView: 1,
          centeredSlides: false,
        },
        768: {
          slidesPerView: 2,
          spaceBetween: 15,
          centeredSlides: false,
        },
        992: {
          slidesPerView: 3,
          spaceBetween: 20,
          centeredSlides: false,
        },
        1200: {
          slidesPerView: 4,
          spaceBetween: 25,
          centeredSlides: false,
        },
      },

      on: {
        slideChange: function () {
          nextBtn.classList.toggle('swiper-button-disabled', this.isEnd);
          prevBtn.classList.toggle('swiper-button-disabled', this.isBeginning);
        },
        init: function () {
          this.emit('slideChange');
        }
      }
    });
  });
});

// const swiper = new Swiper(".mySwiper", {
//   slidesPerView: 1.2,
//   spaceBetween: 5,
//   loop: false,
//   centeredSlides: true,
//   navigation: {
//     nextEl: ".swiper-button-next",
//     prevEl: ".swiper-button-prev",
//   },
//   breakpoints: {
//     576: {
//       slidesPerView: 1.1,
//       spaceBetween: 10,
//     },
//     768: {
//       slidesPerView: 2,
//       spaceBetween: 15,
//       centeredSlides: false,
//     },
//     992: {
//       slidesPerView: 3,
//       spaceBetween: 20,
//       centeredSlides: false,
//     },
//   },
// });
