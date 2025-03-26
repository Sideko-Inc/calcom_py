import pydantic
import typing_extensions


class DestinationCalendar20240614(typing_extensions.TypedDict):
    """
    DestinationCalendar20240614
    """

    external_id: typing_extensions.Required[str]
    """
    The external ID of the destination calendar. Refer to the /api/v2/calendars endpoint to retrieve the external IDs of your connected calendars.
    """

    integration: typing_extensions.Required[str]
    """
    The integration type of the destination calendar. Refer to the /api/v2/calendars endpoint to retrieve the integration type of your connected calendars.
    """


class _SerializerDestinationCalendar20240614(pydantic.BaseModel):
    """
    Serializer for DestinationCalendar20240614 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    external_id: str = pydantic.Field(
        alias="externalId",
    )
    integration: str = pydantic.Field(
        alias="integration",
    )
