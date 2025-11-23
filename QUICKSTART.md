# Quick Start Guide

Get your Face Recognition Attendance System running in 5 minutes!

## 🚀 Fast Setup

### 1. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 2. Add Your Face Images

1. Open the `Images_Attendance` folder
2. Add photos with names as filenames:
   - `JOHN_DOE.jpg`
   - `JANE_SMITH.png`
   - `YOUR_NAME.jpeg`

**Tips for best results:**
- Use clear, front-facing photos
- Good lighting
- Minimum 200x200 pixels
- One face per image

### 3. Run the System

```bash
python AttendanceProject.py
```

**First run**: Takes 5-10 seconds (generating encodings)  
**Next runs**: Instant startup (uses cache)

### 4. Use the System

- Stand in front of camera
- System detects and shows your name
- Attendance automatically marked
- Press **Enter** to exit

### 5. Check Attendance

Open `Attendance.csv` to see records:
```
Name,Time,Date
HASNAIN HAIDER,14:30:45,23/11/2025
```

## 🎯 That's It!

Your attendance system is now running!

## 📚 Next Steps

- Read [README.md](README.md) for full documentation
- Check [TECHNICAL_DOCUMENTATION.md](TECHNICAL_DOCUMENTATION.md) for details
- Follow [GITHUB_SETUP_GUIDE.md](GITHUB_SETUP_GUIDE.md) to upload to GitHub

## ❓ Quick Troubleshooting

**Camera not working?**
```python
# In AttendanceProject.py, change:
cap = cv2.VideoCapture(0)  # Try 1 or 2
```

**Not recognizing faces?**
- Ensure good lighting
- Face the camera directly
- Check if your image is in Images_Attendance folder

**System slow?**
- Already optimized! Running at 25-30 FPS
- If still slow, increase frame skip in code

## 🆘 Need Help?

Email: hhnain1006@gmail.com

---

**Enjoy your automated attendance system! 🎉**
