# extensions.py

def main():
    # Prompt the user for the name of a file
    file_name = input("Enter the name of a file: ")

    # Extract the file extension (suffix) and convert to lowercase
    file_extension = file_name.lower().strip().split('.')[-1] if '.' in file_name else ''

    # Map file extension to media type
    media_type = get_media_type(file_extension)

    # Output the media type
    print(media_type)

def get_media_type(extension):
    # Map file extensions to media types
    media_types = {
        'gif': 'image/gif',
        'jpg': 'image/jpeg',
        'jpeg': 'image/jpeg',
        'png': 'image/png',
        'pdf': 'application/pdf',
        'txt': 'text/plain',
        'zip': 'application/zip',
    }

    # Return the corresponding media type or default to 'application/octet-stream'
    return media_types.get(extension, 'application/octet-stream')

if __name__ == "__main__":
    main()
