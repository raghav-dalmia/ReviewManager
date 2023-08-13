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

document.querySelectorAll('div[data-bs-toggle="collapse"]').forEach(collapseEle => {
    collapseEle.addEventListener('click', () => {
        const collapseIcon = collapseEle.getElementsByTagName("i")[0];
        let rotateVal = collapseIcon.getAttribute("data-rotate");
        rotateVal+=180;
        if(rotateVal>=360)
            rotateVal=0;
        collapseIcon.setAttribute("data-rotate", rotateVal);
        collapseIcon.style.transform = `rotate(${rotateVal}deg)`;
    });
});

const contactCollapse = document.getElementById('contact_collapse');
if (contactCollapse) {
    const inputElements = contactCollapse.querySelectorAll('input[type="url"]');
    inputElements.forEach(input => {
        input.addEventListener('blur', function() {
            const urlValue = this.value.trim();
            if (urlValue && !urlValue.startsWith('http://') && !urlValue.startsWith('https://')) {
                this.value = 'https://' + urlValue;
            }
        });
    });
}

document.getElementById('profileUpdate').addEventListener('input', () => {
      document.getElementById('footer').style.display = 'block';
      document.getElementById('profileUpdate').style.marginBottom = '10vh';
});
