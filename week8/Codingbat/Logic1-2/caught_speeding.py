def caught_speeding(speed, is_birthday):
  if not is_birthday:
    if speed <= 60: return 0
    if speed >= 61 and speed <=80: return 1
    if speed >= 81: return 2
  elif is_birthday:  
    if speed <= 65: return 0
    if speed >= 66 and speed <=85: return 1
    if speed >= 86: return 2