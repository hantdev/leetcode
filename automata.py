import os
import re
import requests

def extract_problem_info(file_path):
    match = re.match(r"(\d+)-([a-z0-9-]+)\.py", os.path.basename(file_path))
    if match:
        problem_number, slug = match.groups()
        return int(problem_number), slug, f"[{slug.replace('-', ' ').title()}](https://leetcode.com/problems/{slug}/description/)"
    return None, None, None

def get_problem_difficulty(slug):
    url = "https://leetcode.com/graphql"
    query = """
    query getQuestionDifficulty($titleSlug: String!) {
      question(titleSlug: $titleSlug) {
        difficulty
      }
    }
    """
    response = requests.post(url, json={"query": query, "variables": {"titleSlug": slug}})
    try:
        data = response.json()
        return data["data"]["question"]["difficulty"]
    except (KeyError, TypeError):
        return "Unknown"

def build_readme():
    topics = [d for d in os.listdir('.') if os.path.isdir(d)]
    problem_entries = []
    
    for topic in topics:
        for file in os.listdir(topic):
            if file.endswith(".py"):
                problem_number, slug, problem_title = extract_problem_info(file)
                if problem_number:
                    difficulty = get_problem_difficulty(slug)
                    problem_entries.append((problem_number, problem_title, f"[Python](./{topic}/{file})", topic.replace('_', ' ').title(), difficulty))
    
    problem_entries.sort()
    
    table_header = "| # | Title | Solution | Type | Difficulty |\n|---| ----- | -------- | ---------- | ---------- |"
    table_rows = []
    
    for number, title, solution, topic, difficulty in problem_entries:
        table_rows.append(f"|{number:04d}|{title}|{solution}|{topic}| {difficulty} |")
    
    table_content = "\n".join([table_header] + table_rows)
    readme_content = f"""# Coding Everyday Until I Get A Job

## LeetCode Solutions

{table_content}
"""
    
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme_content)

if __name__ == "__main__":
    build_readme()
    print("README.md has been updated!")
