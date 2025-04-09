import asyncio
from bank_database import DatabaseConn
from support_models import SupportDependencies
from support_agent import support_agent

async def main():
    deps = SupportDependencies(customer_id=123, db=DatabaseConn())

    result = await support_agent.run("What is my current balance?", deps=deps)
    print(result.data)

    result = await support_agent.run("My card is stolen!", deps=deps)
    print(result.data)

if __name__ == "__main__":
    asyncio.run(main())
