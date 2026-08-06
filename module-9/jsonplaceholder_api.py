
# Jared Morris
# Module 9 Assignment
# JSONPlaceholder API Program

import json
import requests

API_URL = "https://jsonplaceholder.typicode.com/users/1"


def test_connection(url):
    """Connect to the API and return the response."""
    try:
        response = requests.get(url, timeout=10)
        print("Connection status code:", response.status_code)
        response.raise_for_status()
        return response
    except requests.RequestException as error:
        print("The API connection failed:", error)
        return None


def print_formatted_user(user):
    """Print selected user information in a readable format."""
    print("\nFormatted User Information")
    print("--------------------------")
    print("Name:", user["name"])
    print("Username:", user["username"])
    print("Email:", user["email"])
    print("Phone:", user["phone"])
    print("Website:", user["website"])
    print("Company:", user["company"]["name"])
    print(
        "Address:",
        f"{user['address']['street']}, "
        f"{user['address']['suite']}, "
        f"{user['address']['city']} "
        f"{user['address']['zipcode']}"
    )


def main():
    response = test_connection(API_URL)

    if response is None:
        return

    print("\nResponse with no formatting:")
    print(response.text)

    user_data = response.json()

    print("\nJSON response with indentation:")
    print(json.dumps(user_data, indent=4))

    print_formatted_user(user_data)


if __name__ == "__main__":
    main()

