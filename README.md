# 👁️ Detecção de Objetos em Vídeo & Web (YOLOv8 + OpenCV + React / TensorFlow.js)

Repositório acadêmico com implementações para detecção e classificação de objetos em vídeo e navegadores, combinando um pipeline de Visão Computacional em Python (YOLOv8 + OpenCV + yt-dlp) e uma aplicação web interativa em React 19 com TypeScript, Vite e Material UI (MUI).

---

## 🎯 Funcionalidades

### 1. Pipeline de Visão Computacional em Python (`main.py`)
- **Detecção com Deep Learning:** Uso da rede neural convolucional YOLOv8 nano (`yolov8n.pt`) para identificação de objetos e pessoas em tempo real.
- **Suporte a Múltiplas Fontes de Vídeo:**
  - Ingestão direta de links do **YouTube** com download automático e merge de áudio/vídeo via `yt-dlp`.
  - Processamento de arquivos de vídeo locais (`.mp4`, `.avi`, `.mkv`, etc.).
- **Visualização em Tempo Real:** Renderização com caixas delimitadoras (*bounding boxes*), rótulo da classe identificada e índice de confiança por frame.
- **Exportação de Resultados:** Gravação automática do vídeo anotado em `output_detectado.mp4`.

### 2. Interface Web em React & TypeScript
- Estrutura moderna com **React 19**, **TypeScript** e **Vite**.
- Componentes visuais com **Material UI (MUI v6/v7)** e Emotion.
- Configurado com dependências para inferência no cliente via **TensorFlow.js** (`@tensorflow/tfjs` e `@tensorflow-models/coco-ssd`).
- Linter ultrarrápido com **Oxlint**.

---

## 🛠️ Tecnologias Utilizadas

- **Pipeline Python:** Python 3.10+, Ultralytics YOLOv8, OpenCV (`cv2`), `yt-dlp`.
- **Frontend Web:** React 19, TypeScript, Vite, Material UI (MUI), TensorFlow.js, Oxlint.

---

## 📁 Estrutura do Repositório

```text
.
├── src/                   # Aplicação frontend em React + TypeScript
│   ├── components/        # Componentes reutilizáveis (button, input)
│   ├── App.tsx            # Layout com drawer responsivo e AppBar Material UI
│   └── main.tsx           # Ponto de entrada React DOM
├── public/                # Assets estáticos
├── main.py                # Script de detecção com YOLOv8 e OpenCV
├── index.html             # Ponto de entrada HTML do Vite
├── package.json           # Dependências e scripts do frontend
├── tsconfig.json          # Configurações TypeScript
├── vite.config.ts         # Configuração de build do Vite
├── .oxlintrc.json         # Regras de linting estático com Oxlint
└── README.md              # Documentação técnica do projeto
```

---

## 🚀 Como Executar

### Opção A: Executar o Pipeline Python (YOLOv8)

#### 1. Criar e ativar o ambiente virtual

```bash
python3 -m venv .venv
source .venv/bin/activate  # Linux/macOS
# ou .venv\Scripts\activate no Windows
```

#### 2. Instalar dependências

```bash
pip install ultralytics opencv-python yt-dlp
```

#### 3. Executar com vídeo padrão do YouTube
```bash
python main.py
```

#### 4. Executar com uma URL específica do YouTube
```bash
python main.py "https://www.youtube.com/watch?v=SEU_LINK"
```

#### 5. Executar com um arquivo de vídeo local
```bash
python main.py "caminho/para/seu_video.mp4"
```

> **Controle interativo:** Para encerrar o processamento antes do fim do vídeo, pressione a tecla `q` na janela de exibição do OpenCV.

---

### Opção B: Executar a Aplicação Web (React + Vite)

#### 1. Instalar as dependências do Node.js

```bash
npm install
```

#### 2. Iniciar o servidor de desenvolvimento

```bash
npm run dev
```

Abra a URL indicada no terminal (geralmente `http://localhost:5173`).

#### 3. Verificar linting e compilação

```bash
npm run lint     # Análise com Oxlint
npm run build    # Checagem de tipos (tsc) e build de produção
```

---

## ⚠️ Limitações e Observações Técnicas

- O processamento de vídeos longos em resolução alta sem GPU dedicada (CUDA) pode apresentar taxa de frames reduzida durante a inferência com OpenCV no script Python.
- Na primeira execução de `main.py`, os pesos pré-treinados `yolov8n.pt` (~6 MB) são baixados automaticamente pelo Ultralytics.
