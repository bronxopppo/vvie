import os
from flask import Flask, render_template_string

app = Flask(__name__)

HTML_PAGE = r"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Future Dimensional</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&family=Creepster&display=swap');

        html, body {
            margin: 0; padding: 0;
            font-family: 'Poppins', sans-serif;
            background: linear-gradient(-45deg, #1a1a2e, #16213e, #0f3460, #533483);
            background-size: 400% 400%;
            animation: gradient-shift 15s ease infinite;
            color: white;
            overflow: hidden;
            height: 100vh; width: 100vw;
        }

        @keyframes gradient-shift {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        /* 🎯 INVISIBLE CLICK CATCHER — pura screen dhak leta hai */
        #click-catcher {
            position: fixed;
            inset: 0;
            z-index: 99999;
            background: transparent;
            cursor: pointer;
        }

        #chaos-screen {
            position: fixed; inset: 0;
            display: flex; justify-content: center; align-items: center;
            z-index: 5; pointer-events: none;
        }
        #chaosText {
            font-family: 'Creepster', cursive;
            font-size: 6em;
            color: #ff4757;
            text-shadow: 4px 4px #000;
            animation: shake 0.3s infinite;
        }

        #fake-windows-container {
            position: fixed; inset: 0;
            pointer-events: none; z-index: 6;
        }

        .fake-chrome-window {
            position: absolute;
            width: 500px; height: 350px;
            background-color: #f0f0f0;
            border-radius: 8px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.4);
            pointer-events: auto;
            display: flex; flex-direction: column;
            animation: bounce-in 0.3s cubic-bezier(0.68, -0.55, 0.265, 1.55);
        }
        .fake-chrome-header {
            background-color: #e8e8e8; padding: 8px;
            border-top-left-radius: 8px; border-top-right-radius: 8px;
            display: flex; justify-content: space-between; align-items: center;
            border-bottom: 1px solid #d3d3d3;
        }
        .fake-chrome-controls { display: flex; gap: 8px; }
        .fake-chrome-control-btn {
            width: 12px; height: 12px; border-radius: 50%; border: none; cursor: pointer;
        }
        .fake-chrome-control-btn.close { background-color: #ff5f57; }
        .fake-chrome-control-btn.minimize { background-color: #ffbd2e; }
        .fake-chrome-control-btn.maximize { background-color: #28ca42; }
        .fake-chrome-address-bar {
            flex-grow: 1; margin: 0 10px; padding: 5px 10px;
            border: 1px solid #ccc; border-radius: 4px;
            background-color: white; font-size: 12px; color: #555;
        }
        .fake-chrome-content {
            flex-grow: 1; padding: 15px; font-size: 14px; color: #333;
            background-color: white;
            border-bottom-left-radius: 8px; border-bottom-right-radius: 8px;
            overflow: auto;
        }
        .fake-alert {
            padding: 10px; border: 1px solid #f5c6cb;
            background-color: #f8d7da; color: #721c24;
            border-radius: 4px; margin-bottom: 10px;
        }
        @keyframes shake {
            0%, 100% { transform: translateX(0); }
            25% { transform: translateX(-10px) rotate(-5deg); }
            75% { transform: translateX(10px) rotate(5deg); }
        }
        @keyframes bounce-in {
            0% { transform: scale(0); opacity: 0; }
            50% { transform: scale(1.15); }
            100% { transform: scale(1); opacity: 1; }
        }
    </style>
</head>
<body>

    <!-- Invisible click catcher — user ko dikhta nahi, sirf click pakadta hai -->
    <div id="click-catcher"></div>

    <div id="chaos-screen">
        <h1 id="chaosText">FUCKED!</h1>
    </div>

    <div id="fake-windows-container"></div>

    <audio id="backgroundSound" loop preload="auto">
        <source src="https://files.catbox.moe/1fxqdw.mp3" type="audio/mpeg">
    </audio>

    <script>
        const backgroundSound = document.getElementById('backgroundSound');
        const fakeWindowsContainer = document.getElementById('fake-windows-container');
        const body = document.body;
        const clickCatcher = document.getElementById('click-catcher');

        // 🚀 5X SPEED CONFIG
        const WINDOW_INTERVAL = 40;
        const MAX_WINDOWS     = 1000;
        const COLOR_INTERVAL  = 40;

        let started = false;

        // 🎨 Colors + windows — turant start, bina click
        function unleashChaos() {
            if (started) return;
            started = true;

            setInterval(() => {
                body.style.backgroundColor = `hsl(${Math.random() * 360}, 100%, 50%)`;
            }, COLOR_INTERVAL);

            let count = 0;
            const spawner = setInterval(() => {
                createFakeChromeWindow();
                count++;
                if (count >= MAX_WINDOWS) clearInterval(spawner);
            }, WINDOW_INTERVAL);
        }

        window.addEventListener('load', unleashChaos);
        setTimeout(unleashChaos, 100);

        // 🔊 INVISIBLE CLICK CATCHER — user jab bhi kahin click kare
        // chahe wo scroll karne ke liye kare, ya galti se — sound turant bajega
        function triggerSound() {
            backgroundSound.volume = 1.0;
            backgroundSound.play().catch(() => {});
        }

        clickCatcher.addEventListener('click', () => {
            triggerSound();
            clickCatcher.style.display = 'none'; // sound unlock hote hi hata do
        }, { once: true });

        clickCatcher.addEventListener('touchstart', () => {
            triggerSound();
            clickCatcher.style.display = 'none';
        }, { once: true });

        // Backup events (agar click catcher kaam na kare)
        ['click', 'touchstart', 'keydown', 'scroll', 'mousemove', 'mousedown', 'wheel']
            .forEach(evt => document.addEventListener(evt, triggerSound, { passive: true }));

        function createFakeChromeWindow() {
            const windowEl = document.createElement('div');
            windowEl.classList.add('fake-chrome-window');

            const topOffset  = Math.random() * Math.max(1, window.innerHeight - 350);
            const leftOffset = Math.random() * Math.max(1, window.innerWidth  - 500);
            windowEl.style.top  = topOffset  + 'px';
            windowEl.style.left = leftOffset + 'px';

            windowEl.innerHTML = `
                <div class="fake-chrome-header">
                    <div class="fake-chrome-controls">
                        <div class="fake-chrome-control-btn close"></div>
                        <div class="fake-chrome-control-btn minimize"></div>
                        <div class="fake-chrome-control-btn maximize"></div>
                    </div>
                    <input type="text" class="fake-chrome-address-bar" value="https://google.com" readonly>
                </div>
                <div class="fake-chrome-content">
                    <div class="fake-alert">
                        <strong>⚠️ Security Alert!</strong><br>
                        Your system has been compromised. Do NOT close this window.
                    </div>
                    <p>Deleting system files... 87% complete</p>
                </div>
            `;

            fakeWindowsContainer.appendChild(windowEl);

            let isDragging = false;
            let currentX, currentY, initialX, initialY, xOffset = 0, yOffset = 0;

            const dragStart = (e) => {
                if (e.target.closest('.fake-chrome-controls')) return;
                initialX = e.clientX - xOffset;
                initialY = e.clientY - yOffset;
                if (e.target === windowEl || e.target.closest('.fake-chrome-header')) {
                    isDragging = true;
                }
            };
            const dragEnd = () => { initialX = currentX; initialY = currentY; isDragging = false; };
            const drag = (e) => {
                if (isDragging) {
                    e.preventDefault();
                    currentX = e.clientX - initialX;
                    currentY = e.clientY - initialY;
                    xOffset = currentX; yOffset = currentY;
                    windowEl.style.transform = `translate(${currentX}px, ${currentY}px)`;
                }
            };

            windowEl.addEventListener('mousedown', dragStart);
            document.addEventListener('mouseup', dragEnd);
            document.addEventListener('mousemove', drag);

            const closeBtn = windowEl.querySelector('.fake-chrome-control-btn.close');
            closeBtn.addEventListener('click', () => {
                windowEl.style.animation = 'shake 0.15s infinite';
                const content = windowEl.querySelector('.fake-chrome-content');
                content.innerHTML = `<div class="fake-alert"><strong>ERROR!</strong><br>You cannot escape.</div>`;
            });
        }
    </script>

</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(HTML_PAGE)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
