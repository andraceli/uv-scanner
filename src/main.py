from src.banner import display_banner
from src.scanner import scan_usb

def main():
    display_banner()  

    usb_path = input("Enter the path of the USB drive (e.g., /media/usb): ").strip()
    if not usb_path or not os.path.isdir(usb_path):
        print("Invalid USB path.")
        return

    suspicious_files = scan_usb(usb_path)
    if suspicious_files:
        print("Potentially malicious files detected:")
        for file_path, reason in suspicious_files:
            print(f"{file_path} - {reason}")
    else:
        print("No suspicious files detected.")

if __name__ == "__main__":
    main()
