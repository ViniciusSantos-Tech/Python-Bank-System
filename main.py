import uvicorn
import bank
from api import app 

def start_system():
    print("--- Phase 1: Database Setup ---")
    try:
        bank.Base.metadata.create_all(bind=bank.engine)
        print("Database tables verified/created.")
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return
    print("\n--- Phase 2: Starting API Server ---")
    uvicorn.run(app, host="127.0.0.1", port=8000)

if __name__ == "__main__":
    start_system()
