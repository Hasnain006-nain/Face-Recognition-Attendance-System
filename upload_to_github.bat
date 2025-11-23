@echo off
echo ========================================
echo   GitHub Upload Helper
echo   For: Hasnain Haider (Hasnain006-nain)
echo ========================================
echo.

echo Checking if Git is installed...
git --version >nul 2>&1
if %errorlevel% neq 0 (
    echo.
    echo [ERROR] Git is not installed!
    echo.
    echo Please install Git first:
    echo 1. Go to: https://git-scm.com/download/win
    echo 2. Download and install
    echo 3. Restart this script
    echo.
    echo OR use GitHub Desktop (easier):
    echo https://desktop.github.com/
    echo.
    pause
    exit /b
)

echo Git is installed!
echo.

echo Step 1: Initializing Git repository...
git init
if %errorlevel% neq 0 (
    echo [ERROR] Failed to initialize repository
    pause
    exit /b
)

echo Step 2: Adding all files...
git add .
if %errorlevel% neq 0 (
    echo [ERROR] Failed to add files
    pause
    exit /b
)

echo Step 3: Creating initial commit...
git commit -m "Initial commit: Professional Face Recognition Attendance System with optimizations"
if %errorlevel% neq 0 (
    echo [ERROR] Failed to commit
    pause
    exit /b
)

echo.
echo ========================================
echo   IMPORTANT: Next Steps
echo ========================================
echo.
echo 1. Go to: https://github.com/Hasnain006-nain
echo 2. Click the '+' icon (top right)
echo 3. Click 'New repository'
echo 4. Name: Face-Recognition-Attendance-System
echo 5. Description: Real-time face recognition attendance system
echo 6. Choose 'Public'
echo 7. DO NOT check 'Initialize with README'
echo 8. Click 'Create repository'
echo.
echo After creating the repository, press any key to continue...
pause >nul

echo.
echo Step 4: Connecting to GitHub...
git remote add origin https://github.com/Hasnain006-nain/Face-Recognition-Attendance-System.git
git branch -M main

echo.
echo Step 5: Pushing to GitHub...
echo.
echo You will be asked for credentials:
echo Username: Hasnain006-nain
echo Password: Use your Personal Access Token (NOT your GitHub password)
echo.
echo To create a token:
echo 1. Go to: https://github.com/settings/tokens
echo 2. Click 'Generate new token (classic)'
echo 3. Check 'repo' permissions
echo 4. Copy the token and use it as password
echo.
pause

git push -u origin main

if %errorlevel% equ 0 (
    echo.
    echo ========================================
    echo   SUCCESS! 🎉
    echo ========================================
    echo.
    echo Your project is now on GitHub!
    echo.
    echo View it at:
    echo https://github.com/Hasnain006-nain/Face-Recognition-Attendance-System
    echo.
    echo Share it on LinkedIn, Twitter, and your resume!
    echo.
) else (
    echo.
    echo [ERROR] Failed to push to GitHub
    echo.
    echo Common issues:
    echo 1. Repository not created on GitHub yet
    echo 2. Wrong credentials
    echo 3. Network issues
    echo.
    echo Try using GitHub Desktop instead:
    echo https://desktop.github.com/
    echo.
)

pause
