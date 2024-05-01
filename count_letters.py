def count_letters(file_content):
  map = {}
  lowered_content = file_content.lower()
  for char in lowered_content:
    if char.isalpha():
      if char in map:
        map[char] += 1
      else:
        map[char] = 1

  lst = [] 
  for key in map:
    value = map[key]
    obj = {key: value}
    lst.append(obj)

  lst.sort(reverse=True, key=lambda x: list(x.values())[0])
  return lst