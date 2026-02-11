# ---------------------------------
# -----------Definitions-----------
# ---------------------------------

class Pantry:
    """Pantry Manager Class:
        Manages Pantry and Shopping Lists"""

    def __init__(self, name):
        """Initialization Function
            defines name of Pantry (Default: 'Home')"""
        self._pantry_list = []  # starts with empty pantry
        self._shopping_list = []  # starts with empty shopping list
        pass

    def load_from_file(self, filename):
        # needs input verification, clean user interface options, data validations

        """Save all foods in pantry to a file """
        pass

    def save_to_file(self, filename):
        # needs input verification, clean user interface options, data validations

        """Load foods from a file into Pantry"""
        pass

    def printout_pantry(self, method):
        # needs input verification, clean user interface options, data validations

        """User Chooses a Method which allows multiple types of printout of Pantry to be delivered
        Options include By Quantity, Alphabetically, and By Category(Eventually)"""
        pass

    def printout_shopping_list(self, method):
        # needs input verification, clean user interface options, data validations

        """User Chooses a Method which allows multiple types of printout of Shopping List to be delivered
            Options include By Chronology, Alphabetically, and By Category(Eventually)"""

        pass

    ##############
    # All Modification Methods need to save a filename_1
    # and previous_copy_name upon full verification
    # and completion
    ##############
    def create_item(self):
        # track common typos in most common food words and add mistake-correction
        """Takes User input as temp variables and then
            runs 'Food' __init__ function creating new Food Items
            adds them to pantry_list """

        current_item_num = len(self._pantry_list)
        while True:
            category = input(
                "What type of food are we creating today?: \n(basic, produce, fruit, meat, dairy, frozen, bakery, condiment, spice, snack, shelf stable) \n('EXIT' to quit): ").lower()

            if category == "exit":
                break

            if category in ["", "basic"]:
                name = input("What is this food's name?: ")
                while True:
                    qty_input = input("How many are there?: ")
                    try:
                        quantity = int(qty_input)
                        break
                    except ValueError:
                        print("Invalid input. Please enter a number.")

                while True:
                    perish_input = input("Is it perishable? (Y/N): ").lower()
                    if perish_input == "y":
                        perishable = True
                        break
                    elif perish_input == "n":
                        perishable = False
                        break
                    else:
                        print("Invalid input, please enter Y or N.")

                while True:
                    days_input = input("How many days until it expires?: ")
                    try:
                        days_left = int(days_input)
                        break
                    except ValueError:
                        print("Invalid input. Please enter a number.")

                item_obj = Food(name, quantity, perishable, days_left)
                print()
                item_obj.define()

                final_confirmation_input = input("Is this correct (Y/N)").lower()
                if final_confirmation_input == "y":
                    self._pantry_list.append(item_obj)
                    break
                elif final_confirmation_input == "n":
                    print("Many Apologies, Please Try Again")
                else:
                    print("Invalid Input, Please Try Again")

            elif category in ["produce"]:
                name = input("What is this food's name?: ")
                while True:
                    qty_input = input("How many are there?: ")
                    try:
                        quantity = int(qty_input)
                        break
                    except ValueError:
                        print("Invalid input. Please enter a number.")

                while True:
                    perish_input = input("Is it perishable? (Y/N): ").lower()
                    if perish_input == "y":
                        perishable = True
                        break
                    elif perish_input == "n":
                        perishable = False
                        break
                    else:
                        print("Invalid input, please enter Y or N.")

                while True:
                    days_input = input("How many days until it expires?: ")
                    try:
                        days_left = int(days_input)
                        break
                    except ValueError:
                        print("Invalid input. Please enter a number.")

                storage_location = input("Where are you storing it?")
                while True:
                    purchase_enter_bool = input("Do you want to enter a purchase date? (Y/N)").lower()
                    if purchase_enter_bool == "y":
                        purchase_date = input("When did you purchase this?")
                        break
                    else:
                        purchase_date = None
                        break

                while True:
                    notes_enter_bool = input("Do you want to enter any additional information? (Y/N)").lower()
                    if notes_enter_bool == "y":
                        notes = input("Type Notes Here: ")
                        break
                    else:
                        notes = ""
                        break

                item_obj = Fresh_Produce(name, quantity, perishable, days_left, storage_location, purchase_date, notes)
                print()
                item_obj.define()

                final_confirmation_input = input("Is this correct (Y/N)").lower()
                if final_confirmation_input == "y":
                    self._pantry_list.append(item_obj)
                    break
                elif final_confirmation_input == "n":
                    print("Many Apologies, Please Try Again")
                else:
                    print("Invalid Input, Please Try Again")

            elif category in ["fruit"]:
                name = input("What is this food's name?: ")
                while True:
                    qty_input = input("How many are there?: ")
                    try:
                        quantity = int(qty_input)
                        break
                    except ValueError:
                        print("Invalid input. Please enter a number.")

                while True:
                    perish_input = input("Is it perishable? (Y/N): ").lower()
                    if perish_input == "y":
                        perishable = True
                        break
                    elif perish_input == "n":
                        perishable = False
                        break
                    else:
                        print("Invalid input, please enter Y or N.")

                while True:
                    days_input = input("How many days until it expires?: ")
                    try:
                        days_left = int(days_input)
                        break
                    except ValueError:
                        print("Invalid input. Please enter a number.")

                storage_location = input("Where are you storing it?")
                while True:
                    purchase_enter_bool = input("Do you want to enter a purchase date? (Y/N)").lower()
                    if purchase_enter_bool == "y":
                        purchase_date = input("When did you purchase this?")
                        break
                    else:
                        purchase_date = None
                        break

                while True:
                    ripen_enter = input("How ripe is it? (Under/Ripe/Over)").lower()
                    if ripen_enter not in ["under", "ripe", "over"]:
                        print("Invalid Enter. How ripe is it? (Under/Ripe/Over)")
                    else:
                        ripeness = ripen_enter
                        break

                while True:
                    cut_input = input("Has this been Cut/Sliced? (Y/N)").lower()
                    if cut_input == "y":
                        is_cut = True
                        break
                    elif cut_input == "n":
                        is_cut = False
                        break
                    else:
                        print("Invalid Input. Has this been Cut/Sliced? (Y/N)?")

                while True:
                    washed_input = input("Has this been Washed? (Y/N)").lower()
                    if washed_input == "y":
                        washed = True
                        break
                    elif washed_input == "n":
                        washed = False
                        break
                    else:
                        print("Invalid Input. Has this been Washed? (Y/N)")

                while True:
                    notes_enter_bool = input("Do you want to enter any additional information? (Y/N)").lower()
                    if notes_enter_bool == "y":
                        notes = input("Type Notes Here: ")
                        break
                    else:
                        notes = ""
                        break

                item_obj = Fruit_Produce(name, quantity, perishable, days_left, storage_location, purchase_date,
                                         ripeness, is_cut, washed, notes)
                print()
                item_obj.define()

                final_confirmation_input = input("Is this correct (Y/N)").lower()
                if final_confirmation_input == "y":
                    self._pantry_list.append(item_obj)
                    break
                elif final_confirmation_input == "n":
                    print("Many Apologies, Please Try Again")
                else:
                    print("Invalid Input, Please Try Again")

            elif category in ["meat"]:
                name = input("What is this food's name?: ")
                while True:
                    qty_input = input("How many are there?: ")
                    try:
                        quantity = int(qty_input)
                        break
                    except ValueError:
                        print("Invalid input. Please enter a number.")

                while True:
                    perish_input = input("Is it perishable? (Y/N): ").lower()
                    if perish_input == "y":
                        perishable = True
                        break
                    elif perish_input == "n":
                        perishable = False
                        break
                    else:
                        print("Invalid input, please enter Y or N.")

                while True:
                    days_input = input("How many days until it expires?: ")
                    try:
                        days_left = int(days_input)
                        break
                    except ValueError:
                        print("Invalid input. Please enter a number.")

                storage_location = input("Where are you storing it?")
                while True:
                    purchase_enter_bool = input("Do you want to enter a purchase date? (Y/N)").lower()
                    if purchase_enter_bool == "y":
                        purchase_date = input("When did you purchase this?")
                        break
                    else:
                        purchase_date = None
                        break

                while True:
                    meat_input = input("What kind of Meat is it?")
                    if meat_input == "":
                        meat_input = "unspecified"
                        break
                    else:
                        meat_type = meat_input
                        break

                while True:
                    froz_input = input("Is this Frozen? (Y/N)").lower()
                    if froz_input == "y":
                        frozen = True
                        break
                    elif froz_input == "n":
                        frozen = False
                        break
                    else:
                        print("Invalid Input. Is this Frozen? (Y/N)")

                while True:
                    use_today_input = input("Does this need to be used Today? (Y/N)").lower()
                    if use_today_input == "y":
                        use_today = True
                    elif use_today_input == "n":
                        use_today = False
                    else:
                        print("Invalid Input. Does this need to be used Today? (Y/N)")

                while True:
                    notes_enter_bool = input("Do you want to enter any additional information? (Y/N)").lower()
                    if notes_enter_bool == "y":
                        notes = input("Type Notes Here: ")
                        break
                    else:
                        notes = ""
                        break

                item_obj = Raw_Meat(name, quantity, perishable, days_left, meat_type, storage_location, purchase_date,
                                    frozen, use_today, notes)
                print()
                item_obj.define()

                final_confirmation_input = input("Is this correct (Y/N)").lower()
                if final_confirmation_input == "y":
                    self._pantry_list.append(item_obj)
                    break
                elif final_confirmation_input == "n":
                    print("Many Apologies, Please Try Again")
                else:
                    print("Invalid Input, Please Try Again")

            elif category in ["dairy"]:
                name = input("What is this food's name?: ")
                while True:
                    qty_input = input("How many are there?: ")
                    try:
                        quantity = int(qty_input)
                        break
                    except ValueError:
                        print("Invalid input. Please enter a number.")

                while True:
                    perish_input = input("Is it perishable? (Y/N): ").lower()
                    if perish_input == "y":
                        perishable = True
                        break
                    elif perish_input == "n":
                        perishable = False
                        break
                    else:
                        print("Invalid input, please enter Y or N.")

                while True:
                    days_input = input("How many days until it expires?: ")
                    try:
                        days_left = int(days_input)
                        break
                    except ValueError:
                        print("Invalid input. Please enter a number.")

                storage_location = input("Where are you storing it?")
                while True:
                    purchase_enter_bool = input("Do you want to enter a purchase date? (Y/N)").lower()
                    if purchase_enter_bool == "y":
                        purchase_date = input("When did you purchase this?")
                        break
                    else:
                        purchase_date = None
                        break

                while True:
                    dairy_input = input("What type of Dairy is it? (e.g. Cheese, Milk, Yogurt, etc)")
                    if dairy_input == "":
                        dairy_type = "unspecified"
                        break
                    else:
                        dairy_type = dairy_input
                        break

                while True:
                    openness_input = input("Has it been opened? (Y/N)").lower()
                    if openness_input == "y":
                        is_open = True
                        open_date = input("When was it opened?")
                        break
                    elif openness_input == "n":
                        is_open == False
                        open_date = None
                        break
                    else:
                        print("Invalid Input. Has this been opened?")

                while True:
                    notes_enter_bool = input("Do you want to enter any additional information? (Y/N)").lower()
                    if notes_enter_bool == "y":
                        notes = input("Type Notes Here: ")
                        break
                    else:
                        notes = ""
                        break

                item_obj = Dairy(name, quantity, perishable, days_left, dairy_type, storage_location,
                                         purchase_date, open_date, is_open, notes)
                print()
                item_obj.define()

                final_confirmation_input = input("Is this correct (Y/N)").lower()
                if final_confirmation_input == "y":
                    self._pantry_list.append(item_obj)
                    break
                elif final_confirmation_input == "n":
                    print("Many Apologies, Please Try Again")
                else:
                    print("Invalid Input, Please Try Again")

            elif category in ["frozen"]:
                name = input("What is this food's name?: ")
                while True:
                    qty_input = input("How many are there?: ")
                    try:
                        quantity = int(qty_input)
                        break
                    except ValueError:
                        print("Invalid input. Please enter a number.")

                while True:
                    perish_input = input("Is it perishable? (Y/N): ").lower()
                    if perish_input == "y":
                        perishable = True
                        break
                    elif perish_input == "n":
                        perishable = False
                        break
                    else:
                        print("Invalid input, please enter Y or N.")

                while True:
                    days_input = input("How many days until it expires?: ")
                    try:
                        days_left = int(days_input)
                        break
                    except ValueError:
                        print("Invalid input. Please enter a number.")

                storage_location = input("Where are you storing it?")
                while True:
                    purchase_enter_bool = input("Do you want to enter a purchase date? (Y/N)").lower()
                    if purchase_enter_bool == "y":
                        purchase_date = input("When did you purchase this?")
                        break
                    else:
                        purchase_date = None
                        break

                while True:
                    frozen_type_input = input("wWhat is being Frozen? (e.g. Veg, Ready-To-Eat, Stock, etc.)")
                    if frozen_type_input == "":
                        frozen_type = "unspecified"
                        break
                    else:
                        frozen_type = frozen_type_input
                        break
                while True:
                    at_home_input = input("Was this frozen at home? (Y/N)").lower()
                    if at_home_input == "y":
                        frozen_at_home = True
                        break
                    elif at_home_input == "n":
                        frozen_at_home = False
                        break
                    else:
                        print("Invalid Input. Was this frozen at home? (Y/N)")

                while True:
                    openness_input = input("Has this been opened? (Y/N)").lower()
                    if openness_input == "y":
                        is_open = True
                        open_date = input("When was this opened?")
                        break
                    elif openness_input == "n":
                        is_open = False
                        open_date = None
                        break
                    else:
                        print("Invalid Input. Has this been opened? (Y/N)")

                while True:
                    notes_enter_bool = input("Do you want to enter any additional information? (Y/N)").lower()
                    if notes_enter_bool == "y":
                        notes = input("Type Notes Here: ")
                        break
                    else:
                        notes = ""
                        break

                item_obj = Other_Frozen(name, quantity, perishable, days_left, frozen_type, storage_location,
                                        purchase_date, open_date, frozen_at_home, is_open, notes)
                print()
                item_obj.define()

                final_confirmation_input = input("Is this correct (Y/N)").lower()
                if final_confirmation_input == "y":
                    self._pantry_list.append(item_obj)
                    break
                elif final_confirmation_input == "n":
                    print("Many Apologies, Please Try Again")
                else:
                    print("Invalid Input, Please Try Again")

            elif category in ["bakery"]:
                name = input("What is this food's name?: ")
                while True:
                    qty_input = input("How many are there?: ")
                    try:
                        quantity = int(qty_input)
                        break
                    except ValueError:
                        print("Invalid input. Please enter a number.")

                while True:
                    perish_input = input("Is it perishable? (Y/N): ").lower()
                    if perish_input == "y":
                        perishable = True
                        break
                    elif perish_input == "n":
                        perishable = False
                        break
                    else:
                        print("Invalid input, please enter Y or N.")

                while True:
                    days_input = input("How many days until it expires?: ")
                    try:
                        days_left = int(days_input)
                        break
                    except ValueError:
                        print("Invalid input. Please enter a number.")

                storage_location = input("Where are you storing it?")
                while True:
                    purchase_enter_bool = input("Do you want to enter a purchase date? (Y/N)").lower()
                    if purchase_enter_bool == "y":
                        purchase_date = input("When did you purchase this?")
                        break
                    else:
                        purchase_date = None
                        break

                while True:
                    baked_input = input("What type of Baked Good is it? (e.g. Bread, Pastry, Pasta, etc.)")
                    if baked_input == "":
                        baked_type = "unspecified"
                        break
                    else:
                        baked_type = baked_input
                        break

                while True:
                    ready_input = input("Is this Ready-To-Eat? (Y/N)").lower()
                    if ready_input == "y":
                        ready_to_eat = True
                        break
                    elif ready_input == "n":
                        ready_to_eat = False
                        break
                    else:
                        print("Invalid Input. Is this Ready-To-Eat? (Y/N)")

                    while True:
                        homemade_input = input("Is this Homemade? (Y/N)").lower()
                        if homemade_input == "y":
                            homemade = True
                            break
                        elif homemade_input == "n":
                            homemade = False
                            break
                        else:
                            print("Invalid Input. Is this Homemade? (Y/N)")

                while True:
                    notes_enter_bool = input("Do you want to enter any additional information? (Y/N)").lower()
                    if notes_enter_bool == "y":
                        notes = input("Type Notes Here: ")
                        break
                    else:
                        notes = ""
                        break

                item_obj = Baked_Goods(name, quantity, perishable, days_left, baked_type, storage_location,
                                       purchase_date, ready_to_eat, homemade, notes)
                print()
                item_obj.define()

                final_confirmation_input = input("Is this correct (Y/N)").lower()
                if final_confirmation_input == "y":
                    self._pantry_list.append(item_obj)
                    break
                elif final_confirmation_input == "n":
                    print("Many Apologies, Please Try Again")
                else:
                    print("Invalid Input, Please Try Again")

            elif category in ["condiment", "spice"]:
                name = input("What is this food's name?: ")
                while True:
                    qty_input = input("How many are there?: ")
                    try:
                        quantity = int(qty_input)
                        break
                    except ValueError:
                        print("Invalid input. Please enter a number.")

                while True:
                    perish_input = input("Is it perishable? (Y/N): ").lower()
                    if perish_input == "y":
                        perishable = True
                        break
                    elif perish_input == "n":
                        perishable = False
                        break
                    else:
                        print("Invalid input, please enter Y or N.")

                while True:
                    days_input = input("How many days until it expires?: ")
                    try:
                        days_left = int(days_input)
                        break
                    except ValueError:
                        print("Invalid input. Please enter a number.")

                storage_location = input("Where are you storing it?")
                while True:
                    purchase_enter_bool = input("Do you want to enter a purchase date? (Y/N)").lower()
                    if purchase_enter_bool == "y":
                        purchase_date = input("When did you purchase this?")
                        break
                    else:
                        purchase_date = None
                        break

                while True:
                    cond_type_input = input(
                        "What type of Condiment/Spice is this? (Sauce, Dried Herb, Ground Spice, Etc.)")
                    if cond_type_input == "":
                        condiment_type = "unspecified"
                        break
                    else:
                        condiment_type = cond_type_input
                        break

                    while True:
                        openness_input = input("Has this been Opened? (Y/N)").lower()
                        if openness_input == "y":
                            is_open = True
                            open_date = input("When was this opened?")
                            break
                        elif openness_input == "n":
                            is_open = False
                            open_date = None
                            break
                        else:
                            print("Invalid Input. Has this been opened? (Y/N)")

                while True:
                    notes_enter_bool = input("Do you want to enter any additional information? (Y/N)").lower()
                    if notes_enter_bool == "y":
                        notes = input("Type Notes Here: ")
                        break
                    else:
                        notes = ""
                        break

                item_obj = Condiment_Spice(name, quantity, perishable, days_left, storage_location, purchase_date,
                                           open_date, is_open, condiment_type, notes)
                print()
                item_obj.define()

                final_confirmation_input = input("Is this correct (Y/N)").lower()
                if final_confirmation_input == "y":
                    self._pantry_list.append(item_obj)
                    break
                elif final_confirmation_input == "n":
                    print("Many Apologies, Please Try Again")
                else:
                    print("Invalid Input, Please Try Again")

            elif category in ["snacks", "shelf stable"]:
                name = input("What is this food's name?: ")
                while True:
                    qty_input = input("How many are there?: ")
                    try:
                        quantity = int(qty_input)
                        break
                    except ValueError:
                        print("Invalid input. Please enter a number.")

                while True:
                    perish_input = input("Is it perishable? (Y/N): ").lower()
                    if perish_input == "y":
                        perishable = True
                        break
                    elif perish_input == "n":
                        perishable = False
                        break
                    else:
                        print("Invalid input, please enter Y or N.")

                while True:
                    days_input = input("How many days until it expires?: ")
                    try:
                        days_left = int(days_input)
                        break
                    except ValueError:
                        print("Invalid input. Please enter a number.")

                storage_location = input("Where are you storing it?")
                while True:
                    purchase_enter_bool = input("Do you want to enter a purchase date? (Y/N)").lower()
                    if purchase_enter_bool == "y":
                        purchase_date = input("When did you purchase this?")
                        break
                    else:
                        purchase_date = None
                        break

                while True:
                    snack_input = input("What kind of snack/shelf stable item is this?")
                    if snack_input == "":
                        snack_type = "unspecified"
                        break
                    else:
                        snack_type = snack_input
                        break

                while True:
                    flavor_input = input("What flavor is this Snack? (leave blank for 'unspecified')")
                    if flavor_input == "":
                        flavor = "unspecified"
                        break
                    else:
                        flavor = flavor_input
                        break

                while True:
                    request_input = input("Was this Requested by someone? (Y/N)").lower()
                    if request_input == "y":
                        requested_by = input("By Whom was it Requested?")
                        break
                    elif request_input == "n":
                        requested_by = None
                        break
                    else:
                        print("Invalid Input. Was this Requested by someone? (Y/N)")

                while True:
                    openness_input = input("Has this been opened? (Y/N)").lower()
                    if openness_input == "y":
                        is_open = True
                        open_date = input("When was this opened?")
                        break
                    elif openness_input == "n":
                        is_open = False
                        open_date = None
                        break
                    else:
                        print("Invalid Input. Has this been opened? (Y/N)")

                while True:
                    notes_enter_bool = input("Do you want to enter any additional information? (Y/N)").lower()
                    if notes_enter_bool == "y":
                        notes = input("Type Notes Here: ")
                        break
                    else:
                        notes = ""
                        break

                item_obj = Snacks_Shelf_Stable(name, quantity, perishable, days_left, snack_type, storage_location,
                                               purchase_date, open_date, is_open, flavor, requested_by, notes)
                print()
                item_obj.define()

                final_confirmation_input = input("Is this correct (Y/N)").lower()
                if final_confirmation_input == "y":
                    self._pantry_list.append(item_obj)
                    break
                elif final_confirmation_input == "n":
                    print("Many Apologies, Please Try Again")
                else:
                    print("Invalid Input, Please Try Again")

            else:
                print(
                    "Improper Selection... Please Try Again: \n(basic, produce, fruit, meat, dairy, frozen, bakery, condiment, spice, snack, shelf stable) \n('EXIT' to quit)")

    def add_to_pantry(self, item):
        """Adds an Existing Food Object to Pantry List"""
        pass

    def remove_item(self, method):
        # Include duplicates to have a secondary verification before final removal
        # needs input verification, clean user interface options, data validations
        # track common typos in common food words and add mistake-correction
        """User Chooses Method -> program takes user inputs depending
            on method-choice and removes Food items from Pantry List"""
        pass

    def use_item(quantity):
        # Include duplicates to have a secondary verification before final usage modification
        # needs input verification, clean user interface options, data validations
        # track common typos in common food words and add mistake-correction
        """User chooses a Food item to subtract a quantity from
            If user uses all items in inventory, displays a prompt
            informing user and removing it from the Pantry List"""
        pass

    def modify_item(self):
        # Include duplicates to have a secondary verification before final modification
        # needs input verification, clean user interface options, data validations
        # track common typos in common food words and add mistake-correction
        """User chooses a created Food Item to modify
            the Attributes of in the case of Errors or new Information"""
        pass

    def combine_items(self):
        # needs input verification, clean user interface options, data validations
        # track common typos in common food words and add mistake-correction
        # check Subclasses to verify what can be combined
        """Takes all non-perishable items with the same name and adds them all together
            creating a new item of the same name with the total sum as its new quantity
            deletes the previous iterations of the Food Item."""
        # This will be the one item/list modification method that doesn't make a zero-quantity version in the shopping list.
        pass

    def sort_items(self, inventory, method):
        # needs input verification, clean user interface options, data validations
        """Sorts Items in chosen inventory list
            by chosen method (Expiry, Quantity>, Quantity<, Category, Alphabet<)"""
        pass

    def find_item(self, name):
        # needs input verification, clean user interface options, data validations
        """Looks for an Item by Name and
            quickly displays information about it including Qty, Expiry, etc."""
        pass

    def save_and_exit(self):
        # needs input verification, clean user interface options, data validations
        """Asks User if they want to save,
            then either save and exits, or just exits without saving"""

        pass


