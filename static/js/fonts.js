async function loadBannerFonts() {
    const cyrillic = document.getElementById("checkbox-cyrillic").checked;

    try {
        const data = await getFonts(cyrillic);
        populateFontSelect(data.fonts);
    } catch (err) {
        console.error("Failed to load fonts:", err);
    }
}

function populateFontSelect(fonts) {
    const select = document.getElementById("select-font");
    select.innerHTML = '';

    const fragment = document.createDocumentFragment();
    fonts.forEach((font) => {
        const option = document.createElement('option');
        option.value = font;
        option.textContent = font;
        fragment.appendChild(option);
    });
    select.appendChild(fragment);
}

loadBannerFonts().catch(e => alert(e.message));
