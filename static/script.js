const imageContainer = document.querySelector(".image-editor");
const userImage = document.querySelector("#user-image");
const imageUpload = document.querySelector("#user-image-upload");
const downloadButton = document.querySelector(".download-button");
let imageFile = null;
function uploadImage() {
    imageFile = imageUpload.files[0];
    const reader = new FileReader();
    reader.readAsDataURL(imageFile);
    reader.onload = function () {
        userImage.src = reader.result;
        downloadButton.style.display = "block";
    };
}
