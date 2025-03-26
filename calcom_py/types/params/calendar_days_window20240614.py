import pydantic
import typing
import typing_extensions


class CalendarDaysWindow20240614(typing_extensions.TypedDict):
    """
    CalendarDaysWindow20240614
    """

    rolling: typing_extensions.NotRequired[bool]
    """
    
          Determines the behavior of the booking window:
          - If **true**, the window is rolling. This means the number of available days will always be equal the specified 'value' 
            and adjust dynamically as bookings are made. For example, if 'value' is 3 and availability is only on Mondays, 
            a booker attempting to schedule on November 10 will see slots on November 11, 18, and 25. As one of these days 
            becomes fully booked, a new day (e.g., December 2) will open up to ensure 3 available days are always visible.
          - If **false**, the window is fixed. This means the booking window only considers the next 'value' days from the
            moment someone is trying to book. For example, if 'value' is 3, availability is only on Mondays, and the current 
            date is November 10, the booker will only see slots on November 11 because the window is restricted to the next 
            3 calendar days (November 10–12).
        
    """

    type_field: typing_extensions.Required[
        typing_extensions.Literal["businessDays", "calendarDays", "range"]
    ]
    """
    Whether the window should be business days, calendar days or a range of dates
    """

    value: typing_extensions.Required[float]
    """
    How many calendar days into the future can this event be booked
    """


class _SerializerCalendarDaysWindow20240614(pydantic.BaseModel):
    """
    Serializer for CalendarDaysWindow20240614 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    rolling: typing.Optional[bool] = pydantic.Field(alias="rolling", default=None)
    type_field: typing_extensions.Literal["businessDays", "calendarDays", "range"] = (
        pydantic.Field(
            alias="type",
        )
    )
    value: float = pydantic.Field(
        alias="value",
    )
