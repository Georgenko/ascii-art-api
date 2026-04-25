const sections = ['text-to-banner', 'image-to-ascii', 'prompt-to-ascii', 'banner-view', 'image-view', 'docs'];
// TODO: extract constants somewhere and reuse throughout JS and maybe HTML/CSS?
let lastSection = 'text-to-banner';

function show(id) {
    sections.forEach(s => document.getElementById(s).hidden = (s !== id));
    if (id !== 'banner-view' && id !== 'image-view') lastSection = id;
}

show('text-to-banner');

function showResult(result, divElemId) {
    document.querySelector(`#${divElemId} pre`).textContent = result;
    show(divElemId);
}
