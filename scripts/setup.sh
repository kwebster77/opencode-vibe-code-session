#!/bin/bash

echo "Setting up Movie Website Backend..."

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create environment file
cp .env.example .env

echo "Setup complete! To run the server:"
echo "1. Activate virtual environment: source venv/bin/activate"
echo "2. Run the server: cd backend && python -m app.main"
echo "or: cd backend && uvicorn app.main:app --reload --host 0.0.0.0 --port 8000"