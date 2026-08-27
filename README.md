# Atividade Prática – Detecção de Objetos em Vídeo

Algoritmo desenvolvido em Python utilizando **YOLOv8** e **OpenCV** para detecção e classificação de objetos em vídeos (arquivos locais ou links diretos do YouTube).

---

## 🎯 Objetivos e Funcionalidades

- **Detecção de Objetos**: Identificação e classificação com caixas delimitadoras (*bounding boxes*), nome da classe (ex.: `person`, `car`, `bus`, `dog`, etc.) e nível de confiança.
- **Suporte a Múltiplas Fontes**:
  - URLs de vídeos do **YouTube** (processadas e baixadas automaticamente com `yt-dlp`).
  - Arquivos de vídeo **locais** (`.mp4`, `.avi`, `.mkv`, etc.).
- **Visualização em Tempo Real**: Janela interativa OpenCV com opção de encerrar pressionando a tecla `q`.
- **Gravação de Resultados**: Salva o vídeo com as detecções anotadas em `output_detectado.mp4`.

---

## ⚙️ Pré-requisitos e Instalação

1. **Criar e ativar o ambiente virtual:**
   - **Linux / macOS:**
     ```bash
     python -m venv venv
     source venv/bin/activate
     ```
   - **Windows:**
     ```cmd
     python -m venv venv
     venv\Scripts\activate
     ```

2. **Instalar as dependências:**
   ```bash
   python -m pip install ultralytics opencv-python yt-dlp
   ```

---

## 🚀 Como Executar

### 1. Com vídeo padrão do YouTube
```bash
python main.py
```

### 2. Com uma URL personalizada do YouTube
```bash
python main.py "https://www.youtube.com/watch?v=TvJoRRvEeF8"
```

### 3. Com um vídeo local
```bash
python main.py "caminho/para/seu_video.mp4"
```

