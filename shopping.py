import json

# Class representing Product
class Product:
    # Method to create the object (Constructor)
    def __init__(self, name, price, quantity, ean, brand):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.ean = ean
        self.brand = brand

    # Method to return data of each product as json format
    def to_json(self):

        return {"name" : self.name,
                "price" : self.price,
                "quantity": self.quantity,
                "ean" : self.ean,
                "brand" : self.brand
                }

# Class representing Clothing wihch is a subclass of class Product
class Clothing(Product):
    def __init__(self, name, price, quantity, ean, brand, size, material):
        super().__init__(name, price, quantity, ean, brand)
        self.size = size
        self.material = material

    # Method to return data of each product as json format
    def to_json(self):
        return { "name" : self.name,
                "price" : self.price,
                "quantity": self.quantity,
                "ean" : self.ean,
                "brand" : self.brand,
                "size" : self.size,
                "material" : self.material 
                }

# Class representing Food wihch is a subclass of class Product        
class Food(Product):
    def __init__(self, name, price, quantity, ean, brand, expiry_date, gluten_free, suitable_for_vegans):
        super().__init__(name, price, quantity, ean, brand)
        self.expiry_date = expiry_date
        self.gluten_free = gluten_free
        self.suitable_for_vegans = suitable_for_vegans

    # Method to return data of each product as json format
    def to_json(self):
        return { "name" : self.name,
                "price" : self.price,
                "quantity": self.quantity,
                "ean" : self.ean,
                "brand" : self.brand,
                "expiry_date" : self.expiry_date,
                "gluten_free" : self.gluten_free,
                "suitable_for_vegans": self.suitable_for_vegans
                } 

# Class representing Laptop wihch is a subclass of class Product        
class Laptop(Product):
    def __init__(self, name, price, quantity, ean, brand, processor, operating_system, storage_capacity):
        super().__init__(name, price, quantity, ean, brand)
        self.processor = processor
        self.operating_system = operating_system
        self.storage_capacity = storage_capacity

    # Method to return data of each product as json format
    def to_json(self):
        return { "name" : self.name,
                "price" : self.price,
                "quantity": self.quantity,
                "ean" : self.ean,
                "brand" : self.brand,
                "processor" : self.processor,
                "operating_system" : self.operating_system,
                "storage_capacity": self.storage_capacity
                }

# class representing ShoppingCart, which is a container of products in a shopping session.
# This class is a subclass of classes Food, Clothing and Laptop in order to get the attributes and methods from them.
class ShoppingCart(Food, Clothing, Laptop):
    # Constructor - creating the container
    def __init__(self):
        self.__container = []
    # Method for adding a product to the cart
    def addProduct(self, p):
        self.__container.append(p)
    # Method for removing a product from the cart
    def removeProduct(self, p):
        self.__container.remove(p)
    # Method for obtaining the conents of the cart, returned in alphabetical order of product name
    def getContents(self):
        self.__container = sorted(self.__container, key=lambda x: x.name, reverse=False)
        return self.__container
    # Method for changing the quantity of product p to the quantity q        
    def changeProductQuantity(self, p, q):
        for x in self.__container:
            if  x.ean == p.ean:
                x.quantity = q

# Function for user input and validation of name, price, quantity, ean, brand 
def InputAndValidationProduct():
    # Input name
    name = input("Insert its name: ")
                
    while True:
        # Input price 
        price = input("Insert its price (£): ")
        # If the price input is not float then it prints a message
        try:
            price = float(price)
            break
        except:
            print("Enter a float number please!")                
    
    while True:
        # Input quantity 
        quantity = input("Insert its quantity: ")
        try:
            quantity = int(quantity)
            break
        except ValueError:
            print("Enter an integer number please!")

    while True:
        # Input ean
        ean = input("Insert its EAN code: ")
        # Assigned the allowed values to a string (values 0-9)
        allowed = "0123456789"
        # If the the characters of the ean match with the allowed characters and its length is 13
        if all(c in allowed for c in ean) and len(ean) == 13:
            # If the list is not empty
            if len(theList.getContents()) != 0:
                isUnique = True
                for x in theList.getContents():
                    # If a product in the list has the same ean code as the user's input it prints a message
                    if x.ean == ean:
                        isUnique = False
                        print("The EAN code already exists in the shopping list!")
                # If the ean code input is uniqe then it is fine
                if isUnique:
                    break
                else:
                    continue

            else:
                break
        else:
            print("The sequence of the EAN code should be length of 13 and contain numbers from 0 to 9")
    # Input brand
    brand = input("Insert its brand: ")
    # return the variables name, price, quantity, ean, brand
    return name, price, quantity, ean, brand

