from fastapi import FastAPI, HTTPException
import uvicorn

app = FastAPI(title="Calculator API")

@app.get("/")
def read_root():
    return {"message": "Calculator is running. Navigate to /docs to use the UI."}

@app.get("/add")
def add(a: float, b: float):
    return {"operation": "addition", "result": a + b}

@app.get("/subtract")
def subtract(a: float, b: float):
    return {"operation": "subtraction", "result": a - b}

@app.get("/divide")
def divide(a: float, b: float):
    if b == 0:
        raise HTTPException(status_code=400, detail="Cannot divide by zero")
    return {"operation": "division", "result": a / b}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)