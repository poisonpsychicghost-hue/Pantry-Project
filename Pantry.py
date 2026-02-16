# ---------------------------------
# -----------Definitions-----------
# ---------------------------------
from datetime import datetime

today = datetime.now().strftime("%Y-m-%d")  # Y-M-D '2025-04-24'


class Pantry:
    """Pantry Manager Class:
        Manages Pantry and Shopping Lists"""

    def __init__(self, name):
        """Initialization Function
            defines name of Pantry (Default: 'Home')"""
        self._pantry_list = []  # starts with empty pantry
        self._shopping_list = []  # starts with empty shopping list
        self._name = name

    def load_from_file(self, filename):
        """Loads saved Inventory Data from a saved .
            txt and imports it into Program for user applications"""
        # need to add ._shopping_list to save/load
        self._pantry_list = []
        pantry_filename = "pantry_" + filename
        shopping_filename = "shopping_" + filename
        with open(filename, "r") as file:
            for line in file:
                fields = line.strip().split(',')

                (category, name, quantity, perishable, days_left,
                 storage_location, purchase_date, notes, ripeness, is_cut, washed,
                 meat_type, dairy_type, frozen_type, baked_type, condiment_type, snack_type,
                 frozen, use_today, open_date, frozen_at_home, ready_to_eat, homemade, flavor, requested) = fields

                quantity = int(quantity)
                perishable = perishable == "True"
                days_left = int(days_left)
                is_cut = is_cut == "True"
                washed = washed == "True"
                frozen = frozen == "True"
                use_today = use_today == "True"
                ready_to_eat = ready_to_eat == "True"
                homemade = homemade == "True"
                is_open = open_date not in [None, "", "None"]
                frozen_at_home = frozen_at_home == "True"

                if category == "Fresh_Produce":
                    item_obj = Fresh_Produce(name, quantity, perishable, days_left, storage_location, purchase_date,
                                             notes)
                elif category == "Fruit_Produce":
                    item_obj = Fruit_Produce(name, quantity, perishable, days_left, storage_location, purchase_date,
                                             ripeness, is_cut, washed, notes)
                elif category == "Raw_Meat":
                    item_obj = Raw_Meat(name, quantity, perishable, days_left, meat_type, storage_location,
                                        purchase_date,
                                        frozen, use_today, notes)
                elif category == "Dairy":
                    item_obj = Dairy(name, quantity, perishable, days_left, dairy_type, storage_location, purchase_date,
                                     open_date, is_open, notes)
                elif category == "Other_Frozen":
                    item_obj = Other_Frozen(name, quantity, perishable, days_left, frozen_type, storage_location,
                                            purchase_date, open_date, frozen_at_home, is_open, notes)
                elif category == "Baked_Goods":
                    item_obj = Baked_Goods(name, quantity, perishable, days_left, baked_type, storage_location,
                                           purchase_date, ready_to_eat, homemade, notes)
                elif category == "Condiment_Spice":
                    item_obj = Condiment_Spice(name, quantity, perishable, days_left, storage_location, purchase_date,
                                               open_date, is_open, condiment_type, notes)
                elif category == "Snacks_Shelf_Stable":
                    item_obj = Snacks_Shelf_Stable(name, quantity, perishable, days_left, snack_type, storage_location,
                                                   purchase_date, open_date, is_open, flavor, requested, notes)
                else:
                    item_obj = Food(name, quantity, perishable, days_left)

                self._pantry_list.append(item_obj)
        print(f"Shopping List loaded from {shopping_filename}")

        with open(shopping_filename, "r") as file:
            for line in file:
                fields = line.strip().split(',')

                (category, name, quantity, perishable, days_left,
                 storage_location, purchase_date, notes, ripeness, is_cut, washed,
                 meat_type, dairy_type, frozen_type, baked_type, condiment_type, snack_type,
                 frozen, use_today, open_date, frozen_at_home, ready_to_eat, homemade, flavor, requested) = fields

                quantity = int(quantity)
                perishable = perishable == "True"
                days_left = int(days_left)
                is_cut = is_cut == "True"
                washed = washed == "True"
                frozen = frozen == "True"
                use_today = use_today == "True"
                ready_to_eat = ready_to_eat == "True"
                homemade = homemade == "True"
                is_open = open_date not in [None, "", "None"]
                frozen_at_home = frozen_at_home == "True"

                if category == "Fresh_Produce":
                    item_obj = Fresh_Produce(name, quantity, perishable, days_left, storage_location, purchase_date,
                                             notes)
                elif category == "Fruit_Produce":
                    item_obj = Fruit_Produce(name, quantity, perishable, days_left, storage_location, purchase_date,
                                             ripeness, is_cut, washed, notes)
                elif category == "Raw_Meat":
                    item_obj = Raw_Meat(name, quantity, perishable, days_left, meat_type, storage_location,
                                        purchase_date,
                                        frozen, use_today, notes)
                elif category == "Dairy":
                    item_obj = Dairy(name, quantity, perishable, days_left, dairy_type, storage_location, purchase_date,
                                     open_date, is_open, notes)
                elif category == "Other_Frozen":
                    item_obj = Other_Frozen(name, quantity, perishable, days_left, frozen_type, storage_location,
                                            purchase_date, open_date, frozen_at_home, is_open, notes)
                elif category == "Baked_Goods":
                    item_obj = Baked_Goods(name, quantity, perishable, days_left, baked_type, storage_location,
                                           purchase_date, ready_to_eat, homemade, notes)
                elif category == "Condiment_Spice":
                    item_obj = Condiment_Spice(name, quantity, perishable, days_left, storage_location, purchase_date,
                                               open_date, is_open, condiment_type, notes)
                elif category == "Snacks_Shelf_Stable":
                    item_obj = Snacks_Shelf_Stable(name, quantity, perishable, days_left, snack_type, storage_location,
                                                   purchase_date, open_date, is_open, flavor, requested, notes)
                else:
                    item_obj = Food(name, quantity, perishable, days_left)

                self._shopping_list.append(item_obj)
        print(f"Shopping List loaded from {shopping_filename}")

    def save_to_file(self, filename):
        """Load foods from a file into Pantry"""
        pantry_filename = "pantry_" + filename
        shopping_filename = "shopping_" + filename
        with open(pantry_filename, "w") as file:
            for item in self._pantry_list:
                data = [
                    str(item._category),
                    str(item._name),
                    str(item._quantity),
                    str(item._perishable),
                    str(item._days_left),
                    str(getattr(item, '_storage_location', '')),
                    str(getattr(item, '_purchase_date', '')),
                    str(getattr(item, '_notes', '')),
                    str(getattr(item, '_ripeness', '')),
                    str(getattr(item, '_is_cut', '')),
                    str(getattr(item, '_washed', '')),
                    str(getattr(item, '_meat_type', '')),
                    str(getattr(item, '_dairy_type', '')),
                    str(getattr(item, '_frozen_type', '')),
                    str(getattr(item, '_baked_type', '')),
                    str(getattr(item, '_condiment_type', '')),
                    str(getattr(item, '_snack_type', '')),
                    str(getattr(item, '_frozen', '')),
                    str(getattr(item, '_use_today', '')),
                    str(getattr(item, '_open_date', '')),
                    str(getattr(item, '_frozen_at_home', '')),
                    str(getattr(item, '_ready_to_eat', '')),
                    str(getattr(item, '_homemade', '')),
                    str(getattr(item, '_flavor', '')),
                    str(getattr(item, '_requested', '')),

                ]
                file.write(','.join(data) + '\n')
        print(f"Pantry saved to {pantry_filename}")

        with open(shopping_filename, "w") as file:
            for item in self._shopping_list:
                data = [
                    str(item._category),
                    str(item._name),
                    str(item._quantity),
                    str(item._perishable),
                    str(item._days_left),
                    str(getattr(item, '_storage_location', '')),
                    str(getattr(item, '_purchase_date', '')),
                    str(getattr(item, '_notes', '')),
                    str(getattr(item, '_ripeness', '')),
                    str(getattr(item, '_is_cut', '')),
                    str(getattr(item, '_washed', '')),
                    str(getattr(item, '_meat_type', '')),
                    str(getattr(item, '_dairy_type', '')),
                    str(getattr(item, '_frozen_type', '')),
                    str(getattr(item, '_baked_type', '')),
                    str(getattr(item, '_condiment_type', '')),
                    str(getattr(item, '_snack_type', '')),
                    str(getattr(item, '_frozen', '')),
                    str(getattr(item, '_use_today', '')),
                    str(getattr(item, '_open_date', '')),
                    str(getattr(item, '_frozen_at_home', '')),
                    str(getattr(item, '_ready_to_eat', '')),
                    str(getattr(item, '_homemade', '')),
                    str(getattr(item, '_flavor', '')),
                    str(getattr(item, '_requested', '')),

                ]
                file.write(','.join(data) + '\n')
        print(f"Shopping List saved to {shopping_filename}")

    def printout_pantry(self):
        # would it be better to load from save before split logic|confirm internal data?
        """User Chooses a Method which allows multiple types of printout of Pantry to be delivered
        Options include By Quantity, Alphabetically, and By Category(Eventually)"""
        print(f"Printout {self._name}'s Inventory?")
        method = input(
            "Please choose an Inventory Sort Method \nPlease Enter: (Alphabet, Category, Quantity) \n(exit to escape)").lower()
        today = datetime.now().strftime("%Y-%m-%d")
        header = f"=+= Pantry {self._name} Inventory Report for {today} =+="
        print(header)
        border = "-^" * 25
        print(border)
        while True:
            if method == "exit":
                break
            elif method not in ["alphabet", "category", "quantity"]:
                print("Invalid Input... \nPlease Enter: (Alphabet, Category, Quantity) \n(exit to escape)")
            else:
                print_filename = f"pantry_printout_{today}.txt"
                sorted_items = self.sort_items(method)

                with open(print_filename, "w") as file:
                    file.write(header + f"\n{border}" + "\n")
                    for item in sorted_items:
                        print_out = item.define()
                        file.write(print_out + "\n")
                break

    def printout_shopping_list(self, method):
        """User Chooses a Method which allows multiple types of printout of Shopping List to be delivered
            Options include By Chronology, Alphabetically, and By Category(Eventually)"""
        print(f"Printout {self._name}'s Shopping List?")
        method = input(
            "Please choose an Shopping List Sort Method \nPlease Enter: (Alphabet, Category) \n(exit to escape)").lower()
        today = datetime.now().strftime("%Y-%m-%d")
        header = f"=+= Pantry {self._name} Shopping List Report for {today} =+="
        print(header)
        border = "-^" * 25
        print(border)
        while True:
            if method == "exit":
                break
            elif method not in ["alphabet", "category"]:
                print("Invalid Input... \nPlease Enter: (Alphabet, Category, Quantity) \n(exit to escape)")
            else:
                print_filename = f"shopping_printout_{today}.txt"
                if method == "alphabet":
                    sorted_items = sorted(self._shopping_list, key=lambda item: item._name)
                else:
                    sorted_items = sorted(self._shopping_list, key=lambda item: item._name)
                with open(print_filename, "w") as file:
                    file.write(header + f"\n{border}" + "\n")
                    for item in sorted_items:
                        print_out = f"{item._name} ({item._category}) \n- Added on: {item._shopp_add_date if item._shopp_add_date else ""}"
                        file.write(print_out + "\n")
                break

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
                    break
                else:
                    print("Invalid Input, Please Try Again")
                    continue

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
                    break
                else:
                    print("Invalid Input, Please Try Again")
                    continue

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
                    break
                else:
                    print("Invalid Input, Please Try Again")
                    continue

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
                    break
                else:
                    print("Invalid Input, Please Try Again")
                    continue

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
                    break
                else:
                    print("Invalid Input, Please Try Again")
                    continue

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
                    break
                else:
                    print("Invalid Input, Please Try Again")
                    continue

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
                    break
                else:
                    print("Invalid Input, Please Try Again")
                    continue

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
                    break
                else:
                    print("Invalid Input, Please Try Again")
                    continue

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
                    self.save_to_file(f"{self._name}.txt")
                    break
                elif final_confirmation_input == "n":
                    print("Many Apologies, Please Try Again")
                    break
                else:
                    print("Invalid Input, Please Try Again")
                    continue

            else:
                print(
                    "Improper Selection... Please Try Again: \n(basic, produce, fruit, meat, dairy, frozen, bakery, condiment, spice, snack, shelf stable) \n('EXIT' to quit)")
                continue

    def add_to_pantry(self, item):
        """Adds an Existing Food Object to Pantry List"""
        if item not in self._pantry_list:
            self._pantry_list.append(item)
            self.save_to_file(f"{self._name}.txt")
            print(f"Adding {item._name} to {self._name}'s pantry")
        else:
            print(f"Item: {item._name} already in {self._name}'s pantry!")

    def remove_item(self, item):
        # track common typos in common food words and add mistake-correction
        """ program takes user inputs
            and removes Food items from Pantry List"""
        if item in self._pantry_list:

            self._pantry_list.remove(item)
            print(f"Removing {item._name} from {self._name}'s pantry")
            item._quantity = 0
            self._shopping_list.append(item)
            self.save_to_file(f"{self._name}.txt")
            print(f"Added {item._name} to {self._name}'s Shopping List")
        else:
            print("Item not found!")

    def use_item(self, item, quantity):
        # track common typos in common food words and add mistake-correction
        """User chooses a Food item to subtract a quantity from
            If user uses all items in inventory, displays a prompt
            informing user and removing it from the Pantry List"""
        if item in self._pantry_list:
            orig_quantity = item._quantity
            item._quantity -= quantity

            if item._quantity < 0:
                item._quantity = 0
                self.remove_item(item)
                print(
                    f"Used {orig_quantity} of {item._name}. {item._name.capitalize()} now out of stock and moved to shopping list")
            else:
                print(f"Used {quantity} of {item._name}. {item._quantity} {item._name} left in pantry")
            self.save_to_file(f"{self._name}.txt")
        else:
            print("Item not found")

    def modify_item(self):
        # track common typos in common food words and add mistake-correction
        """User chooses a created Food Item to modify
            the Attributes of in the case of Errors or new Information"""
        print(f"Items in {self._name}'s inventory to be modified")
        for item in self._pantry_list:
            print(item._name)
        while True:
            item_lookup_val = input("Which item do you want to modify? ('exit' to escape)")
            if item_lookup_val.lower() == "exit":
                break
            selected = None
            for item in self._pantry_list:
                if item_lookup_val.lower() == item._name.lower():
                    selected = item
                    break
            if not selected:
                print("Item not found. Try again or 'exit'.")
                continue
            while True:
                attr_map = {attr.lstrip('_'): attr for attr in vars(selected)}
                print(f"Modifiable Attributes: {', '.join(attr_map.keys())}")
                attr_to_mod = input("Which attribute do you want to update? ").lower().strip()
                if attr_to_mod in attr_map:
                    new_value = input(f"Enter new value for {attr_to_mod}: ")
                    old_val = getattr(selected, attr_map[attr_to_mod])
                    if isinstance(old_val, bool):
                        new_value = new_value.lower() in ["true", "yes", "y", "1"]
                    elif isinstance(old_val, int):
                        new_value = int(new_value)
                    setattr(selected, attr_map[attr_to_mod], new_value)
                    print(f"{attr_to_mod} updated succesfully")
                    self.save_to_file(f"{self._name}.txt")
                    another_attr = input("Modify another attribute of this item (Y/N): ").lower()
                    if another_attr != "y":
                        break
                else:
                    print("Invalid Attribute. No changees made.")
            # Code Logic for return or exit Item Modify

    def sort_items(self, method="alphabet"):
        """Sorts Items in chosen inventory list
            by chosen method (Expiry, Quantity>, Quantity<, Category, Alphabet<)"""
        if method == "alphabet":
            return sorted(self._pantry_list, key=lambda item: item._name)
        elif method == "category":
            return sorted(self._pantry_list, key=lambda item: item._category)
        elif method == "quantity":
            return sorted(self._pantry_list, key=lambda item: item._quantity, reverse=True)
        else:
            print(f"Unknown sort method: {method}. Returning unsorted list.")
            return self._pantry_list

    def find_item(self, name):
        """Looks for an Item by Name and
            quickly displays information about it including Qty, Expiry, etc."""
        for item in self._pantry_list:
            if item._name.lower() == name.lower():
                print(f"Item {item._name} found in Pantry {self._name}'s Inventory!")
                item.define()
                return item
        for item in self._shopping_list:
            if item._name.lower() == name.lower():
                print(f"Item {item._name} found in Pantry {self._name}'s Shopping List!")
                return item

    def save_and_exit(self):
        """Asks User if they want to save,
            then either save and exits, or just exits without saving"""
        print("Save and Exit Program")
        import sys
        exit_var = input("Do you want to save before you exit? (Y/N)").lower()
        if exit_var not in ["y", "n"]:
            print("Invalid Input. \nDo you want to save before you exit? (Y/N) ")
        elif exit_var == "y":
            self.save_to_file(f"{self._name}.txt")
            sys.exit("Pantry Saved \nThank You for Using Pantry Manager!")
        else:
            sys.exit("Thank You for Using Pantry Manager!")


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

    def time_day_passed(self, last_checked_date=None):
        """Counts time in 24hr quantities and removes a 'day' from
                Perishables day counter or adds a 'day' to expired label"""

        if not last_checked_date:
            return

        last_date = datetime.strptime(last_checked_date, "%Y-%m-%d")
        today = datetime.now()
        days_passed = (today - last_date).days

        if days_passed > 0:
            self._days_left -= days_passed
            if self._days_left < 0:
                self._days_left = 0

    def is_expired(self):
        """Checks if Perishable is True
            and if days left are zero
            Adds a 'Check Me!' expired label with days since listed"""
        if self._perishable == True and self._days_left == 0:
            if "Check Me Before Use!" not in self._notes:
                self._notes += "\nCheck Me Before Use!"
            return True
        return False

    def update_quantity(self, amount):
        """Updates an Item's Quantity
            preventing negative amounts stored and checking for absurdities"""
        try:
            amount_int = int(amount)
            if amount_int < 0:
                amount_int = 0
            self._quantity = amount_int
            return True
        except ValueError:
            print("Invalid Input. Amount Must be a Number!")
            return False

    def define(self):
        """Prints out all saved information on Food Item
                formatted for ease of reading"""
        if self._perishable == True:
            perish_var = "Y"
        else:
            perish_var = "N"
        result = "\n" + "--*--=" * 6
        result += "\nBasic Food Item Summary:"
        result = "\n" + "--*--=" * 6

        result += f"\nName: {self._name}| Quantity: {self._quantity}| Perishable?: {perish_var}| Days Remaining: {self._days_left} \n"
        # add silent function
        # print(result)
        return result

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
        result = super().define()
        result += "--*--=" * 6 + "\n"
        result += "\nProduce Specific Item Summary:"
        result += f"\nLocation: {self._storage_location}| Purchase Date: {self._purchase_date}"
        result += f"\nAdditional Notes:{self._notes}"
        # add silent function
        # print(result)
        return result

    def is_expired(self):
        """Prints Unique Produce Spoilage Messages"""
        expired = super().is_expired()
        if expired:
            self._notes += ("\nCheck For Rot/Mold \nIf None: Is Okay to Eat/Cook.")
            return True
        return False

