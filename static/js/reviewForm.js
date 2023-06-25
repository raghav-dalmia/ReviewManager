document.querySelectorAll('.feedback li').forEach(entry => entry.addEventListener('click', e => {
    if(!entry.classList.contains('active')) {
        document.querySelector('.feedback li.active').classList.remove('active');
        entry.classList.add('active');
        document.getElementById("rating").value = entry.getAttribute("data-val");
    }
    e.preventDefault();
}));

let textarea = document.getElementById("feedback");
let heightLimit = 200;
let id = 0;
const inputImageMap = new Map();
const imageContainer = $("#previewImages");

textarea.oninput = function() {
  textarea.style.height = "";
  textarea.style.height = Math.min(textarea.scrollHeight, heightLimit) + "px";
};

function clearImage(pid) {
    console.log("Deleting " + pid)
    $("#prev_"+pid).remove();
    inputImageMap.delete(pid);
}

function clearFormData(id) {
    $('#form')[0].reset()
    for(let image_id = 1; image_id <= id; image_id++){
        console.log(image_id)
        clearImage(image_id)
    }
}

$("#attachment").on("change", function (e) {
    const files = e.target.files;
    const filesArr = Array.prototype.slice.call(files);
    filesArr.forEach(function (file, index) {
        if (!file.type.match('image.*')) {
          return;
        }
        inputImageMap[id]=file;
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
    const feedback = $("#feedback").val();
    return feedback && feedback.length <= 1500;

}
$("#formSubmit").on('click', function (e) {
    e.preventDefault();
    const subUrl = $("#formSubmit").attr("data-action");
    var inputImages = new Array()
    for(var image_id = 0; image_id < id; image_id++){
        inputImages.push(inputImageMap[image_id])
    }
    if(!isValidInput(inputImages)){
        alert("form not valid");
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
            alert('success');
            clearFormData(id);
        },
        error: function (err) {
            alert('error' + err.toString());
        }
    });
    
});