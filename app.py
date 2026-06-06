import os
import time  # New library to handle pauses

target_folder = "../TestDesktop"

print("🚀 File Sorter Daemon is running in the background...")
print("Drop any file into TestDesktop to see it work. Press Ctrl+C to stop.")

# This creates an infinite loop. The script will run forever until you kill it.
while True:
    if os.path.exists(target_folder):
        all_files = os.listdir(target_folder)
        
        for item in all_files:
            # Skip folders so we don't loop infinitely inside them
            if os.path.isdir(os.path.join(target_folder, item)):
                continue
                
            # --- Your exact sorting logic from yesterday goes here ---
            ends = item.split('.')[-1].lower() 
            source_path = os.path.join(target_folder, item)
            
            if ends == "txt":
                dest_folder = os.path.join(target_folder, "TextFiles")
            elif ends == "pdf":
                dest_folder = os.path.join(target_folder, "PDFFiles")
            elif ends == "png":
                dest_folder = os.path.join(target_folder, "ImageFiles")
            else:
                dest_folder = os.path.join(target_folder, "Others")
                
            if not os.path.exists(dest_folder):
                os.makedirs(dest_folder)
                
            destination_path = os.path.join(dest_folder, item)
            os.rename(source_path, destination_path)
            print(f"⚡ Automatically sorted: {item}")
            with open("log.txt","a") as file:
                if ends == "txt":
                    file.write(f"{item} item.txt moved to TextFiles\n")
                elif ends == "pdf":
                    file.write(f"{item} item.pdf moved to PDFFiles\n")
                elif ends == "png":
                    file.write(f"{item} item.png moved to imagefiles\n")
                else:
                    file.write(f"{item} item.moved to Others\n")
    
    # CRUCIAL STEP: Tell Python to sleep for 5 seconds before checking again.
    # Without this line, your CPU will run at 100% capacity and crash your computer!
    time.sleep(5)