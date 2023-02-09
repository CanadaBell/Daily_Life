#dictionaries
food = {
    "a": {
        "Item": "Cheese burger with fries",
        "Cost": 9.59,
    },
    "b": {
        "Item": "Poutine",
        "Cost": 5.99,
    },
    "c": {
        "Item": "Hotdog (ketchup + mustard) and chips (original)",
        "Cost": 10.60,
    }, 
}
fit = {
    "a": {
        "Item": "Yoga class",
        "Cost": 25.78,
    },
    "b": {
        "Item": "5 km walk in the river valley",
        "Cost": 0.00,
    },
    "c": {
        "Item": "Swimming",
        "Cost": 17.50,
    }, 
}
fit_o = {
    "a": "You will be going to a Yoga Class at the Clareview Community Recreation Center. It starts at 4:30 pm and lasts 60 minutes.", 
    "b": "You will sttart at Hermitage Park and walk on the trail to Rundle Park.",
    "c": "You will go to a pool at the Clareview Community Recreation Center and do laps around the pool.",
}
enter = {
    "a": {
        "Item": "Movie",
        "Cost": 10.00,
    },
    "b": {
        "Item": "See art",
        "Cost": 17.00,
    },
    "c": {
        "Item": "Go to a concert",
        "Cost": 34.99,
    }, 
}
enter_o = {
    "a": "You will be watching Shrek 2 at Cineplex", 
    "b": "You will be going to an art show and it is located at: The Edmonton Expo Centre",
    "c": "You will be going to an concert and it is located at: Rogers Place",
}
#functions
def food_c():
    for fo_id, fo_info in food.items():
        print(f"\n[{fo_id}]")
    
        for key in fo_info:
            print(key + ':', fo_info[key])
def fit_c():
    for fi_id, fi_info in fit.items():
        print(f"\n[{fi_id}]")
    
        for key in fi_info:
            print(key + ':', fi_info[key])
def ent_c():
    for ent_id, ent_info in enter.items():
        print(f"\n[{ent_id}]")
    
        for key in ent_info:
            print(key + ':', ent_info[key])
import os
def clear():
    os.system('cls' if os.name =='nt' else 'clear')