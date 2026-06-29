Entities & Tables


1. FoodItem

Field	Type	Required	Description

id	int (PK)	Yes	(Unique identifier)

name	string	Yes	(Name of the food)

category_id	int (FK)	Yes	(Linked category)

location_id	int (FK)	Yes	(Storage location)

quantity	float/int	Yes	(Quantity on hand)

unit	string	Yes	(Select from predefined units)

expiration_date	date	Yes	(When the item expires)

status	string	Yes	(e.g. in_stock, opened, expired)

notes	text	No	(Arbitrary extra info)

metadata	JSONB	Yes	(Category- and item-specific) fields
added_on	date	Yes	(When added to inventory)

purchased_at	date	No	(When purchased (optional))


2. Category

Field	Type	Required	Description

id	int (PK)	Yes	(Unique identifier)

name	string	Yes	(e.g. Fruit, Dairy, etc.)

style	JSONB	No	(Theme color set per category)

icon	string	No	(Emoji or SVG icon)

description	string	No	(User-facing summary of category)

metadata_keys	JSONB or array	Yes	(List of keys for 
category-specific metadata)


3. InventoryLocation

Field	Type	Required	Description

id	int (PK)	Yes	(Unique identifier)

name	string	Yes	(e.g. Pantry, Fridge, Freezer, etc.)

type	string	Yes	(pantry/fridge/freezer/other)

emoji	string	Yes	(Emoji/icon (preset for built-ins, select for customs))

description	string	No	(Human-readable or tooltip info)

4. ShoppingItem

Field	Type	Required	Description

id	int (PK)	Yes	(Unique identifier)

fooditem_id	int (FK)	No	(Reference to FoodItem (nullable))

name	string	Yes	(Name of shopping item)

requested_by	string	No	(Optional—who requested )(nullable)

date_added	date	Yes	(When added to the list)

date_needed	date	No	((Optional) Required by date)

completed_at	date	No	(When marked as purchased)

notes	string	No	(Extra info)


5. User/Household

Field	Type	Required	Description

id	int (PK)	Yes	(Unique identifier)

userkey	string	Yes	(Unique encryption/login key)

household_name	string	Yes	(Family/household name)

email	string	No	(Optional)

created_at	datetime	Yes	(Profile creation time)

settings	JSONB	No	(Preferences, notification settings, etc.)

members	JSONB	Yes	(Dict of member profiles and admin/user roles)

encrypted	boolean	Yes	(All household data is encrypted)


Notes

All PII is to be considered encrypted by default.

Category/entity-specific fields are stored in metadata and validated as needed.

unit is selected from a controlled set; general string not allowed in UI.

Future fields (e.g. price, UPC/barcode, photo, event logs) are planned but deferred for now.

Simple, clear relationships: FoodItem links to 
Category and InventoryLocation; ShoppingItem may link to FoodItem or exist standalone.