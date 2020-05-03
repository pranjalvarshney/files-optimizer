import os
import shutil

files = os.listdir()
files.remove("main.py")

def createFolder(folderName):
    if folderName not in os.listdir():
        return os.makedirs(folderName)

def moveFile(fileName,folder):
    for image in fileName:
        shutil.move(image,folder) 


imageExtension = [".jpg",".jpeg",".gif",".ai",".bmp",".ico",".png",".psd",".svg"]
audioExtension = [".wav",".mpa",".aif",".mp3"]
videoExtension = [".avi",".flv",".m4v",".mkv",".mov",".mp4",".mpg",".mpeg",".wmv",".swf",".vob"]
docExtension = [".doc",".odt",".pdf",".rtf",".tex",".txt",".wpd",".xls",".ods",".ppt",".pptx",".key",".odp",".pps"]

images = [file for file in files if os.path.splitext(file)[1].lower() in imageExtension]
video = [file for file in files if os.path.splitext(file)[1].lower() in videoExtension]
audio = [file for file in files if os.path.splitext(file)[1].lower() in audioExtension]
docs = [file for file in files if os.path.splitext(file)[1].lower() in docExtension]
other= []

for file in files:
    xtension =  os.path.splitext(file)[1].lower()
    if xtension not in imageExtension and xtension not in videoExtension and xtension not in audioExtension and xtension not in docExtension and os.path.isfile(file):
        other.append(file)

allFolders = ["Audio","Video","Images","Documents","Others"] 
filetypes = ["audio","video","images","docs" ,"other"]
for f in allFolders:
    createFolder(f)

moveFile(audio,"Audio")
moveFile(video,"Video")
moveFile(images,"Images")
moveFile(docs,"Documents")
moveFile(other,"Others")