class Fruit_Produce(Food):
    """Subclass of Food:
        Fresh Produce: Ready To Eat
        e.g. Strawberries, Apples, Bananas"""

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

        result = super().define()
        result += "--*--=" * 6 + "\n"
        result += "\nFruit Specific Item Summary:"
        result += f"\nLocation: {self._storage_location}| Purchase Date: {self._purchase_date}"
        result += f"\nRipeness: {self._ripeness}| Washed?: {wash_var}| Cut?: {cut_var}"
        result += f"\nAdditional Notes:{self._notes}"
        # add silent function
        # print(result)
        return result

    def ripeness_mover(self):
        """Changes _ripeness
            and _days_left on a Fruit Item"""
        new_ripeness = input("What is the new Ripeness of Fruit? (Unripe/Ripe/Overripe)").lower()
        if new_ripeness not in ["unripe", "ripe", "overripe"]:
            print("Invalid Input! Ripeness Not Changed")
            return False
        elif new_ripeness == "unripe":
            self._days_left = 7
            self._ripeness = new_ripeness
        elif new_ripeness == "ripe":
            self._days_left = 3
            self._ripeness = new_ripeness
        else:
            self._days_left = 1
            self._ripeness = new_ripeness
        print(f"Ripeness updated to {self._ripeness}. Days left updated to {self._days_left}.")
        return True

    def cut_fruit(self):
        """Changes _is_cut State from False to True"""
        self._is_cut = True
        print(f"Fruit {self._name} has been cut.")
        return True

    def wash_fruit(self):
        """Changes _washed State from False to True"""
        self._washed = True
        print(f"Fruit {self._name} has been washed.")
        return True

    def is_expired(self):
        """Prints Unique Fruit Spoilage Messages"""
        expired = super().is_expired()
        if expired:
            if not self._is_cut:
                self._notes += ("\nCheck For Rot/Mold \nIf None: Is Okay to Eat.")
                return True
            else:
                self._notes = ("Throw Away! Unsafe to Eat!")
                return True
        return False

