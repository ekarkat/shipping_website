/* ======= SHOW MENU ========*/
document.addEventListener("DOMContentLoaded", function() {

    const panel = document.getElementById('panel');
    const navToggle = document.getElementById('nav__toggle');
    const navClose = document.getElementById('nav__close');
    navClose.style.display = 'none'
    // Show the panel of icons
    if (navToggle) {
        navToggle.addEventListener('click', () => {
            panel.classList.add('show-panel');
            navClose.style.display = 'block'
        });
    }
    // Hide the Panel
    if (navClose) {
        navClose.addEventListener('click', () => {
            panel.classList.remove('show-panel');
            navClose.style.display = 'none'

        });
    }
    const logItem = document.querySelectorAll('.login_item');
    const linkAction = () =>{
        const panel = document.getElementById('panel')
        // when we click on each logItem, we remove the show panel class
        panel.classList.remove('show-panel');
        navClose.style.display = 'none'
    }

    logItem.forEach(n => n.addEventListener('click', linkAction))

    const blurheader = () => {
        const header = document.getElementById('header');
        window.scrollY >= 10 ? header.classList.add('blur-header') : header.classList.remove('blur-header');
    }
    window.addEventListener('scroll', blurheader);


    const scrollUp = () =>{
        const scrollUp = document.getElementById('scroll-up')
        // when the scroll is higher than 350 -viewport height 
        this.scrollY >= 350 ? scrollUp.classList.add('show-scroll')
                            : scrollUp.classList.remove('show-scroll');
    }
    window.addEventListener('scroll', scrollUp)
    
    /* ==================== SCROLL SECTIONS ACTIVE LINK ===================== */
    const sections = document.querySelectorAll('section[id]')

    const scrollActive = () => {
        const scrollDown = window.scrollY
        sections.forEach(current => {
            const sectionHeight = current.offsetHeight,
                    sectionTop = current.offsetTop - 58,
                    sectionId = current.getAttribute('id'),
                    sectionsClass = document.querySelector(".panel a[href*=" + sectionId + "]")

                    if(scrollDown > sectionTop && scrollDown <= sectionTop + sectionHeight){
                        sectionsClass.classList.add('active-link')
                    }else{
                        sectionsClass.classList.remove('active-link')
                    }
        })
    }
    window.addEventListener('scroll', scrollActive)

})








