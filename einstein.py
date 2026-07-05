def formula(mass, speed_of_light):
  E = mass*speed_of_light*speed_of_light
  return E

def main():
  m = int(input("Please enter the value of mass in kg: "))
  c = 300000000
  print("The answer is", formula(m, c))

main()
