from ultralytics import YOLO
import cv2


MODEL_PATH = "bird-dataset/runs/detect/train/weights/best.pt"
CONF_THRESHOLD = 0.65
MIN_BOX_AREA = 3000


model = YOLO(MODEL_PATH)
print("Classes:", model.names)

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Camera not detected")
    exit()

print("Camera started. Press Q to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break


    results = model(frame, conf=CONF_THRESHOLD, verbose=False)

    bird_detected = False

    for r in results:
        if r.boxes is None:
            continue

        for box in r.boxes:
            cls = int(box.cls.item())
            name = model.names[cls]
            conf = float(box.conf.item())

            x1, y1, x2, y2 = map(int, box.xyxy[0])


            box_width = x2 - x1
            box_height = y2 - y1
            box_area = box_width * box_height

            if box_area < MIN_BOX_AREA:
                continue



            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)


            cv2.putText(
                frame,
                f"{name} {conf:.2f}",
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 0),
                2
            )

            if name.lower() == "bird":
                bird_detected = True


    if bird_detected:
        cv2.putText(
            frame,
            "BIRD DETECTED",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            3
        )
        print("Bird Detected")


    cv2.imshow("AI Bird Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
