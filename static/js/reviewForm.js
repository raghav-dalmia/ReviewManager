document.querySelectorAll('.feedback li').forEach(entry => entry.addEventListener('click', e => {
    if(!entry.classList.contains('active')) {
        document.querySelector('.feedback li.active').classList.remove('active');
        entry.classList.add('active');
        document.getElementById("rating").value = entry.getAttribute("data-val");
    }
    e.preventDefault();
}));

let id = 0;
const inputImageMap = new Map();
const imageContainer = $("#previewImages");

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

function clearImage(pid) {
    $("#prev_"+pid).remove();
    inputImageMap.delete(pid);
}

function compressImage(file, callback) {
    const reader = new FileReader();
    reader.onload = function (event) {
        const img = new Image();
        img.src = event.target.result;

        img.onload = function () {
            const canvas = document.createElement('canvas');
            const ctx = canvas.getContext('2d');
            const maxWidth = 800;
            const maxHeight = 800;
            let width = img.width;
            let height = img.height;

            if (width > maxWidth) {
                height *= maxWidth / width;
                width = maxWidth;
            }

            if (height > maxHeight) {
                width *= maxHeight / height;
                height = maxHeight;
            }

            canvas.width = width;
            canvas.height = height;
            ctx.drawImage(img, 0, 0, width, height);

            canvas.toBlob(function (blob) {
                callback(blob);
            }, 'image/jpeg', 0.8);
        };
    };

    reader.readAsDataURL(file);
}

$("#attachment").on("change", function (e) {
    const files = e.target.files;
    const filesArr = Array.prototype.slice.call(files);
    filesArr.forEach(function (file, index) {
        if (!file.type.match('image.*')) {
          return;
        }
        if (file.size > 100 * 1024) {
            compressImage(file, function (compressedBlob) {
                const compressedFile = new File([compressedBlob], file.name, {
                    type: 'image/jpeg',
                });
                inputImageMap[id]=compressedFile;
            });
        } else {
            inputImageMap[id]=file;
        }
        id += 1
        const reader = new FileReader();
        reader.onload = function (e) {
            const htmlPreview = "<div id='prev_" + id + "' class=\"col-3\">\n" +
            "                        <div class=\"position-relative border border-white rounded\" style=\"height: 60px; width: 60px; background-size: cover; background-repeat: no-repeat; background-image:url(" + e.target.result + " \">\n" +
            "                            <span class=\"position-absolute top-0 start-100 translate-middle text-center badge border border-light rounded-circle bg-dark\" style='cursor: pointer;' onclick='clearImage(" + id + ")'>\n" +
            "                                <i class=\"fa-solid fa-xmark\"></i>\n" +
            "                            </span>\n" +
            "                        </div>\n" +
            "                    </div>";
            imageContainer.append(htmlPreview);
        }
        reader.readAsDataURL(file);
    });
});

function isValidInput(inputImages) {
    const igHandle = $("#igHandle").val();
    if(igHandle && igHandle>200)
        return false;
    const rating = $("#rating").val();
    if(rating<1 || rating>5)
        return false;
    const packaging = $("#packaging").val();
    if(packaging && packaging.length > 1500)
        return false;
    const feedback = $("#feedback");
    if(feedback && feedback.val())
        return feedback.val().length <= 1500;
    return true;
}
$("#formSubmit").on('click', function (e) {
    e.preventDefault();
    const subUrl = $("#formSubmit").attr("data-action");
    var inputImages = new Array()
    for(var image_id = 0; image_id < id; image_id++){
        inputImages.push(inputImageMap[image_id])
    }
    if(!isValidInput(inputImages)){
        showToast("Opps!! something went wrong... Please try again.");
        return;
    }
    const reviewFormData = new FormData($('form')[0]);
    reviewFormData.append('attachment', inputImages);
    $.ajax({
        url: subUrl,
        type: 'POST',
        cache: false,
        contentType: false,
        processData: false,
        enctype: 'multipart/form-data',
        data: reviewFormData,
        success: function () {
            window.location.reload(true);
        },
        error: function (err) {
            showToast("Opps!! something went wrong... Please try again.");
        }
    });
    
});