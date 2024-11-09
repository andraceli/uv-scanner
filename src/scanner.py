import os
from src.config import SUSPICIOUS_EXTENSIONS
from src.hash_utils import calculate_md5
from src.virus_total import check_file_with_virustotal

def scan_usb(path):
    # yo cool api gonna scan 
    suspicious_files = []
    for root, dirs, files in os.walk(path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            file_ext = os.path.splitext(file_name)[1].lower()
            # fo yo suspicious ass
            if file_ext in SUSPICIOUS_EXTENSIONS:
                suspicious_files.append((file_path, 'Suspicious extension'))
            # hash fo virustotal
            try:
                file_hash = calculate_md5(file_path)
                is_malicious, positives = check_file_with_virustotal(file_hash)
                if is_malicious:
                    suspicious_files.append((file_path, f"Malicious file detected by {positives} sources on VirusTotal"))
                elif positives is None:
                    print(f"{file_path} - File not found in VirusTotal database.")
            except Exception as e:
                print(f"Error reading {file_path}: {e}")
            # autorun bro, they hate it
            if 'autorun.inf' in file_name.lower():
                suspicious_files.append((file_path, 'Autorun file detected'))
    return suspicious_files
