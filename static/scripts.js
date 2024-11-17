document.addEventListener("DOMContentLoaded", function () {
    // Example JavaScript to enhance interactivity
    // Add your custom JS here

    // Example: Basic form validation
    const forms = document.querySelectorAll("form");
    forms.forEach(form => {
        form.addEventListener("submit", function (event) {
            // Add custom validation logic if needed
            const inputs = form.querySelectorAll("input, select");
            let isValid = true;
            inputs.forEach(input => {
                if (!input.value) {
                    isValid = false;
                    input.style.border = "1px solid red";
                } else {
                    input.style.border = "";
                }
            });
            if (!isValid) {
                event.preventDefault();
                alert("Please fill in all fields.");
            }
        });
    });
});
