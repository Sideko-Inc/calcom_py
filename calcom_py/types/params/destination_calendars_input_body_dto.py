import pydantic
import typing
import typing_extensions


class DestinationCalendarsInputBodyDto(typing_extensions.TypedDict):
    """
    DestinationCalendarsInputBodyDto
    """

    delegation_credential_id: typing_extensions.NotRequired[str]

    external_id: typing_extensions.Required[str]
    """
    Unique identifier used to represent the specific calendar, as returned by the /calendars endpoint
    """

    integration: typing_extensions.Required[
        typing_extensions.Literal[
            "apple_calendar", "google_calendar", "office365_calendar"
        ]
    ]
    """
    The calendar service you want to integrate, as returned by the /calendars endpoint
    """


class _SerializerDestinationCalendarsInputBodyDto(pydantic.BaseModel):
    """
    Serializer for DestinationCalendarsInputBodyDto handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    delegation_credential_id: typing.Optional[str] = pydantic.Field(
        alias="delegationCredentialId", default=None
    )
    external_id: str = pydantic.Field(
        alias="externalId",
    )
    integration: typing_extensions.Literal[
        "apple_calendar", "google_calendar", "office365_calendar"
    ] = pydantic.Field(
        alias="integration",
    )
