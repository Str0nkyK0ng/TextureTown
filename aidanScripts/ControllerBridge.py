import time
import pygame
import win32gui
import win32con
import win32api
import os
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController

# --- CONFIGURATION ---
MOUSE_SENSITIVITY = 15
DEADZONE = 0.2
# ---------------------

def make_borderless_fullscreen(window_title):
    # 1. Find the window handle (HWND)
    hwnd = win32gui.FindWindow(None, window_title)
    if not hwnd:
        print(f"Window '{window_title}' not found!")

    # 2. Get the current window style
    # GWL_STYLE retrieves the window's style bits
    style = win32gui.GetWindowLong(hwnd, win32con.GWL_STYLE)

    # 3. Remove the title bar and borders
    # We use bitwise AND (&) with NOT (~) to remove specific style flags
    # WS_CAPTION = Title bar
    # WS_THICKFRAME = Resizing border
    style = style & ~win32con.WS_CAPTION & ~win32con.WS_THICKFRAME
    
    # Apply the new style
    win32gui.SetWindowLong(hwnd, win32con.GWL_STYLE, style)

    # 4. Get the screen resolution
    # 0 = SystemMetric for Screen Width
    # 1 = SystemMetric for Screen Height
    screen_width = win32api.GetSystemMetrics(0)
    screen_height = win32api.GetSystemMetrics(1)

    # 5. Resize and move the window
    # HWND_TOP = Place it at the top of the Z-order
    # SWP_FRAMECHANGED = Forces the window to redraw its style
    win32gui.SetWindowPos(
        hwnd, 
        win32con.HWND_TOP, 
        0, 0, screen_width, screen_height, 
        win32con.SWP_FRAMECHANGED | win32con.SWP_SHOWWINDOW
    )
    
    print(f"Successfully transformed '{window_title}'")

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
    # wait a moment for the game to start and then make it borderless fullscreen
    time.sleep(5)  # Adjust this delay as needed for your game to load
    make_borderless_fullscreen("Toontown")  # Change this to your game's window title

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
            # do the triggers too
            # Right Trigger (Axis 5 or 4 depending on controller/OS)
            rt = joystick.get_axis(5)  # Adjust if your controller uses a different axis
            lt = joystick.get_axis(4)  # Left Trigger if you want to use it for something
            
            if rt > DEADZONE:
                if not state.get('rt_pressed', False):
                    mouse.press(Button.left)
                    state['rt_pressed'] = True
            else:
                if state.get('rt_pressed', False):
                    mouse.release(Button.left)
                    state['rt_pressed'] = False
            
            if lt > DEADZONE:
                if not state.get('lt_pressed', False):
                    keyboard.press(Key.space)
                    state['lt_pressed'] = True
            else:
                if state.get('lt_pressed', False):
                    keyboard.release(Key.space)
                    state['lt_pressed'] = False

            # Sleep to prevent high CPU usage
            time.sleep(0.01)
        

    except KeyboardInterrupt:
        print("\nExiting mapper...")
        pygame.quit()

if __name__ == "__main__":
    main()