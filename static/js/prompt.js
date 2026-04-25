async function convertPromptToImage(){
    const prompt = document.getElementById("textarea-prompt").value;
    const minimal = document.getElementById("checkbox-minimal-prompt").checked;

    if (!prompt) {
        alert('Text cannot be empty');
        return;
    }

    const request = buildPromptRequest(prompt, minimal);

    try {
        const imageResult = await postPromptToImage(request);
        showResult(imageResult, "image-view");
    } catch (err) {
        alert(`Failed to convert prompt to ASCII:\n${err.message}`);
    }
}

function buildPromptRequest(prompt, minimal, width = 500, num_chars = 50) {
    return {prompt, width, num_chars, minimal};
}
