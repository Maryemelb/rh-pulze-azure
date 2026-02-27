
from fastapi import FastAPI
from sqlalchemy_utils import create_database, database_exists
from backend.app.models.user import User
from backend.app.models.jobs import Jobs
from backend.app.models.skills import Skills
from backend.app.db.database import engine, Base,DATABASE_URL
from backend.app.routes.login import router as loginRouter
from backend.app.routes.register import router as registerRouter
from backend.app.routes.health import router as healthRouter
from backend.app.routes.jobs import router as jobsRouter
from backend.app.routes.predict import router as predictSalaryRouter
from backend.app.routes.extract_skills import router as extractSkillsRouter
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

# if not database_exists(DATABASE_URL):
#     create_database(DATABASE_URL)
Base.metadata.create_all(bind=engine)


origins=[
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://backend:8000"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(loginRouter)
app.include_router(registerRouter)
app.include_router(healthRouter)
app.include_router(predictSalaryRouter)
app.include_router(jobsRouter)

# if __name__ == "__main__":
#     main()
