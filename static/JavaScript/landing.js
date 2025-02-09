document.addEventListener("DOMContentLoaded", function () {
    const welcomeScreen = document.getElementById("welcome-screen");
    const mainContent = document.getElementById("main-content");

    // Show welcome screen for 3 seconds, then fade out and show main content
    setTimeout(() => {
        welcomeScreen.classList.add("hidden");
        setTimeout(() => {
            welcomeScreen.style.display = "none";
            mainContent.style.display = "block";
        }, 1000);
    }, 3000);
});