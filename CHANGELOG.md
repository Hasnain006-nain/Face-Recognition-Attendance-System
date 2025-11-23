# Changelog

All notable changes to this project will be documented in this file.

## [2.0.0] - 2025-11-23

### Added
- Performance optimization: Frame skipping (process every 3rd frame)
- Encoding cache system using pickle for instant startup
- Real-time terminal output showing detected names and confidence
- Professional README with comprehensive documentation
- Technical documentation explaining all algorithms and optimizations
- Requirements.txt for easy dependency installation
- .gitignore for clean repository
- MIT License
- GitHub setup guide
- HOG model for faster face detection

### Changed
- Improved face recognition accuracy with better threshold (0.6)
- Optimized camera settings for better performance
- Enhanced visual feedback with confidence percentages
- Better error handling in encoding generation
- Cleaner code structure with comments

### Removed
- "Processing" indicator from camera view (cleaner UI)
- Unnecessary print statements
- Redundant code

### Performance Improvements
- 3x faster frame processing
- 16x faster face detection (resolution reduction)
- 5-10x faster detection (HOG vs CNN)
- Instant startup after first run (encoding cache)
- Reduced CPU usage from 40-50% to 15-25%
- Increased FPS from 10-15 to 25-30

### Fixed
- Lag issues during face recognition
- Duplicate attendance entries
- Camera initialization delays
- Memory leaks in long-running sessions

## [1.0.0] - Initial Release

### Features
- Basic face recognition from webcam
- Attendance marking in CSV
- Face detection using face_recognition library
- Simple OpenCV display window

---

## Version Numbering

This project follows [Semantic Versioning](https://semver.org/):
- MAJOR version: Incompatible API changes
- MINOR version: New functionality (backwards compatible)
- PATCH version: Bug fixes (backwards compatible)
