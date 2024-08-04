let rotation = 0;
let isGrayScale = false;
function rotateImage() {
    rotation = rotation + 90; // Rotate 90 degrees at a time
    userImage.style.transform = `rotate(${rotation}deg)`;
    userImage.style.transformOrigin = "center center";
}

function grayscaleImage() {
    if (isGrayScale) {
        userImage.style.filter = "grayscale(0)";
        isGrayScale = false;
    } else {
        userImage.style.filter = "grayscale(1)";
        isGrayScale = true;
    }
}
function downloadImage() {
    if (imageFile === null) {
        alert("Please select an image file first.");
        return;
    }
    const formData = new FormData();
    formData.append("image", imageFile);
    formData.append("rotation", rotation % 360);
    formData.append("grayscale", isGrayScale);
    fetch("/upload", {
        method: "POST",
        body: formData,
    })
        .then((response) => response.blob())
        .then((blob) => {
            const url = URL.createObjectURL(blob);
            const a = document.createElement("a");
            a.href = url;
            a.download = "edited-image.png";
            a.click();
            URL.revokeObjectURL(url);
        });
}
