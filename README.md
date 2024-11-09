# uv-scanner

a python tool that scans usb drives for suspicious files and checks them against virustotal for known malware.

## structure

- `config.py`: configuration settings, such as the VirusTotal API key.
- `hash_utils.py`: utility functions for file hashing.
- `virus_total.py`: handles communication with the VirusTotal API.
- `scanner.py`: contains the scanning logic for USB files.
- `main.py`: main script to run the scanner.

## setup

1. clone the repository.
2. install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. set up your virustotal api key in `config.py`.

## usage

run the scanner with:

```bash
python src/main.py
```
