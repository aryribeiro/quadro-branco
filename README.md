Obs.: caso o app esteja no modo "sleeping" (dormindo) ao entrar, basta clicar no botão que estará disponível e aguardar, para ativar o mesmo.

<p align="center"><img width="337" height="404" alt="print" src="https://github.com/user-attachments/assets/ef2f9296-9774-486b-8735-7fcbb8f68b99" /></p>


[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://quadro.streamlit.app)
![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat&logo=python&logoColor=white)
![Fabric.js](https://img.shields.io/badge/Fabric.js-5.3.1-blue?style=flat)
![License](https://img.shields.io/badge/License-MIT-green.svg)

O 🎨 **Quadro Branco** (Web App & Canvas Editor) é uma aplicação de alta fidelidade, desenvolvida em **Streamlit** com arquitetura **Fullstack (HTML5 / Fabric.js / CSS3 / JavaScript)**.

O projeto é resultado da **engenharia reversa e refatoração completa** de uma extensão WebExtension para navegadores, convertida em uma ferramenta standalone de tela cheia, fluida e totalmente responsiva.

Por **Ary Ribeiro**: https://www.linkedin.com/in/aryribeiro
---

## 🌟 Destaques & Recursos Avançados

* 🤍 **Interface "Tela Branca" Minimalista:** Zera e oculta cabeçalhos, rodapés e margens nativas do Streamlit.
* 🍔 **Menu Hambúrguer Flutuante:** Posicionado no canto superior esquerdo, recolhido por padrão.
* ⚡ **Performance de 60 FPS:** Motor gráfico **Fabric.js** executado diretamente no navegador do cliente sem gargalos de *rerun* no servidor.
* 🎯 **Ponteiro Laser Neon (Com Fade-out):** Desenhe um rastro incandescente que se dissipa suavemente em frações de segundo. Isolado do histórico (`undo/redo`) e sem arrastar objetos ou imagens do quadro.
* ✂️ **Ferramenta de Recorte Interativa (Crop):** Selecione uma imagem existente ou desenhe uma caixa pontilhada em qualquer área livre da tela para realizar o corte instantâneo.
* 📋 **Suporte a Colar da Área de Transferência (`Ctrl + V`):** Cole screenshots e imagens diretamente no quadro sem necessidade de upload manual.
* 🔊 **Feedback Sonoro:** Som de obturador sintetizado via **Web Audio API** ao exportar o quadro.

---

## 🛠️ Tabela Completa de Ferramentas

| Ícone | Ferramenta | Descrição |
| :---: | :--- | :--- |
| 🎨 | **Seletor de Cores** | Ajusta a cor de traços, preenchimentos, formas e textos. |
| ↩️ / ↪️ | **Desfazer / Refazer** | Controle total de histórico da área de trabalho. |
| 🖐️ | **Selecionar / Mover** | Selecione, dimensione, rotacione e reposicione elementos. |
| ✏️ | **Pincel / Caneta** | Desenho livre ajustável. |
| 🖍️ | **Marca-Texto** | Traço translúcido para destacar informações. |
| 🧽 | **Borracha** | Apaga traços diretamente sobre o plano de fundo. |
| 🔤 | **Texto** | Inserção de caixa de texto editável (`IText`). |
| 🔲 / ⭕ | **Formas Vazadas** | Retângulos e Círculos com contorno customizado. |
| ⬛ / 🔴 | **Formas Preenchidas** | Retângulos e Círculos sólidos. |
| ➖ / ➡️ | **Linhas e Setas** | Criação de linhas retas e setas direcionais. |
| 🖼️ | **Carregar Imagem** | Upload local com escala e centralização inteligente. |
| 📋 | **Duplicar Objeto** | Clona elementos ativos na área de trabalho. |
| 🔝 | **Trazer para Frente** | Ajusta a ordem das camadas do canvas (Z-Index). |
| 🗑️ | **Excluir Selecionado** | Remove o objeto ou conjunto de objetos ativos. |
| ✂️ | **Ferramenta de Corte (Crop)** | Recorta imagens ativas ou regiões do quadro. |
| 🎯 | **Ponteiro Laser** | Rastro vermelho incandescente temporário para apresentações. |
| 🔍 | **Zoom In / Out** | Controle de ampliação e navegação. |
| 🧹 | **Limpar Tela** | Reseta todo o quadro para branco. |
| 💾 | **Exportar PNG** | Baixa a imagem final em alta resolução com efeito sonoro. |

---

## ⌨️ Atalhos de Teclado (Hotkeys)

| Atalho | Ação |
| :--- | :--- |
| `Ctrl + Z` / `Cmd + Z` | Desfazer (*Undo*) |
| `Ctrl + Y` / `Cmd + Y` | Refazer (*Redo*) |
| `Ctrl + V` / `Cmd + V` | Colar Imagem da Área de Transferência |
| `Enter` | Confirmar Recorte no Modo Crop |
| `Delete` / `Backspace` | Excluir elemento selecionado |
| `P` | Ativar Pincel |
| `E` | Ativar Borracha |
| `T` | Inserir Texto |
| `R` | Desenhar Retângulo |
| `C` | Desenhar Círculo |
| `L` | Desenhar Linha Reta |
| `A` | Inserir Seta |
| `V` ou `M` | Modo Selecionar / Mover |

---

## 🚀 Como Executar Localmente

### Pré-requisitos
* **Python 3.9 ou superior** instalado.

**Clone este repositório:**
   ```bash
   git clone https://github.com/aryribeiro/quadro-branco.git
   cd quadro-branco
