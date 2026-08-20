<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
    <title>✨ RAJA BOT PANEL ✨</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;700&display=swap');

        :root {
            --pink-primary: #ff4d8d;
            --purple-primary: #d500f9;
            --blue-primary: #2979ff;
            --gold: #ffd700;
        }

        body {
            margin: 0;
            padding: 20px 10px;
            font-family: 'Poppins', sans-serif;
            background: linear-gradient(135deg, #ff4d8d, #d500f9, #2979ff);
            background-size: 400% 400%;
            animation: gradientBG 15s ease infinite;
            color: #fff;
            display: flex;
            flex-direction: column;
            min-height: 100vh;
            overflow-x: hidden;
            max-width: 100%;
        }

        @keyframes gradientBG {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        .title-container {
            text-align: center;
            margin-bottom: 25px;
            perspective: 1000px;
        }

        .sonam-barbie-title {
            font-size: clamp(2rem, 6vw, 3.5rem);
            font-weight: 700;
            text-align: center;
            margin: 0 0 10px;
            color: white;
            text-shadow: 0 0 5px #fff, 0 0 10px var(--pink-primary), 0 0 15px var(--purple-primary), 0 0 20px var(--blue-primary);
            user-select: none;
            animation: rgbGlow 3s linear infinite, float3d 6s ease-in-out infinite;
            display: inline-block;
            padding: 10px 20px;
            border-radius: 20px;
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(5px);
            border: 1px solid rgba(255, 255, 255, 0.3);
        }

        @keyframes rgbGlow {
            0% { text-shadow: 0 0 5px #fff, 0 0 10px var(--pink-primary), 0 0 15px var(--purple-primary), 0 0 20px var(--blue-primary); }
            33% { text-shadow: 0 0 5px #fff, 0 0 10px var(--purple-primary), 0 0 15px var(--blue-primary), 0 0 20px var(--pink-primary); }
            66% { text-shadow: 0 0 5px #fff, 0 0 10px var(--blue-primary), 0 0 15px var(--pink-primary), 0 0 20px var(--purple-primary); }
            100% { text-shadow: 0 0 5px #fff, 0 0 10px var(--pink-primary), 0 0 15px var(--purple-primary), 0 0 20px var(--blue-primary); }
        }

        @keyframes float3d {
            0%, 100% { transform: translateY(0) rotateX(5deg) rotateY(5deg); }
            50% { transform: translateY(-10px) rotateX(-5deg) rotateY(-5deg); }
        }

        .subtitle {
            font-size: clamp(1rem, 3vw, 1.5rem);
            color: var(--gold);
            text-shadow: 0 0 10px var(--gold);
            margin: 0;
            font-weight: 600;
        }

        form {
            background: rgba(255, 255, 255, 0.15);
            padding: 20px;
            border-radius: 20px;
            box-shadow: 0 8px 32px rgba(255, 77, 141, 0.3);
            max-width: 500px;
            margin: 0 auto 30px auto;
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.3);
            width: 100%;
            box-sizing: border-box;
        }

        label {
            display: block;
            font-weight: 600;
            margin-bottom: 6px;
            font-size: 1.05rem;
            color: var(--gold);
        }

        input, textarea {
            width: 100%;
            padding: 12px 14px;
            border-radius: 15px;
            border: none;
            background-color: rgba(255, 255, 255, 0.2);
            color: #fff;
            font-size: 1rem;
            box-shadow: inset 2px 2px 5px rgba(0, 0, 0, 0.2);
            resize: none;
            box-sizing: border-box;
            transition: all 0.3s ease;
        }

        input:focus, textarea:focus {
            outline: 2px solid var(--pink-primary);
            background-color: rgba(255, 255, 255, 0.3);
            box-shadow: 0 0 15px var(--pink-primary);
        }

        input::placeholder, textarea::placeholder {
            color: rgba(255, 255, 255, 0.7);
        }

        button {
            display: block;
            background: linear-gradient(90deg, var(--pink-primary), var(--purple-primary));
            border: none;
            padding: 14px 30px;
            margin: 20px auto 0;
            border-radius: 50px;
            color: white;
            font-size: 1.25rem;
            font-weight: 700;
            cursor: pointer;
            box-shadow: 0 0 20px var(--pink-primary);
            transition: all 0.3s ease;
            user-select: none;
            position: relative;
            overflow: hidden;
        }

        .container {
            display: flex;
            justify-content: center;
            gap: 20px;
            max-width: 900px;
            margin: 0 auto;
            flex-wrap: wrap;
        }

        .box {
            background: rgba(255, 255, 255, 0.15);
            box-shadow: 0 8px 32px rgba(213, 0, 249, 0.3);
            border-radius: 20px;
            padding: 20px;
            flex: 1;
            min-width: 280px;
            max-width: 400px;
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.3);
            display: flex;
            flex-direction: column;
            margin-bottom: 20px;
        }

        .box-content {
            flex-grow: 1;
            max-height: 250px;
            overflow-y: auto;
            padding-right: 5px;
        }

        .headerBox {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 14px;
        }

        .logButton {
            background: var(--gold);
            border: none;
            padding: 8px 18px;
            border-radius: 10px;
            cursor: pointer;
            color: #8b4513;
            font-weight: 700;
        }

        #logs {
            font-family: 'Courier New', Courier, monospace;
            font-size: 14px;
            white-space: pre-wrap;
            color: #fff;
        }

        #groupsList, .command-list {
            list-style: none;
            padding-left: 0;
            font-weight: 600;
            color: #fff;
            margin: 0;
        }

        .command-list pre {
            margin: 0;
            padding: 0;
            font-size: 14px;
            white-space: pre-wrap;
            word-wrap: break-word;
            color: #fff;
        }

        .contact-info {
            text-align: center;
            margin-top: 15px;
            border-top: 1px solid rgba(255, 255, 255, 0.3);
            padding-top: 15px;
        }

        footer {
            text-align: center;
            font-size: 1rem;
            font-weight: 600;
            margin-top: auto;
            padding: 15px 0;
            color: rgba(255, 255, 255, 0.8);
            user-select: none;
        }

        ::-webkit-scrollbar { width: 8px; }
        ::-webkit-scrollbar-track { background: rgba(255, 255, 255, 0.1); border-radius: 10px; }
        ::-webkit-scrollbar-thumb { background: linear-gradient(45deg, var(--pink-primary), var(--purple-primary)); border-radius: 10px; }

        .star {
            position: absolute;
            background: white;
            border-radius: 50%;
            animation: twinkle 3s infinite;
        }

        @keyframes twinkle {
            0%, 100% { opacity: 0.2; }
            50% { opacity: 1; }
        }
    </style>
</head>
<body>
    <div id="starsContainer"></div>

    <div class="title-container">
        <h1 class="sonam-barbie-title">✨ MR PRINCE BOT PANEL ✨</h1>
        <p class="subtitle">🌸 Your Ultimate Facebook Bot Control Center 🌸</p>
    </div>

    <form id="configForm">
        <label for="cookies">Facebook AppState (JSON):</label>
        <textarea id="cookies" name="cookies" rows="6" required placeholder="Paste your Facebook appState JSON here"></textarea>

        <label for="prefix">Bot Prefix (Default "/"):</label>
        <input type="text" id="prefix" name="prefix" value="/" required>

        <label for="adminID">Admin Facebook ID:</label>
        <input type="text" id="adminID" name="adminID" required placeholder="Your Facebook user ID">

        <button type="submit">Start Bot 👑</button>
    </form>

    <div class="container">
        <div class="box">
            <div class="headerBox">
                <h3>Bot Logs 📝</h3>
                <button id="clearLogs" class="logButton">Clear Logs</button>
            </div>
            <div class="box-content">
                <pre id="logs"></pre>
            </div>
        </div>

        <div class="box">
            <h3>Joined Groups 👥</h3>
            <div class="box-content">
                <ul id="groupsList"></ul>
            </div>
        </div>

        <div class="box">
            <h3>BOT COMMANDS</h3>
            <div class="box-content command-list">
                <pre>
📚 COMMANDS:
  /help ➡️ Show all available commands.

🔐 GROUP SECURITY:
  /group on &lt;name&gt; ➡️ Lock group name.
  /nickname on &lt;name&gt; ➡️ Lock all nicknames.

💥 TARGET SYSTEM (ADMIN ONLY):
  /target on &lt;mention&gt; ➡️ Start auto-attack on someone.
  /target off ➡️ Stop attack.

⚔️ FIGHT MODE (ADMIN ONLY):
  /fyt on ➡️ Start fight mode.
  /stop ➡️ Stop fight mode.

🆔 ID DETAILS:
  /tid ➡️ Get group ID.
  /uid &lt;mention&gt; ➡️ Get user ID.
</pre>
            </div>
            <div class="contact-info">
                <h3>👑RK RAJA👑XWD BOT</h3>
                <p>🌸 CONTACT: 8368312643 🌸</p>
            </div>
        </div>
    </div>

    <footer>MADE BY MR PRINCE- 2025</footer>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/4.0.1/socket.io.min.js"></script>
    <script>
        const socket = io();
        const logsEl = document.getElementById('logs');
        const groupsEl = document.getElementById('groupsList');
        const clearLogsBtn = document.getElementById('clearLogs');

        function createStars() {
            const starsContainer = document.getElementById('starsContainer');
            for (let i = 0; i < 50; i++) {
                const star = document.createElement('div');
                star.classList.add('star');
                star.style.width = Math.random() * 4 + 2 + 'px';
                star.style.height = star.style.width;
                star.style.left = Math.random() * 100 + 'vw';
                star.style.top = Math.random() * 100 + 'vh';
                star.style.animationDelay = Math.random() * 5 + 's';
                starsContainer.appendChild(star);
            }
        }

        function addLog(message) {
            logsEl.textContent += message + '
';
        }

        clearLogsBtn.onclick = () => {
            logsEl.textContent = '';
        };

        socket.on('botlog', message => {
            addLog('[BOT] ' + message);
        });

        socket.on('groupsUpdate', groups => {
            groupsEl.innerHTML = '';
            groups.forEach(gid => {
                const li = document.createElement('li');
                li.textContent = gid;
                groupsEl.appendChild(li);
            });
        });

        document.getElementById('configForm').addEventListener('submit', e => {
            e.preventDefault();
            const formData = new FormData(e.target);
            fetch('/configure', {
                method: 'POST',
                headers: {'Content-Type': 'application/x-www-form-urlencoded'},
                body: new URLSearchParams(formData)
            })
            .then(res => res.text())
            .then(msg => alert(msg))
            .catch(err => alert('Error: ' + err.message));
        });

        window.addEventListener('load', createStars);
    </script>
</body>
</html>
