const sections = ['text-to-banner', 'image-to-ascii', 'prompt-to-ascii', 'result-view', 'more'];
let lastSection = 'text-to-banner';

function show(id) {
    sections.forEach(s => document.getElementById(s).hidden = (s !== id));
    if (id !== 'result-view') lastSection = id;
}

show('text-to-banner');
