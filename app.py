import base64
import io
import json
import numpy as np
import streamlit as st
from PIL import Image, ImageDraw
from streamlit_drawable_canvas import st_canvas

# ==========================================
# 1. CONFIGURAÇÃO DA PÁGINA & ESTADO INICIAL
# ==========================================
st.set_page_config(
    page_title="Quadro Branco - Editor & Anotação",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="collapsed"  # Menu hambúrguer fechado por padrão no canto superior esquerdo
)

# Inicialização de Session States para Histórico
if "history" not in st.session_state:
    st.session_state["history"] = []
if "play_sound" not in st.session_state:
    st.session_state["play_sound"] = False

# ==========================================
# 2. INJEÇÃO DE CSS & JS FULLSTACK (UI HACKS)
# ==========================================
CUSTOM_CSS = """
<style>
    /* Estilização Geral e Tema Dark Glassmorphism */
    .stApp {
        background-color: #0e1117;
        color: #e0e0e0;
    }
    
    /* Destaque para o botão do Menu Hambúrguer recolhido */
    [data-testid="stSidebarCollapseButton"] {
        background-color: #262730 !important;
        border: 1px solid #4f46e5 !important;
        border-radius: 8px !important;
        padding: 4px !important;
        transition: all 0.3s ease;
    }
    [data-testid="stSidebarCollapseButton"]:hover {
        background-color: #4f46e5 !important;
        color: #ffffff !important;
        box-shadow: 0px 0px 10px rgba(79, 70, 229, 0.6);
    }

    /* Ocultar elementos nativos desnecessários */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Container do Canvas com borda brilhante */
    .canvas-container {
        border: 2px solid #31333f;
        border-radius: 12px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        background: #1a1c23;
        margin: auto;
    }

    /* Cartões do Histórico */
    .history-card {
        background: #1e222d;
        border-radius: 8px;
        padding: 10px;
        border: 1px solid #2e3440;
        margin-bottom: 10px;
    }
</style>
"""
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# JS para Feedback Sonoro de Captura (Simula o capture.mp3 via Web Audio API)
JS_AUDIO_SHUTTER = """
<script>
function playShutterSound() {
    const audioCtx = new (window.AudioContext || window.webkitAudioContext)();
    const osc = audioCtx.createOscillator();
    const gain = audioCtx.createGain();
    
    osc.type = 'sine';
    osc.frequency.setValueAtTime(800, audioCtx.currentTime);
    osc.frequency.exponentialRampToValueAtTime(400, audioCtx.currentTime + 0.08);
    
    gain.gain.setValueAtTime(0.3, audioCtx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.08);
    
    osc.connect(gain);
    gain.connect(audioCtx.destination);
    
    osc.start();
    osc.stop(audioCtx.currentTime + 0.08);
}
playShutterSound();
</script>
"""

def trigger_audio():
    st.components.v1.html(JS_AUDIO_SHUTTER, height=0, width=0)

