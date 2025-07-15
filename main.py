import cv2
import pygame
from rep_counter import RepCounter
from pose_module import PoseDetector

pygame.mixer.init()
correct_sound = pygame.mixer.Sound("sounds/correct.wav")
wrong_sound = pygame.mixer.Sound("sounds/wrong.wav")

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("❌ ERROR: Webcam not accessible")
    exit()

detector = PoseDetector()
exercise = "Squats"
counter = RepCounter(exercise)
prev_fingers = []

while True:
    success, frame = cap.read()
    if not success:
        continue

    frame = cv2.flip(frame, 1)
    h, w = frame.shape[:2]

    landmarks = detector.find_pose(frame)

    fingers = detector.fingers_up(frame)
    if fingers and fingers != prev_fingers:
        prev_fingers = fingers

        if fingers[1] == 1 and fingers[2:] == [0, 0, 0]:  # Index only
            exercise = "Push-ups"
            counter = RepCounter(exercise)
        elif fingers[2] == 1 and fingers[1] == 0 and fingers[3] == 0:  # Middle only
            exercise = "Squats"
            counter = RepCounter(exercise)
        elif fingers[3] == 1 and fingers[1] == 0 and fingers[2] == 0:  # Ring only
            exercise = "Crunches"
            counter = RepCounter(exercise)

    cv2.putText(frame, f"Exercise: {exercise}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)

    if landmarks:
        valid_form, stage = counter.update(landmarks)
        if valid_form:
            correct_sound.play()
        elif stage == "down":
            wrong_sound.play()

        cv2.putText(frame, f"Reps: {counter.count}", (w - 200, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 3)

    cv2.imshow("Fitness Rep Counter", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
