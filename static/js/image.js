async function convertImageToAscii(){
    const fileInput = document.querySelector('#image-to-ascii input[type="file"]');
    const file = fileInput.files[0];

    if (!file) {
        alert('Please select an image first');
        return;
    }

    const formData = new FormData();
    formData.append('image', file);

    const minimal = true;
    try {
        const result = await postImageToAscii(formData, minimal)
        showResult(result);
    } catch (err) {
        alert(`Failed to convert image to ascii:\n${err.message}`);
    }
}
