import pyautogui

def take_screenshot(output_file):
    screenshot = pyautogui.screenshot()

    screenshot.save(output_file)

    print(f"Screenshot Saved as {output_file}")

output_file = input("Enter File Output Name + (.png , .jpg): ")
take_screenshot(output_file)
