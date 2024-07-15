districts = ["Select a District to visit Hotels:", "1: Namakkal", "2: Erode", "3: Salem", "4: Karur", "5: Thiruppur"]
hotels = {
    "Namakkal": ["1: Annapoorna Hotel", "2: Sangam Hotel", "3: Sakthi Hotel"],
    "Erode": ["1: Vasantha Hotel", "2: Sree Devi Hotel", "3: Arun Hotel"],
    "Salem": ["1: Shenbaga Hotel", "2: Emerald Hotel", "3: Sona Hotel"],
    "Karur": ["1: Nandini Hotel", "2: Sakthi Hotel", "3: Sree Hotel"],
    "Thiruppur": ["1: Kovai Hotel", "2: Sree Devi Hotel", "3: Arun Hotel"]
}

food_menu = {
    "Annapoorna Hotel": [("1 | Idli  Sambar",        30),
                         ("2 | Masala  Dosa",        40),
                         ("3 | Pongal      ",        25),
                         ("4 | Poori Masala",        35),
                         ("5 | Vada  Sambar",        30),
                         ("6 | Apple juice ",        60)],
                          
    "Sangam Hotel":     [("1 | Chicken Biryani ",   150),
                         ("2 | Mutton Biryani  ",   180),
                         ("3 | Veg Biryani     ",   100),
                         ("4 | Tandoori Chicken",   200),
                         ("5 | Butter Naan     ",    20),
                         ("6 | Orange juice ",       30)],
                     
    "Sakthi Hotel":     [("1 | Chettinad Chicken",  180),
                         ("2 | Mutton Curry     ",  200),
                         ("3 | Veg Curry        ",  120),
                         ("4 | Parotta (set)    ",   35),
                         ("5 | Appam            ",   20),
                         ("6 | lemon soda juice ",   20)],
                         
    "Vasantha Hotel":   [("1 | Rava Dosa     ",      35),
                         ("2 | Onion Uthappam",      30),
                         ("3 | Podi Idli     ",      25),
                         ("4 | Vada          ",      20),
                         ("5 | Kesari Bath   ",      30),
                         ("6 | Apple juice ",        60)],

                         
    "Sree Devi Hotel":  [("1 | Chicken 65    ",     150),
                         ("2 | Mutton Sukka  ",     180),
                         ("3 | Veg Manchurian",     100),
                         ("4 | Naan          ",      25),
                         ("5 | Rumali Roti   ",      20),
                         ("6 | grape juice   ",      60)],
                         
    "Arun Hotel":       [("1 | Chicken Tikka     ", 180),
                         ("2 | Mutton Seekh Kebab", 200),
                         ("3 | Paneer Tikka      ", 120),
                         ("4 | Garlic Naan       ",  20),
                         ("5 | Kulfi             ",  30),
                         ("6 | Mojito  (lime)    ",  60)],
                         
    "Shenbaga Hotel":   [("1 | Chicken Dum Biryani", 180),
                         ("2 | Mutton Dum Biryani ", 200),
                         ("3 | Veg Dum Biryani    ", 120), 
                         ("4 | Chicken Tikka      ", 200),
                         ("5 | Naan (set)         ",  50),
                         ("6 | Panner soda        ",  25)],
                         
    "Emerald Hotel":    [("1 | Chicken Curry",      150),
                         ("2 | Mutton Curry ",      180),
                         ("3 | Veg Curry    ",      100),
                         ("4 | Parotta      ",       15), 
                         ("5 | Appam        ",       20),
                         ("6 | Panner soda  ",       25)],
                      
    "Sona Hotel":       [("1 | Chicken Lollipop",   150),
                         ("2 | Mutton Chukka   ",   180),
                         ("3 | Veg Manchurian  ",   100),
                         ("4 | Butter Naan     ",    20),
                         ("5 | Gulab Jamun     ",    30),
                         ("6 | Panner soda     ",    25)],
                   
    "Nandini Hotel":    [("1 | Chicken Biryani ",   130),
                         ("2 | Mutton Biryani  ",   180),
                         ("3 | Veg Biryani     ",   100),
                         ("4 | Tandoori Chicken",   200),
                         ("5 | Rumali Roti     ",    30),
                         ("6 | Panner soda     ",    25)],
                      
    "Sree Hotel":       [("1 | Chettinad Chicken",  180),
                         ("2 | Mutton Curry     ",  200), 
                         ("3 | Veg Curry        ",  120),
                         ("4 | Parotta          ",   15),
                         ("5 | Appam            ",   20),
                         ("6 | Panner soda      ",   25)],
                   
    "Kovai Hotel":      [("1 | Chicken 65    ",     150),
                         ("2 | Mutton Sukka  ",     180),
                         ("3 | Veg Manchurian",     100),
                         ("4 | Naan          ",      25),
                         ("5 | Kulfi         ",      30),
                         ("6 | Panner soda   ",      25)]
}

