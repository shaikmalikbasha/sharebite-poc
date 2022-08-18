from datetime import datetime
from typing import Any, List, Optional

from pydantic import BaseModel


class PBaseSchema(BaseModel):
    id: Optional[int]
    created_at: datetime
    updated_at: datetime


class PModifierSchema(PBaseSchema):
    description: str
    items: list = []

    class config:
        orm_mode = True


class PItemSchema(PBaseSchema):
    name: str
    description: str
    price: float
    section_id: int
    modifers: List[PModifierSchema] = []

    class config:
        orm_mode = True


class PSectionSchema(PBaseSchema):
    name: str
    description: str
    items: List[PItemSchema] = []

    class config:
        orm_mode = True