class Food:
    """Main Class of Pantry Items
            All Items Are Foods..."""

    _days_left = 0

    def __init__(self, name, quantity, perishable, days_left):
        # may need to expand with more variables as project expands
        """Initialization Function
            Defines name, quantity, perishable = T/F"""
        self._name = name.capitalize()
        self._quantity = quantity
        self._perishable = perishable
        self._days_left = days_left
        self._category = self.__class__.__name__

    def time_day_passed(self):
        # can we make this self-running???
        """Counts time in 24hr quantities and removes a 'day' from
                Perishables day counter or adds a 'day' to expired label"""
        pass

    def is_expired(self):
        """Checks if Perishable is True
            and if days left are zero
            Adds a 'Check Me!' expired label with days since listed"""
        pass

    def update_quantity(self, amount):
        # needs input verification, clean user interface options, data validations
        """Updates an Item's Quantity
            preventing negative amounts stored and checking for absurdities"""
        pass

    def define(self):
        """Prints out all saved information on Food Item
                formatted for ease of reading"""
        if self._perishable == True:
            perish_var = "Y"
        else:
            perish_var = "N"
        print("--*--=" * 6)
        print("Basic Food Item Summary:")
        print(
            f"Name: {self._name}| Quantity: {self._quantity}| Perishable?: {perish_var}| Days Remaining: {self._days_left} ")

    def to_dict(self):
        """Return dictionary of this food item for saving."""
        # return {
        #    'name': self.name,
        #   'quantity': self.quantity,
        #   'perishable': self.perishable,
        #   'days_left': self.days_left
        # }
        pass

    @staticmethod
    def from_dict(data):
        """Static method to create Food from a dictionary."""
        # return Food(
        #   name=data['name'],
        #   quantity=data['quantity'],
        #   perishable=data['perishable'],
        #   days_left=data.get('days_left', 0)
        # )
        pass


