
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



    document.addEventListener("DOMContentLoaded", function () {
        // Accept Terms Button Click Event
        const acceptButton = document.querySelector(".accept-terms");
    
        if (acceptButton) {
            acceptButton.addEventListener("click", function () {
                alert("Thank you for accepting the Terms and Conditions!");
                // Store acceptance in localStorage
                localStorage.setItem("termsAccepted", "true");
            });
        }
    
        // Smooth Scrolling for Internal Links
        document.querySelectorAll("a[href^='#']").forEach(anchor => {
            anchor.addEventListener("click", function (e) {
                e.preventDefault();
                document.querySelector(this.getAttribute("href")).scrollIntoView({
                    behavior: "smooth"
                });
            });
        });
    
        // Sticky Navigation Effect
        const header = document.querySelector(".header");
        if (header) {
            window.addEventListener("scroll", function () {
                if (window.scrollY > 50) {
                    header.classList.add("sticky");
                } else {
                    header.classList.remove("sticky");
                }
            });
        }
    });
    

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


        document.addEventListener("DOMContentLoaded", function () {
            const filterButtons = document.querySelectorAll(".filter-btn");
            const pressCards = document.querySelectorAll(".press-card");
        
            filterButtons.forEach(button => {
                button.addEventListener("click", function () {
                    filterButtons.forEach(btn => btn.classList.remove("active"));
                    this.classList.add("active");
        
                    const filterValue = this.getAttribute("data-filter");
        
                    pressCards.forEach(card => {
                        const category = card.getAttribute("data-category");
        
                        if (filterValue === "all" || category === filterValue) {
                            card.style.display = "block";
                        } else {
                            card.style.display = "none";
                        }
                    });
                });
            });
        });
            

