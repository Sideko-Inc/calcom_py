import pydantic
import typing

from .connected_calendar import ConnectedCalendar
from .destination_calendar import DestinationCalendar


class ConnectedCalendarsData(pydantic.BaseModel):
    """
    ConnectedCalendarsData
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    connected_calendars: typing.List[ConnectedCalendar] = pydantic.Field(
        alias="connectedCalendars",
    )
    destination_calendar: DestinationCalendar = pydantic.Field(
        alias="destinationCalendar",
    )
