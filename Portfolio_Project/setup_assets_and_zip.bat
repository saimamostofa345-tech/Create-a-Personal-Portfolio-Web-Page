@echo off
title Portfolio Project Asset Setup & Zip Creator
echo ============================================================
echo   Setting up Portfolio_Project Assets and Creating ZIP
echo ============================================================
echo.

if not exist "images" mkdir images
if not exist "videos" mkdir videos

echo [1/3] Copying high-resolution generated profile & project preview images...
copy /Y "C:\Users\NS-Computer\.gemini\antigravity-ide\brain\bf25fc67-671d-4dd8-847e-e92cc3f12422\profile_portrait_*.jpg" "images\profile.jpg" >nul
copy /Y "C:\Users\NS-Computer\.gemini\antigravity-ide\brain\bf25fc67-671d-4dd8-847e-e92cc3f12422\ecommerce_preview_*.jpg" "images\project1.jpg" >nul
copy /Y "C:\Users\NS-Computer\.gemini\antigravity-ide\brain\bf25fc67-671d-4dd8-847e-e92cc3f12422\task_platform_preview_*.jpg" "images\project2.jpg" >nul

echo [2/3] Setting up intro.mp4 video file...
python build_assets.py

echo [3/3] Compressing into Portfolio_Project.zip...
powershell -Command "Compress-Archive -Path 'index.html', 'style.css', 'images', 'videos' -DestinationPath '..\Portfolio_Project.zip' -Force"

echo.
echo ============================================================
echo   SUCCESS!
echo   1. Images copied to images/
echo   2. Videos setup in videos/
echo   3. Portfolio_Project.zip created at:
echo      c:\Users\NS-Computer\Downloads\my project\Portfolio_Project.zip
echo ============================================================
pause
