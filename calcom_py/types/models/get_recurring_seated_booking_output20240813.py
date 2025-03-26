import pydantic
import typing
import typing_extensions

from .booking_host import BookingHost
from .event_type import EventType
from .seated_attendee import SeatedAttendee


class GetRecurringSeatedBookingOutput20240813(pydantic.BaseModel):
    """
    GetRecurringSeatedBookingOutput20240813
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    absent_host: bool = pydantic.Field(
        alias="absentHost",
    )
    attendees: typing.List[SeatedAttendee] = pydantic.Field(
        alias="attendees",
    )
    cancellation_reason: typing.Optional[str] = pydantic.Field(
        alias="cancellationReason", default=None
    )
    cancelled_by_email: typing.Optional[str] = pydantic.Field(
        alias="cancelledByEmail", default=None
    )
    created_at: str = pydantic.Field(
        alias="createdAt",
    )
    description: str = pydantic.Field(
        alias="description",
    )
    duration: float = pydantic.Field(
        alias="duration",
    )
    end: str = pydantic.Field(
        alias="end",
    )
    event_type: EventType = pydantic.Field(
        alias="eventType",
    )
    event_type_id: float = pydantic.Field(
        alias="eventTypeId",
    )
    """
    Deprecated - rely on 'eventType' object containing the id instead.
    """
    hosts: typing.List[BookingHost] = pydantic.Field(
        alias="hosts",
    )
    id: float = pydantic.Field(
        alias="id",
    )
    location: str = pydantic.Field(
        alias="location",
    )
    meeting_url: typing.Optional[str] = pydantic.Field(alias="meetingUrl", default=None)
    """
    Deprecated - rely on 'location' field instead.
    """
    metadata: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="metadata", default=None
    )
    rating: typing.Optional[float] = pydantic.Field(alias="rating", default=None)
    recurring_booking_uid: str = pydantic.Field(
        alias="recurringBookingUid",
    )
    rescheduled_by_email: typing.Optional[str] = pydantic.Field(
        alias="rescheduledByEmail", default=None
    )
    rescheduled_from_uid: typing.Optional[str] = pydantic.Field(
        alias="rescheduledFromUid", default=None
    )
    rescheduling_reason: typing.Optional[str] = pydantic.Field(
        alias="reschedulingReason", default=None
    )
    start: str = pydantic.Field(
        alias="start",
    )
    status: typing_extensions.Literal[
        "accepted", "cancelled", "pending", "rejected"
    ] = pydantic.Field(
        alias="status",
    )
    title: str = pydantic.Field(
        alias="title",
    )
    uid: str = pydantic.Field(
        alias="uid",
    )
    updated_at: str = pydantic.Field(
        alias="updatedAt",
    )