class Fresh_Produce(Food):
    """Subclass of Food:
        Fresh Produce to be cooked
        e.g. Tomatoes, Zucchini, Onions, Potatoes"""

    # unique printouts for expired veggies mentioning mold or wilt
    # disallow duplicate merges
    def __init__(
            self,
            name,
            quantity=1,
            perishable=True,
            days_left=10,
            storage_location="fridge",
            purchase_date=None,
            notes="",
    ):
        """Initialization Program For Fresh Produce Subclass
            Sets up Unique Class Attributes in addition to
            running Super's __init__ for Base Attrib."""
        super().__init__(name, quantity, perishable, days_left)
        self._storage_location = storage_location
        self._purchase_date = purchase_date
        self._notes = notes
        self._category = self.__class__.__name__

    def define(self):
        """Prints Unique Produce Stats in addition
            to running Super's define for Base Attrib."""
        super().define()
        print("Produce Specific Item Summary:")
        print(f"Location: {self._storage_location}| Purchase Date: {self._purchase_date}")
        print(f"Additional Notes:{self._notes}")

    def is_expired(self):
        """Prints Unique Produce Spoilage Messages"""
        pass


class Fruit_Produce(Food):
    """Subclass of Food:
        Fresh Produce: Ready To Eat
        e.g. Strawberries, Apples, Bananas"""

    # no merging of duplicates
    def __init__(
            self,
            name,
            quantity=1,
            perishable=True,
            days_left=5,
            storage_location="Back Fridge",
            purchase_date=None,
            ripeness="Ripe",
            is_cut=False,
            washed=False,
            notes=""

    ):
        """Initialization Program for Fresh Fruits Subclass
            Sets up Unique Class Attributes in addition to
            running Super's __init__ for Base Attrib."""
        super().__init__(name, quantity, perishable, days_left)
        self._storage_location = storage_location
        self._purchase_date = purchase_date
        self._notes = notes
        self._ripeness = ripeness
        self._is_cut = is_cut
        self._washed = washed
        self._category = self.__class__.__name__

    def define(self):
        """Prints Unique Fruit Stats in addition
            to running Super's define for Base Attrib."""
        if self._washed == True:
            wash_var = "Y"
        else:
            wash_var = "N"
        if self._is_cut == True:
            cut_var = "Y"
        else:
            cut_var = "N"

        super().define()
        print("Fruit Specific Item Summary:")
        print(f"Location: {self._storage_location}| Purchase Date: {self._purchase_date}")
        print(f"Ripeness: {self._ripeness}| Washed?: {wash_var}| Cut?: {cut_var}")
        print(f"Additional Notes:{self._notes}")

    def ripeness_mover(self):
        """Takes Time Check and Changes _ripeness
            and _days_left on a Fruit Item"""
        pass

    def cut_fruit(self):
        """Changes _is_cut State from False to True"""
        pass

    def wash_fruit(self):
        """Changes _washed State from False to True"""
        pass

    def is_expired(self):
        """Prints Unique Fruit Spoilage Messages"""
        pass


