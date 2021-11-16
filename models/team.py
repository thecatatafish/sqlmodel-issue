from typing import Optional, List, TYPE_CHECKING

from sqlmodel import SQLModel, Field, Relationship
from models.hero import HeroRead

if TYPE_CHECKING:
    from models.hero import Hero, HeroRead


class TeamBase(SQLModel):
    name: str
    headquarters: str


class Team(TeamBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    heroes: List["Hero"] = Relationship(back_populates="team")


class TeamCreate(TeamBase):
    pass


class TeamRead(TeamBase):
    id: int


class TeamUpdate(SQLModel):
    id: Optional[int] = None
    name: Optional[str] = None
    headquarters: Optional[str] = None


class TeamReadWithHeroes(TeamRead):
    heroes: List["HeroRead"] = []

