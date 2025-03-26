import pydantic
import typing


class DestinationCalendar(pydantic.BaseModel):
    """
    DestinationCalendar
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    credential_id: typing.Optional[float] = pydantic.Field(
        alias="credentialId",
    )
    delegation_credential_id: typing.Optional[str] = pydantic.Field(
        alias="delegationCredentialId", default=None
    )
    email_field: typing.Optional[str] = pydantic.Field(alias="email", default=None)
    event_type_id: typing.Optional[float] = pydantic.Field(
        alias="eventTypeId",
    )
    external_id: str = pydantic.Field(
        alias="externalId",
    )
    id: typing.Dict[str, typing.Any] = pydantic.Field(
        alias="id",
    )
    integration: str = pydantic.Field(
        alias="integration",
    )
    integration_title: typing.Optional[str] = pydantic.Field(
        alias="integrationTitle", default=None
    )
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    primary: typing.Optional[bool] = pydantic.Field(alias="primary", default=None)
    primary_email: typing.Optional[str] = pydantic.Field(
        alias="primaryEmail",
    )
    read_only: typing.Optional[bool] = pydantic.Field(alias="readOnly", default=None)
    user_id: typing.Optional[float] = pydantic.Field(
        alias="userId",
    )
