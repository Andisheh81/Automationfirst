import os

# 1. SETTINGS: Define where the messy folder is
target_folder = "../TestDesktop"

# 2. SCAN: Look inside the folder and get a list of all files
if os.path.exists(target_folder):
    all_files = os.listdir(target_folder)
    
    # 3. LOOP: Go through every single file found one by one
    for item in all_files:
        
        # Skip folders if any exist, we only want to sort files
        if os.path.isdir(os.path.join(target_folder, item)):
            continue
            
        # 4. ISOLATE THE EXTENSION (Your Way, made bulletproof!)
        # item.split('.') breaks "notes.txt" into a list: ['notes', 'txt']
        # [-1] grabs the very last item in that list, which is always the extension!
        ends = item.split('.')[-1].lower() 
        
        # Define current location of the file
        source_path = os.path.join(target_folder, item)
        
        # 5. DECIDE AND MOVE
        if ends == "txt":
            dest_folder = os.path.join(target_folder, "TextFiles")
        elif ends == "pdf":
            dest_folder = os.path.join(target_folder, "PDFFiles")
        elif ends == "png":
            dest_folder = os.path.join(target_folder, "ImageFiles")
        else:
            dest_folder = os.path.join(target_folder, "Others")
            
        # Create the destination folder if it doesn't exist yet
        if not os.path.exists(dest_folder):
            os.makedirs(dest_folder)
            
        # Move the file inside
        destination_path = os.path.join(dest_folder, item)
        os.rename(source_path, destination_path)
        
    print("Automation complete! TestDesktop is completely clean.")
else:
    print("Error: Target folder not found.")