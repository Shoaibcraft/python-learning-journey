def convert(text):
  # Replace emoticons with emoji
  # Note: Use the actual emoji characters here
  text = text.replace(":)", "🙂")
  text = text.replace(":(", "🙁")
  return text

def main():
  # Take input from user
  user_input = input("")
  # output and calling the convert function
  print(convert(user_input))

# Call main function for execution
main()
