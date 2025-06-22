import valid as v
PIECES_PERHOUR = 250
ADD_LEGO_SET = 1
PRINT_LIST = 2
QUIT = 3

def main():

  names = []
  pieces = []
  hours = []
  minutes = []
  option = 0

  print_intro()
  print_menu()

  option = get_option()

  while option != QUIT:
    if option == ADD_LEGO_SET:
      add_lego(names, pieces, hours, minutes)
      print_menu()
      option = get_option()
    if option == PRINT_LIST:
      print_results(names, pieces, hours, minutes)
      print_menu()
      option = get_option()
  print_results(names, pieces, hours, minutes)
  print_outro()



def print_intro(): 
  """
  Prints program intro.
  :return: none
  """
  print("Lego Time Calculator!")


def print_menu():
  """
  Function to print menu to add a Lego set, or quit.
  :return: none
  """
  print("\n1. Add Lego Set")
  print("2. Print Results")
  print("3. Quit")


def get_option():
  """
  Function to get menu option from the user
  :param: none
  :return: option
  """
  option = 0
  option = v.get_integer("\nEnter Option: ")
  while option < ADD_LEGO_SET or option > QUIT:
    print("Invalid option! Enter a 1, 2 or 3.")
    option = v.get_integer("\nEnter Option: ")
  return option

def add_lego(names, pieces, hours, minutes):
  lego_set_name = ""
  pieces_in_set = 0
  time_to_build = 0
  hours_to_build = 0
  minutes_to_build = 0

  lego_set_name = get_lego_set_name()
  names.append(lego_set_name)
  pieces_in_set = get_pieces_in_set()
  pieces.append(pieces_in_set)
  time_to_build = int(pieces_in_set) / PIECES_PERHOUR * 60
  hours_to_build = int(time_to_build) // 60
  hours.append(hours_to_build)
  minutes_to_build = int(time_to_build) % 60
  minutes.append(minutes_to_build)


def get_lego_set_name():
  """
  Prompts the user for the Lego set name and returns it
  :param: none
  :return: string containing Lego set name
  """
  lego_set_name = ""
  #lego_set_name = (input("\nEnter the name of your Lego set: "))
  lego_set_name = v.get_string("\nEnter the name of your Lego set: ")
  return lego_set_name


def get_pieces_in_set():
  """
  Prompts the user for the number of pieces in their Lego set and returns it
  :param: none
  :return: integer containing Lego pieces
  """
  pieces_in_set = 0
  #pieces_in_set = int(input("Enter the number of pieces in your set: "))
  pieces_in_set = v.get_integer("Enter the number of pieces in your set: ")
  while pieces_in_set <= 0 or pieces_in_set > 11000:
    print("\nEnter valid amount of pieces. Between 1 and 11,000.")
    pieces_in_set = v.get_integer("Enter the number of pieces in your set: ")
  return pieces_in_set


def print_results(names, pieces, hours, minutes):
  total_time_to_build = 0
  total_pieces_in_set = 0
  total_hours = 0
  total_minutes = 0
  index = 0
  print("\n---------------------------------------------------")
  print("Results:\n")
  print("Name\t\t\tPieces\t\t\tHours\t\tMinutes")
  print("----------------------------------------------------")  
  while index < len(names):
    print(f"{names[index]:9}", end = '')
    print(f"{pieces[index]:9}", end = '')
    print(f"{hours[index]: 9}", end = '')
    print(f"{minutes[index]: 12}")
    total_pieces_in_set = total_pieces_in_set + pieces[index]
    index += 1
  total_time_to_build = int(total_pieces_in_set) / PIECES_PERHOUR * 60
  total_hours = int(total_time_to_build) // 60
  total_minutes = int(total_time_to_build) % 60
  print("-----------------------------------------")
  print("Total hours: ", total_hours, end = '')
  print("    Total minutes: ", total_minutes)

      

def print_outro():
  """
  Prints program outro
  :param: none
  :return: none
  """
  print("\nHappy Lego!")

main()