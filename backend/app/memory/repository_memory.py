from app.tools.file_tools import list_files


class RepositoryMemory:

    def build(self, repo_path):

        files = list_files(repo_path)

        summary = {
            "files": [],
            "models": [],
            "routes": [],
            "sql_files": []
        }

        for file in files:

            summary["files"].append(file)

            lower = file.lower()

            if "/models/" in lower or "\\models\\" in lower:
                summary["models"].append(file)

            if "/routes/" in lower or "\\routes\\" in lower:
                summary["routes"].append(file)

            if lower.endswith(".sql"):
                summary["sql_files"].append(file)

        return summary