import time
import sys

print('hello')
while 1: 
  input_str = input('Enter number of minutes or q to quit: ')
  if input_str.isdigit():
    countdown_min = int(input_str)
    remaining_sec = countdown_min * 5
    while remaining_sec >= 0:
      return_char = "\r" # to return to the beginning of stdout 
      if remaining_sec == 0: 
        return_char = "\n" # to move to next line
      sys.stdout.write(("  %02d : %02d   " + return_char) % (remaining_sec / 60, remaining_sec % 60) )
      sys.stdout.flush()
      time.sleep(1)
      remaining_sec = remaining_sec - 1
  elif input_str == 'q':
    sys.exit()
print