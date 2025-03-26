import pydantic


class ReserveSlotOutput20240904(pydantic.BaseModel):
    """
    ReserveSlotOutput20240904
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    event_type_id: float = pydantic.Field(
        alias="eventTypeId",
    )
    """
    The ID of the event type for which slot was reserved.
    """
    reservation_duration: float = pydantic.Field(
        alias="reservationDuration",
    )
    """
    For how many minutes the slot is reserved - for this long time noone else can book this event type at `start` time.
    """
    reservation_uid: str = pydantic.Field(
        alias="reservationUid",
    )
    """
    The unique identifier of the reservation. Use it to update, get or delete the reservation.
    """
    reservation_until: str = pydantic.Field(
        alias="reservationUntil",
    )
    """
    ISO 8601 datestring in UTC timezone representing time until which the slot is reserved.
    """
    slot_duration: float = pydantic.Field(
        alias="slotDuration",
    )
    """
    By default slot duration is equal to event type length, but if you want to reserve a slot for an event type that has a variable length you can specify it here. If you don't have this set explicitly that event type can have one of many lengths you can omit this.
    """
    slot_end: str = pydantic.Field(
        alias="slotEnd",
    )
    """
    ISO 8601 datestring in UTC timezone representing slot end.
    """
    slot_start: str = pydantic.Field(
        alias="slotStart",
    )
    """
    ISO 8601 datestring in UTC timezone representing available slot.
    """
