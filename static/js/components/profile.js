document.getElementById("resultRange").onchange = function() {
    const rangeVal = document.getElementById("resultRange").value;
    document.getElementById("numberOfResults").value = rangeVal;
}

const imageInput = document.getElementById('profile');
imageInput.addEventListener('change', function() {
    const imagePreview = document.getElementById('profile_preview');
    const file = imageInput.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function(e) {
          imagePreview.src = e.target.result;
        }
        reader.readAsDataURL(file);
    }
});

function showToast(message) {
      // Create a new toast element
      var toastElement = document.createElement("div");
      toastElement.classList.add("toast");
      toastElement.setAttribute("role", "alert");
      toastElement.setAttribute("aria-live", "assertive");
      toastElement.setAttribute("aria-atomic", "true");
      toastElement.setAttribute("data-bs-autohide", "true");
      toastElement.setAttribute("data-bs-delay", "3000");

      // Create the toast header
      var toastHeader = document.createElement("div");
      toastHeader.classList.add("toast-header", "bg-dark", "text-primary");
      var strongElement = document.createElement("strong");
      strongElement.classList.add("me-auto");
      strongElement.textContent = "Message";
      var closeButton = document.createElement("button");
      closeButton.setAttribute("type", "button");
      closeButton.classList.add("btn-close", "btn-close-white");
      closeButton.setAttribute("data-bs-dismiss", "toast");
      closeButton.setAttribute("aria-label", "Close");

      // Create the toast body
      var toastBody = document.createElement("div");
      toastBody.classList.add("toast-body", "bg-dark", "text-light");
      toastBody.textContent = message;

      // Build the toast structure
      toastHeader.appendChild(strongElement);
      toastHeader.appendChild(closeButton);
      toastElement.appendChild(toastHeader);
      toastElement.appendChild(toastBody);

      // Add the toast to the toast container
      var toastContainer = document.querySelector("#toastContainer");
      toastContainer.appendChild(toastElement);

      // Create an instance of bootstrap.Toast and show the toast
      var toast = new bootstrap.Toast(toastElement, {
        backdrop: false // Optional: Disable clicking outside to close the toast
      });
      toast.show();
}

document.getElementById('profileUpdate').addEventListener('submit', function(event) {
    var isValid = true;
    const question = document.getElementById('question').value.trim();
    if(question==''){
        showToast("Opps!! you forget to enter question.");
        isValid = false;
    }
    const email = document.getElementById('email').value.trim();
    if(!validateEmail(email)){
        showToast("Opps!! you enter invalid email.");
        isValid = false;
    }
    const firstname = document.getElementById('firstname').value.trim();
    if(firstname==''){
        showToast("Opps!! you forget to enter firstname.");
        isValid = false;
    }
    const lastname = document.getElementById('lastname').value.trim();
    if(lastname==''){
        showToast("Opps!! you forget to enter lastname.");
        isValid = false;
    }
    const description = document.getElementById('description').value.trim();
    if(description==''){
        showToast("Opps!! you forget to enter description.");
        isValid = false;
    }
    const phone = document.getElementById('phone').value.trim();
    if(phone!='' && !validatePhoneNumber(phone)){
        showToast("Opps!! you enter invalid phone.");
        isValid = false;
    }
    const instagram = document.getElementById('instagram').value.trim();
    if(instagram!='' && !validateInstagramLink(instagram)){
        showToast("Opps!! you enter invalid instagram profile.");
        isValid = false;
    }
    const linkedin = document.getElementById('linkedin').value.trim();
    if(linkedin!='' && validateLinkedInLink(linkedin)){
        showToast("Opps!! you enter invalid linkedin profile.");
        isValid = false;
    }
    const facebook = document.getElementById('facebook').value.trim();
    if(facebook!='' && !validateFacebookLink(facebook)){
        showToast("Opps!! you enter invalid facebook profile.");
        isValid = false;
    }
    if(!isValid){
        event.preventDefault();
    } else {
        this.submit();
    }
})

function validateEmail(email) {
    var pattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return pattern.test(email);
}

function validatePhoneNumber(phoneNumber) {
    var pattern = /^[5-9]\d{9}$/;
    return pattern.test(phoneNumber);
}

function validateInstagramLink(instagramLink) {
    var pattern = /^(?:https?:\/\/)?(?:www\.)?instagram\.com\/([A-Za-z0-9_\-\.]+)/;
    return pattern.test(instagramLink);
}

function validateLinkedInLink(linkedinLink) {
    var pattern = /^(?:https?:\/\/)?(?:www\.)?linkedin\.com\/in\/([A-Za-z0-9_\-\.]+)/;
    return pattern.test(linkedinLink);
}

function validateFacebookLink(facebookLink) {
    var pattern = /^(?:https?:\/\/)?(?:www\.)?facebook\.com\/([A-Za-z0-9_\-\.]+)/;
    return pattern.test(facebookLink);
}

