import argparse
import os
import time


isRunning = False


parser = argparse.ArgumentParser()
parser.add_argument('--runningcmd', type=str, required=True) # The command that runs if program is running
parser.add_argument('--stoppedcmd', type=str, required=True)
parser.add_argument('--app', required=True) # Target program
args = parser.parse_args()


while True:
    time.sleep(10) # Wait 10 seconds before checking again
    if os.popen(f'pgrep {args.app}').read() != '': # Check if program is running
        if not isRunning: # Makes sure runningmcd only runs once
            print(f"Program running; executing {args.runningcmd}...")
            os.system(args.runningcmd) # Runs runningcmd
            isRunning = True
    else:
        if isRunning: # Makes sure stoppedcmd only runs once
            print(f"Program stopped; executing {args.stoppedcmd}...")
            os.system(args.stoppedcmd) # Runs stoppedcmd
            isRunning = False