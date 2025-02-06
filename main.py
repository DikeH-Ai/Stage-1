from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from math import sqrt
import requests

app = FastAPI()

# enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def isprime(number: int):  # checks prime status
    if number < 2:
        return False
    for i in range(2, int(sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


def is_perfect(number: int):  # checks perfect status
    if number < 6:
        return False

    divisors_sum = 0

    for i in range(1, (number // 2) + 1):
        if number % i == 0:
            divisors_sum += i
    if divisors_sum == number:
        return True
    return False


def properties(number: int):  # returns number properties
    properties = []

    str_num = str(number)
    num_digits = len(str_num)  # Number of digits in the number
    armstrong_sum = 0

    for i in str_num:
        # Sum of digits raised to the power of number of digits
        armstrong_sum += int(i) ** num_digits

    if armstrong_sum == number:
        properties.append("armstrong")

    if number % 2 == 0:
        properties.append("even")
    else:
        properties.append("odd")

    return properties


def digit_sum(number: int):
    return sum(int(digit) for digit in str(number))


def get_funfact(number: int):
    response = requests.get(f"http://numbersapi.com/{number}?json")
    if response.status_code == 200:
        fact = response.json().get("text", "")
        return fact
    return f"No fun fact available for {number}"


@app.get("/api/classify-number")
async def numclass(number):
    # Check if the input is valid
    try:
        number = int(number)
    except:
        return JSONResponse(
            status_code=400,
            content={
                "number": "alphabet",
                "error": True
            }
        )
    is_prime = isprime(number)
    perfect = is_perfect(number)
    proper = properties(number)
    fun_fact = get_funfact(number)

    return {
        "number": number,
        "is_prime": is_prime,
        "is_perfect": perfect,
        "properties": proper,
        "digit_sum": digit_sum(number),
        "fun_fact": fun_fact
    }
