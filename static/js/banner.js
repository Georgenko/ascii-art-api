async function convertTextToBanner() {
    const text = document.getElementById("textarea-banner").value;
    const font = document.getElementById("select-font").value;
    const cyrillic = document.getElementById("checkbox-cyrillic").checked;
    const request = buildBannerRequest(text, font, cyrillic);

    try {
        const banner = await postTextToBanner(request);
        showResult(banner);
    } catch (err) {
        alert(`Failed to generate banner:\n${err.message}`);
    }
}

function buildBannerRequest(text, font = "standard", cyrillic = false) {
    return {text, font, cyrillic};
}
