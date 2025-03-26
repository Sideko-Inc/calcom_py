import pydantic
import typing
import typing_extensions

from .org_team_output_dto import OrgTeamOutputDto


class OrgTeamsOutputResponseDto(pydantic.BaseModel):
    """
    OrgTeamsOutputResponseDto
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.List[OrgTeamOutputDto] = pydantic.Field(
        alias="data",
    )
    status: typing_extensions.Literal["error", "success"] = pydantic.Field(
        alias="status",
    )
