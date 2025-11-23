# GitHub Setup Guide

## Step 1: Install Git

### For Windows:
1. Download Git from: https://git-scm.com/download/win
2. Run the installer
3. Use default settings
4. Restart your terminal/command prompt

### Verify Installation:
```bash
git --version
```

## Step 2: Configure Git

Open terminal and run:

```bash
git config --global user.name "Your Name"
git config --global user.email "hhnain1006@gmail.com"
```

## Step 3: Initialize Git Repository

Navigate to your project folder and run:

```bash
cd Face-recognition-Attendance-System-Project-main
git init
```

## Step 4: Add Files to Git

```bash
git add .
git commit -m "Initial commit: Face Recognition Attendance System with optimizations"
```

## Step 5: Create GitHub Repository

1. Go to https://github.com
2. Click the "+" icon (top right) → "New repository"
3. Repository name: `Face-Recognition-Attendance-System`
4. Description: `Real-time face recognition attendance system with Python, OpenCV, and face_recognition`
5. Choose "Public" (to share) or "Private"
6. **DO NOT** initialize with README (we already have one)
7. Click "Create repository"

## Step 6: Connect Local Repository to GitHub

GitHub will show you commands. Use these:

```bash
git remote add origin https://github.com/Hasnain006-nain/Face-Recognition-Attendance-System.git
git branch -M main
git push -u origin main
```

## Step 7: Verify Upload

1. Go to your GitHub repository URL
2. You should see all files uploaded
3. README.md will be displayed on the main page

## Alternative: Using GitHub Desktop

If you prefer a GUI:

1. Download GitHub Desktop: https://desktop.github.com/
2. Install and sign in with your GitHub account
3. Click "Add" → "Add Existing Repository"
4. Select your project folder
5. Click "Publish repository"
6. Choose public/private and click "Publish"

## Updating Your Repository Later

When you make changes:

```bash
git add .
git commit -m "Description of changes"
git push
```

## Common Issues

### Issue: "Permission denied"
**Solution**: Set up SSH key or use personal access token
- Go to GitHub Settings → Developer settings → Personal access tokens
- Generate new token with "repo" permissions
- Use token as password when pushing

### Issue: "Repository not found"
**Solution**: Check the remote URL
```bash
git remote -v
git remote set-url origin https://github.com/YOUR_USERNAME/REPO_NAME.git
```

### Issue: "Failed to push"
**Solution**: Pull first, then push
```bash
git pull origin main --allow-unrelated-histories
git push origin main
```

## Your Repository Structure

After upload, your GitHub repo will have:

```
Face-Recognition-Attendance-System/
├── README.md                      ⭐ Main documentation
├── TECHNICAL_DOCUMENTATION.md     📚 Technical details
├── HOW_TO_USE.md                  📖 Usage guide
├── PROGRAM_FLOW.md                🔄 Flow diagram
├── LICENSE                        ⚖️ MIT License
├── requirements.txt               📦 Dependencies
├── .gitignore                     🚫 Ignored files
├── AttendanceProject.py           🎯 Main system
├── main.py                        🧪 Demo script
├── run.bat                        ▶️ Windows launcher
└── Images_Attendance/             📁 Training images
```

## Making Your Repository Stand Out

### 1. Add Topics
On GitHub, click "⚙️ Settings" → Add topics:
- `face-recognition`
- `opencv`
- `python`
- `attendance-system`
- `computer-vision`
- `machine-learning`

### 2. Add Description
Edit repository description:
> Real-time face recognition attendance system using Python, OpenCV, and face_recognition. Features optimized performance, automatic attendance marking, and CSV export.

### 3. Add Website
Link to your portfolio or demo video

### 4. Enable Issues
Allow others to report bugs and suggest features

### 5. Add Screenshots
Create a `screenshots` folder and add demo images to README

## Sharing Your Project

Share your repository URL:
```
https://github.com/Hasnain006-nain/Face-Recognition-Attendance-System
```

On LinkedIn, Twitter, or your portfolio!

---

**Need Help?**
- GitHub Docs: https://docs.github.com
- Git Tutorial: https://git-scm.com/docs/gittutorial
- Contact: hhnain1006@gmail.com
