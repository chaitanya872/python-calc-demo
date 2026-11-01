from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI(title="Calculator API")

@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <html>
        <head>
            <title>Web Calculator</title>
            <style>
                body { font-family: Arial, sans-serif; text-align: center; margin-top: 50px; }
                input, button { padding: 10px; margin: 5px; font-size: 16px; }
            </style>
        </head>
        <body>
            <h1>Simple Calculator</h1>
            <input type="number" id="num1" placeholder="Number 1">
            <input type="number" id="num2" placeholder="Number 2">
            <br>
            <button onclick="calculate('add')">Add</button>
            <button onclick="calculate('subtract')">Subtract</button>
            <button onclick="calculate('divide')">Divide</button>
            <h2 id="result">Result: </h2>
            
            <script>
                async function calculate(operation) {
                    const a = document.getElementById('num1').value;
                    const b = document.getElementById('num2').value;
                    const response = await fetch(`/${operation}?a=${a}&b=${b}`);
                    const data = await response.json();
                    
                    if (response.ok) {
                        document.getElementById('result').innerText = 'Result: ' + data.result;
                    } else {
                        document.getElementById('result').innerText = 'Error: ' + data.detail;
                    }
                }
            </script>
        </body>
    </html>
    """

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