from fastapi import APIRouter

from app.agents.backend_agent import BackendAgent
from app.agents.planner_agent import PlannerAgent

from app.schemas.request_schema import AgentRequest

router = APIRouter()

planner = PlannerAgent()
backend_agent = BackendAgent()


@router.post("/generate")
def generate(req: AgentRequest):

    plan = planner.plan(
        req.requirement
    )

    results = []
    MAX_TASKS = 3

    for task in plan["tasks"][:MAX_TASKS]:

        print()
        print("=" * 50)
        print(f"EXECUTING TASK: {task}")
        print("=" * 50)

        result = backend_agent.execute(
            task
        )

        results.append({
            "task": task,
            "result": result
        })

    return {
        "plan": plan,
        "results": results
    }