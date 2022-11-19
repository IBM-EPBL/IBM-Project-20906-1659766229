// <!-- nav bar scripts -->
    // grab everything we need
    const btn = document.querySelector('button.mobile-menu-button');
    const menu = document.querySelector(".mobile-menu");
    const btnclose = document.querySelector(".btnclose")

    // add event listener
    btn.addEventListener("click", () => {
        menu.classList.remove("hidden");
    });
    btnclose.addEventListener("click",()=>{
        menu.classList.add("hidden");
    })
// <!-- nav bar end -->