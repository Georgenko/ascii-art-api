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

async function handleResponseError(response) {
    let error;
    try {
        error = await response.json();
    } catch {
        throw new Error(`Request failed with status ${response.status}`);
    }
    throw new Error(error.detail ?? "Request failed"); // FastApi returns errors in "detail"
}
