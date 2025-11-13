class CookieConsent {
    constructor() {
        this.cookieName = 'cookie_consent';
        this.cookieExpiry = 365; 
        this.preferences = {
            necessary: true,
            analytics: false,
            marketing: false,
            preferences: false
        };
        this.init();
    }

    init() {
        const savedConsent = this.getConsent();
        if (!savedConsent) {
            setTimeout(() => this.showBanner(), 1000);
        } else {
            this.loadPreferences(savedConsent);
        }
    }

    showBanner() {
        const existingBanner = document.getElementById('cookie-banner');
        if (existingBanner) existingBanner.remove();

        const banner = document.createElement('div');
        banner.id = 'cookie-banner';
        banner.innerHTML = `
            <div class="cookie-container">
                <div class="cookie-content">
                    <div class="cookie-header">
                        <span class="cookie-icon">🍪</span>
                        <h3>We use cookies</h3>
                    </div>
                    <p>We use cookies to enhance your browsing experience, serve personalized content, and analyze our traffic. By clicking "Accept All", you consent to our use of cookies.</p>
                    <div class="cookie-buttons">
                        <button class="cookie-btn accept-btn">Accept All</button>
                        <button class="cookie-btn reject-btn">Reject All</button>
                        <button class="cookie-btn settings-btn">Preferences</button>
                    </div>
                    <a href="/privacy" class="privacy-link">Cookie Policy</a>
                </div>
            </div>
        `;
        document.body.appendChild(banner);

        banner.querySelector('.accept-btn').addEventListener('click', () => this.acceptAll());
        banner.querySelector('.reject-btn').addEventListener('click', () => this.rejectAll());
        banner.querySelector('.settings-btn').addEventListener('click', () => this.showSettings());
    }

    showSettings() {
        const modal = document.createElement('div');
        modal.id = 'cookie-settings';
        modal.innerHTML = `
            <div class="cookie-modal-overlay">
                <div class="cookie-modal">
                    <div class="modal-header">
                        <h3>Cookie Preferences</h3>
                        <button class="close-btn">&times;</button>
                    </div>
                    <div class="modal-content">
                        <div class="cookie-option">
                            <label class="switch">
                                <input type="checkbox" id="necessary-cookies" checked disabled>
                                <span class="slider"></span>
                            </label>
                            <div class="option-text">
                                <strong>Necessary Cookies</strong>
                                <p>Required for the website to function properly</p>
                            </div>
                        </div>
                        
                        <div class="cookie-option">
                            <label class="switch">
                                <input type="checkbox" id="analytics-cookies">
                                <span class="slider"></span>
                            </label>
                            <div class="option-text">
                                <strong>Analytics Cookies</strong>
                                <p>Help us understand how visitors interact with our website</p>
                            </div>
                        </div>
                        
                        <div class="cookie-option">
                            <label class="switch">
                                <input type="checkbox" id="marketing-cookies">
                                <span class="slider"></span>
                            </label>
                            <div class="option-text">
                                <strong>Marketing Cookies</strong>
                                <p>Used to track visitors across websites for advertising</p>
                            </div>
                        </div>
                        
                        <div class="cookie-option">
                            <label class="switch">
                                <input type="checkbox" id="preferences-cookies">
                                <span class="slider"></span>
                            </label>
                            <div class="option-text">
                                <strong>Preference Cookies</strong>
                                <p>Remember your settings and preferences</p>
                            </div>
                        </div>
                    </div>
                    <div class="modal-footer">
                        <button class="cookie-btn save-btn">Save Preferences</button>
                        <button class="cookie-btn accept-all-btn">Accept All</button>
                    </div>
                </div>
            </div>
        `;
        document.body.appendChild(modal);

        this.loadModalPreferences();

        modal.querySelector('.close-btn').addEventListener('click', () => this.closeModal());
        modal.querySelector('.save-btn').addEventListener('click', () => this.savePreferences());
        modal.querySelector('.accept-all-btn').addEventListener('click', () => this.acceptAll());
        modal.querySelector('.cookie-modal-overlay').addEventListener('click', (e) => {
            if (e.target.classList.contains('cookie-modal-overlay')) this.closeModal();
        });
    }

    loadModalPreferences() {
        const saved = this.getConsent();
        if (saved) {
            this.preferences = { ...this.preferences, ...saved };
        }
        
        document.getElementById('analytics-cookies').checked = this.preferences.analytics;
        document.getElementById('marketing-cookies').checked = this.preferences.marketing;
        document.getElementById('preferences-cookies').checked = this.preferences.preferences;
    }

    savePreferences() {
        this.preferences.analytics = document.getElementById('analytics-cookies').checked;
        this.preferences.marketing = document.getElementById('marketing-cookies').checked;
        this.preferences.preferences = document.getElementById('preferences-cookies').checked;

        this.setConsent(this.preferences);
        this.closeModal();
        this.hideBanner();
        
        this.applyPreferences();
        this.showToast('Preferences saved successfully!');
    }

    acceptAll() {
        this.preferences = {
            necessary: true,
            analytics: true,
            marketing: true,
            preferences: true
        };
        
        this.setConsent(this.preferences);
        this.closeModal();
        this.hideBanner();
        this.applyPreferences();
        this.showToast('All cookies accepted!');
    }

    rejectAll() {
        this.preferences = {
            necessary: true, 
            analytics: false,
            marketing: false,
            preferences: false
        };
        
        this.setConsent(this.preferences);
        this.hideBanner();
        this.applyPreferences();
        this.showToast('Non-essential cookies rejected.');
    }

    applyPreferences() {
        if (this.preferences.analytics) {
            this.loadAnalytics();
        } else {
            this.disableAnalytics();
        }
        if (this.preferences.marketing) {
            this.loadMarketing();
        } else {
            this.disableMarketing();
        }
        if (this.preferences.preferences) {
            this.saveUserPreferences();
        }
    }

    loadAnalytics() {
        console.log('Loading analytics...');
    }

    disableAnalytics() {
        console.log('Analytics disabled');
    }

    loadMarketing() {
        console.log('Loading marketing scripts...');
    }

    disableMarketing() {
        console.log('Marketing disabled');
    }

    saveUserPreferences() {
        console.log('Saving user preferences...');
    }

    setConsent(preferences) {
        const consent = JSON.stringify(preferences);
        const date = new Date();
        date.setTime(date.getTime() + (this.cookieExpiry * 24 * 60 * 60 * 1000));
        const expires = "expires=" + date.toUTCString();
        document.cookie = this.cookieName + "=" + consent + ";" + expires + ";path=/;SameSite=Lax";
    }

    getConsent() {
        const name = this.cookieName + "=";
        const decodedCookie = decodeURIComponent(document.cookie);
        const ca = decodedCookie.split(';');
        
        for (let i = 0; i < ca.length; i++) {
            let c = ca[i];
            while (c.charAt(0) === ' ') {
                c = c.substring(1);
            }
            if (c.indexOf(name) === 0) {
                return JSON.parse(c.substring(name.length, c.length));
            }
        }
        return null;
    }

    loadPreferences(savedConsent) {
        this.preferences = { ...this.preferences, ...savedConsent };
        this.applyPreferences();
    }

    hideBanner() {
        const banner = document.getElementById('cookie-banner');
        if (banner) {
            banner.style.animation = 'slideDown 0.3s ease forwards';
            setTimeout(() => banner.remove(), 300);
        }
    }

    closeModal() {
        const modal = document.getElementById('cookie-settings');
        if (modal) modal.remove();
    }

    showToast(message) {
        const toast = document.createElement('div');
        toast.className = 'cookie-toast';
        toast.textContent = message;
        document.body.appendChild(toast);

        setTimeout(() => {
            toast.classList.add('show');
        }, 100);

        setTimeout(() => {
            toast.classList.remove('show');
            setTimeout(() => toast.remove(), 300);
        }, 3000);
    }
    isAllowed(cookieType) {
        const consent = this.getConsent();
        return consent ? consent[cookieType] : false;
    }
}
document.addEventListener('DOMContentLoaded', function() {
    window.cookieConsent = new CookieConsent();
});

if (typeof module !== 'undefined' && module.exports) {
    module.exports = CookieConsent;
}