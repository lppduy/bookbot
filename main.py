from count_words import count_words
from count_letters import count_letters
from print_report import print_report

file_path = 'books/frankenstein.txt'

try:
  with open(file_path, 'r') as file:
    file_content = file.read()
    count_words = count_words(file_content)
    count_letters = count_letters(file_content)
    print_report(file_path, count_words, count_letters)

except FileNotFoundError:
  print(f"File '{file_path}' not found.")

except Exception as e:
  print(f"An error occurred: {e}")


