
from fastapi import FastAPI
from sqlalchemy_utils import create_database, database_exists
from backend.app.models.user import User
from backend.app.db.database import engine, Base,DATABASE_URL
from backend.app.routes.login import router as loginRouter
from backend.app.routes.register import router as registerRouter
from backend.app.routes.health import router as healthRouter
from backend.app.routes.jobs import router as jobsRouter
from backend.app.routes.extract_skills import router as extractSkillsRouter

app = FastAPI()

# if not database_exists(DATABASE_URL):
#     create_database(DATABASE_URL)
Base.metadata.create_all(bind=engine)


app.include_router(loginRouter)
app.include_router(registerRouter)
app.include_router(healthRouter)


# if __name__ == "__main__":
#     main()