class Raw_Meat(Food):
    """Subclass of Food:
    Meat to be cooked
    e.g. Pork Loin, Sausages, Chicken Thighs, Chorizo"""

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

        result = super().define()
        result += "--*--=" * 6 + "\n"
        result += "\nMeat Specific Item Summary:"
        result += f"\nMeat Type: {self._meat_type}"
        result += f"\nLocation: {self._storage_location}| Purchase Date: {self._purchase_date}"
        result += f"\nFrozen?: {froz_var}| Use Today?: {use_today_var}"
        if self._use_today == True:
            result += f"\n{self._name} Needs to be used TODAY!"
        result += f"\nAdditional Notes:{self._notes}"
        # add silent function
        # print(result)
        return result

    def is_expired(self):
        """Prints Unique Meat Spoilage Messages"""
        expired = super().is_expired()
        if expired:
            if not self._frozen:
                self._notes += ("\nCheck For Rot and/or Discoloration \nIf None: Is Okay to Cook.")
                return True
            else:
                self._notes += ("\nCheck for Freezer-Burn!")
                return True
        return False

    def make_use_today(self):
        """Changes _use_today State to True
            and _days_left to 1"""
        self._use_today = True
        self._days_left = 0
        print(f"Meat Item {self._name} has been made Use Today! Days Remaining changed to 1.")
        return True

    def freeze_meat(self):
        """Changes _frozen State to True
            and _days_left to 60"""
        self._frozen = True
        self._days_left = 60
        print(f"Meat Item: {self._name} has been frozen. Days Remaining changed to 60.")
        return True


