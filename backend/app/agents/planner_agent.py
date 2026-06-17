from app.services.llm_service import generate_code
import json


class PlannerAgent:

    def plan(self, requirement):

        prompt = f"""
You are a Senior Engineering Manager.

Break the requirement into at most 3 HIGH-LEVEL implementation tasks.

Requirement:

{requirement}

Return ONLY valid JSON.

Format:

{{
  "tasks": [
    "task 1",
    "task 2",
    "task 3"
  ]
}}

Rules:

1. Maximum 3 tasks
2. High-level implementation tasks only
3. Do NOT create micro-tasks
4. Do NOT create more than 3 tasks
5. Return JSON only
6. No markdown
7. No explanations
8. No code fences

Good Example:

{{
  "tasks": [
    "Create Product model",
    "Create Product routes",
    "Update application entry point"
  ]
}}

Bad Example:

{{
  "tasks": [
    "Define attributes",
    "Define data types",
    "Write constructor",
    "Add validation",
    "Add methods",
    "Add comments"
  ]
}}
"""

        print("=" * 50)
        print("PLANNER AGENT")
        print("=" * 50)

        response = generate_code(prompt)

        print("=" * 50)
        print("PLANNER RESPONSE")
        print("=" * 50)

        print(response)

        try:

            plan = json.loads(response)

            if "tasks" not in plan:
                raise Exception("Missing tasks key")

            plan["tasks"] = plan["tasks"][:3]

            return plan

        except Exception as e:

            print("=" * 50)
            print("PLANNER PARSE ERROR")
            print("=" * 50)

            print(e)

            return {
                "tasks": [
                    requirement
                ]
            }