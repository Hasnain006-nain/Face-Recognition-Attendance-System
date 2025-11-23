# Face Recognition Attendance System - User Guide

## 📋 Overview
This system automatically marks attendance by recognizing faces through your webcam. When a face is detected and matches someone in the database, their attendance is recorded with timestamp.

## 🚀 How to Run the Program

### Method 1: Using Batch File (Easiest)
1. Double-click `run.bat` in the project folder
2. Wait for the webcam window to open

### Method 2: Using Command Line
1. Open Command Prompt or PowerShell
2. Navigate to the project folder
3. Run: `python AttendanceProject.py`

## 📸 Adding People to the System

1. Take a clear photo of the person's face
2. Save the image with the person's name (e.g., `JOHN DOE.jpg` or `SARAH.png`)
3. Place the image in the `Images_Attendance` folder
4. The filename (without extension) will be used as the person's name in attendance

**Image Requirements:**
- Clear, front-facing photo
- Good lighting
- Face clearly visible
- Supported formats: .jpg, .jpeg, .png

## 🎥 Using the Webcam

Once the program starts:
1. A window titled "webcam" will open showing live video
2. The system will automatically detect and recognize faces
3. When a face is recognized:
   - A green rectangle appears around the face
   - The person's name is displayed
   - Attendance is recorded automatically

## 🛑 How to Close the Program

**Three ways to stop:**
1. Press **Enter** key (recommended)
2. Click the **X** button on the webcam window
3. Press **Ctrl+C** in the command window

## 📊 Viewing Attendance Records

Open `Attendance.csv` to see all recorded attendance:
- **Name**: Person's name (from image filename)
- **Time**: Time when attendance was marked (HH:MM:SS)
- **Date**: Date of attendance (DD/MM/YYYY)

**Note:** Each person is recorded only once per session to prevent duplicates.

## 🔧 How the System Works

### Step 1: Loading Phase
```
['ALI HAIDER.jpeg', 'ELIAS.jpeg', 'HASNAIN HAIDER.jpeg', 'MOWLID.png', 'SAJID.jpeg']
['ALI HAIDER', 'ELIAS', 'HASNAIN HAIDER', 'MOWLID', 'SAJID']
```
- Loads all images from `Images_Attendance` folder
- Extracts names from filenames

### Step 2: Encoding Phase
```
Successfully encoded ALI HAIDER
Successfully encoded ELIAS
Successfully encoded HASNAIN HAIDER
Successfully encoded MOWLID
Successfully encoded SAJID
Encoding Complete
```
- Creates facial encodings (mathematical representations) for each face
- This allows fast recognition during live detection

### Step 3: Recognition Phase
- Webcam captures live video
- Detects faces in each frame
- Compares detected faces with stored encodings
- Marks attendance when match is found

## 📁 Project Structure

```
Face-recognition-Attendance-System-Project-main/
│
├── AttendanceProject.py      # Main program file
├── main.py                    # Test/demo file
├── run.bat                    # Quick launch script
├── Attendance.csv             # Attendance records
├── Images_Attendance/         # Folder for face images
│   ├── ALI HAIDER.jpeg
│   ├── ELIAS.jpeg
│   ├── HASNAIN HAIDER.jpeg
│   ├── MOWLID.png
│   └── SAJID.jpeg
└── README.md                  # Project information
```

## ⚙️ Technical Details

**Libraries Used:**
- `opencv-python` (cv2): Webcam capture and image processing
- `face-recognition`: Face detection and recognition
- `numpy`: Numerical operations
- `dlib`: Machine learning backend for face recognition

**System Requirements:**
- Python 3.12
- Webcam
- Windows OS
- Minimum 4GB RAM

## 🐛 Troubleshooting

### Webcam not opening?
- Check if another application is using the webcam
- Ensure webcam permissions are granted
- Try restarting the program

### Face not recognized?
- Ensure good lighting
- Face the camera directly
- Make sure the training image is clear
- Try adding multiple images of the same person

### "No module named cv2" error?
- Run: `pip install opencv-python numpy face-recognition`
- Or use the provided `run.bat` file

### Program runs but no faces detected?
- Check if faces are clearly visible
- Ensure adequate lighting
- Move closer to the camera

## 💡 Tips for Best Results

1. **Good Training Images:**
   - Use high-quality, well-lit photos
   - Face should be clearly visible
   - Avoid sunglasses or face coverings

2. **During Recognition:**
   - Face the camera directly
   - Ensure good lighting
   - Stay still for 1-2 seconds
   - Be within 1-2 meters of the camera

3. **Performance:**
   - Close other applications using the webcam
   - Ensure good internet connection (if using cloud features)
   - Keep the Images_Attendance folder organized

## 📞 Support

If you encounter issues:
- Check the console output for error messages
- Verify all images are in the correct folder
- Ensure all libraries are installed correctly
- Contact: vatshayan007@gmail.com

## 🎯 Quick Start Checklist

- [ ] Install required libraries
- [ ] Add face images to `Images_Attendance` folder
- [ ] Run `run.bat` or `python AttendanceProject.py`
- [ ] Wait for "Encoding Complete" message
- [ ] Webcam window opens automatically
- [ ] Show face to camera
- [ ] Check `Attendance.csv` for records
- [ ] Press Enter to close

---

**Version:** 1.0  
**Last Updated:** November 2025  
**Author:** Face Recognition Attendance System Team
