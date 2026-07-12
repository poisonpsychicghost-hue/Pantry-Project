App Structure – High-Level Layout


Main App Layout:

Header:
Primary Navigation: Pantry | Shopping | Bulk Add
Hamburger Menu: Full Site Navigation (all tabs/screens)

Body:
Switchable Tab Content (driven by top nav/menu)

Footer:
API version, developer credits


Body Tabs/Screens

Startup/Login:
Household login fields
User selection
Admin login field (password protected)

Main (“Home”):
Warnings (expiring, low stock, etc.)
Recents (recently used, recently added, etc.)

Pantry Inventory:
Full inventory table/list
Filter/sort controls
Expandable item cards
Click to view/edit item details

Pantry Item Card:
Shows full item data
Editable whitelisted fields
Category-specific metadata fields

Shopping List:
Full shopping list
Filter/sort controls
Expandable item cards
Click to edit/move to inventory/mark purchased

Shopping Item Card:
Shows full shopping item data
Editable whitelisted fields

Bulk Add:
Multi-row entry form
[+ Add item] expands input rows for batch entry

Settings:
User settings
Admin settings (if admin logged in)
UX/Access Notes:


Hamburger/slide menu makes all tabs easily accessible, desktop or mobile.
Admin-only sections/settings show only if admin is logged in.
Every card/form only exposes whitelisted fields as editable.
Quick navigation between major features; no page reloads required.