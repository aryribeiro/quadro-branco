# 🎨 Quadro Branco — Web App & Canvas Editor

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://quadro.streamlit.app)
![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat&logo=python&logoColor=white)
![Fabric.js](https://img.shields.io/badge/Fabric.js-5.3.1-blue?style=flat)
![License](https://img.shields.io/badge/License-MIT-green.svg)

O **Quadro Branco** é um Web Application de alta fidelidade desenvolvido em **Streamlit** com injeção **Fullstack (HTML5 / Fabric.js / CSS3 / JavaScript)**. 

O projeto é resultado da **engenharia reversa e refatoração** de uma extensão WebExtension para navegadores, transformando-a em uma aplicação standalone de tela cheia, sem distrações e pronta para rodar em qualquer dispositivo ou navegador.

---

## 🌟 Destaques & Diferenciais

* 🤍 **Interface "Tela Branca" Minimalista:** Zero distrações, sem cabeçalhos, rodapés ou menus nativos poluindo a viewport.
* 🍔 **Menu Hambúrguer Flutuante:** Posicionado no canto superior esquerdo e recolhido por padrão. Ao clicar, abre a paleta completa de ferramentas.
* 🚀 **Renderização de Alta Performance:** Canvas vetorial rodando a 60 FPS via **Fabric.js** diretamente no navegador do cliente.
* 📋 **Suporte a Colar da Área de Transferência (`Ctrl + V`):** Cole screenshots e imagens copiadas diretamente no quadro sem precisar fazer upload manual.
* 🖼️ **Upload Inteligente de Imagens:** Redimensionamento e centralização automática de imagens sem ocultação ou bugs de renderização.
* 🔊 **Feedback Sonoro:** Efeito sonoro de obturador de câmera sintetizado via **Web Audio API** ao exportar a imagem.

---

## 🛠️ Ferramentas Disponíveis

| Ícone | Ferramenta | Descrição |
| :---: | :--- | :--- |
| 🎨 | **Seletor de Cores** | Cor customizada para traços, formas e textos. |
| ↩️ / ↪️ | **Undo / Redo** | Histórico completo de ações (Desfazer e Refazer). |
| 🖐️ | **Selecionar / Mover** | Manipule, redimensione e rotacione elementos na tela. |
| ✏️ | **Pincel** | Desenho livre ajustável. |
| 🖍️ | **Marca-Texto** | Traço translúcido para destacar textos e áreas. |
| 🧽 | **Borracha** | Apaga traços diretamente no plano de fundo. |
| 🔤 | **Texto** | Inserção de caixa de texto editável. |
| 🔲 / ⭕ | **Formas Vazadas** | Retângulos e Círculos com contorno. |
| ⬛ / 🔴 | **Formas Preenchidas** | Retângulos e Círculos com preenchimento sólido. |
| ➖ / ➡️ | **Linhas e Setas** | Desenho de linhas retas e setas direcionais. |
| 🖼️ | **Carregar Imagem** | Upload de imagens locais/screenshots. |
| 📋 | **Duplicar Objeto** | Clona o elemento selecionado no canvas. |
| 🔝 | **Trazer para Frente** | Ajusta a ordem de camadas (Z-Index). |
| 🗑️ | **Excluir Selecionado** | Remove o objeto ativo no momento. |
| 🔍 | **Zoom In / Out** | Controle de zoom para navegação no quadro. |
| 🧹 | **Limpar Tela** | Reseta todo o canvas para branco. |
| 💾 | **Salvar PNG** | Exporta o quadro atual em alta resolução. |

---

## ⌨️ Atalhos de Teclado (Hotkeys)

| Atalho | Ação |
| :--- | :--- |
| `Ctrl + Z` / `Cmd + Z` | Desfazer (*Undo*) |
| `Ctrl + Y` / `Cmd + Y` | Refazer (*Redo*) |
| `Ctrl + V` / `Cmd + V` | Colar Imagem da Área de Transferência |
| `Delete` / `Backspace` | Excluir elemento selecionado |
| `P` | Ativar Pincel |
| `E` | Ativar Borracha |
| `T` | Inserir Texto |
| `R` | Criar Retângulo |
| `C` | Criar Círculo |
| `L` | Criar Linha |
| `A` | Criar Seta |
| `V` ou `M` | Modo Selecionar / Mover |

---

## 🚀 Como Executar Localmente

### Pré-requisitos
* **Python 3.9+** instalado na máquina.

### Passo a Passo

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/aryribeiro/quadro-branco.git](https://github.com/aryribeiro/quadro-branco.git)
   cd quadro-branco