// Dark/Light Mode Toggle
const themeToggle = document.getElementById('theme-toggle');
const themeIcon = themeToggle.querySelector('i');
const savedTheme = localStorage.getItem('theme') || 'light';
document.documentElement.setAttribute('data-theme', savedTheme);
updateThemeIcon(savedTheme);

themeToggle.addEventListener('click', function() {
    const currentTheme = document.documentElement.getAttribute('data-theme');
    const newTheme = currentTheme === 'light' ? 'dark' : 'light';
    
    document.documentElement.setAttribute('data-theme', newTheme);
    localStorage.setItem('theme', newTheme);
    updateThemeIcon(newTheme);
});

function updateThemeIcon(theme) {
    if (theme === 'dark') {
        themeIcon.className = 'fas fa-sun';
        themeIcon.title = 'Switch to Light Mode';
    } else {
        themeIcon.className = 'fas fa-moon';
        themeIcon.title = 'Switch to Dark Mode';
    }
}

if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches && !localStorage.getItem('theme')) {
    document.documentElement.setAttribute('data-theme', 'dark');
    updateThemeIcon('dark');
}

// ScrollMagic Animations
const controller = new ScrollMagic.Controller();

window.addEventListener('scroll', function() {
    const navbar = document.querySelector('.navbar');
    if (window.scrollY > 100) {
        navbar.classList.add('scrolled');
    } else {
        navbar.classList.remove('scrolled');
    }
});

document.addEventListener('DOMContentLoaded', function() {
    const cards = document.querySelectorAll('.city-card');
    cards.forEach((card, index) => {
        new ScrollMagic.Scene({
            triggerElement: card,
            triggerHook: 0.8,
            reverse: false
        })
        .setTween(gsap.fromTo(card, 
            { opacity: 0, y: 50 },
            { opacity: 1, y: 0, duration: 1 }
        ))
        .addTo(controller);
    });

    const headings = document.querySelectorAll('h1, h2, h3');
    headings.forEach(heading => {
        new ScrollMagic.Scene({
            triggerElement: heading,
            triggerHook: 0.9,
            reverse: false
        })
        .setTween(gsap.fromTo(heading,
            { opacity: 0, x: -50 },
            { opacity: 1, x: 0, duration: 1 }
        ))
        .addTo(controller);
    });
});

// Floating Elements Animation
function createFloatingElements() {
    const hero = document.querySelector('.hero-section');
    if (hero) {
        for (let i = 0; i < 15; i++) {
            const element = document.createElement('div');
            element.style.cssText = `
                position: absolute;
                width: ${Math.random() * 100 + 50}px;
                height: ${Math.random() * 100 + 50}px;
                background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 70%);
                border-radius: 50%;
                top: ${Math.random() * 100}%;
                left: ${Math.random() * 100}%;
                animation: floatElement ${Math.random() * 10 + 10}s infinite ease-in-out;
                animation-delay: ${Math.random() * 5}s;
                pointer-events: none;
                z-index: 1;
            `;
            hero.appendChild(element);
        }
    }
}

// Add floating animations CSS
const style = document.createElement('style');
style.textContent = `
    @keyframes floatElement {
        0%, 100% { transform: translateY(0px) translateX(0px) rotate(0deg); }
        33% { transform: translateY(-30px) translateX(20px) rotate(120deg); }
        66% { transform: translateY(20px) translateX(-20px) rotate(240deg); }
    }
`;
document.head.appendChild(style);

// Cookie-Controlled Analytics
function loadAnalyticsIfAllowed() {
    if (window.cookieConsent && window.cookieConsent.isAllowed('analytics')) {
        // Load Google Analytics or other analytics
        console.log('Loading analytics...');
        // Example: gtag('config', 'GA_MEASUREMENT_ID');
        
        // You can add your analytics script here
        const analyticsScript = document.createElement('script');
        analyticsScript.src = 'https://www.googletagmanager.com/gtag/js?id=YOUR_GA_ID';
        analyticsScript.async = true;
        document.head.appendChild(analyticsScript);
        
        window.dataLayer = window.dataLayer || [];
        function gtag(){dataLayer.push(arguments);}
        gtag('js', new Date());
        gtag('config', 'YOUR_GA_ID');
    }
}

// Cookie-Controlled Marketing
function loadMarketingIfAllowed() {
    if (window.cookieConsent && window.cookieConsent.isAllowed('marketing')) {
        console.log('Loading marketing scripts...');
        // Add Facebook Pixel, Google Ads, etc.
    }
}

// Initialize everything when page loads
window.addEventListener('load', function() {
    createFloatingElements();
    AOS.init();
    
    // Wait a bit for cookie consent to initialize
    setTimeout(() => {
        loadAnalyticsIfAllowed();
        loadMarketingIfAllowed();
    }, 1000);
});

// Enhanced city card interactions
document.addEventListener('DOMContentLoaded', function() {
    const cityCards = document.querySelectorAll('.city-card');
    
    cityCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-10px) scale(1.02)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0) scale(1)';
        });
        
        // Click animation
        card.addEventListener('click', function() {
            this.style.transform = 'scale(0.95)';
            setTimeout(() => {
                this.style.transform = 'scale(1)';
            }, 150);
        });
    });
});

// Smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Lazy loading for images
document.addEventListener('DOMContentLoaded', function() {
    const lazyImages = document.querySelectorAll('img[data-src]');
    
    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src;
                img.classList.remove('lazy');
                imageObserver.unobserve(img);
            }
        });
    });
    
    lazyImages.forEach(img => imageObserver.observe(img));
});