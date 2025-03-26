import pydantic
import typing_extensions


class CancelSeatedBookingInput20240813(typing_extensions.TypedDict):
    """
    CancelSeatedBookingInput20240813
    """

    seat_uid: typing_extensions.Required[str]
    """
    Uid of the specific seat within booking.
    """


class _SerializerCancelSeatedBookingInput20240813(pydantic.BaseModel):
    """
    Serializer for CancelSeatedBookingInput20240813 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    seat_uid: str = pydantic.Field(
        alias="seatUid",
    )
