def main():
  user_input = input("Howdy? ")
  output = greeting(user_input)
  print(output, end = "")

def greeting(n):
  n = n.lower().strip()
  if n.startswith("hello"):
    return "$0"
  elif n.startswith("h"):
    return "$20"
  else:
    return "$100"

main()

