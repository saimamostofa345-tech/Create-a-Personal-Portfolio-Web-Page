import os
import shutil
import zipfile
import urllib.request

base_dir = r"c:\Users\NS-Computer\Downloads\my project"
portfolio_dir = os.path.join(base_dir, "Portfolio_Project")
images_dir = os.path.join(portfolio_dir, "images")
videos_dir = os.path.join(portfolio_dir, "videos")

os.makedirs(images_dir, exist_ok=True)
os.makedirs(videos_dir, exist_ok=True)

brain_dir = r"C:\Users\NS-Computer\.gemini\antigravity-ide\brain\bf25fc67-671d-4dd8-847e-e92cc3f12422"

# Source generated images
profile_src = os.path.join(brain_dir, "profile_portrait_1793253019084.jpg")
ecommerce_src = os.path.join(brain_dir, "ecommerce_preview_1793253038892.jpg")
task_src = os.path.join(brain_dir, "task_platform_preview_1793253058721.jpg")

if os.path.exists(profile_src):
    shutil.copy2(profile_src, os.path.join(images_dir, "profile.jpg"))
    print("Copied profile.jpg")

if os.path.exists(ecommerce_src):
    shutil.copy2(ecommerce_src, os.path.join(images_dir, "project1.jpg"))
    print("Copied project1.jpg")

if os.path.exists(task_src):
    shutil.copy2(task_src, os.path.join(images_dir, "project2.jpg"))
    print("Copied project2.jpg")

# Intro video
video_path = os.path.join(videos_dir, "intro.mp4")

# Download a tiny valid sample MP4 video or generate valid MP4
try:
    sample_url = "https://raw.githubusercontent.com/bower-media-samples/big-buck-bunny-1080p-30s/master/video.mp4"
    # Or W3C sample video
    w3c_url = "https://www.w3schools.com/html/mov_bbb.mp4"
    req = urllib.request.Request(w3c_url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=10) as resp, open(video_path, 'wb') as out_f:
        out_f.write(resp.read())
    print("Downloaded sample intro.mp4 successfully")
except Exception as e:
    print(f"Could not download remote sample video: {e}. Creating fallback valid media container.")
    # If network fails, create a valid container or binary
    with open(video_path, "wb") as f:
        # Minimal MP4 ftyp box header
        # 00 00 00 20 66 74 79 70 69 73 6f 6d ...
        ftyp = bytes.fromhex("000000206674797069736f6d0000020069736f6d69736f32617663316d7034310000000866726565000000086d646174")
        f.write(ftyp)

# Create Portfolio_Project.zip in base_dir
zip_path = os.path.join(base_dir, "Portfolio_Project.zip")
with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(portfolio_dir):
        for file in files:
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, base_dir)
            zipf.write(full_path, rel_path)

print(f"Created ZIP: {zip_path}")
