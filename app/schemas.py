# generated by datamodel-codegen:
#   filename:  oas.yaml
#   timestamp: 2020-12-09T22:53:23+00:00

from __future__ import annotations

from enum import Enum
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field


class Error(BaseModel):
    detail: Optional[str] = None


class Priority(Enum):
    low = 'low'
    medium = 'medium'
    high = 'high'


class Status(Enum):
    pending = 'pending'
    progress = 'progress'
    completed = 'completed'


class CreateTaskSchema(BaseModel):
    priority: Optional[Priority] = 'low'
    status: Optional[Status] = 'pending'
    task: str


class Priority1(Enum):
    low = 'low'
    medium = 'medium'
    high = 'high'


class Status1(Enum):
    pending = 'pending'
    progress = 'progress'
    completed = 'completed'


class GetTaskSchema(BaseModel):
    id: UUID
    created: int = Field(..., description='Date in the form of UNIX timestmap')
    priority: Priority1
    status: Status1
    task: str
