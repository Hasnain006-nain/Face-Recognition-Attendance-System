# Full Project Code Mail : vatshayan007@gmail.com
# If you get error then Mail : vatshayan007@gmail.com
import cv2
import numpy as np
import face_recognition

# Load HASNAIN HAIDER image
imgHasnain = face_recognition.load_image_file('Images_Attendance/HASNAIN HAIDER.jpeg')
imgHasnain = cv2.cvtColor(imgHasnain, cv2.COLOR_BGR2RGB)

# Load ELIAS image for comparison
imgElias = face_recognition.load_image_file('Images_Attendance/ELIAS.jpeg')
imgElias = cv2.cvtColor(imgElias, cv2.COLOR_BGR2RGB)

# Detect and encode HASNAIN HAIDER's face
facelocHasnain = face_recognition.face_locations(imgHasnain)[0]
encodeHasnain = face_recognition.face_encodings(imgHasnain)[0]
cv2.rectangle(imgHasnain, (facelocHasnain[3], facelocHasnain[0]), (facelocHasnain[1], facelocHasnain[2]), (0, 255, 0), 2)
cv2.putText(imgHasnain, 'HASNAIN HAIDER', (facelocHasnain[3], facelocHasnain[0]-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

# Detect and encode ELIAS's face
facelocElias = face_recognition.face_locations(imgElias)[0]
encodeElias = face_recognition.face_encodings(imgElias)[0]
cv2.rectangle(imgElias, (facelocElias[3], facelocElias[0]), (facelocElias[1], facelocElias[2]), (0, 255, 0), 2)

# Compare the two faces
results = face_recognition.compare_faces([encodeHasnain], encodeElias)
faceDis = face_recognition.face_distance([encodeHasnain], encodeElias)
print(f"Match: {results[0]}, Distance: {round(faceDis[0], 2)}")

# Display result on ELIAS image
match_text = "MATCH" if results[0] else "NO MATCH"
color = (0, 255, 0) if results[0] else (0, 0, 255)
cv2.putText(imgElias, f'ELIAS - {match_text}', (facelocElias[3], facelocElias[0]-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)
cv2.putText(imgElias, f'Distance: {round(faceDis[0],2)}', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

cv2.imshow('HASNAIN HAIDER', imgHasnain)
cv2.imshow('ELIAS (Comparison)', imgElias)
cv2.waitKey(0)
cv2.destroyAllWindows()