def display_hotels(district):
    print(f"Hotels in {district}:")
    print()
    for hotel in hotels[district]:
        print(hotel)
        print()

def display_food_menu(hotel):
    print(f"Food Menu at {hotel}:")
    print()
    for item, price in food_menu[hotel]:
        print(f"{item} - ₹{price}")
        print()

def calculate_bill(order):
    total = 0
    order_details = []
    for item, price, quantity in order:
        item_total = price * quantity
        total += item_total
        order_details.append((item, price, quantity, item_total))
    gst = total * 0.18
    total_with_gst = total + gst
    return order_details, total, gst, total_with_gst

def main():
    while True:
        for item in districts:
            print(item)
        choice = input("Enter your choice (1-5) or 'q' to quit: ")
        print()
        if choice.lower() == 'q':
            print("Exiting...")
            break
        elif choice in ['1', '2', '3', '4', '5']:
            district = districts[int(choice)].split(":")[1].strip()
            display_hotels(district)
            hotel_choice = input("Enter the hotel number (1-3) or 'b' to go back: ")
            print()
            if hotel_choice.lower() == 'b':
                continue
            elif hotel_choice in ['1', '2', '3']:
                hotel = hotels[district][int(hotel_choice) - 1].split(":")[1].strip()
                display_food_menu(hotel)
                order = []
                while True:
                    item_choice = input("Make your order (1-6) or 'b' to exit: ")
                    if item_choice.lower() == 'b':
                        break
                    elif item_choice in ['1', '2', '3', '4', '5', '6']:
                        item, price = food_menu[hotel][int(item_choice) - 1]
                        quantity = int(input(f"Enter quantity  {item}: "))
                        order.append((item, price, quantity))
                        print(f"{item} added to the order.")
                        print()
                    else:
                        print("Invalid choice. Please try again.")

                order_details, total, gst, total_with_gst = calculate_bill(order)
                print()
                print()
                print("*Computer generated Bill*")
                print() 
                print("__________________________________________________")
                print()
                print(f"                  **{hotel}**                    ")
                print(f"                       {district}                ")
                print("__________________________________________________")
                print(f"\n                   Order Summary               ")
                print("------+++-------------------+++--------+++-----+++")
                print(f"{'Item':<30} {'Quantity':<10} {'Price':<10}")
                print("------+++-------------------+++--------+++-----+++")
                print()
                for item, price, quantity, item_total in order_details:
                    print(f"{item:<30} {quantity:<10} ₹ {item_total:<10}")
                print()
                print("--------------------------------------------------")
                print(f"\nTotal         :                         ₹ {total:.2f}")
                print(f"GST (18%)     :                         ₹ {gst:.2f}")
                print("--------------------------------------------------")
                print("--------------------------------------------------")
                print(f"Total with GST:                         ₹ {total_with_gst:.2f}")
                print()
                print()
                print()
                print("                     THANK YOU                    ")
                print("                Please visit again !!!            ")
                print("                   *************                  ")
                print()
                print()
                print()
                print("We value your feedback! Please rate your experience:")
                rating = int(input("Enter a rating (1-5): "))
                feedback = input("Enter your feedback (optional): ")

                print("\nThank you for your feedback!")
                print(f"Rating: {rating} out of 5")
                if feedback:
                    print(f"Feedback: {feedback}")

                print("\nHave a great day!")
                print()
                print()

            else:
                print("Invalid choice. Please try again.")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()