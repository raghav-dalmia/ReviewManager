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
      var toastElement = document.createElement("div");
      toastElement.classList.add("toast");
      toastElement.setAttribute("role", "alert");
      toastElement.setAttribute("aria-live", "assertive");
      toastElement.setAttribute("aria-atomic", "true");
      toastElement.setAttribute("data-bs-autohide", "true");
      toastElement.setAttribute("data-bs-delay", "5000");

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

      var toastBody = document.createElement("div");
      toastBody.classList.add("toast-body", "bg-dark", "text-light");
      toastBody.textContent = message;

      toastHeader.appendChild(strongElement);
      toastHeader.appendChild(closeButton);
      toastElement.appendChild(toastHeader);
      toastElement.appendChild(toastBody);

      var toastContainer = document.querySelector("#toastContainer");
      toastContainer.appendChild(toastElement);

      var toast = new bootstrap.Toast(toastElement, {
        backdrop: false
      });
      toast.show();
}

document.getElementById('urlForm').addEventListener('click', function(event) {
    var isValid = true;
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
    const description = document.getElementById('description').value.trim();
    if(description==''){
        showToast("Opps!! you forget to enter description.");
        isValid = false;
    }
//    const instagram = document.getElementById('instagram').value.trim();
//    if(instagram!='' && !validateInstagramLink(instagram)){
//        showToast("Opps!! you enter invalid instagram profile.");
//        isValid = false;
//    }
//    const linkedin = document.getElementById('linkedin').value.trim();
//    if(linkedin!='' && validateLinkedInLink(linkedin)){
//        showToast("Opps!! you enter invalid linkedin profile.");
//        isValid = false;
//    }
//    const facebook = document.getElementById('facebook').value.trim();
//    if(facebook!='' && !validateFacebookLink(facebook)){
//        showToast("Opps!! you enter invalid facebook profile.");
//        isValid = false;
//    }
    if(!isValid){
        event.preventDefault();
    } else {
        document.getElementById('profileUpdate').submit();
    }
})

function validateEmail(email) {
    var pattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return pattern.test(email);
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

const ele = document.getElementById('rotate-icon');
let cr = 0;
ele.addEventListener('click', () => {
  cr = (cr+180)%360;
  ele.style.transform = `rotate(${cr}deg)`;
});

const ele1 = document.getElementById('rotate-icon-1');
let cr1 = 0;
ele1.addEventListener('click', () => {
  cr1 = (cr1+180)%360;
  ele1.style.transform = `rotate(${cr1}deg)`;
});

const ele2 = document.getElementById('rotate-icon-2');
let cr2 = 0;
ele2.addEventListener('click', () => {
  cr2 = (cr2+180)%360;
  ele2.style.transform = `rotate(${cr2}deg)`;
});
