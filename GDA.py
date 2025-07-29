import mss
import numpy as np
import cv2
import win32gui, win32con
import time

def glitch_frame(frame):
    # Balanced brightness and saturation
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV).astype(np.float32)
    hsv[:,:,2] = np.clip(hsv[:,:,2] * np.random.uniform(0.95, 1.05), 0, 255)  # Minimal brightness change
    hsv[:,:,1] = np.clip(hsv[:,:,1] * np.random.uniform(1.2, 1.5), 0, 255)  # Moderate saturation boost
    img = cv2.cvtColor(hsv.astype(np.uint8), cv2.COLOR_HSV2BGR)

    # Band + channel glitch
    h, w, _ = img.shape
    gl = img.copy()
    band_h = np.random.choice([4,6,8,10])
    for y in range(0, h, band_h):
        shift = np.random.randint(-30,30)
        gl[y:y+band_h] = np.roll(gl[y:y+band_h], shift, axis=1)
    b,g,r = cv2.split(gl)
    b = np.roll(b, np.random.randint(-12,12), axis=1)
    g = np.roll(g, np.random.randint(-12,12), axis=0)
    r = np.roll(r, np.random.randint(-12,12), axis=1)
    gl = cv2.merge([b,g,r])

    # Balanced scanlines with glow
    overlay = np.zeros_like(gl)  # Start with black overlay
    num_lines = np.random.randint(3,6)
    for _ in range(num_lines):
        y = np.random.randint(0, h)
        thickness = np.random.randint(1,3)
        cv2.line(overlay, (0,y), (w,y), (255,255,255), thickness)  # White scanlines
    
    # Gentle glow effect
    glow = cv2.GaussianBlur(overlay, (0,0), sigmaX=3, sigmaY=3)
    gl = cv2.addWeighted(gl, 1.0, glow, 0.3, 0)  # Add glow without darkening

    return gl

# Fullscreen setup
win = 'GLITCH'
cv2.namedWindow(win, cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty(win, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

# Configure window transparency BEFORE first display
hwnd = win32gui.FindWindow(None, win)
if hwnd:
    style = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
    new_style = style | win32con.WS_EX_LAYERED | win32con.WS_EX_TRANSPARENT | win32con.WS_EX_TOPMOST
    win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, new_style)
    win32gui.SetLayeredWindowAttributes(hwnd, 0, 255, win32con.LWA_ALPHA)

# Capture and process first frame
sct = mss.mss()
mon = sct.monitors[1]
first = np.array(sct.grab(mon))[:,:,:3]
first = glitch_frame(first)
cv2.imshow(win, first)
cv2.waitKey(1)

# Main loop
while True:
    frame = np.array(sct.grab(mon))[:,:,:3]
    glitched = glitch_frame(frame)
    cv2.imshow(win, glitched)
    if cv2.waitKey(1) == 27:  # ESC
        break

cv2.destroyAllWindows()
sct.close()
