import pydantic
import typing_extensions

from .team_membership_output import TeamMembershipOutput


class GetTeamMembershipOutput(pydantic.BaseModel):
    """
    GetTeamMembershipOutput
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: TeamMembershipOutput = pydantic.Field(
        alias="data",
    )
    status: typing_extensions.Literal["error", "success"] = pydantic.Field(
        alias="status",
    )
