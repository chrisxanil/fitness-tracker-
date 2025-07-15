# pose_module.py
import cv2
import mediapipe as mp
import numpy as np

class PoseDetector:
    def __init__(self):
        self.pose = mp.solutions.pose.Pose()
        self.hands = mp.solutions.hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
        self.draw = mp.solutions.drawing_utils

    def find_pose(self, img):
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = self.pose.process(img_rgb)

        landmarks = {}
        if results.pose_landmarks:
            self.draw.draw_landmarks(img, results.pose_landmarks, mp.solutions.pose.POSE_CONNECTIONS)
            for id, lm in enumerate(results.pose_landmarks.landmark):
                h, w = img.shape[:2]
                cx, cy = int(lm.x * w), int(lm.y * h)
                landmarks[id] = (cx, cy)

        return landmarks

    def find_angle(self, p1, p2, p3):
        a = np.array(p1)
        b = np.array(p2)
        c = np.array(p3)

        radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
        angle = np.abs(radians * 180.0 / np.pi)
        if angle > 180:
            angle = 360 - angle
        return angle

    def fingers_up(self, img):
        fingers = []
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = self.hands.process(img_rgb)

        if results.multi_hand_landmarks:
            hand_landmarks = results.multi_hand_landmarks[0]
            lm_list = []
            h, w = img.shape[:2]
            for id, lm in enumerate(hand_landmarks.landmark):
                cx, cy = int(lm.x * w), int(lm.y * h)
                lm_list.append((cx, cy))

            if lm_list[4][0] < lm_list[3][0]:
                fingers.append(1)
            else:
                fingers.append(0)

            tips = [8, 12, 16, 20]
            for tip in tips:
                if lm_list[tip][1] < lm_list[tip - 2][1]: 
                    fingers.append(1)
                else:
                    fingers.append(0)

        return fingers 
