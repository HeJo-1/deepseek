import requests

def fetch_content(input_value):
    url = f"https://deepseek-r1.istebutolga.workers.dev/?prompt={input_value}"
    response = requests.get(url)
    if response.status_code == 200:
        print(response.content.decode('utf-8'))
    else:
        print(f"Error: {response.status_code}")

if __name__ == "__main__":
    user_input = input("Lütfen bir input girin: ")
    fetch_content(user_input)