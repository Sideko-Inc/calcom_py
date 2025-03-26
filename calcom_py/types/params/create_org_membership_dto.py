import pydantic
import typing
import typing_extensions


class CreateOrgMembershipDto(typing_extensions.TypedDict):
    """
    CreateOrgMembershipDto
    """

    accepted: typing_extensions.NotRequired[bool]

    disable_impersonation: typing_extensions.NotRequired[bool]

    role: typing_extensions.Required[
        typing_extensions.Literal["ADMIN", "MEMBER", "OWNER"]
    ]

    user_id: typing_extensions.Required[float]


class _SerializerCreateOrgMembershipDto(pydantic.BaseModel):
    """
    Serializer for CreateOrgMembershipDto handling case conversions
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
