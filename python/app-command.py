import argparse
import os
import time


is_running = False


parser = argparse.ArgumentParser()
parser.add_argument('--runningcmd', type=str, required=True) # The command that runs if program is running
parser.add_argument('--stoppedcmd', type=str, required=True)
parser.add_argument('--app', required=True) # Target program
args = parser.parse_args()


while True:
    time.sleep(1) # Wait 1 second before checking again
    if os.popen(f'pgrep {args.app}').read() != '': # Check if program is running
        if not is_running: # Makes sure runningmcd only runs once
            print(f"Program running; executing {args.runningcmd}...")
            os.system(args.runningcmd) # Runs runningcmd
            is_running = True
    else:
        if is_running: # Makes sure stoppedcmd only runs once
            print(f"Program stopped; executing {args.stoppedcmd}...")
            os.system(args.stoppedcmd) # Runs stoppedcmd
            is_running = False
