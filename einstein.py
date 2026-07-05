# Definne a funcrion where the Energy formula will be applied
def formula(mass, speed_of_light):
  E = mass*speed_of_light*speed_of_light
  # Get the answer back as return value
  return E

def main():
  # Take mass input
  m = int(input("Please enter the value of mass in kg: "))
  c = 300000000
  # Take output using input formula
  print("The answer is", formula(m, c))

main()
