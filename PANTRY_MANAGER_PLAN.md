
Pantry Manager – Fullstack App Rebuild
Project Goal:

Redesign our legacy CLI “Pantry Manager” as a modern, maintainable, production-ready fullstack web application.

Table of Contents:
01 - Intro & Background
02 - Analysis of Legacy App
03 - Requirements & User Stories
04 - System & Database Design
05 - Wireframes & Architecture
06 - Backend Development Plan
07 - Frontend Development Plan
08 - Integration Plan
09 - Analytics & Dashboard
10 - Mobile Responsiveness & Polish
11 - Testing & Deployment
12 - Future Features
13 - Development Workflow


1. Intro & Background
Transform the original Python CLI pantry manager into a single-page, mobile-ready web dashboard.

Tech stack:
Frontend: Vue 3 (Composition API), Tailwind CSS, Pinia
Backend: FastAPI (Python), SQLAlchemy ORM, PostgreSQL


2. Analysis of Legacy App
Weaknesses:

Logic, data, UI tightly coupled
No real DB (uses text files)
Custom subclasses for every item type—hard to extend
CLI-only, single user, no real validation
Linear flows (tedious, error-prone)
Minimal analytics
Resolution (Web App Approach):

Separate UI/backend/logical layers
Use normalized RDBMS schema
Use flexible JSON fields for per-category variations
Build responsive, interactive SPA
Provide analytics, smart warnings, mobile-first access


3. Requirements & User Stories
Core User Goals

Track all pantry, fridge, and freezer inventory
Monitor expiration/spoilage, get warnings
Maintain searchable, sortable tables and views
Auto-create and manage shopping list
Reduce food waste with actionable stats
User Stories (examples)

“As a user, I want to quickly see items about to expire.”
“As a user, I want to add a new dairy item and record if it’s opened.”
“As a user, I want to move items from shopping list to inventory.”
“As a user, I want a visual overview of waste risk.”


4. System & Database Design
Use SQLAlchemy models + PostgreSQL
Core tables: FoodItem, Category, ShoppingItem, InventoryLocation
Use metadata: JSONB in FoodItem for category specifics
Example:
FoodItem(id, name, category_id, quantity, storage_location_id, expiration_date, added_at, metadata, notes, ...)


5. Wireframes & Architecture
Screens: Dashboard, Inventory, Add/Edit, Item Detail, Shopping List, Expiration Center, Analytics
Component Hierarchy:
App.vue → SidebarNavigation, MainContent
UX Requirements:
Mobile-first, SPA, responsive
Floating “Add” button, modals, confirmation dialogs
Color-coded urgency indicators


6. Backend Development Plan
Scaffold FastAPI project, configure DB
Create SQLAlchemy models & Alembic migrations
Implement API endpoints (CRUD, analytics, lists)
Seed database with sample categories and storage locations


7. Frontend Development Plan
Scaffold Vue 3 (Vite) project
Set up Tailwind, Pinia, Vue Router, Axios
Build layouts, sidebar/topbar, pages, table and chart components
Implement dynamic forms (fields per category)


8. Integration Plan
Connect frontend to FastAPI endpoints
Enable live add/edit/delete; show feedback and errors
Add search, sort, filter, pagination to inventory table


9. Analytics & Dashboard
KPIs: Total items, expiring today/soon, shopping count, recent
Charts: Expiration heatmap, inventory by category, waste potential
Expiration Center: expired, soon, safe, color-coded


10. Mobile Responsiveness & Polish
Test collapsible sidebar, mobile nav, touch zones
Transform tables to cards on mobile
Ensure forms and modals work on all screen sizes


11. Testing & Deployment
Backend: Write unit and integration tests
Frontend: Unit/E2E tests for components and flows
Dockerize both apps
Deploy backend & frontend (Heroku, Railway, Vercel, Netlify, etc.)


12. Future Features
User accounts, households/sharing
Barcode/QR entry
Push notifications for expiry
Meal planner & recipes
Waste analytics, reporting
IoT integrations


13. Development Workflow
Use Git for version control: feature branches, PRs, merge review
Commit early and often, with clear messages
Pause after each feature/bugfix: document what changed and why
Example commit message style:
feat: implement shopping list CRUD endpoints
fix: correct date bug on expiration center
docs: add wireframes to project folder
Use issues/projects for all work, subdivided by milestone
