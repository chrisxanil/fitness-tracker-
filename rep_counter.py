from pose_module import PoseDetector

class RepCounter:
    def __init__(self, exercise):
        self.count = 0
        self.dir = 0 
        self.exercise = exercise
        self.detector = PoseDetector()

    def update(self, lm):
        if self.exercise == "Push-ups":
            return self._pushup_logic(lm)
        elif self.exercise == "Squats":
            return self._squat_logic(lm)
        elif self.exercise == "Crunches":
            return self._crunch_logic(lm)
        return False, None

    def _pushup_logic(self, lm):
        if 11 in lm and 13 in lm and 15 in lm:
            angle = self.detector.find_angle(lm[11], lm[13], lm[15])  

            if angle < 90 and self.dir == 0:
                self.dir = 1
            if angle > 160 and self.dir == 1:
                self.count += 1
                self.dir = 0
                return True, "up"
            return False, "down"
        return False, None

    def _squat_logic(self, lm):
        if 23 in lm and 25 in lm and 27 in lm:
            angle = self.detector.find_angle(lm[23], lm[25], lm[27]) 

            if angle < 90 and self.dir == 0:
                self.dir = 1
            if angle > 160 and self.dir == 1:
                self.count += 1
                self.dir = 0
                return True, "up"
            return False, "down"
        return False, None

    def _crunch_logic(self, lm):
        if 11 in lm and 23 in lm and 25 in lm:
            angle = self.detector.find_angle(lm[11], lm[23], lm[25])

            if angle < 100 and self.dir == 0:
                self.dir = 1
            if angle > 150 and self.dir == 1:
                self.count += 1
                self.dir = 0
                return True, "up"
            return False, "down"
        return False, None
