from fastapi import UploadFile
from typing import List
from pydantic import BaseModel, Field
from enum import Enum


class SourceType(str, Enum):
    user = "user"
    laptop = "laptop"
    telephone = "telephone"
    planshets = "planshet"


class CreateFile(BaseModel):
    new_files: List[UploadFile]
    source: SourceType
    source_id: int = Field(..., gt=0)