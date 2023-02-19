# A Python program that will read from the text file inventory.txt and perform the following on the data, 
# to prepare for presentation to your managers:

# from tabulate import tabulate # didn't use tabulate

#========The beginning of the class==========
class Shoe:
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

# return the cost of the shoe in this method.
    def get_cost(self):
        return self.cost
        
# return the quantity of the shoes.
    def get_quantity(self):
        return self.quantity

# returns a string representation of a class.
    def __str__(self):
        return f"Shoe: \tcountry = {self.country} \n\tcode = {self.code} \n\tproduct = {self.product} \n\tcost = {self.cost} \n\tquantity = {self.quantity}"

#=============Shoe list===========

shoe_list = []

#==========Functions outside the class==============

# read the data from file inventory.txt then create a shoes object with this data and append this object into the shoes list.
# One line in this file represent data to create one object of shoes. You must use the try-except in this function
# for error handling. Remember to skip the first line using your code.

def read_shoes_data():
    try:
        with open('inventory.txt', "r") as file:
            lines = file.readlines()
            for line in lines:
                if line.startswith("country"):
                    continue
                country, code, product, cost, quantity = line.strip("\n").split(",")
                cost = float(cost)
                quantity = int(quantity)
                shoe_list.append(Shoe(country, code, product, cost, quantity))          
    except Exception as error:
            print("An error occurred:", error)
    return ""

#-------------------------------------------------------------------------------------------------------

# This function will allow a user to capture data about a shoe and use this data to create a shoe object
# and append this object inside the shoe list. 

def capture_shoes():
    if len(shoe_list) == 0:
        read_shoes_data()

    country = input("What is the shoe country? ")
    code = input("What is the shoe code? ") 
    product = input("What is the product? ")
    while True:
        try:
            cost = float(input("What is the cost? ")) 
            break
        except ValueError:
            print("That was not a valid number. ")
    while True:
        try:
            quantity = int(input("What is the item quantity? "))
            break
        except ValueError:
            print("That was not a valid number. ") 
    shoe_list.append(Shoe(country, code, product, cost, quantity)) 

# not on task but I'm assuming best to add to the txt file:

    try:
        with open('inventory.txt', "w") as file:
            file.write("country, code, product, cost, quantity\n")
            for shoe in shoe_list:
                file.write(f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n")
        return("\nShoe has been added to record.")
    except Exception as e:
        print(f"An error occurred: {e}")


#-------------------------------------------------------------------------------------------------------

# This function will iterate over the shoes list and print the details of the shoes returned from the __str__
# function. Optional: you can organise your data in a table format by using Python’s tabulate module.

def view_all():
    if len(shoe_list) == 0:
        read_shoes_data()

    for shoe in shoe_list:
        print(shoe)
    return ""

#-------------------------------------------------------------------------------------------------------

# function will find the shoe object with the lowest quantity, which is the shoes that need to be re-stocked. 

def re_stock():
    if len(shoe_list) == 0:
        read_shoes_data()

    low_stock = []
    for i in shoe_list:
        if len(low_stock) == 0:
            low_stock.append(i)
        elif i.quantity < low_stock[0].quantity:
            low_stock = [i]
        elif i.quantity == low_stock[0].quantity:
            low_stock.append(i)
    print("The lowest stock item(s) is:")
    for line in low_stock:
        print(line)

# Ask the user if they want to add this quantity of shoes and then update it.
    while True:
        restock = input("Would you like to restock shoe(s)? (yes/no) ").lower()
        if restock == "no":
            return None
        if restock == "yes":
            while True:
                try:
                    new_quanity = int(input("What is the new quantity for the shoe(s)? "))
                    break
                except ValueError:
                    new_quanity = int(input("That was not a valid number. What is the new quantity for the shoe(s)? "))

# need to swap in the new quantity to the correct line in the original task list- do check to find the matching line
            for line in shoe_list:
                for shoe in low_stock:
                    if line.country == shoe.country and line.code == shoe.code and line.product == shoe.product:
                        line.quantity = new_quanity
                 
# This quantity should be updated on the file for this shoe.
            try:
                with open('inventory.txt', "w") as file:
                    file.write("country, code, product, cost, quantity\n")
                    for shoe in shoe_list:
                        file.write(f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n")

                return "Shoe(s) restocked."
            except Exception as e:
                print(f"An error occurred: {e}")
        else:
            print("Invalid option")
            continue

#-------------------------------------------------------------------------------------------------------

# This function will search for a shoe from the list using the shoe code and return this object so that it will be printed.
def search_shoe(code):
    if len(shoe_list) == 0:
        read_shoes_data()

    result = None
    for shoe in shoe_list:
        if shoe.code == code:
            result = shoe
            break
    if result is None:
        return f"Shoe with code {code} not found in inventory."
    return result

    # for shoe in shoe_list:
    #     if shoe.code == code:
    #         return shoe
    # return None

#-------------------------------------------------------------------------------------------------------

# This function will calculate the total value for each item.
# Please keep the formula for value in mind: value = cost * quantity.
# Print this information on the console for all the shoes.
def value_per_item():
    if len(shoe_list) == 0:
        read_shoes_data()

    for shoe in shoe_list:
        value = shoe.cost * shoe.quantity
        print(f"Shoe code {shoe.code} has a stock value of {value}")
    return ""

#-------------------------------------------------------------------------------------------------------

# Write code to determine the product with the highest quantity and print this shoe as being for sale.
def highest_qty():
    if len(shoe_list) == 0:
        read_shoes_data()

    high_stock = []
    for i in shoe_list:
        if len(high_stock) == 0:
            high_stock.append(i)
        elif i.quantity > high_stock[0].quantity:
            high_stock = [i]
        elif i.quantity == high_stock[0].quantity:
            high_stock.append(i)
    print("The following stock item(s) is now on sale:")
    for line in high_stock:
        print(line)
    return ""

#==========Main Menu=============

while True:
    print("\nWelcome!\n")
    print("\t1. Present shoe data")
    print("\t2. Input shoe")
    print("\t3. Restock shoe")
    print("\t4. Search shoe") 
    print("\t5. Get total stock values")   
    print("\t6. Generate SALE")   
    print("\t0. Quit\n")

    while True:
        try:
            option = int(input("Choose an option: "))
            break
        except ValueError:
            print("Please enter a valid number: ")
    
    if option == 1:
        print(view_all())

    elif option == 2:
        print(capture_shoes())

    elif option == 3:
        print(re_stock())

    elif option == 4:
        code = input("What is the code of the shoe you want to search? ")
        print(search_shoe(code))

    elif option == 5:
        print(value_per_item())

    elif option == 6:
        print(highest_qty())

    elif len(shoe_list) == 0:       
        print("Please select option 1 to load most recent data before proceeding.")


    elif option == 0:
        print("Exiting inventory.")
        break

    else:
        print("Invalid option, try again.")




# didn't get round to testing this
# pip install tabulate

# data = [    ["South Africa", "SKU44386", "Air Max 90", 2300, 20],
#     ["China", "SKU90000", "Jordan 1", 3200, 50],
#     ["Vietnam", "SKU63221", "Blazer", 1700, 19],
#     ["United States", "SKU29077", "Cortez", 970, 60],
# ]

# headers = ["Country", "Code", "Product", "Cost", "Quantity"]

# print(tabulate(data, headers, tablefmt="fancy_grid"))
