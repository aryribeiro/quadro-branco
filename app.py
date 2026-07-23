import streamlit as st
import streamlit.components.v1 as components

# ==========================================
# 1. CONFIGURAÇÃO DE PÁGINA (TELA CHEIA)
# ==========================================
st.set_page_config(
    page_title="Quadro Branco",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==========================================
# 2. REMOÇÃO DE ELEMENTOS PADRÃO DO STREAMLIT
# ==========================================
st.markdown("""
    <style>
        /* Ocultar barra de topo, rodapé e margens nativas */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .block-container {
            padding: 0rem !important;
            margin: 0rem !important;
            max-width: 100% !important;
        }
        iframe {
            display: block;
            border: none !important;
        }
        body {
            background-color: #ffffff !important;
            overflow: hidden;
        }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 3. EMULAÇÃO COMPLETA DA EXTENSÃO (HTML5/FABRIC.JS)
# ==========================================
HTML_EMULATOR = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/fabric.js/5.3.1/fabric.min.js"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            user-select: none;
        }
        html, body {
            width: 100%;
            height: 100vh;
            background-color: #ffffff;
            overflow: hidden;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        }

        /* Canvas Cobrindo a Tela Toda */
        #canvas-container {
            width: 100vw;
            height: 100vh;
            position: absolute;
            top: 0;
            left: 0;
            background: #ffffff;
        }

        /* Botão Hambúrguer Flutuante (Canto Superior Esquerdo) */
        #hamburger-btn {
            position: fixed;
            top: 15px;
            left: 15px;
            z-index: 9999;
            width: 48px;
            height: 48px;
            background-color: #1e1e24;
            color: #ffffff;
            border: none;
            border-radius: 10px;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 20px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
            transition: all 0.2s ease-in-out;
        }
        #hamburger-btn:hover {
            background-color: #3b82f6;
            transform: scale(1.05);
        }

        /* Painel de Ferramentas (Escondido por Padrão) */
        #toolbar {
            position: fixed;
            top: 72px;
            left: 15px;
            z-index: 9998;
            background: #1e1e24;
            border-radius: 12px;
            padding: 12px;
            display: none; /* Fechado por padrão */
            flex-direction: column;
            gap: 10px;
            box-shadow: 0 8px 24px rgba(0,0,0,0.25);
            width: 220px;
            color: #fff;
        }
        #toolbar.active {
            display: flex;
        }

        .tool-group {
            display: flex;
            flex-wrap: wrap;
            gap: 6px;
        }

        .tool-btn {
            background: #2b2d35;
            color: #e2e8f0;
            border: 1px solid #3f424e;
            width: 38px;
            height: 38px;
            border-radius: 8px;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 15px;
            transition: all 0.15s;
        }
        .tool-btn:hover, .tool-btn.active {
            background: #3b82f6;
            color: #fff;
            border-color: #60a5fa;
        }

        .control-label {
            font-size: 11px;
            color: #94a3b8;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            margin-top: 4px;
        }

        input[type="color"] {
            -webkit-appearance: none;
            border: none;
            width: 38px;
            height: 38px;
            border-radius: 8px;
            cursor: pointer;
            background: none;
        }
        input[type="color"]::-webkit-color-swatch-wrapper {
            padding: 0;
        }
        input[type="color"]::-webkit-color-swatch {
            border: 1px solid #3f424e;
            border-radius: 8px;
        }

        input[type="range"] {
            width: 100%;
            accent-color: #3b82f6;
            cursor: pointer;
        }

        .action-btn {
            background: #ef4444;
            color: white;
            border: none;
            padding: 8px 12px;
            border-radius: 6px;
            cursor: pointer;
            font-size: 12px;
            font-weight: bold;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 6px;
        }
        .action-btn.save {
            background: #10b981;
        }
        .action-btn:hover {
            opacity: 0.9;
        }
    </style>
</head>
<body>

    <button id="hamburger-btn" onclick="toggleMenu()" title="Abrir Ferramentas">
        <i class="fa-solid fa-bars"></i>
    </button>

    <div id="toolbar">
        <div class="control-label">Modo de Desenho</div>
        <div class="tool-group">
            <button class="tool-btn active" id="btn-select" onclick="setMode('select')" title="Mover/Selecionar">
                <i class="fa-solid fa-hand"></i>
            </button>
            <button class="tool-btn" id="btn-draw" onclick="setMode('draw')" title="Pincel">
                <i class="fa-solid fa-pen-nib"></i>
            </button>
            <button class="tool-btn" id="btn-line" onclick="setMode('line')" title="Linha Reta">
                <i class="fa-solid fa-slash"></i>
            </button>
            <button class="tool-btn" id="btn-rect" onclick="setMode('rect')" title="Retângulo">
                <i class="fa-regular fa-square"></i>
            </button>
            <button class="tool-btn" id="btn-circle" onclick="setMode('circle')" title="Círculo">
                <i class="fa-regular fa-circle"></i>
            </button>
            <button class="tool-btn" id="btn-text" onclick="addText()" title="Inserir Texto">
                <i class="fa-solid fa-font"></i>
            </button>
            <button class="tool-btn" id="btn-eraser" onclick="setMode('eraser')" title="Borracha">
                <i class="fa-solid fa-eraser"></i>
            </button>
        </div>

        <div class="control-label">Cor & Espessura</div>
        <div style="display: flex; align-items: center; gap: 10px;">
            <input type="color" id="color-picker" value="#000000" onchange="updateColor(this.value)">
            <input type="range" id="stroke-width" min="1" max="50" value="4" oninput="updateWidth(this.value)">
        </div>

        <div class="control-label">Ações</div>
        <button class="action-btn save" onclick="saveImage()">
            <i class="fa-solid fa-camera"></i> Salvar Imagem
        </button>
        <button class="action-btn" onclick="clearCanvas()">
            <i class="fa-solid fa-trash"></i> Limpar Tela
        </button>
    </div>

    <div id="canvas-container">
        <canvas id="c"></canvas>
    </div>

    <script>
        // Inicialização do Canvas Fabric.js
        const canvas = new fabric.Canvas('c', {
            isDrawingMode: false,
            backgroundColor: '#ffffff'
        });

        // Redimensionar Canvas para ocupar a janela inteira
        function resizeCanvas() {
            canvas.setWidth(window.innerWidth);
            canvas.setHeight(window.innerHeight);
            canvas.renderAll();
        }
        window.addEventListener('resize', resizeCanvas);
        resizeCanvas();

        // Alternar Visualização do Menu
        function toggleMenu() {
            const toolbar = document.getElementById('toolbar');
            toolbar.classList.toggle('active');
        }

        // Configuração de Modos
        let currentMode = 'select';
        let currentColor = '#000000';
        let currentWidth = 4;

        function setMode(mode) {
            currentMode = mode;
            document.querySelectorAll('.tool-btn').forEach(btn => btn.classList.remove('active'));
            
            canvas.isDrawingMode = (mode === 'draw' || mode === 'eraser');
            
            if (mode === 'draw') {
                document.getElementById('btn-draw').classList.add('active');
                canvas.freeDrawingBrush.color = currentColor;
                canvas.freeDrawingBrush.width = parseInt(currentWidth, 10);
            } else if (mode === 'eraser') {
                document.getElementById('btn-eraser').classList.add('active');
                canvas.freeDrawingBrush.color = '#ffffff'; // Cor da tela branca
                canvas.freeDrawingBrush.width = parseInt(currentWidth, 10) * 3;
            } else if (mode === 'select') {
                document.getElementById('btn-select').classList.add('active');
            } else if (mode === 'rect') {
                document.getElementById('btn-rect').classList.add('active');
                addRectangle();
            } else if (mode === 'circle') {
                document.getElementById('btn-circle').classList.add('active');
                addCircle();
            } else if (mode === 'line') {
                document.getElementById('btn-line').classList.add('active');
                addLine();
            }
        }

        function updateColor(color) {
            currentColor = color;
            if (canvas.isDrawingMode && currentMode !== 'eraser') {
                canvas.freeDrawingBrush.color = currentColor;
            }
            const activeObj = canvas.getActiveObject();
            if (activeObj) {
                if (activeObj.type === 'i-text') activeObj.set('fill', currentColor);
                else activeObj.set('stroke', currentColor);
                canvas.renderAll();
            }
        }

        function updateWidth(width) {
            currentWidth = width;
            if (canvas.isDrawingMode) {
                canvas.freeDrawingBrush.width = parseInt(width, 10) * (currentMode === 'eraser' ? 3 : 1);
            }
        }

        // Adição de Formas Vetoriais (Fabric.js)
        function addRectangle() {
            const rect = new fabric.Rect({
                left: window.innerWidth / 2 - 50,
                top: window.innerHeight / 2 - 50,
                fill: 'transparent',
                stroke: currentColor,
                strokeWidth: parseInt(currentWidth, 10),
                width: 100,
                height: 100
            });
            canvas.add(rect);
            canvas.setActiveObject(rect);
            setMode('select');
        }

        function addCircle() {
            const circle = new fabric.Circle({
                left: window.innerWidth / 2 - 50,
                top: window.innerHeight / 2 - 50,
                fill: 'transparent',
                stroke: currentColor,
                strokeWidth: parseInt(currentWidth, 10),
                radius: 50
            });
            canvas.add(circle);
            canvas.setActiveObject(circle);
            setMode('select');
        }

        function addLine() {
            const line = new fabric.Line([50, 50, 200, 50], {
                left: window.innerWidth / 2 - 75,
                top: window.innerHeight / 2,
                stroke: currentColor,
                strokeWidth: parseInt(currentWidth, 10)
            });
            canvas.add(line);
            canvas.setActiveObject(line);
            setMode('select');
        }

        function addText() {
            const text = new fabric.IText('Clique para editar', {
                left: window.innerWidth / 2 - 80,
                top: window.innerHeight / 2,
                fill: currentColor,
                fontSize: 24
            });
            canvas.add(text);
            canvas.setActiveObject(text);
            setMode('select');
        }

        function clearCanvas() {
            canvas.clear();
            canvas.setBackgroundColor('#ffffff', canvas.renderAll.bind(canvas));
        }

        // Emulação de Áudio de Captura (Web Audio API)
        function playShutterSound() {
            try {
                const ctx = new (window.AudioContext || window.webkitAudioContext)();
                const osc = ctx.createOscillator();
                const gain = ctx.createGain();
                osc.type = 'sine';
                osc.frequency.setValueAtTime(800, ctx.currentTime);
                osc.frequency.exponentialRampToValueAtTime(300, ctx.currentTime + 0.08);
                gain.gain.setValueAtTime(0.3, ctx.currentTime);
                gain.gain.exponentialRampToValueAtTime(0.01, ctx.currentTime + 0.08);
                osc.connect(gain);
                gain.connect(ctx.destination);
                osc.start();
                osc.stop(ctx.currentTime + 0.08);
            } catch(e) {}
        }

        // Exportação de Imagem
        function saveImage() {
            playShutterSound();
            const dataURL = canvas.toDataURL({
                format: 'png',
                quality: 1.0
            });
            const link = document.createElement('a');
            link.download = 'quadro_branco_captura.png';
            link.href = dataURL;
            link.click();
        }
    </script>
</body>
</html>
"""

# Renderiza a aplicação HTML5/Fabric.js ocupando 100% da viewport
components.html(HTML_EMULATOR, height=950, scrolling=False)