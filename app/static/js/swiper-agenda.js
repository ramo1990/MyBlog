  const swiper = new Swiper(".mySwiper", {
    slidesPerView: 1.1, // pour effet de "carte qui dépasse"
    spaceBetween: 10, // réduit l'espace entre les slides
    centeredSlides: true, // centre les slides dans le wrapper
    loop: false, // Désactiver la boucle
    watchOverflow: true, // Désactiver flèches si 1 seul slide

    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },

    breakpoints: {
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
      // 1200: {
      //   slidesPerView: 3,
      //   spaceBetween: 30
      // },
    },
    on: {
      slideChange: function() {
        const swiperInstance = this;
        document.querySelector('.swiper-button-next')
          .classList.toggle('swiper-button-disabled', swiperInstance.isEnd);
        document.querySelector('.swiper-button-prev')
          .classList.toggle('swiper-button-disabled', swiperInstance.isBeginning);
      },
      // À l'initialisation
      init: function() {
        this.emit('slideChange');
      }
    }
  });
