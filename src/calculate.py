from fastapi import FastAPI

app = FastAPI()

def add_func(a: float,b: float) -> float:
    return a+b

# -------------

@app.get("/")
def home():
    return {"status": "Online", "message": "這是簡易計算機 API"}

@app.get("/add")
def calculate_add(a: float, b: float):
    # add_func
    result = add_func(a, b)
    return {"operation": "addition", "a": a, "b": b, "result": result}