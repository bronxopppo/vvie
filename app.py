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

        body {
            margin: 0;
            font-family: 'Poppins', sans-serif;
            background: linear-gradient(-45deg, #1a1a2e, #16213e, #0f3460, #533483);
            background-size: 400% 400%;
            animation: gradient-shift 15s ease infinite;
            color: white;
            overflow: hidden;
            position: relative;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            text-align: center;
        }

        @keyframes gradient-shift {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        /* --- CHAOS SCREEN STYLES --- */
        #chaos-screen {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            z-index: 5;
        }

        #chaosText {
            font-family: 'Creepster', cursive;
            font-size: 5em;
            color: #ff4757;
            text-shadow: 3px 3px #000;
            animation: shake 0.5s infinite;
        }

        /* --- FAKE CHROME WINDOWS STYLES --- */
        #fake-windows-container {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: 6;
        }

        .fake-chrome-window {
            position: absolute;
            width: 500px;
            height: 350px;
            background-color: #f0f0f0;
            border-radius: 8px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
            pointer-events: auto;
            display: flex;
            flex-direction: column;
            animation: bounce-in 0.5s cubic-bezier(0.68, -0.55, 0.265, 1.55);
        }

        .fake-chrome-header {
            background-color: #e8e8e8;
            padding: 8px;
            border-top-left-radius: 8px;
            border-top-right-radius: 8px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid #d3d3d3;
        }

        .fake-chrome-controls {
            display: flex;
            gap: 8px;
        }

        .fake-chrome-control-btn {
            width: 12px;
            height: 12px;
            border-radius: 50%;
            border: none;
            cursor: pointer;
        }
        .fake-chrome-control-btn.close { background-color: #ff5f57; }
        .fake-chrome-control-btn.minimize { background-color: #ffbd2e; }
        .fake-chrome-control-btn.maximize { background-color: #28ca42; }

        .fake-chrome-address-bar {
            flex-grow: 1;
            margin: 0 10px;
            padding: 5px 10px;
            border: 1px solid #ccc;
            border-radius: 4px;
            background-color: white;
            font-size: 12px;
            color: #555;
        }

        .fake-chrome-content {
            flex-grow: 1;
            padding: 15px;
            font-size: 14px;
            color: #333;
            background-color: white;
            border-bottom-left-radius: 8px;
            border-bottom-right-radius: 8px;
            overflow: auto;
        }

        .fake-alert {
            padding: 10px;
            border: 1px solid #f5c6cb;
            background-color: #f8d7da;
            color: #721c24;
            border-radius: 4px;
            margin-bottom: 10px;
        }

        @keyframes shake {
            0%, 100% { transform: translateX(0); }
            25% { transform: translateX(-10px) rotate(-5deg); }
            75% { transform: translateX(10px) rotate(5deg); }
        }

        @keyframes bounce-in {
            0% { transform: scale(0); opacity: 0; }
            50% { transform: scale(1.1); }
            100% { transform: scale(1); opacity: 1; }
        }

        /* Start overlay to unlock audio (browser autoplay policy) */
        #start-overlay {
            position: fixed;
            inset: 0;
            background: rgba(0,0,0,0.85);
            z-index: 9999;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            color: white;
        }
        #start-overlay h1 {
            font-size: 2.5em;
            margin-bottom: 10px;
            text-shadow: 0 0 20px rgba(255,255,255,0.5);
        }
        #start-overlay p {
            font-size: 1.1em;
            color: #ccc;
            animation: pulse 1.5s infinite;
        }
        @keyframes pulse {
            0%,100% { opacity: 0.6; }
            50% { opacity: 1; }
        }
    </style>
</head>
<body>

    <!-- Start overlay to unlock autoplay sound -->
    <div id="start-overlay">
        <h1>🚀 Click to Enter</h1>
        <p>Click anywhere to launch the experience</p>
    </div>

    <!-- The chaotic screen -->
    <div id="chaos-screen">
        <h1 id="chaosText">FUCKED!</h1>
    </div>

    <!-- Container for fake chrome windows -->
    <div id="fake-windows-container"></div>

    <!-- Background sound -->
    <audio id="backgroundSound" loop>
        <source src="https://files.catbox.moe/1fxqdw.mp3" type="audio/mpeg">
    </audio>

    <script>
        const chaosScreen = document.getElementById('chaos-screen');
        const backgroundSound = document.getElementById('backgroundSound');
        const fakeWindowsContainer = document.getElementById('fake-windows-container');
        const body = document.body;
        const startOverlay = document.getElementById('start-overlay');

        let chaosInterval;
        let started = false;

        function startChaos() {
            if (started) return;
            started = true;

            console.log("SUPER PRANK UNLEASHED!");

            startOverlay.style.display = 'none';

            // Play sound immediately (user gesture unlocks it)
            backgroundSound.volume = 0.7;
            backgroundSound.play().catch(err => console.log("Sound blocked:", err));

            chaosInterval = setInterval(() => {
                const randomColor = `hsl(${Math.random() * 360}, 100%, 50%)`;
                body.style.backgroundColor = randomColor;
            }, 200);

            // Open many fake chrome windows
            for (let i = 0; i < 300; i++) {
                setTimeout(() => {
                    createFakeChromeWindow();
                }, i * 200);
            }
        }

        function createFakeChromeWindow() {
            const windowEl = document.createElement('div');
            windowEl.classList.add('fake-chrome-window');

            const topOffset = Math.random() * (window.innerHeight - 350);
            const leftOffset = Math.random() * (window.innerWidth - 500);
            windowEl.style.top = topOffset + 'px';
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
                        <strong>Security Alert!</strong><br>
                        Your system has been compromised. Please do not close this window.
                    </div>
                    <p>Deleting system files...</p>
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

            const dragEnd = () => {
                initialX = currentX;
                initialY = currentY;
                isDragging = false;
            };

            const drag = (e) => {
                if (isDragging) {
                    e.preventDefault();
                    currentX = e.clientX - initialX;
                    currentY = e.clientY - initialY;
                    xOffset = currentX;
                    yOffset = currentY;
                    windowEl.style.transform = `translate(${currentX}px, ${currentY}px)`;
                }
            };

            windowEl.addEventListener('mousedown', dragStart);
            document.addEventListener('mouseup', dragEnd);
            document.addEventListener('mousemove', drag);

            const closeBtn = windowEl.querySelector('.fake-chrome-control-btn.close');
            closeBtn.addEventListener('click', () => {
                windowEl.style.animation = 'shake 0.2s infinite';
                const content = windowEl.querySelector('.fake-chrome-content');
                content.innerHTML = `<div class="fake-alert"><strong>Error!</strong><br>You cannot escape!</div>`;
            });
        }

        // Start chaos on first click anywhere
        startOverlay.addEventListener('click', startChaos);
        document.addEventListener('click', startChaos, { once: true });
        document.addEventListener('keydown', startChaos, { once: true });
    </script>

</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(HTML_PAGE)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
