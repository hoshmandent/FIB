#!/bin/bash

# Clone the repository
git clone https://github.com/hoshmandctf/FIB.git

cd FIB

read -p "Do you want to set up FIB credentials? (Y/N): " setup_credentials

if [[ $setup_credentials =~ ^[Yy]$ ]]; then
    python3 setup_credentials.py
fi

read -p "Do you want to run the fib_payment_script to make a test payment? (Y/N): " run_payment

if [[ $run_payment =~ ^[Yy]$ ]]; then
    python3 fib_payment_script.py
fi
