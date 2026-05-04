from fastapi import FastAPI

app = FastAPI()


def add_func(a, b):
    return a + b


def sub_func(a, b):
    # temp = 123  # non-use var
    return a - b


def mut_func(a: float, b: float) -> float:
    # return "123"
    return a * b


@app.get("/")
def home():
    return {"這是簡易計算機"}


@app.get("/add")
def calculate_add(a: float, b: float):
    result = add_func(a, b)
    return {"operation:": "addition", "a": a, "b": b, "result": result}
