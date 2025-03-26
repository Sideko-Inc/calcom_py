import pydantic
import typing
import typing_extensions


class CreateOrgTeamMembershipDto(typing_extensions.TypedDict):
    """
    CreateOrgTeamMembershipDto
    """

    accepted: typing_extensions.NotRequired[bool]

    disable_impersonation: typing_extensions.NotRequired[bool]

    role: typing_extensions.Required[
        typing_extensions.Literal["ADMIN", "MEMBER", "OWNER"]
    ]

    user_id: typing_extensions.Required[float]


class _SerializerCreateOrgTeamMembershipDto(pydantic.BaseModel):
    """
    Serializer for CreateOrgTeamMembershipDto handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    accepted: typing.Optional[bool] = pydantic.Field(alias="accepted", default=None)
    disable_impersonation: typing.Optional[bool] = pydantic.Field(
        alias="disableImpersonation", default=None
    )
    role: typing_extensions.Literal["ADMIN", "MEMBER", "OWNER"] = pydantic.Field(
        alias="role",
    )
    user_id: float = pydantic.Field(
        alias="userId",
    )
