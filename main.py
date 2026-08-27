import os
import cv2
import sys
import tempfile
import yt_dlp
from ultralytics import YOLO

os.environ["PATH"] = os.path.expanduser("~/.deno/bin") + ":" + os.environ.get("PATH", "")


def download_video(url):
    print(f"Baixando video do YouTube: {url}")
    tmp = tempfile.mkdtemp()
    output = os.path.join(tmp, "video.mp4")

    ydl_opts = {
        "format": "bestvideo[vcodec^=avc1][height<=480]+bestaudio[ext=m4a]/best[ext=mp4][height<=480]/best[ext=mp4]/best",
        "outtmpl": output,
        "merge_output_format": "mp4",
        "quiet": True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    if not os.path.exists(output):
        for f in os.listdir(tmp):
            if f.endswith((".mp4", ".webm", ".mkv")):
                output = os.path.join(tmp, f)
                break

    print(f"Video salvo: {output}")
    return output


def main():
    source = sys.argv[1] if len(sys.argv) > 1 else "https://www.youtube.com/watch?v=TvJoRRvEeF8"

    if source.startswith("http"):
        video_path = download_video(source)
    else:
        video_path = source

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Erro ao abrir o video")
        sys.exit(1)

    model = YOLO("yolov8n.pt")
    classNames = model.names

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS) or 30

    output_file = "output_detectado.mp4"
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter(output_file, fourcc, fps, (width, height))

    print(f"Processando video... ({width}x{height}, {fps:.0f} FPS)")
    print("Pressione 'q' para sair")

    frame_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_count += 1
        results = model(frame, verbose=False)

        for r in results:
            for box in r.boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                confidence = float(box.conf[0])
                class_id = int(box.cls[0])
                label = classNames[class_id]

                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                text = f"{label} {confidence:.2f}"
                (tw, th), _ = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 1)
                cv2.rectangle(frame, (x1, y1 - th - 10), (x1 + tw, y1), (0, 255, 0), -1)
                cv2.putText(frame, text, (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 1)

        out.write(frame)
        cv2.imshow("YOLO Deteccao de Objetos", frame)

        if frame_count % 30 == 0:
            print(f"Frame {frame_count} processado...")

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()
    print(f"\nFinalizado! {frame_count} frames -> {output_file}")


if __name__ == "__main__":
    main()
