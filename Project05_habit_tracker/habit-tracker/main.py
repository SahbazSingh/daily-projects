import requests
from datetime import datetime
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

USERNAME = "baz02"
TOKEN = os.getenv("PIXELA_TOKEN")
GRAPH_ID = "graph02"

pixela_endpoint = "https://pixe.la/v1/users"
headers = {
    "X-USER-TOKEN": TOKEN
}


# 1. Create User (run only once)
def create_user():
    user_params = {
        "token": TOKEN,
        "username": USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes",
    }
    response = requests.post(url=pixela_endpoint, json=user_params)
    print("User:", response.text)


# 2. Create Graph (run only once)
def create_graph():
    graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
    graph_config = {
        "id": GRAPH_ID,
        "name": "Cycling Graph",
        "unit": "Km",
        "type": "float",
        "color": "ajisai"
    }
    response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
    print("Graph:", response.text)


# 3. Add pixel for today
def add_pixel():
    pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
    today = datetime.now().strftime("%Y%m%d")
    quantity = input("How many kilometers did you cycle today? ")
    pixel_data = {
        "date": today,
        "quantity": quantity,
    }
    response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
    print("Add Pixel:", response.text)


# 4. Update today's pixel
def update_pixel(new_quantity="4.5"):
    today = datetime.now().strftime("%Y%m%d")
    update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"
    new_pixel_data = {
        "quantity": new_quantity
    }
    response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
    print("Update Pixel:", response.text)


# 5. Delete today's pixel
def delete_pixel():
    today = datetime.now().strftime("%Y%m%d")
    delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"
    response = requests.delete(url=delete_endpoint, headers=headers)
    print("Delete Pixel:", response.text)


# Main entry point
if __name__ == "__main__":
    # Uncomment the action you want to perform:

    # create_user()
    # create_graph()
    add_pixel()
    # update_pixel("7.2")
    # delete_pixel()