class Raw_Meat(Food):
    """Subclass of Food:
    Meat to be cooked
    e.g. Pork Loin, Sausages, Chicken Thighs, Chorizo"""

    # only allow duplicate merging for frozen
    # storage_location tags
    def __init__(
            self,
            name,
            quantity=1,
            perishable=True,
            days_left=3,
            meat_type="unspecified",
            storage_location="Porch Fridge",
            purchase_date=None,
            frozen=False,
            use_today=False,
            notes=""
    ):
        """Initialization Program for Raw Meats
            Sets up Unique Class Attributes in addition to
            running Super's __init__ for Base Attrib"""
        super().__init__(name, quantity, perishable, days_left)
        if use_today == True:
            self._days_left = 1
        elif frozen == True:
            self._days_left = 60
        else:
            self._days_left = days_left
        self._meat_type = meat_type
        self._storage_location = storage_location
        self._purchase_date = purchase_date
        self._frozen = frozen
        self._use_today = use_today
        self._notes = notes
        self._category = self.__class__.__name__

    def define(self):
        """Prints Unique Meat Stats in addition
            to running Super's define for Base Attrib."""
        if self._frozen == True:
            froz_var = "Y"
        else:
            froz_var = "N"
        if self._use_today == True:
            use_today_var = "Y"
        else:
            use_today_var = "N"

        super().define()
        print("Meat Specific Item Summary:")
        print(f"Meat Type: {self._meat_type}")
        print(f"Location: {self._storage_location}| Purchase Date: {self._purchase_date}")
        print(f"Frozen?: {froz_var}| Use Today?: {use_today_var}")
        if self._use_today == True:
            print(f"{self._name} Needs to be used TODAY!")
        print(f"Additional Notes:{self._notes}")

    def is_expired(self):
        """Prints Unique Meat Spoilage Messages"""
        pass

    def make_use_today(self):
        """Changes _use_today State to True
            and _days_left to 1"""
        pass

    def freeze_meat(self):
        """Changes _frozen State to True
            and _days_left to 60"""
        pass


