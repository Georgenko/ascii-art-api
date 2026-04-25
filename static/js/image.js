async function convertImageToImage(){
    const fileInput = document.querySelector('#image-to-ascii input[type="file"]');
    const file = fileInput.files[0];

    const minimal = document.getElementById("checkbox-minimal-image").checked;
    let width = document.getElementById("image-width").value;
    let numChars = document.getElementById("image-num-chars").value;

    if (!width) {
        width = 500;
    } else {
        if (width && (width <= 0 || width > 10000)) {
            alert("Please enter a Width > 0 and <= 10000");
            return;
        }
    }

    if (!minimal) {
        if (!numChars) {
            alert("Please enter a Number of characters when non-minimal");
            return;
        }

        if (numChars <= 0 || numChars > 70) {
            alert("Please enter a Number of characters > 0 and <= 70");
            return;
        }
    } else {
        numChars = 70;
    }
    // TODO: when choosing a width that is 1000 for banana.png i get the bug of shrinking nav section
    // and its text overflows

    if (!file) {
        alert('Please select an image first');
        return;
    }

    const formData = new FormData();
    formData.append('image', file);

    try {
        const imageResult = await postImageToImage(formData, minimal, width, numChars);
        showResult(imageResult, "image-view");
    } catch (err) {
        alert(`Failed to convert image to ascii:\n${err.message}`);
    }
}
