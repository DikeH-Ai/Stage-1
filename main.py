from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from math import sqrt
import httpx
import requests
from functools import lru_cache

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
    if number % 2 == 0:
        return number == 2
    for i in range(3, int(sqrt(number)) + 1, 2):
        if number % i == 0:
            return False
    return True


def is_perfect(number: int):  # checks perfect status
    if number < 6:
        return False

    divisors_sum = 1
    sqrt_num = int(sqrt(number))

    for i in range(2, sqrt_num + 1):
        if number % i == 0:
            divisors_sum += i
            if i != number // i:
                divisors_sum += number // i
    return divisors_sum == number


def properties(number: int):
    properties = []
    str_num = str(abs(number))
    num_digits = len(str_num)
    armstrong_sum = sum(
        int(digit) ** num_digits for digit in str_num)

    if armstrong_sum == number:
        properties.append("armstrong")

    properties.append("even" if number % 2 == 0 else "odd")

    return properties


def digit_sum(number: int):
    return sum(int(digit) for digit in str(abs(number)))


@lru_cache(maxsize=100)
async def get_funfact(number: int):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"http://numbersapi.com/{number}?json")
        if response.status_code == 200:
            return response.json().get("text", "")
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
                "error": True,
                "number": f"{number}",
            }
        )
    is_prime = isprime(number)
    perfect = is_perfect(number)
    proper = properties(number)
    fun_fact = await get_funfact(number)

    return {
        "number": number,
        "is_prime": is_prime,
        "is_perfect": perfect,
        "properties": proper,
        "digit_sum": digit_sum(number),
        "fun_fact": fun_fact
    }
