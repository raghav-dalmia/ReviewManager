document.getElementById("copyLink").addEventListener("click", copyLink, false);
function copyLink() {
    navigator.clipboard.writeText("http://127.0.0.1:8000{% url 'reviewForm' username=user.username %}");
    alert("link copied");
}

document.getElementById("resultRange").onchange = function() {
    const rangeVal = document.getElementById("resultRange").value;
    document.getElementById("numberOfResults").value = rangeVal;
}