class Dairy(Food):
    """Subclass of Food:
        Milks, Cheeses, Yogurts, Etc
        e.g. Fresh Milk, Gouda, Greek Yogurt, Sour Cream"""

    # Unique Spoilage prints, and warnings for +-3days from spoiled
    # no merging of duplicate types
    def __init__(
            self,
            name,
            quantity=1,
            perishable=True,
            days_left=7,
            dairy_type="unspecified",
            storage_location="Fridge",
            purchase_date=None,
            open_date=None,
            is_open=False,
            notes=""
    ):
        """Initialization Program for Dairy
            Sets up Unique Class Attributes and
            runs Super's __init__ for Base Attrib."""

        super().__init__(name, quantity, perishable, days_left)
        if is_open == True and dairy_type != "Cheese":
            self._days_left = 3
        else:
            self._days_left = days_left
        self._dairy_type = dairy_type
        self._storage_location = storage_location
        self._purchase_date = purchase_date
        self._open_date = open_date
        self._is_open = is_open
        self._notes = notes
        self._category = self.__class__.__name__

    def define(self):
        """Prints Unique Dairy Stats in addition
            to running Super's define for Base Attrib."""
        if self._is_open == True:
            open_var = "Y"
        else:
            open_var = "N"

        super().define()
        print("Dairy Specific Item Summary:")
        print(f"Dairy Type: {self._dairy_type}")
        print(f"Location: {self._storage_location}| Purchase Date: {self._purchase_date}")
        print(f"Open? {open_var}| Open Date: {self._open_date}")
        print(f"Additional Notes:{self._notes}")

    def is_expired(self):
        """Prints Unique Dairy Spoilage Messages"""
        pass

    def open_dairy(self):
        # use same logic from dairy's __init__ here
        """Changes _is_open state to True and
            _days_left to 3 unless _dairy_type is not 'Cheese' """

    pass


