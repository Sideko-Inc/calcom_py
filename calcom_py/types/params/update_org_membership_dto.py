import pydantic
import typing
import typing_extensions


class UpdateOrgMembershipDto(typing_extensions.TypedDict):
    """
    UpdateOrgMembershipDto
    """

    accepted: typing_extensions.NotRequired[bool]

    disable_impersonation: typing_extensions.NotRequired[bool]

    role: typing_extensions.NotRequired[
        typing_extensions.Literal["ADMIN", "MEMBER", "OWNER"]
    ]


class _SerializerUpdateOrgMembershipDto(pydantic.BaseModel):
    """
    Serializer for UpdateOrgMembershipDto handling case conversions
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
