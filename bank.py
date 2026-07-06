def main():
  user_input = input("Howdy? ")
  output = greeting(user_input)
  print(output)

def greeting(n):
  n.lower().strip()
  if n == "hello":
    return "0"
  elif n == "h":
    return "20"
  else:
    return "100"

main()

