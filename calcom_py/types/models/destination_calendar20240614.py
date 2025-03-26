import pydantic


class DestinationCalendar20240614(pydantic.BaseModel):
    """
    DestinationCalendar20240614
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    external_id: str = pydantic.Field(
        alias="externalId",
    )
    """
    The external ID of the destination calendar. Refer to the /api/v2/calendars endpoint to retrieve the external IDs of your connected calendars.
    """
    integration: str = pydantic.Field(
        alias="integration",
    )
    """
    The integration type of the destination calendar. Refer to the /api/v2/calendars endpoint to retrieve the integration type of your connected calendars.
    """
