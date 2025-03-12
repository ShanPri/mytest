import requests

def get_github_repos(username):
    url = f"https://api.github.com/users/{username}/repos"
    try:
        response = requests.get(url)
        response.raise_for_status()
        repos = response.json()
        if repos:
            print(f"\nPublic repositories for user '{username}':")
            for repo in repos:
                print(f"- {repo['html_url']}")  # Print the URL of the repository
        else:
            print(f"No public repositories found for user '{username}'.")
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred for user '{username}': {http_err}")
    except requests.exceptions.RequestException as err:
        print(f"Error occurred for user '{username}': {err}")

def fetch_repos_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            usernames = file.readlines()
            for username in usernames:
                username = username.strip()  # Remove whitespace/newline characters
                if username:
                    get_github_repos(username)
    except FileNotFoundError:
        print(f"The file {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Specify the path to your text file
file_path = 'usernames.txt'
fetch_repos_from_file(file_path)
