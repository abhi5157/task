import github
import os

import google.generativeai as genai
from dotenv import load_dotenv  # Import the dotenv library


load_dotenv()  # Load environment variables from a .env file

# Access tokens from environment variables
github_token = os.getenv("GITHUB_TOKEN")
google_api_key = os.getenv("GOOGLE_API_KEY")

# Github API authentication
g = github.Github(github_token)

# gemini ai authentication
genai.configure(api_key=google_api_key)
model = genai.GenerativeModel('gemini-pro')

def analyze_code(repo_name, file_path, objective):
    repo = g.get_repo(repo_name)
    contents = repo.get_contents(file_path)
    code = contents.decoded_content.decode()
    print(code)

    p = ""
    if objective==1 :
        p = "Improve code and optimize it  and gave optimized code"
    elif objective ==2:
        p = "Improve code performance and udate this code, Identifying areas for efficiency increase, such as reducing time complexity and gave optimized code."
    elif objective==3:
        p = "Strengthen testing and validation. Suggest additional test cases for better coverage."
    else:
        p = "Identify and fix potential bugs,  Pinpointing bugs with possible solutions or preventive measures."

    prompt = f"Analyze this Python code:\n\n{code}\n\n  {p}"
    response = model.generate_content(prompt, stream=True)

    print("Observation applying")

    for chunk in response:
        print(chunk.text)
        # print("_" * 100)



def main():
    user_name = input("Enter GitHub username: ")

    # Get all repositories for the user
    user = g.get_user(user_name)
    repos = user.get_repos()

    # Display repository names
    for repo in repos:
        print(repo.name)

    repo_name = input("Enter the name of the repository to analyze: ")

    repo_path = f"{user_name}/{repo_name}"
    print(repo_path)

    file_path = input("Enter the path of the file to analyze: ")

    objective = input("Choose an objective:\n1. Code Improvement\n2. Code Optimization\n3. Test Case Development\n4. Bug Identification and Resolution\n")

    analyze_code(repo_path, file_path, objective)



if __name__ == "__main__":
    main()