Sure! Here's a README template for your FastAPI application, explaining the purpose, setup, and usage:

---

# FastAPI Number Classifier

This FastAPI application provides an endpoint to classify numbers based on various mathematical properties, such as prime, perfect, Armstrong, and others. Additionally, it returns fun facts about the number and the sum of its digits.

## Features

- **Prime Check**: Determines if a number is prime.
- **Perfect Number Check**: Determines if a number is a perfect number.
- **Properties**: Returns whether a number is even or odd and if it's an Armstrong number.
- **Digit Sum**: Computes the sum of the digits of the number.
- **Fun Fact**: Fetches a fun fact about the number from the Numbers API.
- **Custom Error Handling**: If an invalid input (non-integer) is provided, a custom error message is returned.

## Requirements

- Python 3.7 or higher
- FastAPI
- Uvicorn (for running the application)
- Requests (for fetching fun facts from an API)

## Installation

1. **Clone the repository** (or just download the Python script):

   ```bash
   git clone <repository_url>
   ```

2. **Navigate to the project directory**:

   ```bash
   cd fastapi-number-classifier
   ```

3. **Create a virtual environment** (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

4. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

   Or manually install the required packages:

   ```bash
   pip install fastapi uvicorn requests
   ```

## Running the Application

You can run the FastAPI application using Uvicorn. Use the following command:

```bash
uvicorn main:app --reload
```

- `main` refers to the Python file (`main.py`).
- `--reload` enables automatic reloading of the server during development.

Once the application starts, it will be accessible at `http://127.0.0.1:8000`.

## API Endpoints

### `GET /api/classify-number?number=<int_or_string>`

This endpoint classifies a number based on its properties. You need to provide a number as a query parameter.

#### Parameters:
- `number`: An integer (or string). If the input is invalid (non-integer), a custom error message will be returned.

#### Response:

**Success (200 OK):**
```json
{
    "number": 28,
    "is_prime": false,
    "is_perfect": true,
    "properties": ["even"],
    "digit_sum": 10,
    "fun_fact": "28 is a perfect number."
}
```

**Error (400 Bad Request):**
If an invalid value is passed (such as a string), the response will be:
```json
{
    "number": "alphabet",
    "error": true
}
```

#### Examples:

1. **Valid Request**:
   ```
   GET /api/classify-number?number=28
   ```
   **Response**:
   ```json
   {
       "number": 28,
       "is_prime": false,
       "is_perfect": true,
       "properties": ["even"],
       "digit_sum": 10,
       "fun_fact": "28 is a perfect number."
   }
   ```

2. **Invalid Request**:
   ```
   GET /api/classify-number?number=alphabet
   ```
   **Response**:
   ```json
   {
       "number": "alphabet",
       "error": true
   }
   ```

## Custom Error Handling

If the user provides an invalid number (like a string), the application will return a custom error response:
```json
{
    "number": "invalid_value",
    "error": true
}
```

## How It Works

1. The application accepts a number (as a query parameter).
2. If the number is valid:
   - It checks whether the number is **prime**.
   - It checks whether the number is **perfect**.
   - It calculates the **digit sum**.
   - It checks the number's **properties** (Armstrong, even/odd).
   - It fetches a **fun fact** from the Numbers API.
3. If the input is invalid (non-integer), it returns a custom error message.

## Testing the API

You can test the API using any HTTP client, such as:
- **Postman**
- **curl**
- **Browser** (for simple GET requests)

### Example `curl` command:

```bash
curl "http://127.0.0.1:8000/api/classify-number?number=28"
```

This will return a JSON response with the number's classification.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to adjust any of the information as needed or add more details based on your requirements!