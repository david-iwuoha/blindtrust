from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3
import uuid
from datetime import datetime
import os

app = FastAPI()

# Path to the database file and schema file
db_path = os.path.join(os.getcwd(), 'blindtrust.db')
schema_path = os.path.join(os.getcwd(), 'db', 'schema.sql')

# Function to initialize the database and create tables
def initialize_database():
    if not os.path.exists(db_path):
        # If database doesn't exist, create it and execute schema
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Open and execute schema.sql to create the tables
        with open(schema_path, 'r') as f:
            cursor.executescript(f.read())
        
        conn.commit()
        conn.close()
        print("Database initialized and tables created.")
    else:
        print("Database already exists, skipping initialization.")

# Initialize the database when the app starts
initialize_database()

# Database helper function to create user and seed balance
def create_user_and_seed_balance(name: str, phone: str, language: str):
    user_id = str(uuid.uuid4())
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Connect to SQLite and insert user data
    conn = sqlite3.connect('blindtrust.db')
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO users (id, name, phone, language, created_at) VALUES (?, ?, ?, ?, ?)",
                   (user_id, name, phone, language, created_at))
    conn.commit()
    
    # Seed the user’s account with 10,000 demo Naira
    cursor.execute("INSERT INTO accounts (id, user_id, balance, created_at) VALUES (?, ?, ?, ?)",
                   (str(uuid.uuid4()), user_id, 10000, created_at))
    conn.commit()
    conn.close()

    return user_id, 10000

# Define the signup request and response models
class SignupRequest(BaseModel):
    name: str
    phone: str
    language: str

class SignupResponse(BaseModel):
    user_id: str
    token: str
    seeded_balance: int

@app.post("/signup", response_model=SignupResponse)
async def signup(request: SignupRequest):
    user_id, seeded_balance = create_user_and_seed_balance(request.name, request.phone, request.language)
    token = "generated_token"  # Placeholder for token generation logic
    return SignupResponse(user_id=user_id, token=token, seeded_balance=seeded_balance)
