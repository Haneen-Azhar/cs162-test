#Question 1
import requests

# Base URL for all httpbin requests
base_url = "https://httpbin.org/"

def login_with_basic_auth():
    """Log in using basic authentication."""
    endpoint = base_url + "basic-auth/user/passwd"
    response = requests.get(endpoint, auth=('user', 'passwd'))
    print("Authentication Response:", response.text)

def fetch_image():
    """Download an image file."""
    image_url = base_url + "image/jpeg"
    response = requests.get(image_url)
    with open("output_image.jpeg", "wb") as img_file:
        img_file.write(response.content)
    print(f"Image saved with status: {response.status_code}")

def create_uuid():
    """Generate a UUID version 4."""
    uuid_url = base_url + "uuid"
    response = requests.get(uuid_url)
    print("Generated UUID:", response.text)

def simple_json_fetch():
    """Fetch a basic JSON response."""
    json_url = base_url + "json"
    response = requests.get(json_url)
    print("JSON Response Data:", response.text)

# Execute the functions
login_with_basic_auth()
fetch_image()
create_uuid()
simple_json_fetch()

#Question 2
import requests

def fetch_historical_stock_data(stock_symbol, api_key):
    """Fetch historical stock data for a specific symbol."""
    base_url = "https://api.polygon.io/v1/open-close/"
    chosen_date = "2021-01-01"  # Example date; adjust as needed

    # Create the full API URL with the stock symbol and date
    api_endpoint = f"{base_url}{stock_symbol}/{chosen_date}?apiKey={api_key}"
    response = requests.get(api_endpoint)

    if response.status_code == 200:
        # Convert the response to JSON and return the data
        return response.json()
    else:
        # Print an error message if the request fails
        print("Failed with status code:", response.status_code)
        return None

# Replace 'API_KEY' with the actual key
api_key = "YOUR_API_KEY"
stock_symbol = "AAPL"
data = fetch_historical_stock_data(stock_symbol, api_key)

if data:
    print(data)
    