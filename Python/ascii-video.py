try:
    import cv2
    import sys
    video = cv2.VideoCapture(0)
    choose_letters = int(input("""
    1: █▓▒░:. 
    2: Ñ@#W$9876543210?!abc;:+=-,._
    3: @%#*+=-:.
    Choose: """))

    if choose_letters == 1:
        LETTER = [' ', '.', ':', '░', '▒', '▓', '█']
    elif choose_letters == 2:
        LETTER = [' ', '_', '.', ',', '-', '=', '+', ':', ';', 'c', 'b', 'a', '!', '?',
                  '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '$', 'W', '#', '@', 'Ñ']
    elif choose_letters == 3:
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

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        reduced = cv2.resize(gray, (int(64), int(32)))
        converted = convert_to_ascii(reduced)
        print_array(converted)
        cv2.imshow('frame', reduced)

        print(""" 
        Press Control+C to terminate the program 
        and take a picture. """)

except KeyboardInterrupt:
    print(f"You terminated the program and took a photo.")
    oiginal_stdout = sys.stdout
    # import your file
    with open('picture.txt', 'w') as f:
        sys.stdout = f
        print_array(converted)