class Dairy(Food):
    """Subclass of Food:
        Milks, Cheeses, Yogurts, Etc
        e.g. Fresh Milk, Gouda, Greek Yogurt, Sour Cream"""

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

        result = super().define()
        result += "--*--=" * 6 + "\n"
        result += "\nDairy Specific Item Summary:"
        result += f"Dairy Type: {self._dairy_type}"
        result += f"\nLocation: {self._storage_location}| Purchase Date: {self._purchase_date}"
        result += f"\nOpen? {open_var}| Open Date: {self._open_date}"
        result += f"\nAdditional Notes:{self._notes}"
        # add silent function
        # print(result)
        return result

    def is_expired(self):
        """Prints Unique Dairy Spoilage Messages"""
        expired = super().is_expired()
        if expired:
            if not self._is_open:
                self._notes += ("\nCheck For Rot/Mold \nIf None: Is Okay to Eat/Cook.")
                return True
            else:
                self._notes = ("Spoiled! Throw Away! \nUnsafe To Eat!")
                return True
        return False

    def open_dairy(self):
        """Changes _is_open state to True and
            _days_left to 3 unless _dairy_type is not 'Cheese' """
        self._is_open = True
        if self._dairy_type.lower() != "cheese":
            self._days_left = 3
            print(f"Dairy Item {self._name} has been opened. Days Remaining adjusted to 3")
        else:
            self._days_left = self._days_left
            print(f"Dairy Item {self._name} has been opened. Days Remaining have not been adjusted. Item is a Cheese.")

        return True


