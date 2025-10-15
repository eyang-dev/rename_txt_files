import os
import re
from datetime import datetime

def remove_existing_timestamp(filename):
    """
    Failsafe for if a file has previously been adjusted. This function prevents recursion.
    """
    pattern = r"^\d{8}_\d{6}(AM|PM)_"
    return re.sub(pattern, '', filename)

def rename_txt_files(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            # Remove existing timestamp from filename
            base_filename = remove_existing_timestamp(filename)
            old_path = os.path.join(folder_path, filename)
            new_base_path = os.path.join(folder_path, base_filename)

            # Get path
            os.rename(old_path, new_base_path)  

            # Get creation time
            creation_time = os.path.getctime(new_base_path)
            timestamp = datetime.fromtimestamp(creation_time).strftime("%Y%m%d_%I%M%S%p")

            # Apply new timestamp
            new_filename = f"{timestamp}_{base_filename}"
            final_path = os.path.join(folder_path, new_filename)

            os.rename(new_base_path, final_path)
            print(f"Renamed: {filename} → {new_filename}")
            

# Replace this with your folder path
folder_to_automate = r"C:.."

rename_txt_files(folder_to_automate)
