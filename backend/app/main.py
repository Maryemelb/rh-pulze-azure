
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

print("All packages are correctly installed!")

def main():
    print("Hello from rh-pulze-azure!")


if __name__ == "__main__":
    main()
