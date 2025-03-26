import pydantic
import typing
import typing_extensions

from .org_team_membership_output_dto import OrgTeamMembershipOutputDto


class OrgTeamMembershipsOutputResponseDto(pydantic.BaseModel):
    """
    OrgTeamMembershipsOutputResponseDto
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.List[OrgTeamMembershipOutputDto] = pydantic.Field(
        alias="data",
    )
    status: typing_extensions.Literal["error", "success"] = pydantic.Field(
        alias="status",
    )
