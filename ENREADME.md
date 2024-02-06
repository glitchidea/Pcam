This Python project enables you to remotely use your camera by connecting your Android device wirelessly or via USB using the Android Debug Bridge (ADB) tool. The project allows capturing video either from your phone's camera or your computer's camera.


  

Installation Steps:

----

  

Python Installation:

1. ADB Installation:
- To connect your Android device to your computer using the Android Debug Bridge (ADB), ADB must be installed on your computer first.
- You can obtain ADB from a source such as Android Studio or SDK Platform Tools.
- Specify the correct path to the adb.exe file among the downloaded files in the adb_path variable.


2. Installation of Required Libraries:
- To install the necessary Python libraries, type the following command in the terminal or command prompt: ``` pip install opencv-python numpy```

3. Connecting Your Phone:
- After running the program to connect your phone wirelessly or via USB, make the necessary selections.
- For wireless connection, specify the phone's IP address (such as 192.168.0.11) and port number.
- For USB connection, enable USB debugging mode on your phone and connect it to your computer via a USB cable.

4. Using the Camera:
- The program provides the option to use either the phone's camera or your computer's camera.
- Make your selection and wait for the program to request permission to use the camera.

5. Using the Microphone:
- The program provides the option to use either the phone's microphone or your computer's microphone.
- Make your selection and wait for the program to request permission to use the microphone.

6. Closing the Program:
- The program will capture video using the selected devices and terminate.
- Press any key to close the program.
By following these steps, you can easily use this project to remotely control your phone's camera.

  
  
  

How to Install and Connect ADB?

----

  

ADB Installation:


  

1. Download the appropriate ZIP file for your operating system from the SDK Platform Tools page..

2. Extract the ZIP file into a folder.

3. Determine the path of the adb.exe file in the folder.

Connecting the Phone:
- A. Wireless Connection:
	- Enable 'Developer Options' on your phone from its settings.
	- Turn on 'USB Debugging' and enable 'ADB over network' in the 'Developer options'.
	- On your computer, type the following command in the terminal or command prompt to connect your phone:```adb connect 192.168.0.1:5555```  # Specify the IP address and port number of the phone

  

 - USB Connection:
	- Enable 'Developer Options' on your phone from its settings.
	- Turn on 'USB Debugging' and connect your phone to your computer using a USB cable.
	- On your computer, type the following command in the terminal or command prompt to connect your phone: ```adb devices```
	- If you have successfully connected, you can now run your Python program and remotely control the camera of your Android device.
