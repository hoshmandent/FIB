#!/usr/bin/env python

import os

def main():
    client_id = input("Enter your client_id: ")
    client_secret = input("Enter your client_secret: ")

    with open('.env', 'w') as env_file:
        env_file.write(f"client_id={client_id}\n")
        env_file.write(f"client_secret={client_secret}\n")

    print("Credentials have been saved to .env file.")

if __name__ == "__main__":
    main()
