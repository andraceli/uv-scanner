import os
API_KEY = os.getenv("VIRUSTOTAL_API_KEY", "your_virustotal_api_key") # drop the lonely api key
SUSPICIOUS_EXTENSIONS = {'.exe', '.bat', '.vbs', '.scr', '.pif', '.com', '.cmd'}
