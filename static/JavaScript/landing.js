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



let desti_imgs = document.querySelectorAll(".desti_img");
desti_imgs.forEach((img) => {
    img.addEventListener("click", () => {
        alert('Redirecting to your destination');
        window.location.href= "/static/templates/index.html";
    })
})


// **************************************************************
// js  for the search


// ********************************************** js on email button

document.getElementById("button_connect").addEventListener("click", function(){
    window.location.href = "mailto:"
})