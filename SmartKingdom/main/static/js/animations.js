// أنيميشن الـ typing عند الوصول للقسم
function startTypingAnimation() {
    const mapSection = document.querySelector('.map-section');
    const typingText = document.querySelector('.typing-text');
    const typingDescription = document.querySelector('.typing-description');
    
    // تأكد من وجود العناصر
    if (!mapSection || !typingText || !typingDescription) {
        console.log('بعض العناصر مش موجودة في الصفحة');
        return;
    }
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                console.log('بدأ أنيميشن الكتابة!');
                
                // بدء أنيميشن الكتابة
                typingText.classList.add('start-typing');
                
                // بدء أنيميشن النص التوضيحي بعد 3 ثواني
                setTimeout(() => {
                    typingDescription.classList.add('start-fade');
                    console.log('بدأ أنيميشن النص التوضيحي!');
                }, 3000);
                
                // إيقاف المراقبة بعد التشغيل
                observer.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.3 // يبدأ لما 30% من القسم يظهر
    });
    
    observer.observe(mapSection);
    console.log('بدأت مراقبة قسم الخريطة...');
}

// تأثير فيديو نيوم عند الـ hover
function setupNeomVideoEffect() {
    const neomRegion = document.querySelector('.neom');
    const mapLeft = document.querySelector('.map-left');
    
    if (!neomRegion || !mapLeft) {
        console.log('عناصر نيوم غير موجودة');
        return;
    }
    
    neomRegion.addEventListener('mouseenter', () => {
        mapLeft.classList.add('neom-hovered');
        console.log('🏔️ بدأ تأثير فيديو نيوم المستقبلية!');
    });
    
    neomRegion.addEventListener('mouseleave', () => {
        mapLeft.classList.remove('neom-hovered');
        console.log('🌆 انتهى تأثير فيديو نيوم!');
    });
}

// تأثير فيديو البحر الأحمر عند الـ hover
function setupRedSeaVideoEffect() {
    const redSeaRegion = document.querySelector('.jeddah');
    const mapLeft = document.querySelector('.map-left');
    
    if (!redSeaRegion || !mapLeft) {
        console.log('عناصر البحر الأحمر غير موجودة');
        return;
    }
    
    redSeaRegion.addEventListener('mouseenter', () => {
        mapLeft.classList.add('redsea-hovered');
        console.log('🌊🐠 بدأ تأثير فيديو البحر الأحمر السحري!');
    });
    
    redSeaRegion.addEventListener('mouseleave', () => {
        mapLeft.classList.remove('redsea-hovered');
        console.log('🏖️ انتهى تأثير البحر الأحمر الخلاب!');
    });
}

// تأثير فيديو القدية عند الـ hover
function setupQiddiyaVideoEffect() {
    const qiddiyaRegion = document.querySelector('.qiddiya');
    const mapLeft = document.querySelector('.map-left');
    
    if (!qiddiyaRegion || !mapLeft) {
        console.log('عناصر القدية غير موجودة');
        return;
    }
    
    qiddiyaRegion.addEventListener('mouseenter', () => {
        mapLeft.classList.add('qiddiya-hovered');
        console.log('🎢🎪 بدأ تأثير فيديو القدية المليئة بالمرح والإثارة!');
    });
    
    qiddiyaRegion.addEventListener('mouseleave', () => {
        mapLeft.classList.remove('qiddiya-hovered');
        console.log('🎨🎭 انتهى تأثير القدية الترفيهي الرائع!');
    });
}

// تأثير فيديو الرياض عند الـ hover
function setupRiyadhVideoEffect() {
    const riyadhRegion = document.querySelector('.riyadh');
    const mapLeft = document.querySelector('.map-left');
    
    if (!riyadhRegion || !mapLeft) {
        console.log('عناصر الرياض غير موجودة');
        return;
    }
    
    riyadhRegion.addEventListener('mouseenter', () => {
        mapLeft.classList.add('riyadh-hovered');
        console.log('👑🏛️ بدأ تأثير فيديو الرياض العاصمة الملكية الفخمة!');
    });
    
    riyadhRegion.addEventListener('mouseleave', () => {
        mapLeft.classList.remove('riyadh-hovered');
        console.log('🌆✨ انتهى تأثير العاصمة الذهبية الرياض!');
    });
}

// إضافة أنيميشنات أخرى (للمستقبل)
function initAllAnimations() {
    startTypingAnimation();
    setupNeomVideoEffect();
    setupRedSeaVideoEffect();
    setupQiddiyaVideoEffect();
    setupRiyadhVideoEffect();
    
    // يمكن إضافة أنيميشنات أخرى هنا
    console.log('تم تحميل جميع الأنيميشنات!');
}

// تشغيل المراقب عند تحميل الصفحة
document.addEventListener('DOMContentLoaded', initAllAnimations);

// تشغيل الأنيميشنات عند تحميل النافذة (backup)
window.addEventListener('load', () => {
    setTimeout(initAllAnimations, 100);
});