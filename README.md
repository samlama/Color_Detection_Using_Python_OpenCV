# Color_Detection_Using_Python_OpenCV
Technical Documentation: Real-Time Color Detection and Image Manipulation Using OpenCV
Objective: 
This project demonstrates live computer vision using Python and OpenCV. It incorporates color detection (red, green, blue) with image processing operations such as grayscale conversion, Gaussian blur, and edge detection. It includes appropriate window and camera closure using the 'q' button or the window close button.
For color detector
1.	A live webcam feed interface that:
2.	Detects red, green, and blue objects using HSV color ranges.
3.	Labels objects detected with bounding rectangles and color names.
4.	The user clicks the 'X' button on the camera window.
5.	Created a Tkinter GUI (optional) with a button for manual termination of the camera thread.

This project uses Python and OpenCV to create a real-time camera feed that detects red, green, and blue colors in the environment. The system uses HSV color space for better accuracy in color detection. Detected objects are highlighted with bounding boxes, and their color is labeled on-screen. he application allows the user to safely close the camera feed either by pressing the ‘q’ key or manually clicking the 'X' close button on the OpenCV window.


#How to run: python color_detector_with_close.py -->in your terminal