class Other_Frozen(Food):
    """Subclass of Food:
        Premade Frozen Food, Frozen Veg, Frozen Additives
        e.g. Chicken Nuggets, Frozen Okra, Frozen Veg Stock"""

    # Double Check Nothing is Missing before Final Send.
    # Disallow Merging...
    def __init__(
            self,
            name,
            quantity=1,
            perishable=False,
            days_left=60,
            frozen_type="unspecified",
            storage_location="Freezer",
            purchase_date=None,
            open_date=None,
            frozen_at_home=False,
            is_open=False,
            notes=""

    ):
        """Initialization Program for Miscellaneous Frozen Foods
            Sets up Unique Frozen Attributes in addition to
           Running Super's __init__ for Base Attrib."""
        super().__init__(name, quantity, perishable, days_left)
        self._frozen_type = frozen_type
        self._purchase_date = purchase_date
        self._open_date = open_date
        self._storage_location = storage_location
        self._frozen_at_home = frozen_at_home
        self._is_open = is_open
        self._notes = notes
        self._category = self.__class__.__name__

    def define(self):
        """Prints Unique Frozen Stats in addition
            to running Supers define for Base Attrib."""
        if self._frozen_at_home == True:
            home_var = "Y"
        else:
            home_var = "N"
        if self._is_open == True:
            open_var = "Y"
        else:
            open_var = "N"

        super().define()
        print("Frozen Specific Item Summary:")
        print(f"Frozen Type: {self._frozen_type}| Home Freeze?: {home_var}")
        print(f"Location: {self._storage_location}| Purchase Date: {self._purchase_date}")
        print(f"Open?: {open_var}| Open Date: {self._open_date}")
        print(f"Additional Notes:{self._notes}")

    def is_expired(self):
        """Prints Unique Frozen Spoilage Messages"""
        pass


