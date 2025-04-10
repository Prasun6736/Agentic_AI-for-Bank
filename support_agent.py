from pydantic_ai import Agent, RunContext
from support_models import SupportDependencies, SupportResult
from dotenv import load_dotenv 
import os

# Set your Groq API key and base URL as environment variables (works for 0.0.55)
#os.environ["GROQ_API_KEY"] = "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"
#os.environ["OPENAI_BASE_URL"] = "https://api.groq.com/openai/v1"
load_dotenv()
print("Loaded API Key:", os.getenv("GROQ_API_KEY"))


support_agent = Agent(
    model="groq:llama3-70b-8192",  # or "llama3-70b-8192"
    deps_type=SupportDependencies,
    result_type=SupportResult,
    system_prompt=(
        "You are a support agent in our bank. "
        "Give professional, empathetic responses. "
        "Include customer name if available. "
        "Evaluate the risk level of their query (0 to 10), "
        "and decide if their card should be blocked."
    )
)

@support_agent.system_prompt
async def add_customer_name(ctx: RunContext[SupportDependencies]) -> str:
    name = await ctx.deps.db.customer_name(id=ctx.deps.customer_id)
    return f"The customer's name is {name!r}."

@support_agent.tool
async def customer_balance(ctx: RunContext[SupportDependencies], include_pending: bool) -> float:
    return await ctx.deps.db.customer_balance(id=ctx.deps.customer_id, include_pending=include_pending)
