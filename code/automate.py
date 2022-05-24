import cv2
import numpy as np
import mediapipe as mp
import tensorflow as tf
import time
import os
import webbrowser
import sel_code




# initialize mediapipe
mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mpDraw = mp.solutions.drawing_utils

# Load the gesture recognizer model
model =  tf.keras.models.load_model(r'C:\Users\Aditya\Desktop\Myproject\mets\mp_hand_gesture')
# Load class names
f = open(r'C:\Users\Aditya\Desktop\Myproject\mets\gesture.names', 'r')
classNames = f.read().split('\n')
f.close()





def change_gest():
    pass

def startnewcap(myl):
    tupval=''
    tdownval=''
    stval=''
    rval=''
    for i in myl:
        if "Chrome" in i:
            indval = myl.index(i)
            if indval == 0:
                tupval="os.startfile(r'C:\Program Files/Google/Chrome/Application/chrome.exe')"
            if indval==1:
                tdownval="os.startfile(r'C:\Program Files/Google/Chrome/Application/chrome.exe')"
            if indval==2:
                stval="os.startfile(r'C:\Program Files/Google/Chrome/Application/chrome.exe')"
            if indval==3:
                rval="os.startfile(r'C:\Program Files/Google/Chrome/Application/chrome.exe')"
        elif "Youtube" in i:
            indval = myl.index(i)
            if indval == 0:
                tupval = "webbrowser.open(r'https://www.youtube.com/')"
            if indval == 1:
                tdownval = "webbrowser.open(r'https://www.youtube.com/')"
            if indval == 2:
                stval = "webbrowser.open(r'https://www.youtube.com/')"
            if indval == 3:
                rval = "webbrowser.open(r'https://www.youtube.com/')"
        elif "Notepad" in i:
            indval = myl.index(i)
            if indval == 0:
                tupval = "os.system('notepad')"
            if indval == 1:
                tdownval = "os.system('notepad')"
            if indval == 2:
                stval = "os.system('notepad')"
            if indval == 3:
                rval = "os.system('notepad')"



        elif "Trending" in i:
            indval = myl.index(i)
            if indval == 0:
                tupval = "sel_code.launchBrowser()"
            if indval == 1:
                tdownval = "sel_code.launchBrowser()"
            if indval == 2:
                stval = "sel_code.launchBrowser()"
            if indval == 3:
                rval = "sel_code.launchBrowser()"


    newcap = cv2.VideoCapture(0)
    while True:
        # Read each frame from the webcam
        _, frame = newcap.read()

        x, y, c = frame.shape

        # Flip the frame vertically
        frame = cv2.flip(frame, 1)
        framergb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Get hand landmark prediction
        result = hands.process(framergb)

        # print(result)

        className = ''

        # post process the result
        if result.multi_hand_landmarks:
            landmarks = []
            for handslms in result.multi_hand_landmarks:
                for lm in handslms.landmark:
                    # print(id, lm)
                    lmx = int(lm.x * x)
                    lmy = int(lm.y * y)

                    landmarks.append([lmx, lmy])

                # Drawing landmarks on frames
                mpDraw.draw_landmarks(frame, handslms, mpHands.HAND_CONNECTIONS)

                # Predict gesture
                prediction = model.predict([landmarks])

                classID = np.argmax(prediction)
                className = classNames[classID]

        # show the prediction on the frame
        cv2.putText(frame, className, (10, 50), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 0, 255), 2, cv2.LINE_AA)

        if className == "thumbs up":
            exec(tupval)
        if className == "stop":
            exec(stval)
        if className== "rock":
            exec(rval)
        if className=="thumbs down":
            exec(tdownval)

        # Show the final output
        cv2.imshow("Output", frame)

        if cv2.waitKey(1) == ord('q'):
            break
        if cv2.waitKey(1) == ord('c'):
            pass
    newcap.release()

    cv2.destroyAllWindows()








