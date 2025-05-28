from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# 🧠 Update this with your actual PostgreSQL credentials and DB name
DB_USER = "postgres"
DB_PASSWORD = "12345"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "postgres"

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# 🔌 Create the engine to connect SQLAlchemy to your PostgreSQL DB
engine = create_engine(DATABASE_URL)

# 🔁 Create a session to use in our API routes
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 🧱 Base class for our models
Base = declarative_base()

# Dependency to inject DB session into routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
