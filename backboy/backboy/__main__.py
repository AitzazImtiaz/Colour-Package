from colorama import Back
import sys
def main ():
  command = sys.argv[1]
  if command == "red":
    print(Back.RED)
  elif command == "blue":
    print(Back.BLUE)
  elif command == "yellow":
    print(Back.YELLOW)
  elif command == "cyan":
    print(Back.CYAN)
  elif command == "green":
    print(Back.GREEN)
  elif command == "magenta":
    print(Back.MAGENTA)
  elif command == "white":
    print(Back.WHITE)
  elif command == "black":
    print(Back.BLACK)
  else:
    print("Invalid command kiddo -_- ")
