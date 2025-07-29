import cv2
import numpy as np
import pyautogui
import time
import tkinter as tk
from PIL import Image, ImageTk

def apply_glitch_effect():
    root = tk.Tk()
    root.attributes('-topmost', True)
    root.overrideredirect(True)
    root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}+0+0")
    label = tk.Label(root)
    label.pack()
    
    def update_glitch():
        # Capture screenshot
        screenshot = pyautogui.screenshot()
        screenshot = np.array(screenshot)
        screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)
        
        # Get image dimensions
        height, width, channels = screenshot.shape
        
        # Create glitch effect by shifting rows randomly (without pixelation)
        glitched_image = screenshot.copy()
        for i in range(0, height, 5):  # Apply effect every 5 pixels
            offset = np.random.randint(-50, 50)  # Random horizontal shift (more range)
            glitched_image[i:i+5] = np.roll(screenshot[i:i+5], offset, axis=1)
        
        # Convert to PIL Image
        glitched_image = cv2.cvtColor(glitched_image, cv2.COLOR_BGR2RGB)
        glitched_image = Image.fromarray(glitched_image)
        
        # Update image on label
        img = ImageTk.PhotoImage(glitched_image)
        label.config(image=img)
        label.image = img
        
        # Repeat every seconds
        root.after(5, update_glitch)
    
    update_glitch()
    root.mainloop()

# Example usage
apply_glitch_effect()
