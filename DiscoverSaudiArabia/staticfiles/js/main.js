document.addEventListener('DOMContentLoaded', () => {
    // 🛑 تم تغيير الاستهداف لضمان عمل الزر بناءً على الـ ID في base.html
    const toggleButton = document.getElementById('toggleTheme'); 
    const body = document.body;

    // ===================================================
    // 1. الوضع الداكن (Dark Mode) - كود JavaScript
    // ===================================================
    
    // تحميل التفضيل من التخزين المحلي (Local Storage)
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme === 'dark') {
        body.classList.add('dark-mode');
    }

    // معالج النقر لتبديل الوضع
    if (toggleButton) {
        toggleButton.addEventListener('click', () => {
            // تبديل الفئة 'dark-mode' من عنصر body
            body.classList.toggle('dark-mode');

            // حفظ التفضيل في التخزين المحلي
            if (body.classList.contains('dark-mode')) {
                localStorage.setItem('theme', 'dark');
            } else {
                localStorage.setItem('theme', 'light');
            }
        });
    }

    // ===================================================
    // 2. تعيين صور البطاقات (لصفحة الرياض)
    // ===================================================

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
            
            // تعيين الصورة والتنسيق عبر الجافاسكريبت
            cardElement.style.backgroundImage = `url('${imageUrl}')`;
            cardElement.style.backgroundSize = 'cover';
            cardElement.style.backgroundPosition = 'center';
        }
    });
    
    // ===================================================
    // 🚀 3. منطق التنقل بالأسهم بين صفحات المدن 🚀
    // (تم التعديل لإزالة امتداد .html والعمل مع مسارات Django)
    // ===================================================

    // 💥 القائمة الجديدة بدون امتداد .html 💥
    const cityPages = [
        'riyadh', 
        'jeddah', 
        'alula', 
        'abha', 
        'khobar', 
        'tabuk'
    ];
    
    // 💥 طريقة استخراج اسم الصفحة الحالية من المسار 💥
    const currentPagePath = window.location.pathname.split('/').filter(Boolean).pop();
    const currentIndex = cityPages.indexOf(currentPagePath);

    const prevButton = document.getElementById('prevCityBtn');
    const nextButton = document.getElementById('nextCityBtn');

    if (prevButton && nextButton) {
        // تحديد رابط الصفحة السابقة
        if (currentIndex > 0) {
            // إنشاء الرابط الصحيح لـ Django
            prevButton.href = '/' + cityPages[currentIndex - 1] + '/'; 
            prevButton.style.display = 'flex'; // إظهار الزر
        } else {
            prevButton.style.display = 'none'; // إخفاء الزر في الصفحة الأولى
        }

        // تحديد رابط الصفحة التالية
        if (currentIndex < cityPages.length - 1) {
            // إنشاء الرابط الصحيح لـ Django
            nextButton.href = '/' + cityPages[currentIndex + 1] + '/'; 
            nextButton.style.display = 'flex'; // إظهار الزر
        } else {
            nextButton.style.display = 'none'; // إخفاء الزر في الصفحة الأخيرة
        }
    }
});