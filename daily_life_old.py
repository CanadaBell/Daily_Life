#Imports
import os
import random
#Inputs/Variables 
pas = None
pas_e = None
money = None
food = ('''What do you want for lunch?
a) Cheese burger with fries = $9.59
b) Poutine = 5.99
c) Hotdog (ketchup + mustard) and chips (original) = $10.60
When picking your option, input the letter (i.e. "a")''')
a1 = None
fit = ('''What workout do you want to do?
a) Yoga class = $25.78
b) 5 km walk in the river valley = Free
c) Swimming = $17.50
When picking your option, input the letter (i.e. "a")''')
a = ("You will be going to a Yoga Class at the Clareview Community Recreation Center. It starts at 4:30 pm and lasts 60 minutes.")
b = ("You will sttart at Hermitage Park and walk on the trail to Rundle Park.")
c = ("You will go to a pool at the Clareview Community Recreation Center and do laps around the pool.")
a2 = None
enter = ('''What would you like to do for entertainment?
a) Movie = $10.00
b) See art = $17.00
c) Got to a concert = $34.99
When picking your option, inpput the letter (i.e. "a")''')
a3 = None
intro = ("Welcome to The ~~[Very Important Daily Life Planner]~~")
intro2 = ("Now we can start the planning!")
desc = ("After the password, this app will ask what you want to do today!")
#Proccesing/Output
print (intro)
print (desc)
pas = input("Please enter a password: ")
os.system('cls' if os.name =='nt' else 'clear')
pas_e = input("Re-enter password: ")
if pas_e == pas:
    print (intro2)
    money = float(input("How much money do you want to spend? $"))
    os.system('cls' if os.name =='nt' else 'clear')
    print (f"Balance is ${money}")
    print (food)
    a1 = input("> ")
    if a1 == "a":
        money = money - 9.59
        money = round(money,2)
        print (f"Balance is ${money}")
        x = input("Press enter to continue")
        os.system('cls' if os.name =='nt' else 'clear')
        print(money)
        print (fit)
        a2 = input("> ")
        if a2 == "a":
            money = money - 25.78
            print (f"Balance is ${money}")
            money = round(money,2)
            print (a)
            x = input("Press enter to continue")
            os.system('cls' if os.name =='nt' else 'clear')
            print (f"Balance is ${money}")
            print (enter)
            a3 = input("> ")
            if a3 == "a":
                money = money - 10
                money = round(money,2)
                movie = random.choice(["Boss baby 2", "Shrek", "The Bee Movie", "Toy Story 2"])
                print (f"The movie you are watching is: {movie} and it is located at: Cineplex")
                print(money)
                x = input("Press enter to continue")
                os.system('cls' if os.name =='nt' else 'clear')
                print ("add more money?")
                ask = input("> ")
                if ask == "y" or ask == "yes":
                    add = float(input("How much? $"))
                    money = money + add
                else:
                    print ("ok")
            elif a3 == "b":
                money = money - 17
                money = round(money,2)
                print (f"You will be going to an art show and it is located at: The Edmonton Expo Centre ")
                print(money)
                x = input("Press enter to continue")
                os.system('cls' if os.name =='nt' else 'clear')
                print ("add more money?")
                ask = input("> ")
                if ask == "y" or ask == "yes":
                    add = float(input("How much? $"))
                    money = money + add
                else:
                    print ("ok")
            elif a3 == "c":
                money = money - 34.99
                money = round(money,2)
                print (f"You will be going to an concert and it is located at: Rogers Place ")
                print(money)
                x = input("Press enter to continue")
                os.system('cls' if os.name =='nt' else 'clear')
                print ("add more money?")
                ask = input("> ")
                if ask == "y" or ask == "yes":
                    add = float(input("How much? $"))
                    money = money + add
                else:
                    print ("ok")
        if a2 == "b":
            money = money - 0
            print (f"Balance is ${money}")
            money = round(money,2)
            print (b)
            x = input("Press enter to continue")
            os.system('cls' if os.name =='nt' else 'clear')
            print (f"Balance is ${money}")
            print (enter)
            a3 = input("> ")
            if a3 == "a":
                money = money - 10
                money = round(money,2)
                movie = random.choice(["Boss baby 2", "Shrek", "The Bee Movie", "Toy Story 2"])
                print (f"The movie you are watching is: {movie} and it is located at: Cineplex")
                print(money)
                x = input("Press enter to continue")
                os.system('cls' if os.name =='nt' else 'clear')
                print ("add more money?")
                ask = input("> ")
                if ask == "y" or ask == "yes":
                    add = float(input("How much? $"))
                    money = money + add
                else:
                    print ("ok")
            elif a3 == "b":
                money = money - 17
                money = round(money,2)
                print (f"You will be going to an art show and it is located at: The Edmonton Expo Centre")
                print(money)
                x = input("Press enter to continue")
                os.system('cls' if os.name =='nt' else 'clear')
                print ("add more money?")
                ask = input("> ")
                if ask == "y" or ask == "yes":
                    add = float(input("How much? $"))
                    money = money + add
                else:
                    print ("ok")
            elif a3 == "c":
                money = money - 34.99
                money = round(money,2)
                print (f"You will be going to an concert and it is located at: Rogers Place")
                print(money)
                x = input("Press enter to continue")
                os.system('cls' if os.name =='nt' else 'clear')
                print ("add more money?")
                ask = input("> ")
                if ask == "y" or ask == "yes":
                    add = float(input("How much? $"))
                    money = money + add
                else:
                    print ("ok")
        if a2 == "c":
            money = money - 17.50
            print (f"Balance is ${money}")
            money = round(money,2)
            print (c)
            x = input("Press enter to continue")
            os.system('cls' if os.name =='nt' else 'clear')
            print (f"Balance is ${money}")
            print (enter)
            a3 = input("> ")
            if a3 == "a":
                money = money - 10
                money = round(money,2)
                movie = random.choice(["Boss baby 2", "Shrek", "The Bee Movie", "Toy Story 2"])
                print (f"The movie you are watching is: {movie} and it is located at: Cineplex")
                print(money)
                x = input("Press enter to continue")
                os.system('cls' if os.name =='nt' else 'clear')
                print ("add more money?")
                ask = input("> ")
                if ask == "y" or ask == "yes":
                    add = float(input("How much? $"))
                    money = money + add
                else:
                    print ("ok")
            elif a3 == "b":
                money = money - 17
                money = round(money,2)
                print (f"You will be going to an art show and it is located at: The Edmonton Expo")
                print(money)
                x = input("Press enter to continue")
                os.system('cls' if os.name =='nt' else 'clear')
                print ("add more money?")
                ask = input("> ")
                if ask == "y" or ask == "yes":
                    add = float(input("How much? $"))
                    money = money + add
                else:
                    print ("ok")
            elif a3 == "c":
                money = money - 34.99
                money = round(money,2)
                print (f"You will be going to an concert and it is located at: Rogers Place")
                print(money)
                x = input("Press enter to continue")
                os.system('cls' if os.name =='nt' else 'clear')
                print ("add more money?")
                ask = input("> ")
                if ask == "y" or ask == "yes":
                    add = float(input("How much? $"))
                    money = money + add
                else:
                    print ("ok")    
    elif a1 == "b":
        money = money - 5.99
        money = round(money,2)
        print (f"Balance is ${money}")
        x = input("Press enter to continue")
        os.system('cls' if os.name =='nt' else 'clear')
        print(money)
        print (fit)
        a2 = input("> ")
        if a2 == "a":
            money = money - 25.78
            money = round(money,2)
            print (f"Balance is ${money}")
            print (a)
            x = input("Press enter to continue")
            os.system('cls' if os.name =='nt' else 'clear')
            print (f"Balance is ${money}")
            print (enter)
            a3 = input("> ")
            if a3 == "a":
                money = money - 10
                money = round(money,2)
                movie = random.choice(["Boss baby 2", "Shrek", "The Bee Movie", "Toy Story 2"])
                print (f"The movie you are watching is: {movie} and it is located at: Cineplex")
                print(money)
                x = input("Press enter to continue")
                os.system('cls' if os.name =='nt' else 'clear')
                print ("add more money?")
                ask = input("> ")
                if ask == "y" or ask == "yes":
                    add = float(input("How much? $"))
                    money = money + add
                else:
                    print ("ok")
            elif a3 == "b":
                money = money - 17
                money = round(money,2)
                print (f"You will be going to an art show and it is located at: The Edmonton Expo Centre")
                print(money)
                x = input("Press enter to continue")
                os.system('cls' if os.name =='nt' else 'clear')
                print ("add more money?")
                ask = input("> ")
                if ask == "y" or ask == "yes":
                    add = float(input("How much? $"))
                    money = money + add
                else:
                    print ("ok")
            elif a3 == "c":
                money = money - 34.99
                money = round(money,2)
                print (f"You will be going to an concert and it is located at: Rogers Place")
                print(money)
                x = input("Press enter to continue")
                os.system('cls' if os.name =='nt' else 'clear')
                print ("add more money?")
                ask = input("> ")
                if ask == "y" or ask == "yes":
                    add = float(input("How much? $"))
                    money = money + add
                else:
                    print ("ok")
        if a2 == "b":
            money = money - 0
            print (f"Balance is ${money}")
            money = round(money,2)
            print (b)
            x = input("Press enter to continue")
            os.system('cls' if os.name =='nt' else 'clear')
            print (f"Balance is ${money}")
            print (enter)
            a3 = input("> ")
            if a3 == "a":
                money = money - 10
                money = round(money,2)
                movie = random.choice(["Boss baby 2", "Shrek", "The Bee Movie", "Toy Story 2"])
                print (f"The movie you are watching is: {movie} and it is located at: Cineplex")
                print(money)
                x = input("Press enter to continue")
                os.system('cls' if os.name =='nt' else 'clear')
                print ("add more money?")
                ask = input("> ")
                if ask == "y" or ask == "yes":
                    add = float(input("How much? $"))
                    money = money + add
                else:
                    print ("ok")
            elif a3 == "b":
                money = money - 17
                money = round(money,2)
                print (f"You will be going to an art show and it is located at: The Edmonton Expo ")
                print(money)
                x = input("Press enter to continue")
                os.system('cls' if os.name =='nt' else 'clear')
                print ("add more money?")
                ask = input("> ")
                if ask == "y" or ask == "yes":
                    add = float(input("How much? $"))
                    money = money + add
                else:
                    print ("ok")
            elif a3 == "c":
                money = money - 34.99
                money = round(money,2)
                print (f"You will be going to an concert and it is located at: Rogers Place")
                print(money)
                x = input("Press enter to continue")
                os.system('cls' if os.name =='nt' else 'clear')
                print ("add more money?")
                ask = input("> ")
                if ask == "y" or ask == "yes":
                    add = float(input("How much? $"))
                    money = money + add
                else:
                    print ("ok")
        if a2 == "c":
            money = money - 17.50
            print (f"Balance is ${money}")
            money = round(money,2)
            print (c)
            x = input("Press enter to continue")
            os.system('cls' if os.name =='nt' else 'clear')
            print (f"Balance is ${money}")
            print (enter)
            a3 = input("> ")
            if a3 == "a":
                money = money - 10
                money = round(money,2)
                movie = random.choice(["Boss baby 2", "Shrek", "The Bee Movie", "Toy Story 2"])
                print (f"The movie you are watching is: {movie} and it is located at: Cineplex")
                print(money)
                x = input("Press enter to continue")
                os.system('cls' if os.name =='nt' else 'clear')
                print ("add more money?")
                ask = input("> ")
                if ask == "y" or ask == "yes":
                    add = float(input("How much? $"))
                    money = money + add
                else:
                    print ("ok")
            elif a3 == "b":
                money = money - 17
                money = round(money,2)
                print (f"You will be going to an art show and it is located at: The Edmonton Expo")
                print(money)
                x = input("Press enter to continue")
                os.system('cls' if os.name =='nt' else 'clear')
                print ("add more money?")
                ask = input("> ")
                if ask == "y" or ask == "yes":
                    add = float(input("How much? $"))
                    money = money + add
                else:
                    print ("ok")
            elif a3 == "c":
                money = money - 34.99
                money = round(money,2)
                print (f"You will be going to an concert and it is located at: Rogers Place")
                print(money)
                x = input("Press enter to continue")
                os.system('cls' if os.name =='nt' else 'clear')
                print ("add more money?")
                ask = input("> ")
                if ask == "y" or ask == "yes":
                    add = float(input("How much? $"))
                    money = money + add
                else:
                    print ("ok")
    elif a1 == "c":
        money = money - 10.60
        money = round(money,2)
        print (f"Balance is ${money}")
        x = input("Press enter to continue")
        os.system('cls' if os.name =='nt' else 'clear')
        print(money)
        print (fit)
        a2 = input("> ")
        if a2 == "a":
            money = money - 25.78
            money = round(money,2)
            print (f"Balance is ${money}")
            print (a)
            x = input("Press enter to continue")
            os.system('cls' if os.name =='nt' else 'clear')
            print (f"Balance is ${money}")
            print (enter)
            a3 = input("> ")
            if a3 == "a":
                money = money - 10
                money = round(money,2)
                movie = random.choice(["Boss baby 2", "Shrek", "The Bee Movie", "Toy Story 2"])
                print (f"The movie you are watching is: {movie} and it is located at: Rogers Place")
                print(money)
                x = input("Press enter to continue")
                os.system('cls' if os.name =='nt' else 'clear')
                print ("add more money?")
                ask = input("> ")
                if ask == "y" or ask == "yes":
                    add = float(input("How much? $"))
                    money = money + add
                else:
                    print ("ok")
            elif a3 == "b":
                money = money - 17
                money = round(money,2)
                print (f"You will be going to an art show and it is located at: The Edmonton Expo Centre")
                print(money)
                x = input("Press enter to continue")
                os.system('cls' if os.name =='nt' else 'clear')
                print ("add more money?")
                ask = input("> ")
                if ask == "y" or ask == "yes":
                    add = float(input("How much? $"))
                    money = money + add
                else:
                    print ("ok")
            elif a3 == "c":
                money = money - 34.99
                money = round(money,2)
                print (f"You will be going to an concert and it is located at: Rogers Place")
                print(money)
                x = input("Press enter to continue")
                os.system('cls' if os.name =='nt' else 'clear')
                print ("add more money?")
                ask = input("> ")
                if ask == "y" or ask == "yes":
                    add = float(input("How much? $"))
                    money = money + add
                else:
                    print ("ok")
        if a2 == "b":
            money = money - 0
            print (f"Balance is ${money}")
            money = round(money,2)
            print (b)
            x = input("Press enter to continue")
            os.system('cls' if os.name =='nt' else 'clear')
            print (f"Balance is ${money}")
            print (enter)
            a3 = input("> ")
            if a3 == "a":
                money = money - 10
                money = round(money,2)
                movie = random.choice(["Boss baby 2", "Shrek", "The Bee Movie", "Toy Story 2"])
                print (f"The movie you are watching is: {movie} and it is located at: Cineplex")
                print(money)
                x = input("Press enter to continue")
                os.system('cls' if os.name =='nt' else 'clear')
                print ("add more money?")
                ask = input("> ")
                if ask == "y" or ask == "yes":
                    add = float(input("How much? $"))
                    money = money + add
                else:
                    print ("ok")
            elif a3 == "b":
                money = money - 17
                money = round(money,2)
                print (f"You will be going to an art show and it is located at: The Edmonton Expo Centre ")
                print(money)
                x = input("Press enter to continue")
                os.system('cls' if os.name =='nt' else 'clear')
                print ("add more money?")
                ask = input("> ")
                if ask == "y" or ask == "yes":
                    add = float(input("How much? $"))
                    money = money + add
                else:
                    print ("ok")
            elif a3 == "c":
                money = money - 34.99
                money = round(money,2)
                print (f"You will be going to an concert and it is located at: Rogers Place")
                print(money)
                x = input("Press enter to continue")
                os.system('cls' if os.name =='nt' else 'clear')
                print ("add more money?")
                ask = input("> ")
                if ask == "y" or ask == "yes":
                    add = float(input("How much? $"))
                    money = money + add
                else:
                    print ("ok")
        if a2 == "c":
            money = money - 17.50
            print (f"Balance is ${money}")
            money = round(money,2)
            print (c)
            x = input("Press enter to continue")
            os.system('cls' if os.name =='nt' else 'clear')
            print (f"Balance is ${money}")
            print (enter)
            a3 = input("> ")
            if a3 == "a":
                money = money - 10
                money = round(money,2)
                movie = random.choice(["Boss baby 2", "Shrek", "The Bee Movie", "Toy Story 2"])
                print (f"The movie you are watching is: {movie} and it is located at: Cineplex")
                print(money)
                x = input("Press enter to continue")
                os.system('cls' if os.name =='nt' else 'clear')
                print ("add more money?")
                ask = input("> ")
                if ask == "y" or ask == "yes":
                    add = float(input("How much? $"))
                    money = money + add
                else:
                    print ("ok")
            elif a3 == "b":
                money = money - 17
                money = round(money,2)
                print (f"You will be going to an art show and it is located at: The Edomton Expo Centre ")
                print(money)
                x = input("Press enter to continue")
                os.system('cls' if os.name =='nt' else 'clear')
                print ("add more money?")
                ask = input("> ")
                if ask == "y" or ask == "yes":
                    add = float(input("How much? $"))
                    money = money + add
                else:
                    print ("ok")
            elif a3 == "c":
                money = money - 34.99
                money = round(money,2)
                print (f"You will be going to an concert and it is located at: Rogers Place")
                print(money)
                x = input("Press enter to continue")
                os.system('cls' if os.name =='nt' else 'clear')
                print ("add more money?")
                ask = input("> ")
                if ask == "y" or ask == "yes":
                    add = float(input("How much? $"))
                    money = money + add
                else:
                    print ("ok")
else:
    print ("password is wrong")
print ("Thank you for using the Daily Life Planner. Hope you enjoyed")