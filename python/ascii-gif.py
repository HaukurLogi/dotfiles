import argparse
import colorist
import cv2
import moviepy.editor as mp
import time 

parser = argparse.ArgumentParser()
parser.add_argument('--gif', type=str, required=True) # Gif path
parser.add_argument('--fill-type', type=int, required=True) # Ascii char fill type
args = parser.parse_args()

videoPath = args.gif    

clip = mp.VideoFileClip(f"{videoPath}.gif")
clip.write_videofile(f"{videoPath}.mp4")

video = cv2.VideoCapture(f"{videoPath}.mp4")

frameCounter = 0

if args.fill_type == 1:
    LETTER = [' ', '.', ':', '░', '▒', '▓', '█']
elif args.fill_type == 2:
    LETTER = [' ', '_', '.', ',', '-', '=', '+', ':', ';', 'c', 'b', 'a', '!', '?',
                '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '$', 'W', '#', '@', 'Ñ']
elif args.fill_type == 3:
    LETTER = [' ', '.', ':', '-', '=', '+', '*', '#', '%', '@']
else:
    print("Invalid syntax. :/ ")

def getColor(row, column, source):
    return source[row, column]

def convertRowToAscii(row):    
    letterLength = len(LETTER) - 1    
    return tuple(LETTER[int(x / (255 / letterLength))] for x in row)

def convertToAscii(source):
    return tuple(convertRowToAscii(row) for row in source)

def printArray(inputAsciiArray):
    print('\n'.join((''.join(row) for row in inputAsciiArray)), end='')

while (True):
    width = 160
    height = 45

    ret, frame = video.read()
    if ret:
        time.sleep(0.041666) # 24 fps in seconds
        frameCounter += 1

        if frameCounter == video.get(cv2.CAP_PROP_FRAME_COUNT):
            frameCounter = 0
            video.set(cv2.CAP_PROP_POS_FRAMES, 0)

        colored = frame
        monocrome = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        reducedColored = cv2.resize(colored, (width, height))
        reducedMono = cv2.resize(monocrome, (width, height)) # for 16:9 aspect ratio use 2x the amount of x pixels
        printArray(convertToAscii(reducedMono))
