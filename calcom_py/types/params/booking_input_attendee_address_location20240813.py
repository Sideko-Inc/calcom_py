import pydantic
import typing_extensions


class BookingInputAttendeeAddressLocation20240813(typing_extensions.TypedDict):
    """
    BookingInputAttendeeAddressLocation20240813
    """

    address: typing_extensions.Required[str]

    type_field: typing_extensions.Required[str]
    """
    only allowed value for type is `attendeeAddress`
    """


class _SerializerBookingInputAttendeeAddressLocation20240813(pydantic.BaseModel):
    """
    Serializer for BookingInputAttendeeAddressLocation20240813 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    address: str = pydantic.Field(
        alias="address",
    )
    type_field: str = pydantic.Field(
        alias="type",
    )
