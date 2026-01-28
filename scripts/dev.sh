#!/bin/bash

echo "Starting Movie Website Development Environment..."

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install dependencies if needed
if [ ! -f ".deps_installed" ]; then
    echo "Installing dependencies..."
    pip install -r requirements.txt
    touch .deps_installed
fi

# Create environment file if it doesn't exist
if [ ! -f ".env" ]; then
    cp .env.example .env
fi

# Setup database and seed data
echo "Setting up database..."
cd backend
python -m app.utils.seed_books
cd ..

# Start the backend server
echo "Starting backend server..."
cd backend
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000