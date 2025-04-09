from dataclasses import dataclass
from pydantic import BaseModel, Field
from bank_database import DatabaseConn

@dataclass
class SupportDependencies:
    customer_id: int
    db: DatabaseConn

class SupportResult(BaseModel):
    support_advice: str = Field(description="Advice returned to the customer")
    block_card: bool = Field(description="Whether to block the customer's card")
    risk: int = Field(description="Risk level of query", ge=0, le=10)
