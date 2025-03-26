import pydantic
import typing

from .calendar_link import CalendarLink


class CalendarLinksOutput20240813(pydantic.BaseModel):
    """
    CalendarLinksOutput20240813
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.List[CalendarLink] = pydantic.Field(
        alias="data",
    )
    """
    Calendar links for the booking
    """
    status: typing.Dict[str, typing.Any] = pydantic.Field(
        alias="status",
    )
    """
    The status of the request, always 'success' for successful responses
    """