class Baked_Goods(Food):
    """Subclass of Food:
        Breads, Pastas, Pastries
        e.g. Baguettes, Linguini, Danishes"""

    # Unique spoilage prints
    # Only Merge Pasta, resetting days_left to new purchase_date
    # disallow other merges
    def __init__(
            self,
            name,
            quantity=1,
            perishable=True,
            days_left=7,
            baked_type="unspecified",  # e.g. "Bread" "Pastry" "Pasta"
            storage_location="Bread Basket",
            purchase_date=None,
            ready_to_eat=False,
            homemade=False,
            notes=""
    ):
        """Initialization Program for Baked Goods
            Sets up Unique Baked Attributes in addition to
            Running Super's __init__ for Base Attrib. """
        super().__init__(name, quantity, perishable, days_left)
        if baked_type == "bread":
            self._days_left = 7
            self._ready_to_eat = True
        elif baked_type == "pasta":
            self._days_left = 60
            self._ready_to_eat = False
        elif baked_type == "pastry":
            self._days_left = 3
            self._ready_to_eat = True
        else:
            self._days_left = days_left
            self._ready_to_eat = ready_to_eat
        self._storage_location = storage_location
        self._baked_type = baked_type
        self._purchase_date = purchase_date
        self._homemade = homemade
        self._notes = notes
        self._category = self.__class__.__name__

    def define(self):
        """Prints Unique Baked Goods Stats in addition
            to running Supers define for Base Attrib."""
        if self._ready_to_eat == True:
            ready_var = "Y"
        else:
            ready_var = "N"
        if self._homemade == True:
            home_var = "Y"
        else:
            home_var = "N"
        super().define()
        print("Bakery Specific Item Summary:")
        print(f"Baked Type: {self._baked_type}| Homemade? {home_var}| Ready to Eat?: {ready_var} ")
        print(f"Location: {self._storage_location}| Purchase Date: {self._purchase_date}")
        print(f"Additional Notes:{self._notes}")

    def is_expired(self):
        """Prints Unique Baked Spoilage Messages"""
        pass


