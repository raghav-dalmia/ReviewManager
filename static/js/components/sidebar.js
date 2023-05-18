document.addEventListener("DOMContentLoaded", () => {
    var links = document.querySelectorAll(".left-panel a")
    for(var link of links){
        if(link.href === window.location.href){
            link.classList.add('active-button')
        }
    }
});
