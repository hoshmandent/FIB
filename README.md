# First Iraqi Bank (FIB) API Payment Script

This Python script interacts with the First Iraqi Bank (FIB) API to authenticate, create a payment, and check the payment status until it changes to "paid." The script uses the `requests` library to make HTTP requests to the FIB API and `dotenv` to load environment variables from a `.env` file.

## Prerequisites
Before running the script, ensure you have the following:

1. Python 3.x installed on your system.
1. An account with First Iraqi Bank (FIB) and valid API credentials (Client ID and Client Secret).
1. Internet connectivity to access the FIB API.

## Setup

1. Clone this repository or download the script file to your local machine.

2. Create a .env file in the same directory as the script and add the following lines:

```plaintext
client_id=YOUR_CLIENT_ID
client_secret=YOUR_CLIENT_SECRET
```
Replace YOUR_CLIENT_ID and YOUR_CLIENT_SECRET with your actual FIB API credentials.

3. Install the required Python packages by running the following command in your terminal or command prompt:

```bash
pip install requests python-dotenv
```

## How to Use

1. Ensure you have completed the setup steps mentioned above.
1. Open a terminal or command prompt and navigate to the directory containing the script.
1. Run the script by executing the following command:

```bash
python fib_payment_script.py
```

The script will perform the following actions:

1. Authenticate with the FIB API using the provided client credentials.
1. Create a payment with a monetary value of 120,000.00 IQD and a description.
1. Save the generated QR code image to a file named "output.png" in the same directory.
1. Continuously check the payment status until it changes to "paid." It will print "Payment was made" once the payment is successfully paid.

Please note that the script will wait for the payment to be paid, and this process may take some time depending on the FIB API response.

`Important`: Make sure to keep your API credentials (`client_id` and `client_secret`) secure and do not share them publicly.

## Troubleshooting

1. If you encounter any issues, ensure that your internet connection is stable and that the FIB API is accessible.
1. Double-check that the .env file contains the correct `client_id` and `client_secret`.
1. If you have problems saving the QR code image, check the file path and permissions.

For any additional assistance or inquiries, please contact First Iraqi Bank (FIB) support or refer to the official API documentation.

`Note`: This script is provided as-is without warranty. Use it responsibly and at your own risk. The author is not responsible for any misuse or damage caused by this script.

## Getting Started

this is a bash one liner that will clone the project and run the setup_credentials.py file then it will run the fib_payment_script.py to create a test payment based on the given credentials.

```bash
wget https://raw.githubusercontent.com/hoshmandctf/FIB/main/setup.sh && \
chmod +x setup.sh && ./setup.sh
```