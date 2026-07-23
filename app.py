import streamlit as st
import streamlit.components.v1 as components

# ==========================================
# 1. CONFIGURAÇÃO DE PÁGINA (PAGINA LIMPA)
# ==========================================
st.set_page_config(
    page_title="Quadro Branco",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Oculta completamente cabeçalhos, rodapés e margens do Streamlit
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        [data-testid="stSidebar"] {display: none;}
        .block-container {
            padding: 0rem !important;
            margin: 0rem !important;
            max-width: 100% !important;
        }
        iframe {
            display: block;
            border: none !important;
            width: 100vw;
            height: 100vh;
        }
        body {
            background-color: #ffffff !important;
            overflow: hidden;
        }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 2. EMULAÇÃO COMPLETA DA EXTENSÃO XPI (FABRIC.JS)
# ==========================================
HTML_XPI_EMULATOR = """
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

        #canvas-container {
            width: 100vw;
            height: 100vh;
            position: absolute;
            top: 0;
            left: 0;
            background: #ffffff;
        }

        /* Botão Hambúrguer Topo Esquerdo (Clone XPI) */
        #hamburger-btn {
            position: fixed;
            top: 12px;
            left: 12px;
            z-index: 9999;
            width: 42px;
            height: 42px;
            background-color: #ffffff;
            color: #334155;
            border: 1px solid #e2e8f0;
            border-radius: 12px;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 18px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
            transition: all 0.2s ease;
        }
        #hamburger-btn:hover {
            background-color: #f8fafc;
            transform: scale(1.03);
            border-color: #cbd5e1;
        }

        /* Painel Flutuante Vertical (Clone Fiel da Imagem XPI) */
        #toolbar {
            position: fixed;
            top: 62px;
            left: 12px;
            z-index: 9998;
            background: #ffffff;
            border: 1px solid #e2e8f0;
            border-radius: 20px;
            padding: 10px;
            display: none; /* Fechado por padrão */
            flex-direction: column;
            gap: 8px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
            width: 148px;
        }
        #toolbar.active {
            display: flex;
        }

        .tool-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 6px;
        }

        .tool-btn {
            background: #f8fafc;
            color: #475569;
            border: 1px solid #e2e8f0;
            width: 38px;
            height: 38px;
            border-radius: 10px;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 15px;
            transition: all 0.15s ease;
        }
        .tool-btn:hover {
            background: #f1f5f9;
            color: #1e293b;
        }
        .tool-btn.active {
            background: #dbeafe;
            color: #2563eb;
            border-color: #93c5fd;
        }

        /* Input de Cor Customizado */
        .color-picker-wrapper {
            position: relative;
            width: 38px;
            height: 38px;
            overflow: hidden;
            border-radius: 10px;
            border: 1px solid #cbd5e1;
            cursor: pointer;
        }
        input[type="color"] {
            position: absolute;
            top: -10px;
            left: -10px;
            width: 60px;
            height: 60px;
            cursor: pointer;
            border: none;
        }

        /* Slider de Espessura na parte inferior */
        .slider-container {
            padding: 4px 6px;
            display: flex;
            align-items: center;
        }
        input[type="range"] {
            width: 100%;
            height: 4px;
            background: #cbd5e1;
            border-radius: 2px;
            accent-color: #2563eb;
            cursor: pointer;
        }

        /* Input de arquivo escondido para carregar imagem */
        #img-uploader {
            display: none;
        }
    </style>
</head>
<body>

    <!-- Botão Hambúrguer -->
    <button id="hamburger-btn" onclick="toggleMenu()" title="Ferramentas (Menu)">
        <i class="fa-solid fa-bars"></i>
    </button>

    <!-- Barra de Ferramentas Flutuante -->
    <div id="toolbar">
        <div class="tool-grid">
            <!-- Linha 1: Seletor de Cor | Desfazer | Refazer -->
            <div class="color-picker-wrapper" title="Cor Principal">
                <input type="color" id="color-picker" value="#f97316" onchange="updateColor(this.value)">
            </div>
            <button class="tool-btn" onclick="undo()" title="Desfazer (Ctrl+Z)">
                <i class="fa-solid fa-rotate-left"></i>
            </button>
            <button class="tool-btn" onclick="redo()" title="Refazer (Ctrl+Y)">
                <i class="fa-solid fa-rotate-right"></i>
            </button>

            <!-- Linha 2: Selecionar/Mover | Pincel | Marca-Texto -->
            <button class="tool-btn active" id="btn-select" onclick="setMode('select')" title="Mover / Selecionar (V)">
                <i class="fa-solid fa-arrows-up-down-left-right"></i>
            </button>
            <button class="tool-btn" id="btn-draw" onclick="setMode('draw')" title="Pincel (P)">
                <i class="fa-solid fa-pen"></i>
            </button>
            <button class="tool-btn" id="btn-highlighter" onclick="setMode('highlighter')" title="Marca-Texto">
                <i class="fa-solid fa-highlighter"></i>
            </button>

            <!-- Linha 3: Borracha | Texto | Retângulo Vazado -->
            <button class="tool-btn" id="btn-eraser" onclick="setMode('eraser')" title="Borracha (E)">
                <i class="fa-solid fa-eraser"></i>
            </button>
            <button class="tool-btn" id="btn-text" onclick="addText()" title="Texto (T)">
                <i class="fa-solid fa-font"></i>
            </button>
            <button class="tool-btn" id="btn-rect" onclick="addShape('rect-outline')" title="Retângulo (R)">
                <i class="fa-regular fa-square"></i>
            </button>

            <!-- Linha 4: Círculo Vazado | Linha | Seta -->
            <button class="tool-btn" id="btn-circle" onclick="addShape('circle-outline')" title="Círculo (C)">
                <i class="fa-regular fa-circle"></i>
            </button>
            <button class="tool-btn" id="btn-line" onclick="addShape('line')" title="Linha Reta (L)">
                <i class="fa-solid fa-minus"></i>
            </button>
            <button class="tool-btn" id="btn-arrow" onclick="addArrow()" title="Seta (A)">
                <i class="fa-solid fa-arrow-right"></i>
            </button>

            <!-- Linha 5: Retângulo Cheio | Círculo Cheio | Importar Imagem -->
            <button class="tool-btn" onclick="addShape('rect-filled')" title="Retângulo Preenchido">
                <i class="fa-solid fa-square"></i>
            </button>
            <button class="tool-btn" onclick="addShape('circle-filled')" title="Círculo Preenchido">
                <i class="fa-solid fa-circle"></i>
            </button>
            <button class="tool-btn" onclick="triggerImgUpload()" title="Carregar Imagem / Screenshot">
                <i class="fa-solid fa-image"></i>
            </button>

            <!-- Linha 6: Duplicar Objeto | Trazer para Frente | Deletar Selecionado -->
            <button class="tool-btn" onclick="duplicateSelected()" title="Duplicar Objeto">
                <i class="fa-solid fa-copy"></i>
            </button>
            <button class="tool-btn" onclick="bringToFront()" title="Trazer para Frente">
                <i class="fa-solid fa-layer-group"></i>
            </button>
            <button class="tool-btn" onclick="deleteSelected()" title="Excluir Selecionado (Del)">
                <i class="fa-solid fa-trash-can"></i>
            </button>

            <!-- Linha 7: Seleção de Área | Cursor Laser | Salvar PNG -->
            <button class="tool-btn" onclick="setMode('select')" title="Seleção">
                <i class="fa-solid fa-crop-simple"></i>
            </button>
            <button class="tool-btn" id="btn-pointer" onclick="setMode('pointer')" title="Ponteiro / Laser">
                <i class="fa-solid fa-arrow-pointer"></i>
            </button>
            <button class="tool-btn" onclick="exportPNG()" title="Baixar Imagem PNG">
                <i class="fa-solid fa-download" style="color: #ef4444;"></i>
            </button>

            <!-- Linha 8: Zoom In | Zoom Out | Limpar Tudo -->
            <button class="tool-btn" onclick="zoomIn()" title="Aumentar Zoom (+)">
                <i class="fa-solid fa-magnifying-glass-plus"></i>
            </button>
            <button class="tool-btn" onclick="zoomOut()" title="Reduzir Zoom (-)">
                <i class="fa-solid fa-magnifying-glass-minus"></i>
            </button>
            <button class="tool-btn" onclick="clearCanvas()" title="Limpar Tudo">
                <i class="fa-solid fa-broom"></i>
            </button>
        </div>

        <!-- Controle de Espessura do Traço -->
        <div class="slider-container">
            <input type="range" id="stroke-width" min="1" max="50" value="4" oninput="updateWidth(this.value)" title="Espessura do Traço">
        </div>
    </div>

    <input type="file" id="img-uploader" accept="image/*" onchange="handleImageUpload(event)">

    <div id="canvas-container">
        <canvas id="c"></canvas>
    </div>

    <script>
        // Inicialização do Canvas
        const canvas = new fabric.Canvas('c', {
            isDrawingMode: false,
            backgroundColor: '#ffffff',
            selection: true
        });

        function resizeCanvas() {
            canvas.setWidth(window.innerWidth);
            canvas.setHeight(window.innerHeight);
            canvas.renderAll();
        }
        window.addEventListener('resize', resizeCanvas);
        resizeCanvas();

        // Estado e Histórico (Undo / Redo)
        let undoStack = [];
        let redoStack = [];
        let isStateLocked = false;

        function saveState() {
            if (isStateLocked) return;
            undoStack.push(JSON.stringify(canvas));
            redoStack = [];
        }

        canvas.on('object:added', saveState);
        canvas.on('object:modified', saveState);
        canvas.on('object:removed', saveState);

        function undo() {
            if (undoStack.length <= 1) return;
            isStateLocked = true;
            redoStack.push(undoStack.pop());
            const previousState = undoStack[undoStack.length - 1];
            canvas.loadFromJSON(previousState, () => {
                canvas.renderAll();
                isStateLocked = false;
            });
        }

        function redo() {
            if (redoStack.length === 0) return;
            isStateLocked = true;
            const nextState = redoStack.pop();
            undoStack.push(nextState);
            canvas.loadFromJSON(nextState, () => {
                canvas.renderAll();
                isStateLocked = false;
            });
        }

        // Estado do Menu
        function toggleMenu() {
            document.getElementById('toolbar').classList.toggle('active');
        }

        // Ferramentas e Estilos
        let currentMode = 'select';
        let currentColor = '#f97316';
        let currentWidth = 4;

        function updateColor(val) {
            currentColor = val;
            if (canvas.isDrawingMode) {
                canvas.freeDrawingBrush.color = currentMode === 'highlighter' ? hexToRgba(currentColor, 0.4) : currentColor;
            }
            const activeObj = canvas.getActiveObject();
            if (activeObj) {
                if (activeObj.type === 'i-text') activeObj.set('fill', currentColor);
                else if (activeObj.fill && activeObj.fill !== 'transparent') activeObj.set('fill', currentColor);
                else activeObj.set('stroke', currentColor);
                canvas.renderAll();
            }
        }

        function updateWidth(val) {
            currentWidth = val;
            if (canvas.isDrawingMode) {
                canvas.freeDrawingBrush.width = parseInt(currentWidth, 10) * (currentMode === 'eraser' ? 3 : 1);
            }
        }

        function setMode(mode) {
            currentMode = mode;
            document.querySelectorAll('.tool-btn').forEach(b => b.classList.remove('active'));

            canvas.isDrawingMode = (mode === 'draw' || mode === 'highlighter' || mode === 'eraser');

            if (mode === 'draw') {
                document.getElementById('btn-draw').classList.add('active');
                canvas.freeDrawingBrush = new fabric.PencilBrush(canvas);
                canvas.freeDrawingBrush.color = currentColor;
                canvas.freeDrawingBrush.width = parseInt(currentWidth, 10);
            } else if (mode === 'highlighter') {
                document.getElementById('btn-highlighter').classList.add('active');
                canvas.freeDrawingBrush = new fabric.PencilBrush(canvas);
                canvas.freeDrawingBrush.color = hexToRgba(currentColor, 0.35);
                canvas.freeDrawingBrush.width = parseInt(currentWidth, 10) * 4;
            } else if (mode === 'eraser') {
                document.getElementById('btn-eraser').classList.add('active');
                canvas.freeDrawingBrush = new fabric.PencilBrush(canvas);
                canvas.freeDrawingBrush.color = '#ffffff';
                canvas.freeDrawingBrush.width = parseInt(currentWidth, 10) * 4;
            } else if (mode === 'select') {
                document.getElementById('btn-select').classList.add('active');
            } else if (mode === 'pointer') {
                document.getElementById('btn-pointer').classList.add('active');
            }
        }

        function hexToRgba(hex, alpha) {
            let r = parseInt(hex.slice(1, 3), 16);
            let g = parseInt(hex.slice(3, 5), 16);
            let b = parseInt(hex.slice(5, 7), 16);
            return `rgba(${r}, ${g}, ${b}, ${alpha})`;
        }

        // Formas Vetoriais
        function addShape(type) {
            const w = window.innerWidth / 2 - 50;
            const h = window.innerHeight / 2 - 50;
            let shape;

            if (type === 'rect-outline') {
                shape = new fabric.Rect({ left: w, top: h, width: 100, height: 100, fill: 'transparent', stroke: currentColor, strokeWidth: parseInt(currentWidth, 10) });
            } else if (type === 'rect-filled') {
                shape = new fabric.Rect({ left: w, top: h, width: 100, height: 100, fill: currentColor, stroke: '', strokeWidth: 0 });
            } else if (type === 'circle-outline') {
                shape = new fabric.Circle({ left: w, top: h, radius: 50, fill: 'transparent', stroke: currentColor, strokeWidth: parseInt(currentWidth, 10) });
            } else if (type === 'circle-filled') {
                shape = new fabric.Circle({ left: w, top: h, radius: 50, fill: currentColor, stroke: '', strokeWidth: 0 });
            } else if (type === 'line') {
                shape = new fabric.Line([0, 0, 150, 0], { left: w, top: h, stroke: currentColor, strokeWidth: parseInt(currentWidth, 10) });
            }

            if (shape) {
                canvas.add(shape);
                canvas.setActiveObject(shape);
                setMode('select');
            }
        }

        function addArrow() {
            const w = window.innerWidth / 2;
            const h = window.innerHeight / 2;
            const line = new fabric.Line([0, 0, 120, 0], { stroke: currentColor, strokeWidth: parseInt(currentWidth, 10), originY: 'center' });
            const triangle = new fabric.Triangle({ width: 18, height: 18, fill: currentColor, left: 120, top: 0, angle: 90, originX: 'center', originY: 'center' });
            const arrowGroup = new fabric.Group([line, triangle], { left: w - 60, top: h });

            canvas.add(arrowGroup);
            canvas.setActiveObject(arrowGroup);
            setMode('select');
        }

        function addText() {
            const text = new fabric.IText('Texto...', {
                left: window.innerWidth / 2 - 40,
                top: window.innerHeight / 2 - 20,
                fill: currentColor,
                fontSize: 28,
                fontFamily: 'sans-serif'
            });
            canvas.add(text);
            canvas.setActiveObject(text);
            setMode('select');
        }

        // Ações em Elementos
        function deleteSelected() {
            const activeObjects = canvas.getActiveObjects();
            if (activeObjects.length) {
                activeObjects.forEach(obj => canvas.remove(obj));
                canvas.discardActiveObject();
                canvas.renderAll();
            }
        }

        function duplicateSelected() {
            const activeObj = canvas.getActiveObject();
            if (activeObj) {
                activeObj.clone((cloned) => {
                    canvas.discardActiveObject();
                    cloned.set({ left: cloned.left + 20, top: cloned.top + 20 });
                    if (cloned.type === 'activeSelection') {
                        cloned.canvas = canvas;
                        cloned.forEachObject(obj => canvas.add(obj));
                        cloned.setCoordinates();
                    } else {
                        canvas.add(cloned);
                    }
                    canvas.setActiveObject(cloned);
                    canvas.requestRenderAll();
                });
            }
        }

        function bringToFront() {
            const activeObj = canvas.getActiveObject();
            if (activeObj) {
                canvas.bringToFront(activeObj);
                canvas.renderAll();
            }
        }

        function clearCanvas() {
            canvas.clear();
            canvas.setBackgroundColor('#ffffff', canvas.renderAll.bind(canvas));
            saveState();
        }

        // Zoom
        function zoomIn() {
            canvas.setZoom(canvas.getZoom() * 1.15);
        }
        function zoomOut() {
            canvas.setZoom(canvas.getZoom() / 1.15);
        }

        // Imagem / Screenshot
        function triggerImgUpload() {
            document.getElementById('img-uploader').click();
        }

        function handleImageUpload(e) {
            const file = e.target.files[0];
            if (!file) return;
            const reader = new FileReader();
            reader.onload = function(f) {
                fabric.Image.fromURL(f.target.result, function(img) {
                    img.scaleToWidth(window.innerWidth * 0.6);
                    img.set({ left: window.innerWidth / 2 - (img.scaledWidth / 2), top: window.innerHeight / 2 - (img.scaledHeight / 2) });
                    canvas.add(img);
                    canvas.setActiveObject(img);
                    setMode('select');
                });
            };
            reader.readAsDataURL(file);
        }

        // Efeito Sonoro e Exportação
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

        function exportPNG() {
            playShutterSound();
            const dataURL = canvas.toDataURL({ format: 'png', quality: 1.0 });
            const link = document.createElement('a');
            link.download = 'quadro_branco.png';
            link.href = dataURL;
            link.click();
        }

        // Atalhos de Teclado
        window.addEventListener('keydown', (e) => {
            if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;

            if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'z') {
                e.preventDefault();
                undo();
            } else if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'y') {
                e.preventDefault();
                redo();
            } else if (e.key === 'Delete' || e.key === 'Backspace') {
                deleteSelected();
            } else if (e.key.toLowerCase() === 'p') {
                setMode('draw');
            } else if (e.key.toLowerCase() === 'e') {
                setMode('eraser');
            } else if (e.key.toLowerCase() === 't') {
                addText();
            } else if (e.key.toLowerCase() === 'r') {
                addShape('rect-outline');
            } else if (e.key.toLowerCase() === 'c') {
                addShape('circle-outline');
            } else if (e.key.toLowerCase() === 'l') {
                addShape('line');
            } else if (e.key.toLowerCase() === 'a') {
                addArrow();
            } else if (e.key.toLowerCase() === 'v' || e.key.toLowerCase() === 'm') {
                setMode('select');
            }
        });

        // Estado inicial
        saveState();
    </script>
</body>
</html>
"""

# Renderização sem bordas nem rolagem
components.html(HTML_XPI_EMULATOR, height=1000, scrolling=False)