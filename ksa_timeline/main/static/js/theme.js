  function setCookie(name, value, days) {
    const maxAge = days * 24 * 60 * 60;
    document.cookie =
      encodeURIComponent(name) + "=" + encodeURIComponent(value) +
      "; max-age=" + maxAge + "; path=/; SameSite=Lax";
  }

  function getCookie(name) {
    const key = encodeURIComponent(name) + "=";
    const parts = document.cookie.split("; ");
    for (let i = 0; i < parts.length; i++) {
      if (parts[i].indexOf(key) === 0) {
        return decodeURIComponent(parts[i].substring(key.length));
      }
    }
    return "";
  }

  const body = document.body;
  const btn  = document.getElementById("themeToggle");

  function applyTheme(mode) {
    body.classList.remove("theme-dark", "theme-light");
    body.classList.add(mode === "dark" ? "theme-dark" : "theme-light");
    setCookie("theme", mode, 180);
  }

  (function initTheme() {
    const saved = getCookie("theme");
    if (saved === "dark" || saved === "light") {
      applyTheme(saved);
    } else {
      const prefersDark = window.matchMedia &&
                          window.matchMedia("(prefers-color-scheme: dark)").matches;
      applyTheme(prefersDark ? "dark" : "light");
    }
  })();

  if (btn) {
    btn.addEventListener("click", () => {
      const next = body.classList.contains("theme-dark") ? "light" : "dark";
      applyTheme(next);
    });
  }

  const ddToggle = document.querySelector(".nav-dropdown-toggle");
  const ddMenu   = document.querySelector(".nav-dropdown-menu");
  if (ddToggle && ddMenu) {
    ddToggle.addEventListener("click", () => ddMenu.classList.toggle("show"));
    document.addEventListener("click", (e) => {
      if (!ddToggle.contains(e.target) && !ddMenu.contains(e.target)) ddMenu.classList.remove("show");
    });
  }

  (function () {
    const items = document.querySelectorAll(".timeline-item");
    if (!items.length) return;
    if (!("IntersectionObserver" in window)) {
      items.forEach((el) => el.classList.add("visible"));
      return;
    }
    try {
      const obs = new IntersectionObserver((entries) => {
        entries.forEach((e) => { if (e.isIntersecting) e.target.classList.add("visible"); });
      }, { threshold: 0.12 });
      items.forEach((el) => obs.observe(el));
    } catch {
      items.forEach((el) => el.classList.add("visible"));
    }
  })();

  document.addEventListener("DOMContentLoaded", () => {
    const container = document.querySelector(".page-fade");
    if (container) requestAnimationFrame(() => container.classList.add("show"));
  });

  document.addEventListener("click", (e) => {
    const a = e.target.closest("a");
    if (!a) return;
    const href = a.getAttribute("href") || "";
    if (a.target === "_blank" || href.startsWith("http") || href.startsWith("#") || a.hasAttribute("download")) return;

    const cont = document.querySelector(".page-fade");
    if (!cont) return;

    e.preventDefault();
    cont.classList.remove("show");
    setTimeout(() => { window.location.href = href; }, 250);
  });

  const toReveal = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window && toReveal.length) {
    const io = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("in");
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12 });
    toReveal.forEach((el) => io.observe(el));
  } else {
    toReveal.forEach((el) => el.classList.add("in"));
  }
