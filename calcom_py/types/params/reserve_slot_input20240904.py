import pydantic
import typing
import typing_extensions


class ReserveSlotInput20240904(typing_extensions.TypedDict):
    """
    ReserveSlotInput20240904
    """

    event_type_id: typing_extensions.Required[float]
    """
    The ID of the event type for which slot should be reserved.
    """

    reservation_duration: typing_extensions.NotRequired[float]
    """
    ONLY for authenticated requests with api key, access token or OAuth credentials (ID + secret).
          
          For how many minutes the slot should be reserved - for this long time noone else can book this event type at `start` time. If not provided, defaults to 5 minutes.
    """

    slot_duration: typing_extensions.NotRequired[float]
    """
    By default slot duration is equal to event type length, but if you want to reserve a slot for an event type that has a variable length you can specify it here as a number in minutes. If you don't have this set explicitly that event type can have one of many lengths you can omit this.
    """

    slot_start: typing_extensions.Required[str]
    """
    ISO 8601 datestring in UTC timezone representing available slot.
    """


class _SerializerReserveSlotInput20240904(pydantic.BaseModel):
    """
    Serializer for ReserveSlotInput20240904 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    event_type_id: float = pydantic.Field(
        alias="eventTypeId",
    )
    reservation_duration: typing.Optional[float] = pydantic.Field(
        alias="reservationDuration", default=None
    )
    slot_duration: typing.Optional[float] = pydantic.Field(
        alias="slotDuration", default=None
    )
    slot_start: str = pydantic.Field(
        alias="slotStart",
    )
