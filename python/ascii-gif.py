import argparse
import colorist
import cv2
import moviepy.editor as mp
import time 

parser = argparse.ArgumentParser()
parser.add_argument('--gif', type=str, required=True) # Gif path
parser.add_argument('--fill-type', type=int, required=True) # Ascii char fill type
args = parser.parse_args()

video_path = args.gif    

clip = mp.VideoFileClip(f"{video_path}.gif")
clip.write_videofile(f"{video_path}.mp4")

video = cv2.VideoCapture(f"{video_path}.mp4")

frame_counter = 0

if args.fill_type == 1:
    LETTER = [' ', '.', ':', '░', '▒', '▓', '█']
elif args.fill_type == 2:
    LETTER = [' ', '_', '.', ',', '-', '=', '+', ':', ';', 'c', 'b', 'a', '!', '?',
                '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '$', 'W', '#', '@', 'Ñ']
elif args.fill_type == 3:
    LETTER = [' ', '.', ':', '-', '=', '+', '*', '#', '%', '@']
else:
    print("Invalid syntax. :/ ")

def get_color(row, column, source):
    return source[row, column]

def convert_row_to_ascii(row):    
    letter_length = len(LETTER) - 1    
    return tuple(LETTER[int(x / (255 / letter_length))] for x in row)

def convert_to_ascii(source):
    return tuple(convert_row_to_ascii(row) for row in source)

def print_array(input_ascii_array):
    print('\n'.join((''.join(row) for row in input_ascii_array)), end='')

while (True):
    width = 160
    height = 45

    ret, frame = video.read()
    if ret:
        time.sleep(0.041666) # 24 fps in seconds
        frame_counter += 1

        if frame_counter == video.get(cv2.CAP_PROP_FRAME_COUNT):
            frame_counter = 0
            video.set(cv2.CAP_PROP_POS_FRAMES, 0)

        colored = frame
        monocrome = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        reduced_colored = cv2.resize(colored, (width, height))
        reduced_mono = cv2.resize(monocrome, (width, height)) # for 16:9 aspect ratio use 2x the amount of x pixels
        print_array(convert_to_ascii(reduced_mono))
