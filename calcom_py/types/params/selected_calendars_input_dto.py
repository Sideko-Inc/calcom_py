import pydantic
import typing
import typing_extensions


class SelectedCalendarsInputDto(typing_extensions.TypedDict):
    """
    SelectedCalendarsInputDto
    """

    credential_id: typing_extensions.Required[float]

    delegation_credential_id: typing_extensions.NotRequired[str]

    external_id: typing_extensions.Required[str]

    integration: typing_extensions.Required[str]


class _SerializerSelectedCalendarsInputDto(pydantic.BaseModel):
    """
    Serializer for SelectedCalendarsInputDto handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    credential_id: float = pydantic.Field(
        alias="credentialId",
    )
    delegation_credential_id: typing.Optional[str] = pydantic.Field(
        alias="delegationCredentialId", default=None
    )
    external_id: str = pydantic.Field(
        alias="externalId",
    )
    integration: str = pydantic.Field(
        alias="integration",
    )
