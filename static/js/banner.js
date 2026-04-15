async function convertTextToBanner() {
    const input = document.getElementById("textarea-banner").value;
    const font = document.getElementById("select-font").value;
    const cyrillic = document.getElementById("checkbox-cyrillic").checked;
    const request = buildBannerRequest(input, font, cyrillic);

    try {
        const banner = await postTextToBanner(request);
        showResult(banner);
    } catch (err) {
        console.error(err);
    }
}

function buildBannerRequest(prompt, font = "standard", cyrillic = false) {
    return {prompt, font, cyrillic};
}

function showResult(text) {
    document.getElementById("result").textContent = text;
    show('result-view');
}
