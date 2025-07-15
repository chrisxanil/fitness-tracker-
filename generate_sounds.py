import base64
import os
os.makedirs("sounds", exist_ok=True)
correct_base64 = """
UklGRrQAAABXQVZFZm10IBAAAAABAAEAQB8AAIA+AAACABAAZGF0YYwAAABfAACAPwAAgD8AAIA/
AACAQAAAQD8AAEA/AABAPwAAQD8AAEA/AABAQAAAQD8AAEA/AABAPwAAQD8AAIA/AAAAQAAAQD8A
AIA/AACAQAAAQD8AAEA/AABAQAAAQD8AAEA/AABAQAAAQD8AAEA/AABAQAAAQD8AAEA/AABAQAAA
"""
wrong_base64 = """
UklGRqYAAABXQVZFZm10IBAAAAABAAEAQB8AAIA+AAACABAAZGF0YYoAAACqqqqqqqqqqqqqqqqq
qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq
qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq
"""
with open("sounds/correct.wav", "wb") as f:
    f.write(base64.b64decode(correct_base64))
with open("sounds/wrong.wav", "wb") as f:
    f.write(base64.b64decode(wrong_base64))
print("✅ Sound files created: sounds/correct.wav and sounds/wrong.wav")
