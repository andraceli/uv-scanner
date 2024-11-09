import hashlib

def calculate_md5(file_path):
    hasher = hashlib.md5()
    with open(file_path, 'rb') as file:
        while chunk := file.read(4096):
            hasher.update(chunk)
    return hasher.hexdigest()