# ==========================================
# 3. SIDEBAR - FERRAMENTAS & CONFIGURAÇÕES
# ==========================================
with st.sidebar:
    st.title("🎨 Quadro Branco")
    st.caption("Extensão de Anotação & Edição Recompilada")
    st.markdown("---")

    st.subheader("🛠️ Ferramentas")
    
    # Mapeamento de Ferramentas
    tool_options = {
        "✏️ Pincel / Caneta": "freedraw",
        "📏 Linha Reta": "line",
        "🔲 Retângulo": "rect",
        "⭕ Círculo": "circle",
        "🧽 Borracha": "freedraw", # Tratado dinamicamente com cor de fundo
        "🖐️ Selecionar / Mover": "transform"
    }
    selected_tool_label = st.radio("Escolha a ferramenta:", list(tool_options.keys()))
    drawing_mode = tool_options[selected_tool_label]
    
    is_eraser = "Borracha" in selected_tool_label

    st.markdown("---")
    st.subheader("🎨 Estilo & Cores")

    col_color1, col_color2 = st.columns(2)
    with col_color1:
        stroke_color = st.color_picker("Cor do Traço", "#4F46E5" if not is_eraser else "#ffffff")
    with col_color2:
        fill_color = st.color_picker("Preenchimento", "#000000", help="Usado em formas geométricas")
        has_fill = st.checkbox("Preencher forma?", value=False)

    stroke_width = st.slider("Espessura do Pincel/Linha", min_value=1, max_value=50, value=5)

    st.markdown("---")
    st.subheader("🖼️ Plano de Fundo")
    
    bg_type = st.selectbox("Tipo de Fundo", ["Branco", "Negro", "Papel Quadriculado", "Imagem Personalizada"])
    
    bg_image = None
    bg_color = "#FFFFFF"

    if bg_type == "Branco":
        bg_color = "#FFFFFF"
    elif bg_type == "Negro":
        bg_color = "#121212"
    elif bg_type == "Papel Quadriculado":
        # Gera padrão quadriculado simples em PIL
        grid_img = Image.new("RGB", (40, 40), "#F0F0F0")
        draw = ImageDraw.Draw(grid_img)
        draw.line([(39, 0), (39, 39)], fill="#D0D0D0", width=1)
        draw.line([(0, 39), (39, 39)], fill="#D0D0D0", width=1)
        bg_image = grid_img
    elif bg_type == "Imagem Personalizada":
        uploaded_file = st.file_uploader("Upload de Screenshot ou Imagem", type=["png", "jpg", "jpeg", "webp"])
        if uploaded_file:
            bg_image = Image.open(uploaded_file)

    # Ajuste de cor de borracha automático de acordo com o fundo
    if is_eraser:
        stroke_color = bg_color if bg_type != "Papel Quadriculado" else "#F0F0F0"

    st.markdown("---")
    sound_enabled = st.toggle("Efeitos Sonoros", value=True)

# ==========================================
# 4. ÁREA PRINCIPAL & CANVAS
# ==========================================

# Topbar de Ações Rápidas
col_title, col_actions = st.columns([2, 3])

with col_title:
    st.markdown("### 🖌️ Área de Trabalho")

with col_actions:
    c1, c2, c3 = st.columns(3)
    with c1:
        realtime_update = st.checkbox("Atualização em Tempo Real", value=True)
    with c2:
        clear_canvas = st.button("🗑️ Limpar Tela", use_container_width=True)
    with c3:
        save_btn = st.button("💾 Salvar no Histórico", type="primary", use_container_width=True)

# Dimensões Responsivas do Canvas
canvas_width = 1000
canvas_height = 600

# Tratamento do preenchimento transparente/sólido
final_fill = stroke_color if (drawing_mode in ["rect", "circle"] and has_fill) else "rgba(0, 0, 0, 0)"

# Componente Canvas principal (Baseado no Fabric.js)
canvas_result = st_canvas(
    fill_color=final_fill,
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color if bg_image is None else "",
    background_image=bg_image,
    update_streamlit=realtime_update,
    height=canvas_height,
    width=canvas_width,
    drawing_mode=drawing_mode,
    key="main_canvas" if not clear_canvas else "main_canvas_cleared",
)

# ==========================================
# 5. PROCESSAMENTO DE HISTÓRICO & DOWNLOADS
# ==========================================

if save_btn and canvas_result.image_data is not None:
    # Converte array numpy do canvas em Imagem PIL
    img_data = canvas_result.image_data.astype(np.uint8)
    final_img = Image.fromarray(img_data)
    
    # Salva em memória
    buffered = io.BytesIO()
    final_img.save(buffered, format="PNG")
    img_bytes = buffered.getvalue()

    # Adiciona ao histórico de sessão
    st.session_state["history"].append(img_bytes)
    
    if sound_enabled:
        trigger_audio()
        
    st.toast("Captura salva no histórico com sucesso!", icon="📸")

# Exibição do Histórico e Exportação na Sidebar
with st.sidebar:
    st.markdown("---")
    st.subheader("📚 Histórico de Capturas")
    
    if len(st.session_state["history"]) == 0:
        st.info("Nenhuma captura salva nesta sessão.")
    else:
        for idx, saved_img_bytes in enumerate(reversed(st.session_state["history"])):
            with st.container():
                st.image(saved_img_bytes, caption=f"Captura #{len(st.session_state['history']) - idx}", use_column_width=True)
                
                st.download_button(
                    label=f"⬇️ Baixar PNG #{len(st.session_state['history']) - idx}",
                    data=saved_img_bytes,
                    file_name=f"quadro_branco_captura_{idx+1}.png",
                    mime="image/png",
                    key=f"dl_{idx}",
                    use_container_width=True
                )
                st.markdown("<br>", unsafe_allow_html=True)