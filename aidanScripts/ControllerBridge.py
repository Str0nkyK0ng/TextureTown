import time
import pygame
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController

# --- CONFIGURATION ---
MOUSE_SENSITIVITY = 15
DEADZONE = 0.2
# ---------------------

def main():
    # 1. Initialize Pygame (for Joystick reading only)
    pygame.init()
    pygame.joystick.init()

    if pygame.joystick.get_count() == 0:
        print("No controller found! Plug one in and restart.")
        return

    # Use the first controller
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    print(f"Mapped to: {joystick.get_name()}")
    print("Keep this window open. Press Ctrl+C to stop.")

    # 2. Initialize Controllers
    keyboard = KeyboardController()
    mouse = MouseController()

    # State tracking to prevent key spamming
    state = {
        'up': False,
        'down': False,
        'left': False,
        'right': False,
        'l_click': False
    }

    try:
        while True:
            # Pygame needs to process internal events to update joystick values
            pygame.event.pump()

            # --- LEFT STICK (Movement) ---
            # Axis 0 = Left/Right, Axis 1 = Up/Down
            # Note: Y-axis is usually inverted (Up is negative)
            lx = joystick.get_axis(0)
            ly = joystick.get_axis(1)

            # UP
            if ly < -DEADZONE:
                if not state['up']:
                    keyboard.press(Key.up)
                    state['up'] = True
            else:
                if state['up']:
                    keyboard.release(Key.up)
                    state['up'] = False

            # DOWN
            if ly > DEADZONE:
                if not state['down']:
                    keyboard.press(Key.down)
                    state['down'] = True
            else:
                if state['down']:
                    keyboard.release(Key.down)
                    state['down'] = False

            # LEFT
            if lx < -DEADZONE:
                if not state['left']:
                    keyboard.press(Key.left)
                    state['left'] = True
            else:
                if state['left']:
                    keyboard.release(Key.left)
                    state['left'] = False

            # RIGHT
            if lx > DEADZONE:
                if not state['right']:
                    keyboard.press(Key.right)
                    state['right'] = True
            else:
                if state['right']:
                    keyboard.release(Key.right)
                    state['right'] = False

            # --- RIGHT STICK (Mouse) ---
            # Axis 2 = Left/Right, Axis 3 = Up/Down (Mappings vary by controller!)
            # Xbox standard: RX=3, RY=4 on some OS, or 2/3 on others.
            # You might need to adjust these indices if your mouse moves weirdly.
            rx = joystick.get_axis(2) 
            ry = joystick.get_axis(3)

            if abs(rx) > DEADZONE or abs(ry) > DEADZONE:
                mouse.move(int(rx * MOUSE_SENSITIVITY), int(ry * MOUSE_SENSITIVITY))

            # --- TRIGGERS / BUTTONS (Click) ---
            # Buttons are 0, 1, 2... 
            # Xbox "A" is usually 0. Right Trigger is sometimes an Axis (Z-axis).
            # For simplicity, let's map Button 0 (A) to Jump (Ctrl) 
            # and Button 5 (RB/R1) to Click.
            
            # Jump (A Button)
            if joystick.get_button(0): 
                keyboard.press(Key.ctrl)
            else:
                keyboard.release(Key.ctrl)

            # Click (Right Bumper / R1)
            # If you want Trigger, you often have to check Axis 4 or 5 depending on OS
            if joystick.get_button(5): 
                if not state['l_click']:
                    mouse.press(Button.left)
                    state['l_click'] = True
            else:
                if state['l_click']:
                    mouse.release(Button.left)
                    state['l_click'] = False

            # Sleep to prevent high CPU usage
            time.sleep(0.01)

    except KeyboardInterrupt:
        print("\nExiting mapper...")
        pygame.quit()

if __name__ == "__main__":
    main()