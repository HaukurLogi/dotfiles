import os
from pathlib import Path

SUBDIR = {
        "audio":[".m4a",".m4b",".mp3"],
        "images":[".jpg",".jpeg",".png"],
        "python":[".py"],
        "json":[".json"]
}

def pickDir(value):
    for category, ekstensi in SUBDIR.items():
        for suffix in ekstensi:
            if suffix == value:
                return category
            
def organizeDir():
    for item in os.scandir():
                
        # Just looking for file, skip the directory
        if item.is_dir():
                continue
                
        filePath = Path(item)
        fileType = filePath.suffix.lower()
        directory = pickDir(fileType)
        
        # Just skip, if the file extension not defined.
        if directory == None:
            continue
        
        directoryPath = Path(directory)
        # Make new directory if the category's directory not found.
        if directoryPath.is_dir() != True:
                directoryPath.mkdir()
        filePath.rename(directoryPath.joinpath(filePath))

organizeDir()
