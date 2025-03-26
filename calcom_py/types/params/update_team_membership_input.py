import pydantic
import typing
import typing_extensions


class UpdateTeamMembershipInput(typing_extensions.TypedDict):
    """
    UpdateTeamMembershipInput
    """

    accepted: typing_extensions.NotRequired[bool]

    disable_impersonation: typing_extensions.NotRequired[bool]

    role: typing_extensions.NotRequired[
        typing_extensions.Literal["ADMIN", "MEMBER", "OWNER"]
    ]


class _SerializerUpdateTeamMembershipInput(pydantic.BaseModel):
    """
    Serializer for UpdateTeamMembershipInput handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    accepted: typing.Optional[bool] = pydantic.Field(alias="accepted", default=None)
    disable_impersonation: typing.Optional[bool] = pydantic.Field(
        alias="disableImpersonation", default=None
    )
    role: typing.Optional[typing_extensions.Literal["ADMIN", "MEMBER", "OWNER"]] = (
        pydantic.Field(alias="role", default=None)
    )
