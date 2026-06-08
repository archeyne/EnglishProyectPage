import os

# Your specific directory path
TARGET_DIR = r"C:\Users\AlanTUF\Code\EnglishPage\assets\images\gallery"

print("Starting the renaming process...")

try:
    # 1. Get all files in the directory
    all_files = os.listdir(TARGET_DIR)
    
    # 2. Filter for just JPG/JPEG images and sort them 
    # Sorting ensures they are numbered in a predictable order (alphabetical/numerical)
    image_files = [f for f in all_files if f.lower().endswith(('.jpg', '.jpeg'))]
    image_files.sort()
    
    total_images = len(image_files)
    print(f"Found {total_images} JPG images to rename.")

    # 3. Iterate and rename with a sequential counter
    for index, filename in enumerate(image_files, start=1):
        old_path = os.path.join(TARGET_DIR, filename)
        
        # Get the file extension (safeguard to keep .jpg or .jpeg exactly as it was)
        file_ext = os.path.splitext(filename)[1]
        
        # Construct the new name: gallery1.jpg, gallery2.jpg...
        new_filename = f"gallery{index}{file_ext}"
        new_path = os.path.join(TARGET_DIR, new_filename)
        
        # Rename the file
        os.rename(old_path, new_path)
        
    print(f"\n✅ Success! All {total_images} images have been renamed to gallery1, gallery2, etc.")

except Exception as e:
    print(f"❌ An error occurred: {e}")