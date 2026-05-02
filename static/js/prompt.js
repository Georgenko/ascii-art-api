async function convertPromptToImage(){
    const prompt = document.getElementById("textarea-prompt").value;

    const { minimal, width, numChars } = getImageOptions();

    if (!prompt) {
        alert('Text cannot be empty');
        return;
    }

    const request = buildPromptRequest(prompt, minimal, width, numChars);

    setSectionLoading(true);

    try {
        const imageResult = await postPromptToImage(request);
        showResult(imageResult, "image-view");
    } catch (err) {
        alert(`Failed to convert prompt to ASCII:\n${err.message}`);
    } finally {
        setSectionLoading(false);
    }
}

function buildPromptRequest(prompt, minimal, width, num_chars) {
    return {prompt, width, num_chars, minimal};
}

function setSectionLoading(loading) {
    document.getElementById("spinner").hidden = !loading;
    document.querySelector("#prompt-to-ascii button").disabled = loading;
    document.querySelector("#textarea-prompt").disabled = loading;
    document.querySelectorAll("#image-options input").forEach(input => input.disabled = loading);
}
