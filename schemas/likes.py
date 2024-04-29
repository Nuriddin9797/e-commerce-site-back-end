from enum import Enum
from pydantic import BaseModel, Field


class Source_type(str, Enum):
    laptop = "laptop"
    planshet = "planshet"
    telephone = "telephone"


class CreateLikes(BaseModel):
    source: Source_type
    source_id: int = Field(..., gt=0)
