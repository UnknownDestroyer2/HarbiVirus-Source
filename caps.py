import pyautogui
import time
import random

def cool_animation():
    keys = ['numlock', 'capslock', 'scrolllock']  # Keys to control

    while True:
        # 1. All keys close, then open all at once
        print("Closing all lights...")
        for key in keys:
            pyautogui.press(key)  # Turn off the key (turn off lights)
        time.sleep(0.5)

        print("Opening all lights...")
        for key in keys:
            pyautogui.press(key)  # Turn on the key (turn on lights)
        time.sleep(1)

        # 2. Blinking effect: All keys blink rapidly together multiple times
        for _ in range(5):  # Blink 5 times
            for key in keys:
                pyautogui.press(key)  # Turn on
            time.sleep(0.1)  # Small pause
            for key in keys:
                pyautogui.press(key)  # Turn off
            time.sleep(0.1)  # Small pause

        # 3. Random key opening/closing in random order
        for _ in range(3):  # Do this random effect 3 times
            random.shuffle(keys)  # Randomize the order of the keys
            for key in keys:
                pyautogui.press(key)  # Turn on key
                time.sleep(random.uniform(0.1, 0.3))  # Random delay
            time.sleep(0.5)  # Pause before closing
            for key in keys:
                pyautogui.press(key)  # Turn off key
                time.sleep(random.uniform(0.1, 0.3))  # Random delay
            time.sleep(0.5)  # Pause before next random cycle

        # 4. Flashing lights (all on then off, a few times)
        for _ in range(3):  # Flash the lights 3 times
            for key in keys:
                pyautogui.press(key)  # Turn on all
            time.sleep(0.2)  # Wait
            for key in keys:
                pyautogui.press(key)  # Turn off all
            time.sleep(0.2)  # Wait

        # 5. Keylights open one by one with increasing speed
        delay = 0.5  # Starting delay
        for cycle in range(3):  # 3 cycles
            for key in keys:
                pyautogui.press(key)  # Open key
                time.sleep(delay)  # Delay between opening keys
            delay *= 0.7  # Speed up the animation by decreasing the delay

        # 6. Reverse opening effect (right-to-left)
        for cycle in range(2):  # Do the reverse effect twice
            for key in reversed(keys):
                pyautogui.press(key)  # Open key
                time.sleep(random.uniform(0.1, 0.3))  # Random speed

            # Close all lights after the cycle
            for key in keys:
                pyautogui.press(key)  # Turn off all keys
            time.sleep(0.5)  # Pause before next cycle

        # 7. Flashing alternate keys (one on, one off alternately)
        for _ in range(3):  # Repeat 3 times
            for i, key in enumerate(keys):
                if i % 2 == 0:
                    pyautogui.press(key)  # Turn on alternate keys
            time.sleep(0.2)
            for i, key in enumerate(keys):
                if i % 2 == 0:
                    pyautogui.press(key)  # Turn off alternate keys
            time.sleep(0.2)

        # 8. Random full blinking (randomize all keys on and off at random times)
        for _ in range(5):  # Do the random full blinking 5 times
            for key in keys:
                pyautogui.press(key)  # Turn on key
                time.sleep(random.uniform(0.1, 0.3))  # Random delay
            for key in keys:
                pyautogui.press(key)  # Turn off key
                time.sleep(random.uniform(0.1, 0.3))  # Random delay

        # 9. Lights open in order with speed changes (accelerating)
        delay = 0.6  # Starting delay
        for cycle in range(3):  # 3 cycles
            for key in keys:
                pyautogui.press(key)  # Open key one by one
                time.sleep(delay)
            delay *= 0.7  # Speed up the opening animation

        # 10. Ultimate flashing (All keys flash rapidly and randomly)
        for _ in range(12):  # Flash twice
            for key in keys:
                pyautogui.press(key)  # Turn on all keys
            time.sleep(0.1)
            for key in keys:
                pyautogui.press(key)  # Turn off all keys
            time.sleep(0.1)

    

        time.sleep(1)  # Wait for 1 second before starting the loop again

cool_animation()
