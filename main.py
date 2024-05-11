import os
import random
import time

red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m"
blue = "\033[34m"
magenta = "\033[35m"
cyan = "\033[36m"
white = "\033[0m"

people_list = []


def adding():
  while True:

    def info():
      name_1 = input("\n\n\nEnter your first name: ").strip().title()
      name_2_last = input("\nEnter your last name: ").strip().title()
      if f"{name_1} {name_2_last}" in people_list:
        print(red, "\nalready names are exiting!", white)
        info()
      else:
        add_list = f"{name_1} {name_2_last}"
        people_list.append(add_list)
        print(green, "\nsuccessfully added 👍\n", white)
        print(f"{green}---------> {add_list}  <----------{white}")
        print()
        print("following are the so far added people's to the list: \n\n")
        time.sleep(2)
        num = 1
        for i in people_list:
          print(f"{blue}{num}. {i}{white}\n")
          num += 1
        interation = 0
        while True:
          if interation >= 0:
            ask = input("\nDone with adding in List? (yes or no)  ---> "
                        ).strip().lower()
            if ask == "yes":
              os.system("clear")
              print("\nSaving the content....")
              time.sleep(4)
              os.system("clear")
              print()
              for i in people_list:
                print(f"{i}\n")
              print(green, "\n\nDone! all contact names were SAVED 😄👍\n\n", white)
              exit()
            elif ask == "no":
              os.system("clear")
              print(green, "\n\nSaving...", white)
              time.sleep(2)
              os.system("clear")
              adding()
            else:
              print("You can only answer in yes or no.")
              continue
          else:
            interation += 1
            adding()

      os.system("clear")

    print(magenta, "\n                 MY CONTACT LIST! 👍😄", white)
    print(blue, "          <--------------------------------->\n\n", white)
    print(
        red,
        "if an unexpected error occurred please make your team again (run the programe again 😅)",
        white)
    print("---------------------------------------------------------")
    first_name = input("\n\n\nEnter your first name: ").strip().title()
    last_name = input("\nEnter your last name: ").strip().title()
    if f"{first_name} {last_name}" in people_list:
      print(red, "\nalready names are exiting!", white)
      info()
      # continue
    else:
      add_list = f"{first_name} {last_name}"
      people_list.append(add_list)
      print(green, "\nsuccessfully added 👍\n", white)
      print(f"{green}---------> {add_list}  <----------{white}")
      print()
      print("following are the so far added people's to the list: \n\n")
      time.sleep(2)
      num = 1
      for i in people_list:
        print(f"{blue}{num}. {i}{white}\n")
        num += 1
      break


interation = 0
while True:
  if interation >= 1:
    ask = input(
        "\nDone with adding in List? (yes or no)  ---> ").strip().lower()
    if ask == "yes":
      os.system("clear")
      print("\nSaving the content....")
      time.sleep(4)
      os.system("clear")
      print()
      for i in people_list:
        print(f"{i}\n")
      print(green, "\n\nDone! all contact name were SAVED 😄👍\n\n", white)
      exit()
    elif ask == "no":
      os.system("clear")
      print(green, "\n\nSaving...", white)
      time.sleep(2)
      os.system("clear")
      adding()
    else:
      print("You can only answer in yes or no.")
      continue
  else:
    interation += 1
    adding()
