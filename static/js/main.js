document.addEventListener("DOMContentLoaded", () => {
    // Current year in footer
    const yearEl = document.getElementById("year");
    if (yearEl) {
        yearEl.textContent = new Date().getFullYear();
    }

    // Theme toggle
    const themeToggle = document.getElementById("theme-toggle");
    const htmlEl = document.documentElement;
    const themeIcon = document.getElementById("theme-icon");

    // Load saved theme
    const savedTheme = localStorage.getItem("theme") || "dark";
    htmlEl.setAttribute("data-bs-theme", savedTheme);
    updateThemeIcon(savedTheme);

    if (themeToggle) {
        themeToggle.addEventListener("click", () => {
            const currentTheme = htmlEl.getAttribute("data-bs-theme");
            const newTheme = currentTheme === "dark" ? "light" : "dark";
            htmlEl.setAttribute("data-bs-theme", newTheme);
            localStorage.setItem("theme", newTheme);
            updateThemeIcon(newTheme);
        });
    }

    function updateThemeIcon(theme) {
        if (!themeIcon) return;
        if(theme === "dark") {
            themeIcon.classList.replace("bi-moon-fill", "bi-sun-fill");
        } else {
            themeIcon.classList.replace("bi-sun-fill", "bi-moon-fill");
        }
    }

    // Scroll Observer for Fade-in
    const observerOptions = {
        threshold: 0.1,
        rootMargin: "0px 0px -50px 0px"
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if(entry.isIntersecting) {
                entry.target.classList.add("visible");
                observer.unobserve(entry.target); // Output animation once
            }
        });
    }, observerOptions);

    document.querySelectorAll(".fade-in-up").forEach(el => observer.observe(el));
    
    // Back to top behavior
    const backToTop = document.getElementById("back-to-top");
    if (backToTop) {
        window.addEventListener("scroll", () => {
            if(window.scrollY > 300) {
                backToTop.style.display = "block";
            } else {
                backToTop.style.display = "none";
            }
        });

        backToTop.addEventListener("click", () => {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    }
});
