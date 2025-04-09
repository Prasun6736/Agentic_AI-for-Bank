import asyncio

class DatabaseConn:
    def __init__(self):
        self._customers = {
            123: {"name": "Alice", "balance": 2500.50, "pending": 123.45},
            456: {"name": "Bob", "balance": 1300.00, "pending": 50.00},
        }

    async def customer_name(self, id: int) -> str:
        return self._customers.get(id, {}).get("name", "Unknown")

    async def customer_balance(self, id: int, include_pending: bool = False) -> float:
        data = self._customers.get(id)
        if not data:
            return 0.0
        return data["balance"] + (data["pending"] if include_pending else 0.0)
