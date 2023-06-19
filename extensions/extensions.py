import os

fileName = input("File name: ")
fileExtension = os.path.splitext(fileName)[1].lower().strip()

mediaTypes = {
    '.gif': 'image/gif',
    '.jpg': 'image/jpeg',
    '.jpeg': 'image/jpeg',
    '.png': 'image/png',
    '.pdf': 'application/pdf',
    '.txt': 'text/plain',
    '.zip': 'application/zip'
}

mediaType = mediaTypes.get(fileExtension, 'application/octet-stream')
print(mediaType)