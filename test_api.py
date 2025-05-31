"""
Test script for the PostgreSQL CRUD API
"""
import requests
import json
import time

BASE_URL = "http://localhost:5000"

def test_api():
    """Test the CRUD API endpoints"""
    print("Testing PostgreSQL CRUD API...")
    
    # Setup database
    print("\nSetting up database:")
    response = requests.get(f"{BASE_URL}/setup")
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    
    # Test GET /users (initially empty)
    print("\n1. Getting all users (should be empty initially):")
    response = requests.get(f"{BASE_URL}/users")
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    
    # Test POST /users (create a user)
    print("\n2. Creating a new user:")
    new_user = {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "age": 30
    }
    response = requests.post(f"{BASE_URL}/users", json=new_user)
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    
    # Get the user ID from the response
    user_id = response.json().get("id")
    
    # Test GET /users (should now have one user)
    print("\n3. Getting all users (should have one user now):")
    response = requests.get(f"{BASE_URL}/users")
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    
    # Test GET /users/{id} (get the specific user)
    print(f"\n4. Getting user with ID {user_id}:")
    response = requests.get(f"{BASE_URL}/users/{user_id}")
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    
    # Test PUT /users/{id} (update the user)
    print(f"\n5. Updating user with ID {user_id}:")
    updated_user = {
        "name": "John Doe Updated",
        "age": 31
    }
    response = requests.put(f"{BASE_URL}/users/{user_id}", json=updated_user)
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    
    # Test GET /users/{id} (get the updated user)
    print(f"\n6. Getting updated user with ID {user_id}:")
    response = requests.get(f"{BASE_URL}/users/{user_id}")
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    
    # Test DELETE /users/{id} (delete the user)
    print(f"\n7. Deleting user with ID {user_id}:")
    response = requests.delete(f"{BASE_URL}/users/{user_id}")
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    
    # Test GET /users (should be empty again)
    print("\n8. Getting all users (should be empty again):")
    response = requests.get(f"{BASE_URL}/users")
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    
    print("\nAPI testing complete!")

if __name__ == "__main__":
    # Wait for services to be ready
    print("Waiting for services to be ready...")
    time.sleep(5)
    test_api()