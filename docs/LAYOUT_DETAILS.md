LAYOUT DETAILS

Main App Shell (Wireframe Description)


Header: (Fixed at top, always visible)
QuickNav bar:
Shows up to three main tabs at once (dynamic: e.g. on Pantry, you see Home + Shopping + BulkAdd)
Always prominently visible and one-tap
Household Name & Current User Name/Class
E.g. "Smith Family — Caleb (Admin)"
Hamburger Menu:
Button at right (desktop: real hamburger; mobile: icon)
Opens full navigation: Home, Pantry, Shopping List, Bulk Add, Settings, Logout, (and Analytics when live)


Body: (Scrollable)
Displays currently selected tab content (switches per nav)


Footer: (Fixed at bottom, always visible)
Shows:
API version
Build/developer credits
(Optional) “Contact” or Help link/button


Branding/UX Note:
Header always visible = user never “lost”—always can reach main pages, see where they are, and access account/settings/quick logout.
QuickNav is context-sensitive (shows other “core” tabs for fast jumping, always includes “Home” unless you’re already on it).
Hamburger for everything else: ensures power users/admins can reach all features/settings, but UI stays uncluttered.


Startup/Login Screen


Visual Style:
Clean, uncluttered, centered—white/neutral backgrounds
Reminiscent of Google OAuth (familiar, trusted)

Fields:
Household Name (input)
Password (input, masked)
Remember Me checkbox

Actions:
Login button (prominent, disables until fields are valid)
On login success:
Display an avatar/thumbnail menu for each user in the household
User selects avatar to proceed
Prompt for PIN/password if “Admin” account selected

Other:
Small “Forgot password?” link (optional)
Option to create/join a household (future, not MVP, may appear as “Don’t have a household? Contact Admin.”)
Key Flows/UX:

Two-stage login:
Authenticate household
Choose user avatar (add admin PIN step if needed)
Familiar, trustworthy, frictionless as possible


Main Home Page (Dashboard) – FINAL

Header: (fixed)

Body – Dashboard Layout:

Welcome Banner:
Friendly greeting with household and user’s name:
“Welcome back, Caleb! Here’s what’s happening in your kitchen.”

KPIs/Status Cards:
Expiring Soon
Expired Today
Total Inventory Count
Shopping List Count

Quick Add Button:
Floating action button; always visible (corner or header)
Opens “Add Item” flow/modal from anywhere on Dashboard

Charts/Graphs:
Pie/bar: Inventory by category/location
Line/bar: Waste/trends

Recent Activity Table/List:
Recently added foods
Recently completed shopping items

Warnings/Alerts Panel:
“Critical” (immediate) and “Warning” (soon/low) badges

Footer: (fixed, all screens)

Mobile:
Same content, with elements stacked and KPIs horizontally scrollable
“Quick Add” and Alerts always accessible


Pantry Inventory Screen

Header: (fixed, as before)

QuickNav:
Shows Home, Shopping, Bulk Add (dynamic based on context)


Body:

Filter & Sort Controls:
Filter by location, category, expiration status, etc.
Search bar (name, category, note text)
Sort by days remaining, quantity, name, location


Inventory Table/Grid:

Each row/card shows:
Item name
Category (icon/emoji/color)
Quantity/unit
Location (emoji/icon)
Days remaining (color-coded chip/badge)
Status (e.g., in_stock, expired, opened)
Expiration warning (e.g., ⚠️, color for urgency)
[Expand/View Details] button/icon
[Edit] quick button (inline or on detail/expand)

Bulk Actions: (optional, advanced/post-MVP)
Checkbox to select multiple items for mass move/delete (can defer)
Floating Quick Add Button:
Opens Add/Edit Item form

Mobile:
Cards stack vertically or as swipeable tiles
Filters and search collapse into modal or menu
Expand item card for full detail/edit


Footer: (fixed)

Actions/Flows:
Clicking a row/card expands to full Pantry Item Card (details + edit)
Quick Add is always present for rapid entry
Filter/search makes even big pantries manageable

Pantry Item Card (Details & Edit)

Header:
Item name prominently displayed
Category icon/emoji & color badge


Main Content:

Core Fields:
Quantity + unit (editable)
Location (dropdown, editable)
Days remaining (computed, color-coded)
Expiration date (read-only or editable if allowed)
Status (badge: in_stock, opened, expired, etc.—editable transitions only)
Notes (free text, editable)
Category-Specific Metadata:

Dynamic section: shows fields per category (e.g., ripeness for fruit, opened date for dairy)
Only metadata allowed by category whitelist is shown

History/Summary:
Added on date
Purchased at date (if present)

Danger Zone:
Delete button (with confirmation)
Move to Shopping List (“out of stock/expired” flow)


Actions:
“Save” / “Cancel” (if fields were edited)
“Close” (if modal/detail view)


