print("                    WELCOME TO SKILL CIRCLE LIBRARY MANAGMENT SYSTEM                      ")

print('''press "1" for 101 book
      press "2" for 102 book
      press "3" for 103 book
      press "4" for 104 book 
      press "5" for 105 book
      ''')


def happy():
      a = int(input("enter a number for book"))
      if a== 1:
            print("BOOK NAME:The Power of Your Subconscious Mind\n"
            "LAUNCH DATE: Originally published in 1958\n"
            "AUTHOR :Joseph Murphy\n"
            "DESCRIPTION: Explores the immense power of the subconscious mind to transform your life\n"
            "PRICE: ₹ 700")
      elif a ==2:
            print("BOOK NAME :Atomic Habits\n"
            "LAUNCH DATE: October 16, 2018\n"
            "AUTHOR:James Clear\n"
            "DESCRIPTION: A practical guide to building good habits and breaking bad ones, with actionable strategies\n"
            "PRICE: ₹900.")
      elif a== 3:
            print("BOOK NAME:Think Like a Monk\n" 
                  "AUTHOR:Jay Shetty\n"
                  "LAUNCH DATE: September 8, 2020\n"
            "DESCRIPTION: Combines ancient wisdom with practical advice for modern-day challenges\n"
            "PRICE: ₹900")
      elif a == 4:
            print("BOOK NAME : How to Win Friends and Influence People\n"
            "AUTHOR:Dale Carnegie\n"
            "LAUNCH DATE: Originally published in 1936\n"
            "DESCRIPTION: Timeless principles on improving relationships and communication skills\n"
            "PRICE: ₹800.")
      elif a == 5:
            print("BOOK NAME:The 5 AM Club\n"  
            "AUTHOR:Robin Sharma\n"
            "LAUNCH DATE: December 4, 2018\n"
            "DESCRIPTION: Teaches how waking up early can unlock productivity and success\n"
            "PRICE: ₹900")
      else :
            print("enter a number between 1 or 5")

      print("press 1 for continue"
      "press 2 for exit")
      b = int(input("enter a number"))
      if b==1:
            b=happy()
      elif b==2:
            print("thanku for using SKILL CIRCLE LIBRABRY MANAGMENT SYSTEM")
happy()
















