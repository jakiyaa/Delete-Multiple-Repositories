import requests

username = "YOUR_GITHUB_USERNAME"
token = "YOUR_PERSONAL_ACCESS_TOKEN"

repos_to_delete = [
    "repo-name-1",
    "repo-name-2",
    "repo-name-3"
]


for repo in repos_to_delete:
    url = f"https://api.github.com/repos/{username}/{repo}"
    response = requests.delete(url, auth=(username, token))
    
    if response.status_code == 204:
        print(f"Deleted {repo} successfully.")
    else:
        print(f"Failed to delete {repo}: {response.status_code}, {response.text}")
