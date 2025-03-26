import pydantic
import typing_extensions

from .team_output_dto import TeamOutputDto


class UpdateTeamOutput(pydantic.BaseModel):
    """
    UpdateTeamOutput
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: TeamOutputDto = pydantic.Field(
        alias="data",
    )
    status: typing_extensions.Literal["error", "success"] = pydantic.Field(
        alias="status",
    )