UX Notes:
Quick, in-place edits; whitelisted fields are visibly editable.
Validation/error feedback per field.
Confirmation dialog on destructive actions.
Smooth motion for mobile (scrolls, modals, slide-ins, etc.)


Shopping List Screen


Header: (fixed as elsewhere)

QuickNav:
Dynamic tabs (Home, Pantry, Bulk Add)


Body:

Filter & Sort Controls:
Filter by: requested_by, category, location (if relevant)
Search bar for item name/notes
Sort by: date needed, date added, name


Shopping List Table/Grid:

Each row/card displays:
Item name
Requested by (icon or text, if present)
Date added / date needed
Status badge (pending, purchased—if tracked)

Quick actions:
[Mark as Purchased] button (moves to inventory, sets completed_at)
[Move Back to Pantry] (for accidental removals)
[Delete] (with confirmation)
[Expand/Edit Details] button or icon

Bulk Actions:
(Optional/Future) Select multiple for batch removal or purchase
Floating Add Item Button:
Opens Add Shopping Item form


Mobile:
Cards or rows stack vertically
Controls collapse into menus or floating actions
Quick tap to mark purchased/delete


Footer: (fixed)

Actions/Flows:
Expanding a row opens the Shopping Item Card (details + inline edit)
Filtering/sorting/paging for long lists (essential for big shopping runs!)
“Purchased” items move instantly to the pantry/inventory


Shopping Item Card (Details & Edit)

Header:
Shopping item name (prominent)
Requested by (if present)
Status badge (pending/purchased)


Main Content:

Core Fields:
Quantity/unit (editable, if tracked)
Notes (free text, editable)
Date needed (editable)
Date added (read-only)

Action Buttons:
Mark as Purchased (moves item to Pantry, sets completed_at)
Move Back to Pantry (without “purchased”, e.g. mistaken add)
Delete (with double-confirmation for accidental clicks)
Save / Cancel (for edits)

Sidebar/Details Area (Post MVP):
Linked FoodItem (if this item exists in inventory, link to view full card—optional for MVP)
Show small “history” (recent times this has been purchased, if logged)


UX Notes:
Editable fields only shown for user-mutable attributes
Single-action buttons are prominent, color-coded for clarity (Save=primary, Move/Delete=danger)
Easy to toggle between detail/compact view (especially on mobile)


Bulk Add Screen

Header: (fixed, consistent with rest of app)

QuickNav: (as before)

Body:

Title/Instructions:

Friendly heading: “Bulk Add Items to Pantry”

Short instructional text: “Quickly add multiple new items below.”

Bulk Add Form:

Table layout or dynamic list:

Each row:
Name (text input)
Category (dropdown/select)
Location (dropdown/select)
Quantity (number)
Unit (dropdown/select)
Expiration Date (date picker)
[Delete Row] (icon/button, to remove that line)
[Metadata Expand] (optional, shows extra fields by category)
[+ Add Another Item] button (adds a new row to the form)

Submit/Cancel Section:
“Add All to Pantry” (submits all valid rows)
“Cancel” (returns without adding)


Mobile:
Rows stack vertically
[+ Add Item] stays visible
Easy swipe/delete for extra rows


UX Notes:
Validation for all required fields before enabling “Add All”
Handles 5–20+ items comfortably for mass inventory updates or store restocks
(Future: import via CSV, photo/receipt scan, etc.)


Settings Screen

Header: (fixed, as before)

QuickNav: (present)


Body:

User Settings Section:
Display user info (name, avatar/icon if used)
Change password/PIN (optional, future)

Theme: dark/light toggle
Notification preferences (if built)
[Save] and [Cancel] for applicable changes

Admin Settings Section: (Visible only for admins—conditional rendering)
Edit Household Name
Manage household members/roles (add/remove, set admin/user)
Reset encrypted status or security info (with heavy warning)
Update email/settings metadata
Export household data (optional, post-MVP)
Delete household/account (double-confirm, danger zone)

About/App Info Section:
App version/build
Developer credits/contact/help link


UX Notes:
User and Admin settings clearly separated, with admin-only fields hidden from non-admins.
Save/cancel visible only if there are editable settings.
Danger zone (delete, reset) shown at bottom, distinct styling to avoid accidental actions.

Optional: Profile picture/avatar support for user friendliness.


Analytics Screen (Coming Soon)

Header: (fixed)

QuickNav: (present)

Body:

Large centered card or banner:
“Analytics & Insights”
“Coming Soon!”

Short blurb:
“Visualize your inventory: trends, category breakdowns, food waste risk, and more. This dashboard feature will be available in a future update.”
Optionally, a fun icon or chart illustration (e.g. 📊, 🥦, ⏳)
[Back to Home] button/link

UX Notes:
Friendly, hopeful tone—users know dashboard/analytics features are planned.
Styled to match the app, but clearly in “placeholder” mode.

