import time
import sys
import face_recognition
import cv2
from firebase_admin import credentials,initialize_app,firestore
import firebase_admin
import numpy as np
from PyQt5.QtWidgets import  QApplication

import upimg
import gestset
import automate



#### Initializing  FIREBASE ###########
if not firebase_admin._apps:
    cred = credentials.Certificate(r'C:\Users\Aditya\Desktop\Myproject\code\serviceaccountcred.json')
    initialize_app(cred)
db = firestore.client()


#getting custom gestures stored in firebase
def  getgest(uname):
    doc_ref = db.collection(u'Gests').document(uname)
    doc = doc_ref.get()
    tempd=doc.to_dict()
    myl=[]
    myl.append(tempd['Thumbs up'])
    myl.append(tempd['Thumbs Down'])
    myl.append(tempd['Stop'])
    myl.append(tempd['Rock'])
    return myl




########################################    SIGNUP   #############################################################

class Signup():
    def signup(self):
        app = QApplication(sys.argv)
        window = upimg.TakeNamewin()
        window.show()
        app.exec()
        val = window.return_val()
        app.quit()
        newapp = QApplication(sys.argv)
        newwin = upimg.UploadWindow(val)
        newwin.show()
        newapp.exec_()
        newapp.quit()
        gestapp = QApplication(sys.argv)
        gestwin = gestset.SetGesturewindow(val)
        gestwin.show()
        gestapp.exec_()
        gestapp.quit()
        #####get custom gestures
        myl = getgest(val)
        automate.startnewcap(myl)








###############################################  LOGIN    #################################################################
class Login():
    known_fe = []
    known_fn = []

    def changeformat(self,value):
        newl = []
        li = list(value.split(" "))
        li[0] = li[0].replace("[", "")
        li[-1] = li[-1].replace("]", "")

        for i in li:
            if i.strip():
                i = float(i)
                newl.append(i)
        final = np.array(newl)
        return final

    def getencodings(self):
        users_ref = db.collection(u'enc')
        docs = users_ref.stream()
        try:
            for doc in docs:
                self.known_fn.append(doc.id)
                d = doc.to_dict()
                final = self.changeformat(d['value'])
                self. known_fe.append(final)

                # print(f'{doc.id} => {doc.to_dict()}')
        except:
            pass

    def login(self):
        print("here1")

        self.getencodings()
        print('here2')
        if len(self.known_fe) == 0:
            print("no users")
        else:

            video_capture = cv2.VideoCapture(0)

            patience = 0

            gotit = 0

            username = ""

            # Initialize some variables
            face_locations = []
            face_encodings = []
            face_names = []
            process_this_frame = True

            while True:
                # Grab a single frame of video
                ret, frame = video_capture.read()

                # Resize frame of video to 1/4 size for faster face recognition processing
                small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

                # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
                rgb_small_frame = small_frame[:, :, ::-1]

                if process_this_frame:
                    # Find all the faces and face encodings in the current frame of video
                    face_locations = face_recognition.face_locations(rgb_small_frame)

                    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

                    face_names = []
                    for face_encoding in face_encodings:
                        # See if the face is a match for the known face(s)
                        matches = face_recognition.compare_faces(self.known_fe, face_encoding)
                        name = "No Match"
                        # Or instead, use the known face with the smallest distance to the new face

                        face_distances = face_recognition.face_distance(self.known_fe, face_encoding)
                        best_match_index = np.argmin(face_distances)
                        if matches[best_match_index]:
                            name = self.known_fn[best_match_index]

                        face_names.append(name)
                    if len(face_names) == 0:
                        pass
                    else:
                        if face_names[0] == "No Match":
                            patience = patience + 1
                            if (patience == 15):
                                print("did not find a match")
                                break

                        else:
                            username = face_names[0]
                            gotit = 1
                cv2.putText(frame, "press 'r' to sign up", (10, 20), cv2.FONT_HERSHEY_DUPLEX, 1.0, (255, 255, 255), 1)

                process_this_frame = not process_this_frame

                # Display the results
                for (top, right, bottom, left), name in zip(face_locations, face_names):
                    # Scale back up face locations since the frame we detected in was scaled to 1/4 size
                    top *= 4
                    right *= 4
                    bottom *= 4
                    left *= 4

                    # Draw a box around the face
                    cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

                    # Draw a label with a name below the face
                    cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)

                    cv2.putText(frame, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_DUPLEX, 1.0, (255, 255, 255), 1)

                # Display the resulting image
                cv2.imshow('Video', frame)

                if (gotit == 1):
                    time.sleep(1)
                    video_capture.release()
                    cv2.destroyAllWindows()
                    myl = getgest(username)
                    automate.startnewcap(myl)

                key = cv2.waitKey(1)
                if key == ord('q'):
                    break
                elif key == ord('r'):
                    video_capture.release()
                    cv2.destroyAllWindows()
                    obj = Signup()
                    obj.signup()
                    break

            video_capture.release()
            cv2.destroyAllWindows()















################################################### MAIN   #################################################################
loginobj=Login()
loginobj.login()












