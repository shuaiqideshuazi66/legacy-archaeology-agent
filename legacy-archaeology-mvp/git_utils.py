from git import Repo

def recent_commits(repo_path, file_path, limit=3):
    repo = Repo(repo_path)
    commits = list(repo.iter_commits(paths=file_path, max_count=limit))
    return [
        {
            "hash": c.hexsha[:7],
            "author": c.author.name,
            "date": c.committed_datetime.strftime("%Y-%m-%d"),
            "msg": c.message.strip()
        }
        for c in commits
    ]
