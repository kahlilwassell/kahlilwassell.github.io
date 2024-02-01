// This is the script that will dynamically change the site
const dropdownButtons = document.querySelectorAll(".nav-item");

const setSelectedDropdown = (option) => {
    // Clear the selected state from all buttons
    dropdownButtons.forEach(button => {
        button.classList.remove('selected'); // Assuming 'selected' is the class for selected state
    });

    // Add the selected state to the clicked button
    option.currentTarget.classList.add('selected');
};

// Event listener
dropdownButtons.forEach((btn) => {
    btn.addEventListener("click", (event) => {
        setSelectedDropdown(event);
    });
});

document.getElementById('skillsButton').addEventListener('click', function() {
    window.location.href = '#skills';
});

document.getElementById('workButton').addEventListener('click', function() {
    window.location.href = '#work';
});