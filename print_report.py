def print_report(file_path, count_words, count_letters):
  print(f"--- Begin report of {file_path} ---")
  print(f"{count_words} words found in the document")
  for item in count_letters:
    # get key and value from the item (dict)
    for key, value in item.items():
      print(f"The '{key}' character was found {value} times")
    
  print(f"--- End of report ---")