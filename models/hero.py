from typing import Optional, TYPE_CHECKING

from sqlmodel import SQLModel, Field, Relationship
if TYPE_CHECKING:
    from models.team import Team, TeamRead


class HeroBase(SQLModel):
    name: str
    secret_name: str
    age: Optional[int] = None

    team_id: Optional[int] = Field(default=None, foreign_key="team.id")


class Hero(HeroBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    team: Optional["Team"] = Relationship(back_populates="heroes")


class HeroRead(HeroBase):
    id: int


class HeroReadWithTeam(HeroRead):
    team: Optional["TeamRead"] = None