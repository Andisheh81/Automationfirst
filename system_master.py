import os
import time

# 1. SETTINGS: Define our sandbox environment
source_dir = "../TestDesktop"

# Define size threshold: 1000 bytes (1 KB)
# Anything larger than this is considered a "Large" file
SIZE_THRESHOLD_BYTES = 1000

print("🔍 Initializing Advanced System File Scan...")

try:
    if os.path.exists(source_dir):
        all_items = os.listdir(source_dir)
        
        for item in all_items:
            # Absolute safety check: Construct full path
            full_source_path = os.path.join(source_dir, item)
            
            # CRUCIAL SYSTEM LOGIC: Skip if it's a folder. We only automate files.
            if os.path.isdir(full_source_path):
                continue
                
            # --- PILLAR 1: METADATA EXTRACTION ---
            # Ask the OS for the file size in bytes
            file_size = os.path.getsize(full_source_path)
            
            # --- PILLAR 2: DYNAMIC DECISION MAKING ---
            if file_size > SIZE_THRESHOLD_BYTES:
                category = "LargeFiles"
            else:
                category = "SmallFiles"
                
            # Define target directory path
            dest_dir = os.path.join(source_dir, category)
            
            # Create category folder safely if missing
            if not os.path.exists(dest_dir):
                os.makedirs(dest_dir)
                
            full_dest_path = os.path.join(dest_dir, item)
            
            # --- PILLAR 3: SECURE OS MANIPULATION ---
            try:
                os.rename(full_source_path, full_dest_path)
                
                # --- PILLAR 4: TIMESTAMPED LOGGING ---
                # Generate a precise system timestamp
                current_timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
                
                log_line = f"[{current_timestamp}] MUTATION SUCCESS: '{item}' ({file_size} bytes) allocated to {category}\n"
                
                with open("system_ledger.log", "a") as ledger:
                    ledger.write(log_line)
                    
                print(f"✅ Processed: {item}")
                
            except FileNotFoundError:
                print(f"⚠️ Race Condition Detected: File '{item}' vanished before processing.")
            except PermissionError:
                print(f"❌ Security Alert: Insufficient OS permissions to move '{item}'.")
    else:
        print("❌ System Error: Target source directory does not exist.")

except Exception as global_error:
    print(f"🚨 Critical System Failure: {global_error}")