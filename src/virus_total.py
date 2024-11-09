import requests
from src.config import API_KEY

def check_file_with_virustotal(file_hash):
    url = f"https://www.virustotal.com/api/v3/files/{file_hash}" # checks
    headers = {"x-apikey": API_KEY}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        json_response = response.json()
        positives = json_response.get('data', {}).get('attributes', {}).get('last_analysis_stats', {}).get('malicious', 0)
        if positives > 0:
            return True, positives
        else:
            return False, 0
    elif response.status_code == 404:
        return False, None
    else:
        print(f"Error: {response.status_code}")
        return False, None
