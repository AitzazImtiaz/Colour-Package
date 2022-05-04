from colorama import Fore
import sys
def main ():
  command = sys.argv[1]
  if command == "red":
    print(Fore.RED)
  elif command == "blue":
    print(Fore.BLUE)
  elif command == "yellow":
    print(Fore.YELLOW)
  elif command == "cyan":
    print(Fore.CYAN)
  elif command == "green":
    print(Fore.GREEN)
  elif command == "magenta":
    print(Fore.MAGENTA)
  elif command == "white":
    print(Fore.WHITE)
  elif command == "black":
    print(Fore.BLACK)
  else:
    print("Invalid command kiddo -_- ")
