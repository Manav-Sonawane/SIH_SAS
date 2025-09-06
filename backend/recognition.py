import cv2
import os
from deepface import DeepFace
from backend.database import mark_attendance

faces_folder = "faces/"
known_faces = [f for f in os.listdir(faces_folder) if f.endswith(".jpg")]


def recognize_face():
    """
    Open webcam and check against known faces.
    If a match is found, mark attendance and close.
    """
    cap = cv2.VideoCapture(0)

    recognized = False

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow("Recognition - Press Q to quit", frame)

        # Save current frame temporarily
        temp_file = "temp.jpg"
        cv2.imwrite(temp_file, frame)

        # Compare with known faces
        for face_img in known_faces:
            try:
                result = DeepFace.verify(
                    f"{faces_folder}{face_img}",
                    temp_file,
                    enforce_detection=False
                )
                if result["verified"]:
                    name = face_img.split(".")[0]
                    mark_attendance(name)
                    print(f"""     
                                            
                          [Recognition] {name} verified. Attendance marked.
                          
                          """)
                    recognized = True
                    break
            except Exception as e:
                print("[Recognition Error]:", e)

        # Exit if recognized OR user presses Q
        if recognized or (cv2.waitKey(1) & 0xFF == ord('q')):
            break

    cap.release()
    cv2.destroyAllWindows()
    return recognized
