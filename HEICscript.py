import os
from PIL import Image
from pillow_heif import register_heif_opener

# Enable HEIF support for Pillow
register_heif_opener()

# Define your source directory and where you want the JPGs to go
SOURCE_DIR = r"C:\Users\AlanTUF\Code\EnglishPage\assets\images\gallery"
OUTPUT_DIR = r"C:\Users\AlanTUF\Code\EnglishPage\assets\images\gallery_jpg"

print("Starting batch conversion... This might take a while depending on the dataset size.")
converted_count = 0

# os.walk travels through all subdirectories
for root, dirs, files in os.walk(SOURCE_DIR):
    for filename in files:
        if filename.lower().endswith(".heic"):
            # Get full path to the source HEIC file
            heic_path = os.path.join(root, filename)
            
            # Determine the relative path to maintain folder structure
            relative_path = os.path.relpath(root, SOURCE_DIR)
            target_folder = os.path.normpath(os.path.join(OUTPUT_DIR, relative_path))
            
            # Create the target subfolder if it doesn't exist
            os.makedirs(target_folder, exist_ok=True)
            
            # Construct the output JPG path
            jpg_filename = os.path.splitext(filename)[0] + ".jpg"
            jpg_path = os.path.join(target_folder, jpg_filename)
            
            try:
                # Open, convert, and save the image
                with Image.open(heic_path) as img:
                    # 'with' statement ensures the file pointer is closed immediately after saving
                    img.convert("RGB").save(jpg_path, "JPEG", quality=95)
                
                converted_count += 1
                if converted_count % 50 == 0:
                    print(f"Progress: Converted {converted_count} images...")
                    
            except Exception as e:
                print(f"❌ Failed to convert {heic_path}. Error: {e}")

print(f"\n✅ Done! Total images successfully converted and reorganized: {converted_count}")