import cv2
import numpy as np
import subprocess
import time
import os

adb_path = r"c:\Users\platform-tools_r34.0.5-windows\platform-tools\adb.exe"  # Directory where ADB is located
os.environ["PATH"] += os.pathsep + os.path.dirname(adb_path)

def capture_webcam(device_id, width, height, fps):
    command = ["adb", "shell", "am", "start", "-a", "android.media.action.STILL_IMAGE_CAMERA"]
    subprocess.run(command)

    time.sleep(2)  # Wait for the camera app to open

    command = ["adb", "shell", "input", "keyevent", "27"]  # Press the camera button
    subprocess.run(command)

    # Capture frames directly from the phone's camera
    cap = cv2.VideoCapture(f"adb shell 'exec:/system/bin/screencap -p'")

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    cap.set(cv2.CAP_PROP_FPS, fps)

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow('Webcam', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    
def connect_phone_wifi():
    print("Connecting to phone via WİFİ...")
    result = subprocess.run(["adb", "connect", "192.168.0.11:5555"], capture_output=True, text=True, check=True) # IP address of the phone
    print("Connected to phone.")
    print(result.returncode)
    print(result.stdout)
    print(result.stderr)


def connect_phone_usb():
    print("Connecting to phone via USB...")
    result = subprocess.run(["adb", "connect", "192.168.0.11:5555"], capture_output=True, text=True, check=True) # IP address of the phone
    print("Connected to phone.")
    print(result.returncode)
    print(result.stdout)
    print(result.stderr)


def main():
    print("Choose connection method:")
    print("1. WİFİ")
    print("2. USB")
    choice = input("Enter the number of your choice: ")

    if choice == "1":
        connect_phone_wifi()
    elif choice == "2":
        connect_phone_usb()
    else:
        print("Invalid choice.")
        return

    print("Choose camera usage:")
    print("1. Use phone's camera")
    print("2. Use PC's camera")
    choice = input("Enter the number of your choice: ")

    if choice == "1":
        print("Using phone's camera.")
        capture_webcam(0, 640, 480, 30)
    elif choice == "2":
        print("Using PC's camera.")
        capture_webcam(0, 640, 480, 30)
    else:
        print("Invalid choice.")

    print("Choose microphone usage:")
    print("1. Use phone's microphone")
    print("2. Use PC's microphone")
    choice = input("Enter the number of your choice: ")

    if choice == "1":
        print("Using phone's microphone.")
    elif choice == "2":
        print("Using PC's microphone.")
    else:
        print("Invalid choice.")
    input("Press Enter to exit the program.")

if __name__ == "__main__":
    main()


    
