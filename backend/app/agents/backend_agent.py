from app.tools.file_tools import (
    list_files,
    read_file,
    write_file
)

from app.tools.json_tools import (
    parse_agent_response
)

from app.services.llm_service import generate_code


class BackendAgent:

    def execute(self, task):

        print("=" * 50)
        print("STEP 1: Reading repository")
        print("=" * 50)

        files = list_files("workspace/sample_repo")

        print("FILES FOUND:")
        print(files)

        context = ""

        for file in files:

            try:

                content = read_file(file)

                context += f"""

FILE: {file}

{content}

"""

            except Exception as e:

                print(f"ERROR READING {file}")
                print(e)

        print("=" * 50)
        print("STEP 2: Sending prompt")
        print("=" * 50)

        prompt = f"""
You are a senior backend engineer.

Repository:

{context}

Task:

{task}

Return ONLY valid JSON.

Format:

{{
  "files": [
    {{
      "action": "create",
      "path": "models/product.py",
      "content": "full file content"
    }},
    {{
      "action": "modify",
      "path": "app.py",
      "content": "full updated file content"
    }}
  ]
}}

Rules:

1. action must be either "create" or "modify"
2. Return JSON only
3. No markdown
4. No explanations
5. No code fences
6. content must contain the FULL file content
7. If modifying a file, return the complete updated file
"""

        result = generate_code(prompt)

        print("=" * 50)
        print("MODEL RESPONSE")
        print("=" * 50)

        print(result)

        print("=" * 50)
        print("STEP 3: Parsing Response")
        print("=" * 50)

        parsed = parse_agent_response(result)

        if not parsed:

            return {
                "success": False,
                "message": "Invalid JSON from model"
            }

        files_processed = 0

        for file in parsed["files"]:

            action = file["action"]

            target_path = (
    "workspace/sample_repo/" +
    file["path"]
)

            print()
            print("=" * 50)
            print(f"ACTION: {action.upper()}")
            print(f"TARGET: {target_path}")
            print("=" * 50)

            try:

                if action == "modify":

                    try:
                        old_content = read_file(target_path)

                        print("OLD CONTENT:")
                        print(old_content)

                    except Exception:
                        print("FILE DOES NOT EXIST YET")

                write_file(
                    target_path,
                    file["content"]
                )

                print()
                print("NEW CONTENT:")
                print(file["content"])

                files_processed += 1

            except Exception as e:

                print("WRITE ERROR")
                print(e)

        print("=" * 50)
        print("STEP 4: COMPLETE")
        print("=" * 50)

        return {
            "success": True,
            "files_processed": files_processed
        }