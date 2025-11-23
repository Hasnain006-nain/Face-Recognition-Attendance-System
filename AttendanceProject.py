# Full Project Code Mail : vatshayan007@gmail.com
# If you get error then Mail : vatshayan007@gmail.com

import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
import pickle

path = 'Images_Attendance'
images = []
classNames = []
myList = os.listdir(path)
print(myList)
for cl in myList:
    # Use face_recognition's image loader instead of cv2
    curImg = face_recognition.load_image_file(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
print(classNames)

def findEncodings(images):
    encodeList =[]
    for i, img in enumerate(images):
        try:
            # Images are already in RGB format from face_recognition.load_image_file
            encodings = face_recognition.face_encodings(img)
            if len(encodings) > 0:
                encode = encodings[0]
                encodeList.append(encode)
                print(f"Successfully encoded {classNames[i]}")
            else:
                print(f"Warning: No face found in image {classNames[i]}")
        except Exception as e:
            print(f"Error processing {classNames[i]}: {e}")
    return encodeList

def markAttendance(name):
    with open('Attendance.csv', 'r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            time_now = datetime.now()
            tString = time_now.strftime('%H:%M:%S')
            dString = time_now.strftime('%d/%m/%Y')
            f.writelines(f'\n{name},{tString},{dString}')

# Try to load cached encodings, otherwise compute them
encoding_file = 'face_encodings.pkl'
if os.path.exists(encoding_file):
    print('Loading cached encodings...')
    with open(encoding_file, 'rb') as f:
        encodeListKnown = pickle.load(f)
    print('Encodings loaded from cache')
else:
    print('Computing encodings...')
    encodeListKnown = findEncodings(images)
    # Save encodings for faster startup next time
    with open(encoding_file, 'wb') as f:
        pickle.dump(encodeListKnown, f)
    print('Encoding Complete and cached')

cap = cv2.VideoCapture(0)
# Optimize camera settings for performance
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_FPS, 30)
cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)  # Reduce buffer to get latest frame

# Performance optimization variables
process_this_frame = True
frame_count = 0
face_locations = []
face_names = []
face_confidences = []

print("Starting camera... Press Enter to exit")

while True:
    success, img = cap.read()
    if not success:
        print("Failed to grab frame")
        break
    
    frame_count += 1
    
    # Process every 3rd frame for better performance
    if frame_count % 3 == 0:
        process_this_frame = True
    else:
        process_this_frame = False
    
    if process_this_frame:
        # Resize to 1/4 size for faster face recognition processing
        imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

        # Find faces using faster HOG model
        face_locations = face_recognition.face_locations(imgS, model='hog')
        
        if len(face_locations) > 0:
            encodesCurFrame = face_recognition.face_encodings(imgS, face_locations)
            
            face_names = []
            face_confidences = []
            
            for encodeFace in encodesCurFrame:
                # Compare with known faces
                faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
                matchIndex = np.argmin(faceDis)
                
                if faceDis[matchIndex] < 0.6:
                    name = classNames[matchIndex].upper()
                    confidence = round((1 - faceDis[matchIndex]) * 100, 2)
                    face_names.append(name)
                    face_confidences.append(confidence)
                    # Print to terminal when face detected
                    print(f"Detected: {name} (Confidence: {confidence}%)")
                    markAttendance(name)
                else:
                    face_names.append("Unknown")
                    face_confidences.append(0)
                    print("Unknown face detected")
        else:
            face_names = []
            face_confidences = []
    
    # Draw results on every frame (even when not processing)
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4
        
        # Draw box and label
        if name != "Unknown":
            color = (0, 255, 0)
            idx = face_names.index(name)
            confidence = face_confidences[idx] if idx < len(face_confidences) else 0
            label = f"{name} {confidence}%"
        else:
            color = (0, 0, 255)
            label = "Unknown"
        
        cv2.rectangle(img, (left, top), (right, bottom), color, 2)
        cv2.rectangle(img, (left, bottom - 35), (right, bottom), color, cv2.FILLED)
        cv2.putText(img, label, (left + 6, bottom - 6), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)
    
    cv2.imshow('Face Recognition Attendance', img)
    
    # Exit on Enter key
    if cv2.waitKey(1) == 13:
        break

cap.release()
cv2.destroyAllWindows()


