def answer(n):
    # Normalize input: lowercase and remove extra spaces
    n = n.lower().strip()

    # Check against allowed variations
    if n == "42" or n == "forty two" or n == "forty-two":
        return "Yes"
    else:
        return "No"

def main():
    # Prompt the user
    user_input = input("What is the answer to the ultimate question of life, the Universe, and Everything? ")

    # Get result
    result = answer(user_input)
    print(f"The answer is: {result}")

main()