class Other_Frozen(Food):
    """Subclass of Food:
        Premade Frozen Food, Frozen Veg, Frozen Additives
        e.g. Chicken Nuggets, Frozen Okra, Frozen Veg Stock"""

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

        result = super().define()
        result += "--*--=" * 6 + "\n"
        result += "\nFrozen Specific Item Summary:"
        result += f"\nFrozen Type: {self._frozen_type}| Home Freeze?: {home_var}"
        result += f"\nLocation: {self._storage_location}| Purchase Date: {self._purchase_date}"
        result += f"\nOpen?: {open_var}| Open Date: {self._open_date}"
        result += f"\nAdditional Notes:{self._notes}"
        # add silent function
        # print(result)
        return result

    def is_expired(self):
        """Prints Unique Frozen Spoilage Messages"""
        expired = super().is_expired()
        if expired:
            self._notes += ("\nCheck For Freezer-Burn \nIf None: Is Okay to Eat/Cook.")
            return True
        return False


class Baked_Goods(Food):
    """Subclass of Food:
        Breads, Pastas, Pastries
        e.g. Baguettes, Linguini, Danishes"""

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

        result = super().define()
        result += "--*--=" * 6 + "\n"
        result += "\nBakery Specific Item Summary:"
        result += f"\nBaked Type: {self._baked_type}| Homemade? {home_var}| Ready to Eat?: {ready_var} "
        result += f"\nLocation: {self._storage_location}| Purchase Date: {self._purchase_date}"
        result += f"\nAdditional Notes:{self._notes}"
        # add silent function
        # print(result)
        return result

    def is_expired(self):
        """Prints Unique Baked Spoilage Messages"""
        expired = super().is_expired()
        if expired:
            self._notes += ("\nCheck For Rot/Mold \nIf None: Is Okay to Eat/Cook.")
            return True
        return False


