import os
import re
import requests

def extract_problem_info(file_path):
    match = re.match(r"(\d+)-([a-z0-9-]+)\.py", os.path.basename(file_path))
    if match:
        problem_number, slug = match.groups()
        return int(problem_number), slug, f"[{slug.replace('-', ' ').title()}](https://leetcode.com/problems/{slug}/description/)"
    return None, None, None

def get_problem_stats(slug):
    url = "https://leetcode.com/graphql"
    query = """
    query getQuestionStats($titleSlug: String!) {
      question(titleSlug: $titleSlug) {
        difficulty
        topicTags {
          name
        }
      }
    }
    """
    response = requests.post(url, json={"query": query, "variables": {"titleSlug": slug}})
    try:
        data = response.json()["data"]["question"]
        difficulty = data["difficulty"]
        tags = ", ".join(tag["name"] for tag in data["topicTags"])
        return difficulty, tags
    except (KeyError, TypeError):
        return "Unknown", "Unknown"

def build_readme():
    topics = [d for d in os.listdir('.') if os.path.isdir(d)]
    problem_entries = []
    
    for topic in topics:
        for file in os.listdir(topic):
            if file.endswith(".py"):
                problem_number, slug, problem_title = extract_problem_info(file)
                if problem_number:
                    difficulty, tags = get_problem_stats(slug)
                    problem_entries.append((problem_number, problem_title, f"[Python](./{topic}/{file})", difficulty, tags))
    
    problem_entries.sort()
    
    table_header = "| # | Title | Solution | Tags | Difficulty |\n|---| ----- | -------- | ---------- | ---- |"
    table_rows = []
    
    for number, title, solution, tags, difficulty in problem_entries:
        table_rows.append(f"|{number:04d}|{title}|{solution}| {tags} | {difficulty} | ")
    
    table_content = "\n".join([table_header] + table_rows)
    readme_content = f"""# 📌 LeetCode Solutions - Coding Every Day Until I Get A Job

Welcome to my LeetCode solutions repository! 🚀 Here, I solve coding challenges every day to improve my problem-solving skills and prepare for technical interviews. 

## 🔥 Problem List

{table_content}

## 🚀 Keep Coding & Stay Motivated!

Happy coding! 😊"""
    
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme_content)

if __name__ == "__main__":
    build_readme()
    print("README.md has been updated!")