print("The program has started")
# print("Insert your next command (H for help):")
terminated = False
# Creating a ShoppingCart object (the container) 
theList = ShoppingCart()
while not terminated:
    # input command
    c = input("Type your next command (H for help): ")
    # T - the script terminates
    if c == 'T':
        terminated = True
    # A - allows the user to add a product to the car
    elif c == 'A':
        print("Adding a new product: ")
        # input product type
        product_type = input("Instert its type: ")
        product_validation = False
        # While product types insert are valid
        while not product_validation:
            if product_type == "Clothing":
                product_validation = True
                # Calling the function InputAndValidationProduct and getting the name, price, quantity, ean, brand
                name, price, quantity, ean, brand = InputAndValidationProduct()
                # input size
                size = input("Insert its size: ")
                # Input material
                material = input("Insert its material: ")
                # Creating a Clothing object - the product
                product = Clothing(name, price, quantity, ean, brand, size, material)
                # Adding the product in the container
                theList.addProduct(product)

                print("The product {} has been added to the cart.".format(product.name))
                print("The cart contains {} products.".format(len(theList.getContents())))

            elif product_type == "Food":
                product_validation = True
                # Calling the function InputAndValidationProduct and getting the name, price, quantity, ean, brand
                name, price, quantity, ean, brand = InputAndValidationProduct()
                expiry_date = input("Insert its expiry date (DD-MM-YYYY): ")

                # Asking the user to input the gluten-free. If it is not True or False it asks again
                while True:
                    gluten_free = input("Insert if it is gluten-free (True or False): ")
                    if gluten_free in ("True", "False"):
                        break
                    else:
                        print("Please inseart True or False")

                # Asking the user to input the suitable_for_vegans. If it is not True or False it asks again
                while True:
                    suitable_for_vegans = input("Insert if it is suitable for vegans (True or False): ")
                    if suitable_for_vegans in ("True", "False"):
                        break
                    else:
                        print("Please inseart True or False")

                # Creating a Food object - the product
                product = Food(name, price, quantity, ean, brand, expiry_date, gluten_free, suitable_for_vegans)
                # Adding the product in the container
                theList.addProduct(product)

                print("The product {} has been added to the cart.".format(product.name))
                print("The cart contains {} products.".format(len(theList.getContents())))

            elif product_type == "Laptop":
                product_validation = True
                 # Calling the function InputAndValidationProduct and getting the name, price, quantity, ean, brand               
                name, price, quantity, ean, brand = InputAndValidationProduct()
                # Input processor
                processor = input("Insert its processor name: ")
                # Input operating_system
                operating_system = input("Insert its operating system: ")

                #  Asking the user to input the storage_capacity. If it is not an intager, it asks again
                while True:
                    storage_capacity = input("Insert its storage capacity: ")
                    try:
                        storage_capacity = int(storage_capacity)
                        break
                    except ValueError:
                        print("Enter an integer number please!")

                # Creating a Laptop object - the product
                product = Laptop(name, price, quantity, ean, brand, processor, operating_system, storage_capacity)
                # Adding the product in the container
                theList.addProduct(product)

                print("The product {} has been added to the cart.".format(product.name))
                print("The cart contains {} products.".format(len(theList.getContents())))

            else:
                # If the product_type is not valid then it asks the user again to enter one of the option
                product_type = input("Please enter a valid type of product!(Clothing, Food, Laptop): ")

    elif c == 'R':
        # If the length of the container is not empty
        if len(theList.getContents()) != 0:
            # In order to be sure the correct product will be removed, I am asking the user to enter both
            # name and ean code of the product. This is because names are not unique
        
            # input the name of the product to be removed
            desiredProductName = input("Please insert the name of the product you want to remove: ")
            # input the ean code of the product to be removed
            desiredProductEanCode = input("Please insert the EAN code of the product you want to remove: ")
            
            productNotInList = True
            for p in theList.getContents():
                # If a product matches the user's inputs then the product will be removed from the cart
                if (p.name == desiredProductName) and (p.ean == desiredProductEanCode):
                    theList.removeProduct(p)
                    productNotInList = False

                    print("The product {} has been removed from the cart.".format(p.name))
                    print("The cart contains {} products.".format(len(theList.getContents())))

            # If a product does not match the user's inputs then a message is printed
            if productNotInList:
                print("There is not such product in the shopping list!")     

        else:
            # if the list is empty, it prints a message
            print("The shoping list is empty!")
    # S - prints out a formatted text summary of the cart
    elif c == 'S':
        print("This is the total of expenses:")
        count = 1
        total = 0
        for x in theList.getContents():
            # printing the names, quantities, partial sums per product type
            print(count,"-", x.quantity, "*", x.name, "=", x.quantity * x.price)
            # Calculating the Total of all products
            total += x.quantity * x.price
            count+=1
        print("Total = £{}".format(total))

    # Q - the user can directly change the quantity of a product already present in the cart.
    elif c == 'Q':
        # If the length of the container is not empty
        if len(theList.getContents()) != 0:
            # In order to be sure the correct product's quantity will be changed, I am asking the user to enter both
            # name and ean code of the product. This is because names are not unique     

            # Input the name of the product
            desiredProductName = input("Please insert the name of the product you want to change the quantity of: ")
            # Input the ean code of the product
            desiredProductEanCode = input("Please insert the EAN code of the product you want to change the quantity of: ")
           
            while True:
                # input the new quantity of the product
                q = input("Insert the new quantity of the product {} with EAN code {}: ".format(desiredProductName, desiredProductEanCode))
                # if the input is not an integer then it asks again
                try:
                    q = int(q)
                    break
                except ValueError:
                    print("Enter an integer number please!")
            
            productNotInList = True
            for p in theList.getContents():
                # If a product matches the user's inputs then the product's quantity will be changed to the new one
                if (p.name == desiredProductName) and (p.ean == desiredProductEanCode):
                    theList.changeProductQuantity(p,q)
                    productNotInList = False

            # If a product does not match the user's inputs then a message is printed
            if productNotInList:
                print("There is not such product in the shopping list!")     

        else:
            # If the cart is empty then a message is printed
            print("The shoping list is empty!")
    # E - generates a summary of the cart as a JSON-formatted data dump, printed to the console
    elif c == 'E':
        #  Creating a list to add all products' json format representations
        listOfJson = []
        for p in theList.getContents():
            # Appending each products' json format representations in the list
            listOfJson.append(p.to_json())

        # Using module json to generate json dumps for each product
        jsonDump = json.dumps(listOfJson, indent=4)
        print(jsonDump)

    #  H - a request for help from the user
    elif c == 'H':
        print("The program supports the following commands:")
        print(" [A] - Add a new product to the cart")
        print(" [R] - Remove a product from the cart")
        print(" [S] - Print a summary of the cart")
        print(" [Q] - Change the quantity of a product")
        print(" [E] - Export a JSON version of the cart")
        print(" [T] - Terminate the program")
        print(" [H] - List the supported commands")

    else:
        # If the user's command is not recognised, a message is printed
        print("Command not recognised. Please try again!")

print("Goodbye")



