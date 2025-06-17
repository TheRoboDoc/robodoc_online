document.addEventListener("DOMContentLoaded", function () {
    const boot = document.getElementById("boot-sequence");
    const raw = document.getElementById("raw-content");
    const container = document.getElementById("typed-container");

    const html = raw.innerHTML;
    let index = 0;
    let buffer = '';
    let inTag = false;
    let typing = true;

    const skipTyping = () => {
        typing = false;
        boot.style.display = "none";
        container.innerHTML = html;
        sessionStorage.setItem("visited", "true");
    };

    function typeHTML() {
        if (!typing || index >= html.length) {
            sessionStorage.setItem("visited", "true");
            return;
        }

        const char = html[index++];
        buffer += char;

        if (char === '<') inTag = true;
        if (char === '>') inTag = false;

        if (!inTag) {
            container.innerHTML = buffer;
        }

        requestAnimationFrame(typeHTML);
    }

    if (sessionStorage.getItem("visited")) {
        skipTyping();
    } else {
        setTimeout(() => {
            boot.style.display = "none";
            typeHTML();
        }, 800);
    }

    document.addEventListener("keydown", skipTyping);
    document.addEventListener("click", skipTyping);
});
