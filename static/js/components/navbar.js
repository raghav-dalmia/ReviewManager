const navItem = document.querySelector(".header .container nav");
const items = document.querySelectorAll(".header .container nav a");
const barIcon = document.querySelector(".bar-icon");
const closeIcon = document.querySelector(".close-icon");
const overlay = document.querySelector(".overlay");
const redirectTabPanel = document.querySelector(".redirect-tab-panel")

items.forEach((item) => {
  item.addEventListener("click", () => {
    items.forEach((item) => {
      item.classList.remove("active");
    });
  });
  item.addEventListener("click", () => {
    item.classList.add("active");
  });
});

barIcon.addEventListener("click", () => {
  navItem.classList.toggle("active");
  overlay.classList.toggle("active");
});

closeIcon.addEventListener("click", () => {
  navItem.classList.toggle("active");
  overlay.classList.toggle("active");
});

overlay.addEventListener("click", () => {
  navItem.classList.toggle("active");
  overlay.classList.toggle("active");
});

redirectTabPanel.addEventListener("click", () => {
    redirectTabPanel.classList.toggle("active")
});

document.addEventListener("DOMContentLoaded", () => {
  console.log("okay")
  var links = document.querySelectorAll(".right-panel div a")
  for(var link of links){
      if(link.href === window.location.href){
          link.classList.add('active-button')
      }
  }
});