import pydantic
import typing
import typing_extensions

from .membership_user_output_dto import MembershipUserOutputDto


class OrgTeamMembershipOutputDto(pydantic.BaseModel):
    """
    OrgTeamMembershipOutputDto
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    accepted: bool = pydantic.Field(
        alias="accepted",
    )
    disable_impersonation: typing.Optional[bool] = pydantic.Field(
        alias="disableImpersonation", default=None
    )
    id: float = pydantic.Field(
        alias="id",
    )
    role: typing_extensions.Literal["ADMIN", "MEMBER", "OWNER"] = pydantic.Field(
        alias="role",
    )
    team_id: float = pydantic.Field(
        alias="teamId",
    )
    user: MembershipUserOutputDto = pydantic.Field(
        alias="user",
    )
    user_id: float = pydantic.Field(
        alias="userId",
    )
