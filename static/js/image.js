async function convertImageToImage(){
    const fileInput = document.querySelector('#image-to-ascii input[type="file"]');
    const file = fileInput.files[0];

    const minimal = document.getElementById("checkbox-minimal-image").checked;

    if (!file) {
        alert('Please select an image first');
        return;
    }

    const formData = new FormData();
    formData.append('image', file);

    try { // TODO: add width input in html and get from user
        const imageResult = await postImageToImage(formData, minimal, 500)
        showResult(imageResult, "image-view");
    } catch (err) {
        alert(`Failed to convert image to ascii:\n${err.message}`);
    }
}
