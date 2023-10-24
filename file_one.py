# Python module to execute
import file_two

print(f'1. File one __name__ is set to: {__name__}')

if __name__ == "__main__":
   print("2. File one executed when ran directly")
else:
   print("3. File one executed when imported")