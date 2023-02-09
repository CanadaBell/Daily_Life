#Imports
import daily_data
import random
import time
#Variables
money = None 
food_in = None
fit_in = None
enter_in = None
#Processing/Output
print("Daily life planner")
pas = random.randint(1000,9999) #Create random password
print (f"""Please input this number set
{pas}
""")
pas_e = int(input("> ")) 
daily_data.clear()
if pas == pas_e or pas_e == 1:
    print("How much money do you want to add")
    money = float(input("> "))
    #Choose Meal
    daily_data.clear()
    print(f"""Please select one of the opions below
    {daily_data.food_c()}

    please input either a, b or c
    """)
    food_in = input("> ")
    money = money - daily_data.food[food_in]["Cost"]
    print("your new balance is: ${:.2f}".format(money))
    time.sleep(5)
    #Choose fitness
    daily_data.clear()
    print(f"""Please select one of the opions below
    {daily_data.fit_c()}

    please input either a, b or c
    """)
    fit_in = input("> ")
    print(daily_data.fit_o[fit_in])
    money = money - daily_data.fit[food_in]["Cost"]
    print("Your new balance is: ${:.2f}".format(money))
    time.sleep(5)
    #Choose Entertainment
    daily_data.clear()
    print(f"""Please select one of the opions below
    {daily_data.ent_c()}

    please input either a, b or c
    """)
    enter_in = input("> ")
    print(daily_data.enter_o[enter_in])
    money = money - daily_data.fit[enter_in]["Cost"]
    print("Your final balance is: ${:.2f}".format(money))
    time.sleep(5)
    money = round(money,2)
    #Re-cap
    print (f"""Here is a recap of your day:
    - For your meal, you will have {daily_data.food[food_in]["Item"]}
    - {daily_data.fit_o[fit_in]} as your fitness activity
    - {daily_data.enter_o[enter_in]} as your entertainment""")
    print("End balance is: ${:.2f}".format(money))
else:
    print("denied")
    daily_data.clear()

time.sleep(10)
daily_data.clear()
print("thanks for using")