import pydantic
import typing
import typing_extensions

from .booking_output20240813 import BookingOutput20240813
from .create_recurring_seated_booking_output20240813 import (
    CreateRecurringSeatedBookingOutput20240813,
)
from .create_seated_booking_output20240813 import CreateSeatedBookingOutput20240813
from .recurring_booking_output20240813 import RecurringBookingOutput20240813


class CreateBookingOutput20240813(pydantic.BaseModel):
    """
    CreateBookingOutput20240813
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Union[
        BookingOutput20240813,
        typing.List[RecurringBookingOutput20240813],
        CreateSeatedBookingOutput20240813,
        typing.List[CreateRecurringSeatedBookingOutput20240813],
    ] = pydantic.Field(
        alias="data",
    )
    """
    Booking data, which can be either a BookingOutput object or an array of RecurringBookingOutput objects
    """
    status: typing_extensions.Literal["error", "success"] = pydantic.Field(
        alias="status",
    )
