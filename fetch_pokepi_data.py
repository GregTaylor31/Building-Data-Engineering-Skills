import requests
import urllib3
import certifi

def fetch_data(url):
    try:
        response = requests.get(url, verify=certifi.where())
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error occurred: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    url = "https://pokeapi.co/api/v2/pokemon/charmander"
    data = fetch_data(url)
    if data:
        print(data)

if __name__ == "__main__":
    main()