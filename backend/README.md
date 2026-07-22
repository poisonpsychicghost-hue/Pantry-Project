Pantry Manager – Backend

A household inventory and shopping management backend for Pantry Manager.

Built with FastAPI, SQLAlchemy, Alembic, and PostgreSQL for secure, robust tracking of pantry, fridge, freezer, and shopping data.

--Project Purpose--
- Track pantry/fridge/freezer inventory
- Manage shopping lists and reduce food waste
- Provide a clear API for the frontend and third-party integration
- Easily seed sample/demo data for dev or onboarding

--Tech Stack--
- Python 3.10+
- FastAPI – modern async web/api framework
- SQLAlchemy – ORM and query builder
- Alembic – database migrations
- PostgreSQL – production-grade SQL database
- Docker Compose – for database containerization

--Setup Instructions--

1. Clone and install dependencies
git clone <your-repo-url>
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

2. Configure your .env file
Copy .env.example to .env and fill in your credentials if needed:
DATABASE_URL=postgresql+psycopg2://pantry_user:yourpassword@localhost:5432/pantry_manager_dev

3. Start PostgreSQL with Docker
docker compose up -d

4. Run database migrations
alembic upgrade head

5. Seed development/demo data
python demo_seed.py



--Running the Backend--
uvicorn main:app --reload

Visit FastAPI docs at: http://localhost:8000/docs


--Folder Structure--
/models – SQLAlchemy ORM models (data structure)
/repositories – direct database access helpers (CRUD)
/services – business logic, validation, whitelisting
/routes – FastAPI routers (API endpoints)
/alembic – database migration scripts
/docs – architecture docs, planning, wireframes
/db.py – session and connection setup
/seed_*.py – scripts for seeding demo/dev data


--Data Seeding Scripts--
seed_categories.py – Add initial categories and metadata keys
seed_locations.py – Add starter locations (pantry, fridge, etc.)
seed_inventory.py – Add demo FoodItems for development/testing
seed_shoppinglist.py – Seed demo shopping list items
demo_seed.py – Run all seeding scripts in order (recommended first-time step)


--Known Gaps & TODOs--
-  Member authentication is frontend/middleware only for MVP (to be moved backend-side in future)
-  Status value validation needs refinement and enums
-  Final API docs for full frontend integration


--Contribution/Development Notes--
- Branching: Feature branches per model or component; merge when tested
- Documentation: Maintain clear top-level/module/function docstrings
- Testing: Test seed scripts and service logic before merging new features
- DB reset: To start fresh, docker compose down -v removes all data; re-run migrations and demo_seed.py


--Credits--

Built by Thomas Caleb `Sirius` Barnard  – 2026

Mentored and reviewed using Maestro
