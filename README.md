# Code Analysis and Optimization with Gemini and GitHub

This project utilizes a large language model (Gemini) to analyze Python code from GitHub repositories and provide suggestions for improvement, optimization, test case development, and bug identification.

Key Features:

. Retrieves code from GitHub repositories: Fetches code using the GitHub API based on user input.
. Integrates with Gemini for code analysis: Sends code snippets to Gemini for analysis and generates suggestions.
. Supports various objectives: Allows users to choose from different analysis goals, including code improvement, optimization, test case development, and bug identification.
. Generates a text-based report: Creates a report summarizing key findings and suggestions after each analysis.
. Securely stores tokens: Uses a .env file to securely store GitHub and Gemini API tokens.

# How to Use

## Install dependencies

```bash
pip install github google-generativeai python-dotenv

GITHUB_TOKEN=your_github_token_here
GOOGLE_API_KEY=your_google_api_key_here ```

## Run Script
 ```bash
python main.py
