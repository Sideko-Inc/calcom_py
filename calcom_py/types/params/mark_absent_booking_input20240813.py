import pydantic
import typing
import typing_extensions

from .attendee import Attendee, _SerializerAttendee


class MarkAbsentBookingInput20240813(typing_extensions.TypedDict):
    """
    MarkAbsentBookingInput20240813
    """

    attendees: typing_extensions.NotRequired[typing.List[Attendee]]

    host: typing_extensions.NotRequired[bool]
    """
    Whether the host was absent
    """


class _SerializerMarkAbsentBookingInput20240813(pydantic.BaseModel):
    """
    Serializer for MarkAbsentBookingInput20240813 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    attendees: typing.Optional[typing.List[_SerializerAttendee]] = pydantic.Field(
        alias="attendees", default=None
    )
    host: typing.Optional[bool] = pydantic.Field(alias="host", default=None)
