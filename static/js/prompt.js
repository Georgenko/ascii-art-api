async function convertPromptToImage(){
    const prompt = document.getElementById("textarea-prompt").value;

    if (!prompt) {
        alert('Text cannot be empty');
        return;
    }

    const request = buildPromptRequest(prompt);

    try {
        const imageResult = await postPromptToImage(request);
        showResult(imageResult, "pre-image", "image-view");
    } catch (err) {
        alert(`Failed to convert prompt to ASCII:\n${err.message}`);
    }
}


function buildPromptRequest(prompt, width = 500, num_chars = 50, minimal = true) {
    return {prompt, width, num_chars, minimal};
}
