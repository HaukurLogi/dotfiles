import argparse
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

def convert_row_to_ascii(row):
    letter_length = len(LETTER) - 1
    return tuple(LETTER[int(x / (255 / letter_length))] for x in row)[::-1]

def convert_to_ascii(input_grays):
    return tuple(convert_row_to_ascii(row) for row in input_grays)

def print_array(input_ascii_array):
    print('\n'.join((''.join(row) for row in input_ascii_array)), end='')

while (True):
    ret, frame = video.read()
    if ret:
        time.sleep(0.041666) # 24 fps in seconds
        frameCounter += 1

        if frameCounter == video.get(cv2.CAP_PROP_FRAME_COUNT):
            frameCounter = 0 #Or whatever as long as it is the same as next line
            video.set(cv2.CAP_PROP_POS_FRAMES, 0)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        reduced = cv2.resize(gray, (int(80), int(45)))
        converted = convert_to_ascii(reduced)
        print_array(converted)
