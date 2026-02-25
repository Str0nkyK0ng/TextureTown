import time
import threading
import win32gui
import win32api
import win32con
from inputs import get_gamepad, devices, UnpluggedError
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController

# --- CONFIGURATION ---
MOUSE_SENSITIVITY = 15
DEADZONE = 0.2  # Normalized 0-1 range
STICK_MAX = 32768  # Max value from evdev/inputs
TRIGGER_MAX = 255  # Max trigger value
POLL_RATE = 0.01
# ---------------------


def make_borderless_fullscreen(window_title):
    """Make window borderless fullscreen."""
    hwnd = win32gui.FindWindow(None, window_title)
    if not hwnd:
        print(f"Window '{window_title}' not found!")
        return False

    style = win32gui.GetWindowLong(hwnd, win32con.GWL_STYLE)
    style = style & ~win32con.WS_CAPTION & ~win32con.WS_THICKFRAME
    win32gui.SetWindowLong(hwnd, win32con.GWL_STYLE, style)

    #fullscreen it
    screen_width = win32api.GetSystemMetrics(win32con.SM_CXSCREEN) 
    screen_height = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)

    win32gui.SetWindowPos(
        hwnd,
        win32con.HWND_TOP,
        0, 0, screen_width, screen_height,
        win32con.SWP_FRAMECHANGED | win32con.SWP_SHOWWINDOW,
    )

    print(f"Successfully transformed '{window_title}'")
    return True


def main():
    keyboard = KeyboardController()
    mouse = MouseController()

    # Axis state (normalized -1 to 1 for sticks, 0 to 1 for triggers)
    axes = {
        "ABS_X": 0.0,   # Left stick X
        "ABS_Y": 0.0,   # Left stick Y
        "ABS_RX": 0.0,  # Right stick X
        "ABS_RY": 0.0,  # Right stick Y
        "ABS_Z": 0.0,   # Left trigger
        "ABS_RZ": 0.0,  # Right trigger
    }

    # Key state tracking (so we only press/release on transitions)
    state = {
        "up": False,
        "down": False,
        "left": False,
        "right": False,
        "jump": False,
        "l_click": False,
        "rt_pressed": False,
        "lt_pressed": False,
    }

    # Wait for game to start, then fullscreen it
    time.sleep(5)
    make_borderless_fullscreen("Toontown")

    print("Waiting for controller...")
    while not devices.gamepads:
        time.sleep(1)
    print(f"Controller found: {devices.gamepads[0]}")
    print("Mapping active. Press Ctrl+C to quit.\n")

    # --- Input reading runs in a thread because get_gamepad() blocks ---
    def read_input_loop():
        while True:
            try:
                events = get_gamepad()
                for event in events:
                    if event.ev_type == "Absolute":
                        if event.code in ("ABS_X", "ABS_Y", "ABS_RX", "ABS_RY"):
                            axes[event.code] = event.state / STICK_MAX
                        elif event.code in ("ABS_Z", "ABS_RZ"):
                            axes[event.code] = event.state / TRIGGER_MAX
                    elif event.ev_type == "Key":
                        # Button events: event.state is 1 (pressed) or 0 (released)
                        handle_button(event.code, event.state)
            except UnpluggedError:
                print("Controller disconnected! Waiting for reconnection...")
                while not devices.gamepads:
                    time.sleep(1)
                print("Controller reconnected!")

    def handle_button(code, pressed):
        # BTN_SOUTH = A button (Xbox) -> Jump (Ctrl)
        if code == "BTN_SOUTH":
            if pressed and not state["jump"]:
                keyboard.press(Key.ctrl_l)
                state["jump"] = True
            elif not pressed and state["jump"]:
                keyboard.release(Key.ctrl_l)
                state["jump"] = False

        # BTN_TR = Right bumper -> Left click
        elif code == "BTN_TR":
            if pressed and not state["l_click"]:
                mouse.press(Button.left)
                state["l_click"] = True
            elif not pressed and state["l_click"]:
                mouse.release(Button.left)
                state["l_click"] = False

    # Start input reader thread
    input_thread = threading.Thread(target=read_input_loop, daemon=True)
    input_thread.start()

    # --- Main loop handles continuous actions (sticks, triggers) ---
    try:
        while True:
            # LEFT STICK -> Arrow keys
            lx = axes["ABS_X"]
            ly = axes["ABS_Y"]

            # Up
            if ly > DEADZONE:
                if not state["up"]:
                    keyboard.press(Key.up)
                    state["up"] = True
            else:
                if state["up"]:
                    keyboard.release(Key.up)
                    state["up"] = False

            # Down
            if ly < -DEADZONE:
                if not state["down"]:
                    keyboard.press(Key.down)
                    state["down"] = True
            else:
                if state["down"]:
                    keyboard.release(Key.down)
                    state["down"] = False

            # Left
            if lx < -DEADZONE:
                if not state["left"]:
                    keyboard.press(Key.left)
                    state["left"] = True
            else:
                if state["left"]:
                    keyboard.release(Key.left)
                    state["left"] = False

            # Right
            if lx > DEADZONE:
                if not state["right"]:
                    keyboard.press(Key.right)
                    state["right"] = True
            else:
                if state["right"]:
                    keyboard.release(Key.right)
                    state["right"] = False

            # RIGHT STICK -> Mouse movement
            rx = axes["ABS_RX"]
            ry = axes["ABS_RY"]
            if abs(rx) > DEADZONE or abs(ry) > DEADZONE:
                mouse.move(int(rx * MOUSE_SENSITIVITY), int(-ry * MOUSE_SENSITIVITY))

            # RIGHT TRIGGER -> Left click
            rt = axes["ABS_RZ"]
            if rt > DEADZONE:
                if not state["rt_pressed"]:
                    mouse.press(Button.left)
                    state["rt_pressed"] = True
            else:
                if state["rt_pressed"]:
                    mouse.release(Button.left)
                    state["rt_pressed"] = False

            # LEFT TRIGGER -> Space
            lt = axes["ABS_Z"]
            if lt > DEADZONE:
                if not state["lt_pressed"]:
                    keyboard.press(Key.space)
                    state["lt_pressed"] = True
            else:
                if state["lt_pressed"]:
                    keyboard.release(Key.space)
                    state["lt_pressed"] = False

            time.sleep(POLL_RATE)

    except KeyboardInterrupt:
        print("\nExiting mapper...")


if __name__ == "__main__":
    main()