class Condiment_Spice(Food):
    """Subclass of Food:
        Condiments, Spices, Herbs, Sauces
        e.g. Ketchup, Cumin, Thyme, P.S. Lemon-Herb Vin"""

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
        result = super().define()
        result += "--*--=" * 6 + "\n"
        result += "\nCondiment/Spice Specific Item Summary:"
        result += f"\nCondiment/Spice?: {self._condiment_type}"
        result += f"\nLocation: {self._storage_location}| Purchase Date: {self._purchase_date}"
        result += f"\nOpen?: {open_var}| Open Date: {self._open_date}"
        result += f"\nAdditional Notes:{self._notes}"
        # add silent function
        # print(result)
        return result

    def is_expired(self):
        """Prints Unique Condiment Spoilage Messages"""
        expired = super().is_expired()
        if expired:
            if not self._is_open:
                self._notes += ("First Check Smell \nCheck For Mold/Damp/Dry \nIf None: Is Okay to Use/Cook.")
                return True
            else:
                self._notes += ("Check Freshness Upon Opening! \nIf Okay, Please Reset Days Till Expired")
                return True
        return False

    def open_spice(self):
        """Changes State of _is_open from False to True
            and adjusts _days_left by _condiment_type rules."""
        self._is_open = True
        if self._condiment_type.lower() == "sauce":
            self._days_left = 30
            print(f"Sauce {self._name} opened. Days Remaining changed to 30.")
        elif self._condiment_type.lower() in ["spice", "dried spice", "herb", "dried herb"]:
            self._days_left = 180
            print(f"Herb/Spice {self._name} opened. Days Remaining changed to 180.")
        else:
            self._days_left = 60
            print(f"Unknown Condiment Type {self._name} opened. Days Remaining changed to 60")
        return True


