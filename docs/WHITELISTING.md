Pantry Manager – Field Update Whitelisting
This document defines which fields on each major entity are allowed to be updated by users in the Pantry Manager app (after creation), and how this is enforced on both the UI and backend.


FoodItem

Editable by User:
location_id
quantity
unit
status (with valid transitions only)
notes
metadata (only keys valid for the item's category)

Immutable (locked after creation):
id
name
category_id
expiration_date
purchased_at
any metadata keys NOT in the metadata_keys of that item's category


Category

End-user editing/addition not allowed in MVP. Categories are managed and locked by the system.


InventoryLocation

Editable (Custom Locations Only):
name
type
emoji
description

Immutable:
id
Preset locations cannot be modified by users.


ShoppingItem

Editable:
name
requested_by
date_needed
notes

Immutable:
id
fooditem_id
date_added
completed_at (set only by the “mark purchased” workflow)


User/Household

Editable by Admin:
household_name
email
settings (JSON)
members (dict, with role-based permissions)
encrypted (with warning, and possibly confirmation code)

Immutable:
id
userkey
created_at


Enforcement

UI: Only whitelisted fields are shown with edit controls. Non-editable fields appear as read-only.

Backend/API: PATCH/PUT endpoints only accept updates to whitelisted fields. All others are ignored or rejected with an error.

Metadata: Only fields explicitly listed in the category’s metadata_keys can be edited/stored.

Admin settings: Only accounts with admin status see admin-only fields and functions.


Note:

This whitelisting policy keeps the system secure, prevents data corruption, and ensures only valid/allowed changes can be made by users or admins. It is enforced at both UI and API/service layers.