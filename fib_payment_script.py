import requests
import base64
import time
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the client_id and client_secret from environment variables
CLIENT_ID = os.getenv('client_id')
CLIENT_SECRET = os.getenv('client_secret')

# Define the FIB API URL
FIB_API_URL = "https://fib.stage.fib.iq"

# Function to save the QR code image to a file
def save_qrcode_to_file(base64_data, file_path):
    try:
        # Decode the base64 data
        binary_data = base64.b64decode(base64_data)

        # Save the binary data to the file
        with open(file_path, 'wb') as file:
            file.write(binary_data)
        
        print(f"QR code saved to: {file_path}")
    except Exception as e:
        print(f"Error saving QR code: {e}")

# Function to authenticate with the FIB API and obtain an access token
def authenticate(client_id, client_secret):
    url = f"{FIB_API_URL}/auth/realms/fib-online-shop/protocol/openid-connect/token"
    
    data = {
        'grant_type': "client_credentials",
        'client_id': client_id,
        'client_secret': client_secret,
    }
    
    # Send a POST request to obtain the access token
    response = requests.post(url, data=data)
    response.raise_for_status()

    # Extract and return the access token from the JSON response
    return response.json()['access_token']

# Function to create a payment with the FIB API
def create_payment(token, data):
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    url = f"{FIB_API_URL}/protected/v1/payments"

    # Send a POST request to create the payment
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()

    # Return the API response
    return response

# Function to check the status of a payment with the FIB API
def check_payment(token, payment_id):
    url = f"{FIB_API_URL}/protected/v1/payments/{payment_id}/status"
    headers = {
        'Authorization': f'Bearer {token}'
    }

    # Send a GET request to check the payment status
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    # Return the API response
    return response

if __name__ == "__main__":
    try:
        # Authenticate with the FIB API
        token = authenticate(CLIENT_ID, CLIENT_SECRET)

        # Data for creating a payment
        data = {
            "monetaryValue": {
                "amount": "120000.00",
                "currency": "IQD"
            },
            "description": "test"
        }

        # Create a payment and obtain the payment ID and QR code
        response = create_payment(token, data)
        response_json = response.json()
        payment = response_json['paymentId']
        qr_code = response_json['qrCode'].split(',')[-1]

        # Save the QR code to a file
        save_qrcode_to_file(qr_code, os.path.join(os.getcwd(), "output.png"))
        print(response_json['readableCode'])

        # Continuously check the payment status until it changes to "paid"
        while True:
            response = check_payment(token, payment)
            status = response.json()['status']
            
            if status == 'PAID':
                print('Payment was made')
                break
            time.sleep(5)

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    except KeyError as e:
        print(f"Response data is missing key: {e}")
    except Exception as e:
        print(f"Unknown error occurred: {e}")
