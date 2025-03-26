import pydantic
import typing
import typing_extensions


class CreateTeamMembershipInput(typing_extensions.TypedDict):
    """
    CreateTeamMembershipInput
    """

    accepted: typing_extensions.NotRequired[bool]

    disable_impersonation: typing_extensions.NotRequired[bool]

    role: typing_extensions.NotRequired[
        typing_extensions.Literal["ADMIN", "MEMBER", "OWNER"]
    ]

    user_id: typing_extensions.Required[float]


class _SerializerCreateTeamMembershipInput(pydantic.BaseModel):
    """
    Serializer for CreateTeamMembershipInput handling case conversions
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
    user_id: float = pydantic.Field(
        alias="userId",
    )
