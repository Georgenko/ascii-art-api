async function convertTextToBanner() {
    const input = document.querySelector("#text-to-banner textarea");
    const request = buildBannerRequest(input.value);

    try {
        const banner = await postTextToBanner(request);
        showResult(banner);
    } catch (err) {
        console.error(err.message);
    }
}

function buildBannerRequest(prompt, font = "standard", cyrillic = false) {
    return {prompt, font, cyrillic};
}

function showResult(text) {
    document.getElementById("result").textContent = text;
    show('result-view');
}
