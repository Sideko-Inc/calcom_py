import pydantic
import typing_extensions

from .org_team_output_dto import OrgTeamOutputDto


class OrgTeamOutputResponseDto(pydantic.BaseModel):
    """
    OrgTeamOutputResponseDto
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: OrgTeamOutputDto = pydantic.Field(
        alias="data",
    )
    status: typing_extensions.Literal["error", "success"] = pydantic.Field(
        alias="status",
    )