class Snacks_Shelf_Stable(Food):
    """Subclass of Food:
        Snacks and Shelf Stable foods
        e.g. Muffins, Canned Pears, Ragu(Garlic)"""

    # high sugary candies and snacks 15-30, crackers 30-60,
    # nuts/jellies/jams/spreads 15-30 if opened, etc
    # Unique spoilage printouts
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

        result = super().define()
        result += "--*--=" * 6 + "\n"
        result += "Shelf Stable Specific Item Summary:"
        result += f"\nFood/Snack Type: {self._snack_type}| Flavor: {self._flavor}"
        result += f"\nLocation: {self._storage_location}| Purchase Date: {self._purchase_date}"
        result += f"\nOpen?: {open_var}| Open Date: {self._open_date}"
        result += f"\nRequested By: {self._requested}"
        result += f"\nAdditional Notes:{self._notes}"
        # add silent function
        # print(result)
        return result

    def is_expired(self):
        """Prints Unique Snack Spoilage Messages"""
        expired = super().is_expired()
        if expired:
            if not self._is_open:
                self._notes += ("\nCheck For Rot/Mold \nIf None: Is Okay to Eat/Cook (May Be Stale!).")
                return True
            else:
                self._notes += ("Check Freshness Upon Opening!")
                return True
        return False

    def open_snack(self):
        """Changes is_opened state from False to True
            in addition to updating _days_left"""
        self._is_open = True
        self._days_left = 30
        print(f"Snack/Shelf Stable {self._name} has been opened. Days Remaining set to 30")
        return True


def help_me():
    """Prints out all calls and needed variables within program"""
    pass


global_common_typos = {"example": "exampel", "tomato": "tomtao"}
# TODO: Look Up common typos for top 200 common food words in America (min 3 typos per word).
# Learn about json to implement this

# ---------------------------------
# ----------Main Program-----------
# ---------------------------------

# TODO: Build test program to save -> orig_name |
# Build test program to load / edit / save -> new_name |
# Build test program to load / check / exit w/out save -> orig/new |


# I think that does it?