import pydantic
import typing
import typing_extensions

from .team_output_dto import TeamOutputDto


class GetTeamsOutput(pydantic.BaseModel):
    """
    GetTeamsOutput
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.List[TeamOutputDto] = pydantic.Field(
        alias="data",
    )
    status: typing_extensions.Literal["error", "success"] = pydantic.Field(
        alias="status",
    )
