
    document.addEventListener("DOMContentLoaded", function () {
        const prevButton = document.querySelector(".carousel-button.prev");
        const nextButton = document.querySelector(".carousel-button.next");
        const carousel = document.querySelector(".blog-carousel");

        const scrollAmount = 320; // Adjust scroll amount (depends on card width)

        nextButton.addEventListener("click", function () {
            carousel.scrollBy({ left: scrollAmount, behavior: "smooth" });
        });

        prevButton.addEventListener("click", function () {
            carousel.scrollBy({ left: -scrollAmount, behavior: "smooth" });
        });
    });




    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });

    // Update active navigation item based on scroll position
    const sections = document.querySelectorAll('.section');
    const navLinks = document.querySelectorAll('.nav-menu a');

    function updateActiveNavItem() {
        let currentSection = '';
        
        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.clientHeight;
            if (window.scrollY >= sectionTop - 100) {
                currentSection = section.getAttribute('id');
            }
        });

        navLinks.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href') === `#${currentSection}`) {
                link.classList.add('active');
            }
        });
    }

    // Show/hide back to top button
    const backToTop = document.querySelector('.back-to-top');

    function updateBackToTop() {
        if (window.scrollY > 300) {
            backToTop.classList.add('visible');
        } else {
            backToTop.classList.remove('visible');
        }
    }

    // Event listeners
    window.addEventListener('scroll', () => {
        updateActiveNavItem();
        updateBackToTop();
    });

    const stats = document.querySelectorAll('.stat-item h3');
        const observerOptions = {
            threshold: 0.5,
            rootMargin: '0px'
        };

        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.style.opacity = 1;
                    entry.target.style.transform = 'translateY(0)';
                }
            });
        }, observerOptions);

        stats.forEach(stat => {
            stat.style.opacity = 0;
            stat.style.transform = 'translateY(20px)';
            stat.style.transition = 'all 0.6s ease';
            observer.observe(stat);
        });

