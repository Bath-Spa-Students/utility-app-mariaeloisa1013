import time

def effects(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)

# ice cream menu with categories: ice cream cones, ice cream cakes, cream milk shakes
menu = {
    'Cones': {
        'N1': {'flavor': 'CookieCreem Cone', 'price': 8.50, 'stock': 20},
        'N2': {'flavor': 'Mangie Cone', 'price': 8.50, 'stock': 15},
        'N3': {'flavor': 'MintChoc Cone', 'price': 8.50, 'stock': 15},
        'N4': {'flavor': 'Rainbow Berry Cone', 'price': 9.50, 'stock': 15},
        'N5': {'flavor': 'Choco Nyom Cone', 'price': 8.50, 'stock': 20},
    },
    'Cakes': {
        'K1': {'flavor': 'CookieCreem Cake', 'price': 45.50, 'stock': 20},
        'K2': {'flavor': 'Mangie Cake', 'price': 45.50, 'stock': 15},
        'K3': {'flavor': 'MintChoc Cake', 'price': 45.50, 'stock': 15},
        'K4': {'flavor': 'Rainbow Berry Cake', 'price': 49.99, 'stock': 15},
        'K5': {'flavor': 'Choco Nyom Cake', 'price': 45.50, 'stock': 20},
    },
    'Shakies': {
        'S1': {'flavor': 'Grizz CookieCreem Shake', 'price': 25.00, 'stock': 15},
        'S2': {'flavor': 'Mangie Mania Shake', 'price': 25.00, 'stock': 15},
        'S3': {'flavor': 'NyomNyom Signature Shake', 'price': 23.00, 'stock': 25},
    },
}

# welcome message
print("\n\t\tWelcome to NYOMNYOM🍦 !!\n\t everyone's favorite ice cream machine\n")

while True:
    while True:
        # customers choose desired category
        effects("\nWhat are your cravings for today? \n\t🍦Cones, Cakes, Shakies? ")
        choice = input().capitalize()
        if choice in menu:
            break
        else:
            print("\nPlease enter either 'Cones', 'Cakes', or 'Shakies'")

    # display the menu of chosen category
    print(f"\nHere's our list of Nyom {choice}:")
    for key, item in menu[choice].items():
        print(f"\t {key}: {item['flavor']} ====== Price: AED{item['price']} || Stock: {item['stock']}")

    # users input code
    while True:
        effects("🍦Enter the Nyom Code: ")
        code = input().capitalize()
        if code in menu[choice]:
            purchased = menu[choice][code]
            print(f"\n\t⚪️1 {purchased['flavor']} for AED {purchased['price']}")
            # food pairing suggestion
            if choice in ['Cones', 'Cakes']:
                suggestion = menu['Shakies']['S3']  
                break
            elif choice in ['Shakies']:
                suggestion = menu['Cones']['N2']
                break
        else: 
            print ("\t pls enter a valid code ^ ^\n")

    # adding order suggestions
    while True:
        effects(f"\n A {suggestion['flavor']} would look good with your {purchased['flavor']} for only AED {suggestion['price']}\n Would you like to add that to your purchase? ")
        recommendation = input()
        if recommendation == 'yes':
            print(f"\n\t⚪️1 {purchased['flavor']} for AED {purchased['price']}")       
            print(f"\t⚪️1 {suggestion['flavor']} for AED {suggestion['price']}\n")
            purchased['price'] += suggestion['price']
            break
        elif recommendation == 'no':
            print(f"\n\t⚪️1 {purchased['flavor']} for AED {purchased['price']}\n")
            break
        else:
            print("\n\t\tplease enter 'yes' or 'no'")
                                
    while True:
        try:
            # displaying total amount to be paid
            effects(f"Your total will be AED{purchased['price']}\n🍦Pay: AED")
            cash = float(input())
            price = purchased['price']
            change = price - cash
            if cash >= price:
                change = cash - price
                # item dispension + collection of change
                print(f"\n\t\t\tserving....\n\t⚪️1 {purchased['flavor']} for AED {purchased['price']}")       
                print(f"\t⚪️1 {suggestion['flavor']} for AED {suggestion['price']}\n")
                effects(f"\nyour nyomnyoms are dispensing !! please retreive your change of AED {change:.2f}")
                # option for last minute additional orders
                additional = input("\nWould you like to check other nyomnyoms? ")
                if additional == 'yes':
                    break    
                elif additional == 'no':
                    # the end
                    effects(f"\n\t\tThank you for having NYOMNYOM <3\n")
                    exit ()
                else:
                    print("please enter 'yes' or 'no'")
            else: 
                # display lacking amount from the amount entered
                print(f"\nYou are lacking AED{change}. Please try again")
        except ValueError:
            print("\nAn error has occurred. Please enter a valid amount.")