import argparse
import os
import time


parser = argparse.ArgumentParser()
parser.add_argument('--runningcmd', type=str, required=True) # The command that runs if program is running
parser.add_argument('--stoppedcmd', type=str, required=True)
parser.add_argument('--app', required=True) # Target program
args = parser.parse_args()


while True:
    time.sleep(10)
    if os.popen(f'pgrep {args.app}').read() != '': # Check if program is running
        print(f"Program running; executing {args.runningcmd}...")
        os.system(args.runningcmd) # Runs runningcmd
    else:
        print(f"Program stopped; executing {args.stoppedcmd}...")
        os.system(args.stoppedcmd) # Runs stoppedcmd