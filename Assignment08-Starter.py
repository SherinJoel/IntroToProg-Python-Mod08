# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# <SSherin>,<9.2.2021>,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #
# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []
listData = []
strChoice = ' '

class Product:
    """Stores data about a product:
    properties:
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price
    methods:
    def __init__(self,product_name): --> Constructor
    def __str__(self):

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        <Ssherin>,<9.4.2021>,Modified code to complete assignment 8
    """

    # Constructor
    def __init__(self, product_name):
        # Attributes
        self._product_name = product_name

    # Properties
    # getter and setter for product_name
    @property
    def product_name(self):
        return self._product_name

    @product_name.setter
    def product_name(self, value):
        self._product_name = value

    # getter and setter for product_price
    @property
    def product_price(self):
        return self._product_price

    @product_price.setter
    def product_price(self, value):
        try:
            self._product_price = float(value)
        except ValueError as e:
            raise Exception("Product price cannot be string")

    def __str__(self):
        return 'ProductName: ' + self._product_name + ', ProductPrice ' + str(self._product_price)


# Data -------------------------------------------------------------------- #
# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        <SSherin>,<9.5.2021>,Modified code to complete assignment 8
    """

    def read_data_from_file(self, file_name, list_of_product_objects):
        """ Reads data from a text file into a list of product objects

                :param file_name: (string) with name of text file:
                :param list_of_product_objects: (list) you want filled with file data:
                :return: (list_of_product_objects) of project objects
                """
        list_of_product_objects.clear() # Clear current data
        try:
            file = open(file_name, "r")
            for productStr in file:
                listData = productStr.split(',')  # Splits the string into a list
                product_name = listData[0]
                product_price = listData[1]
                product = Product(product_name)  # Creating an object for Product class
                product.product_price = product_price # Calling setter for product_price
                list_of_product_objects.append(product)
            file.close()
        except FileNotFoundError as e:
            print(e, e.__doc__, type(e), sep='\n')
        return list_of_product_objects

    def save_data_to_file(self, file_name, list_of_product_objects):
        """ Save data from list to file

                :param file_name: (string) with name of text file:
                :param list_of_product_objects: (list) from which data is read and written to file:
                :return: nothing
                """
        file = open(file_name, "w")
        for product in list_of_product_objects:
            file.write(product._product_name + "," + str(product._product_price) + "\n")
        file.close()
        print("Data saved to file")


# Processing  ------------------------------------------------------------- #
# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ Performs Input and Output tasks

    methods:
        def print_menu_Tasks(self):
        def input_menu_choice(self):
        def print_current_data_in_list(self, list_of_product_objects):
        def add_data_to_list(self, list_of_product_objects):

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        <SSherin>,<9.5.2021>,Modified code to complete assignment 8
    """
    def print_menu_Tasks(self):
        """  Display a menu of choices to the user

                :return: nothing
                """
        print('''
                Menu of Options
                1) Display current data in the list of product objects
                2) Add data to the list of product objects
                3) Save Data to File and exit    
                ''')
        print()  # Add an extra line for looks

    def input_menu_choice(self):
        """ Gets the menu choice from a user

                :return: string
                """
        choice = input("Which option would you like to perform? [1 to 3] - ").strip()
        print()  # Add an extra line for looks
        return choice


    def print_current_data_in_list(self, list_of_product_objects):
        """ Shows the current product objects in the list

                :param list_of_product_objects: (list) of product objects you want to display
                :return: nothing
                """
        print("\n******* The current Products are: *******")
        for product in list_of_product_objects:
            print(product)  # __str__() method run when the print() function is called
            # print(product.product_name, product.product_price)
        print("*******************************************")
        print()  # Add an extra line for looks

    def add_data_to_list(self, list_of_product_objects):
        """ Getting product from user and adding it into a list of product objects

                :param list_of_product_objects: list to which new product object is appended
                :return: (list) of product objects:
                """
        try:
            product_name = input("Enter the product name: ")
            product_price = input("Enter the product price: ")
            product = Product(product_name)  # Creating an object for Product class
            product.product_price = product_price # Calling the setter for product_price
            list_of_product_objects.append(product)
        except Exception as e:
            print(e)
        return list_of_product_objects

# Main Body of Script  ---------------------------------------------------- #
fp = FileProcessor() # Creating an instance for FileProcessor class
io1 = IO() # Creating an instance for IO class

# Load data from file into a list of product objects when script starts
lstOfProductObjects = fp.read_data_from_file(strFileName, lstOfProductObjects)

while (True):

    # Show user a menu of options
    io1.print_menu_Tasks()

    # Get user's menu option choice
    strChoice = io1.input_menu_choice()

    # Show user current data in the list of product objects
    if strChoice == '1':
        io1.print_current_data_in_list(lstOfProductObjects)

    # Let user add data to the list of product objects
    if strChoice == '2':
        lstOfProductObjects = io1.add_data_to_list(lstOfProductObjects)
        continue  # to show the menu

    # Let user save current data to file and exit program
    if strChoice == '3':
        fp.save_data_to_file(strFileName, lstOfProductObjects)
        break
