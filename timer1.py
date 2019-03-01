import time 
import sys

countdown_min = 1
fire_time = int(time.time()) + countdown_min * 5
while 1: 
  current_time = time.time()
  if current_time > fire_time:
    print('fire')
    sys.exit()
  else:
    remaining_sec = fire_time - current_time 
    return_char = "\r" # to return to the beginning of stdout 
    if remaining_sec == 0: 
      return_char = "\n" # to move to next line
    sys.stdout.write(("  %02d : %02d   " + return_char) % (remaining_sec / 60, remaining_sec % 60) )
    sys.stdout.flush()
  time.sleep(0.2)