class Condiment_Spice(Food):
    """Subclass of Food:
        Condiments, Spices, Herbs, Sauces
        e.g. Ketchup, Cumin, Thyme, P.S. Lemon-Herb Vin"""

    # unique prints for spoilage
    # allow merging of all items with resets on days_left to the new opened_date
    def __init__(
            self,
            name,
            quantity=1,
            perishable=False,
            days_left=None,
            storage_location="Pantry",
            purchase_date=None,
            open_date=None,
            is_open=False,
            condiment_type="unspecified",  # e.g. "dried spice" "sauce" "dried herb"
            notes=""
    ):
        """Initialization Program for Condiments and Spices
            Sets up Unique Condiment Attributes in addition to
            Running Super's __init__ for Base Attrib. """
        super().__init__(name, quantity, perishable, days_left)
        if is_open and (condiment_type == "dried spice" or condiment_type == "dried herb"):
            self._days_left = 180
        elif is_open and (condiment_type == "sauce"):
            self._days_left = 30
        self._storage_location = storage_location
        self._purchase_date = purchase_date
        self._open_date = open_date
        self._is_open = is_open
        self._condiment_type = condiment_type
        self._notes = notes
        self._category = self.__class__.__name__

    def define(self):
        """Prints Unique Condiment/Spice Stats in addition
            to running Super's define for Base Attrib."""
        if self._is_open == True:
            open_var = "Y"
        else:
            open_var = "N"
        super().define()
        print("Condiment/Spice Specific Item Summary:")
        print(f"Condiment/Spice?: {self._condiment_type}")
        print(f"Location: {self._storage_location}| Purchase Date: {self._purchase_date}")
        print(f"Open?: {open_var}| Open Date: {self._open_date}")
        print(f"Additional Notes:{self._notes}")

    def is_expired(self):
        """Prints Unique Condiment Spoilage Messages"""
        pass

    def open_spice(self):
        """Changes State of _is_open from False to True
            and adjusts _days_left by _condiment_type rules."""
        pass


class Snacks_Shelf_Stable(Food):
    """Subclass of Food:
        Snacks and Shelf Stable foods
        e.g. Muffins, Canned Pears, Ragu(Garlic)"""

    # high sugary candies and snacks 15-30, crackers 30-60,
    # nuts/jellies/jams/spreads 15-30 if opened, etc
    # Unique spoilage printouts
    # disallow merging open and unopened and differing flavors
    # will need special asks in create_item() to enable these
    def __init__(
            self,
            name,
            quantity=1,
            perishable=False,
            days_left=None,
            snack_type="unspecified",
            storage_location="Pantry",
            purchase_date=None,
            open_date=None,
            is_open=False,
            flavor="unspecified",
            requested_by="",
            notes=""
    ):
        """Initialization Program for Shelf Stable Foods
            Sets up Unique Shelf Stable Attributes in addition to
            Running Super's __init__ for Base Attrib. """
        super().__init__(name, quantity, perishable, days_left)
        # wait for input from wife before encoding logic for snack_type affecting days_left
        self._snack_type = snack_type
        self._storage_location = storage_location
        self._purchase_date = purchase_date
        self._open_date = open_date
        self._flavor = flavor
        self._is_open = is_open
        self._requested = requested_by
        self._notes = notes
        self._category = self.__class__.__name__

    def define(self):
        """Prints Unique Shelf Stable/Snack Stats in addition
        to running Super's define for Base Attrib."""
        if self._is_open == True:
            open_var = "Y"
        else:
            open_var = "N"

        super().define()
        print("Shelf Stable Specific Item Summary:")
        print(f"Food/Snack Type: {self._snack_type}| Flavor: {self._flavor}")
        print(f"Location: {self._storage_location}| Purchase Date: {self._purchase_date}")
        print(f"Open?: {open_var}| Open Date: {self._open_date}")
        print(f"Requested By: {self._requested}")
        print(f"Additional Notes:{self._notes}")

    def is_expired(self):
        """Prints Unique Snack Spoilage Messages"""
        pass

    def open_snack(self):
        """Changes is_opened state from False to True
            in addition to updating _days_left by _snack_type standards"""
        # Use same logic as __init__ here
        pass


def help_me():
    """Prints out all calls and needed variables within program"""
    pass


global_common_typos = {"example": "exampel", "tomato": "tomtao"}
# Look Up common typos for top 200 common food words in America (min 3 typos per word).
# learn about json to implement this

# ---------------------------------
# ----------Main Program-----------
# ---------------------------------

