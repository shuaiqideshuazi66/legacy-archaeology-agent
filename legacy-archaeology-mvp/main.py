from tqdm import tqdm
from repo_utils import scan_repo
from git_utils import recent_commits
from agent import ArchaeologyAgent
from config import REPO_PATH

def main():
    agent = ArchaeologyAgent()
    files = scan_repo(REPO_PATH)
    report = ["# 🏺 遗留系统自动考古报告\n"]

    for f in tqdm(files, desc="Analyzing"):
        commits = recent_commits(REPO_PATH, f["path"])
        result = agent.analyze(f["path"], f["content"], commits)
        report.append(f"## {f['path']}\n")
        report.append(result + "\n")

    with open("ARCHAEOLOGY_REPORT.md", "w", encoding="utf-8") as out:
        out.write("\n".join(report))

    print("✅ 分析完成，已生成 ARCHAEOLOGY_REPORT.md")

if __name__ == "__main__":
    main()
