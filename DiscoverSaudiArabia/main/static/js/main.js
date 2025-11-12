document.addEventListener('DOMContentLoaded', () => {
    const toggleButton = document.getElementById('toggleTheme'); 
    const body = document.body;
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme === 'dark') {
        body.classList.add('dark-mode');
    }
    if (toggleButton) {
        toggleButton.addEventListener('click', () => {
            body.classList.toggle('dark-mode');
            if (body.classList.contains('dark-mode')) {
                localStorage.setItem('theme', 'dark');
            } else {
                localStorage.setItem('theme', 'light');
            }
        });
    }

    const cards = [
        { selector: '.card-kingdom-centre', imageSelector: '#kingdomCentreImage' },
        { selector: '.card-masmak-fort', imageSelector: '#masmakFortImage' },
        { selector: '.card-najd-village', imageSelector: '#najdVillageImage' },
        { selector: '.card-riyadh-park', imageSelector: '#riyadhParkImage' },
        { selector: '.card-boulevard-world', imageSelector: '#boulevardWorldImage' }
    ];

    cards.forEach(cardData => {
        const cardElement = document.querySelector(cardData.selector);
        const imagePathElement = document.querySelector(cardData.imageSelector);

        if (cardElement && imagePathElement) {
            const imageUrl = imagePathElement.value;
            cardElement.style.backgroundImage = `url('${imageUrl}')`;
            cardElement.style.backgroundSize = 'cover';
            cardElement.style.backgroundPosition = 'center';
        }
    });

    const cityPages = [
        'riyadh', 
        'jeddah', 
        'alula', 
        'abha', 
        'khobar', 
        'tabuk'
    ];

        const currentPagePath = window.location.pathname.split('/').filter(Boolean).pop();
        const currentIndex = cityPages.indexOf(currentPagePath);
        const prevButton = document.getElementById('prevCityBtn');
        const nextButton = document.getElementById('nextCityBtn');

    if (prevButton && nextButton) {
        if (currentIndex > 0) {
            prevButton.href = '/' + cityPages[currentIndex - 1] + '/'; 
            prevButton.style.display = 'flex'; 
        } else {
            prevButton.style.display = 'none'; 
        }

     if (currentIndex < cityPages.length - 1) {
            nextButton.href = '/' + cityPages[currentIndex + 1] + '/'; 
            nextButton.style.display = 'flex'; 
        } else {
            nextButton.style.display = 'none'; 
        }
    }
});

    const swiperCategories = new Swiper('.category-swiper', {
        direction: 'horizontal',
        slidesPerView: 'auto', 
        spaceBetween: 20, 
        rtl: true, 
        navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev',
        },
        freeMode: true,
        simulateTouch: true, 
    });

document.addEventListener("DOMContentLoaded", function () {

  const toggleTheme = document.querySelector(".toggleTheme");
  const navMenu = document.querySelector(".nav");

  if (toggleTheme && navMenu) {
    toggleTheme.addEventListener("click", () => {
      navMenu.classList.toggle("active");
    });
  }
});

