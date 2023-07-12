import cv2

video = cv2.VideoCapture(0) # Capture device

while True:
    ret, frame = video.read()

    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    haarcascade = cv2.CascadeClassifier('/home/haukur/python-projects/opencv/face-tracking/haarcascade_frontalface_default.xml') # Well trained face AI which is available at github.com/opencv/opencv
    face_detection = haarcascade.detectMultiScale(grey, 1.1, 4)

    rectangle_color = (255, 255, 255)
    thickness = 4

    for (x, y, w, h) in face_detection:
        frame = cv2.rectangle(frame, (x, y), (x+w, y+h), rectangle_color, thickness) # Creates rectangle around faces

    cv2.imshow('frame', frame) # Draws the frame

    if cv2.waitKey(1) == ord('q'): # If "Q" is pressed then the program stops
        break

video.release()
cv2.destroyAllWindows()