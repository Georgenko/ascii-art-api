const BASE_URL = window.location.hostname === "127.0.0.1"
  ? "http://127.0.0.1:8000"
  : ""; // empty when project is built on Render

async function getFonts(cyrillic = false) {
    const response = await fetch(`${BASE_URL}/fonts?cyrillic=${cyrillic}`);
    if (!response.ok) await handleResponseError(response);
    return response.json();
}

async function postTextToBanner(requestBody) {
    const response = await fetch(`${BASE_URL}/text-to-banner`, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(requestBody),
    });
    if (!response.ok) await handleResponseError(response);
    return response.text();
}

async function postImageToImage(imageData, minimal, width) {
    const response = await fetch (`${BASE_URL}/image-to-image?minimal=${minimal}&width=${width}`, {
        method: "POST",
        body: imageData
    });
    if (!response.ok) await handleResponseError(response);
    return response.text();
}

async function postPromptToImage(requestBody) {
    const response = await fetch (`${BASE_URL}/prompt-to-image`, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(requestBody),
    });
    if (!response.ok) await handleResponseError(response);
    return response.text();
}

async function handleResponseError(response) {
    let error;
    try {
        error = await response.json();
    } catch {
        throw new Error(`Request failed with status ${response.status}`);
    }

    const detail = error?.detail;

    if (typeof detail === "string") {
        throw new Error(detail);
    }

    if (Array.isArray(detail) && detail.length > 0) {
        const { msg, loc } = detail[0];
        throw new Error(`${msg}\n${loc}`);
    }

    throw new Error(`Request failed with status ${response.status}`);
}
