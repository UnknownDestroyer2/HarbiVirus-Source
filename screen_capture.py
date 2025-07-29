import tkinter as tk
from PIL import ImageGrab, ImageTk
import random

def capture_screen():
    """Capture the current screen"""
    return ImageGrab.grab()