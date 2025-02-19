let scrollPosition = 0;
let dayScrollPosition = 0;
const slideWidth = 260;
const daySlideWidth = 420;
const visibleItems = 4;

function slide(direction) {
    const slider = document.getElementById('famous-slider');
    const maxScroll = (slider.children.length - visibleItems) * slideWidth;
    scrollPosition = direction === 'left' ? Math.max(scrollPosition - slideWidth * visibleItems, 0) : Math.min(scrollPosition + slideWidth * visibleItems, maxScroll);
    slider.style.transform = `translateX(-${scrollPosition}px)`;
}

function slideDay(direction) {
    const slider = document.getElementById('day-slider');
    const maxScroll = (slider.children.length - visibleItems) * daySlideWidth;
    dayScrollPosition = direction === 'left' ? Math.max(dayScrollPosition - daySlideWidth, 0) : Math.min(dayScrollPosition + daySlideWidth, maxScroll);
    slider.style.transform = `translateX(-${dayScrollPosition}px)`;
}