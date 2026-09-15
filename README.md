# Computer Automation with Gesture Recognition

Control a Windows desktop with hand gestures in front of a webcam. Sign in by face, bind
gestures to actions, then raise a hand to launch an application.

Published as *Computer Automation using Gesture Recognition and MediaPipe* in IJRASET —
[paper](https://www.ijraset.com/best-journal/computer-automation-using-gesture-recognition-and-mediapipe).

## How it works

`main.py` encodes any face on the webcam with `face_recognition` and matches it against
encodings in Firebase Firestore; a match loads that user's gesture bindings, and pressing
`r` starts registration instead. `automate.py` then runs MediaPipe Hands on the feed and
classifies the 21 returned landmarks with a pretrained Keras model.

Ten gestures are recognised. Four of them — thumbs up, thumbs down, stop, rock — can be
bound to an action: open Notepad, Chrome, YouTube, or a bookmarked link.

## Running it

Windows only. `face_recognition` needs dlib, which wants CMake and a C++ toolchain first.

```bash
pip install opencv-python mediapipe tensorflow face_recognition firebase-admin PyQt5 numpy
cd code
python main.py
```

Requires a Firebase project with Firestore, using two collections: `enc` for face
encodings and `Gests` for bindings. Save the service account key as
`code/serviceaccountcred.json` or point `FIREBASE_CREDENTIALS` at it. The bookmark action
opens `BOOKMARK_URL`. Press `q` to quit.

## Notes

A 2022 undergraduate project, kept as a record of the published work. Two things to know
before reusing it: face encodings are stored in Firestore as plain stringified arrays,
which is not how biometric data should be handled in a real deployment; and `automate.py`
dispatches actions by calling `exec` on fixed strings, where a dictionary of functions
would be the right shape.
