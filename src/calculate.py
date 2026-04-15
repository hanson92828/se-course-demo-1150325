from fastapi import FastAPI

app = FastAPI()

def add_func(a: float,b: float) -> float:
    return a+b

def sub_func(a,b):
    return a-b

def mut_func(a,b):
    # temp = 100 # non-use, ruff會報錯
    return a-b

# -------------

@app.get("/")
def home():
    return {"status": "Online", "message": "這是簡易計算機 API"}

@app.get("/add")
def calculate_add(a: float, b: float):
    # add_func
    result = add_func(a, b)
    return {"operation": "addition", "a": a, "b": b, "result": result}

@app.get("/sub")
def calculate_sub(a,b):
    # sub_func
    result = sub_func(a, b)
    return {"operation": "substraction", "a": a, "b": b, "result": result}

@app.get("/mut")
def calculate_mut(a,b):
    # mut_func
    result = mut_func(a, b)
    return {"operation": "multiple", "a": a, "b": b, "result": result}