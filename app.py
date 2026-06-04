import os

target_folder = ".."

if os.path.exists(target_folder):
    # os.listdir returns a list like ['app.py', '.env']
    all_files = os.listdir(target_folder)
    
    print("\n--- Scanning Workspace ---")
    # We loop through the list one file at a time
    for file_name in all_files:
        print(f"Found file: {file_name}")
        
else:
    print("Error: That folder does not exist.")