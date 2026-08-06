
# Jared Morris
# Module 9 Assignment
# Open Notify Astronaut API Tutorial

import json
import requests

ASTRONAUT_URL = "http://api.open-notify.org/astros.json"


def test_connection(url):
    """Test the API connection and return the response."""
    try:
        response = requests.get(url, timeout=10)
        print("Connection status code:", response.status_code)
        response.raise_for_status()
        return response
    except requests.RequestException as error:
        print("The API connection failed:", error)
        return None


def print_astronauts(data):
    """Print the current astronauts in a readable format."""
    print("\nCurrent Astronauts in Space")
    print("---------------------------")
    print("Total people in space:", data["number"])

    for person in data["people"]:
        print(f"{person['name']} is aboard the {person['craft']}.")


def main():
    response = test_connection(ASTRONAUT_URL)

    if response is None:
        return

    astronaut_data = response.json()

    print("\nUnformatted API response:")
    print(response.text)

    print("\nFormatted JSON response:")
    print(json.dumps(astronaut_data, indent=4))

    print_astronauts(astronaut_data)


if __name__ == "__main__":
    main()

