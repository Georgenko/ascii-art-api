async function convertTextToBanner() {
    const input = document.getElementById("textarea-banner").value;
    const font = document.getElementById("select-font").value;
    const cyrillic = document.getElementById("checkbox-cyrillic").checked;
    const request = buildBannerRequest(input, font, cyrillic);

    try {
        const banner = await postTextToBanner(request);
        showResult(banner);
    } catch (err) {
        alert(`Failed to generate banner:\n${err.message}`);
    }
}

function buildBannerRequest(prompt, font = "standard", cyrillic = false) {
    return {prompt, font, cyrillic};
}
