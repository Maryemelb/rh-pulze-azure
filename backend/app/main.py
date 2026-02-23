
from fastapi import FastAPI
from sqlalchemy_utils import create_database, database_exists
from backend.app.models.user import User
from backend.app.db.database import engine, Base,DATABASE_URL
app = FastAPI()

# if not database_exists(DATABASE_URL):
#     create_database(DATABASE_URL)
Base.metadata.create_all(bind=engine)


@app.get("/")
def read_root():
    return {"message": "Hello World"}

print("All packages are correctly installed!")

def main():
    print("Hello from rh-pulze-azure!")


if __name__ == "__main__":
    main()
