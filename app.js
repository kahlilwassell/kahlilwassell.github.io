// This is the script that will dynamically change the site
const dropdownMenu = document.querySelectorAll(".navbar-nav");
const dropdownButtons = document.querySelectorAll(".nav-item")
//const setSelectedDropdown = (option) => {
//    const dropdownIndex = option.currentTarget.dataset.dropdown;
//    const dropdownElement = document.getElementById(dropdownIndex);
//    console.log(dropdownElement);
//}

dropdownButtons.forEach((btn) => {
    btn.addEventListener("click", () => {
        console.log(btn)
    });
});