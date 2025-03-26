import pydantic
import typing_extensions


class BookingInputOrganizersDefaultAppLocation20240813(typing_extensions.TypedDict):
    """
    BookingInputOrganizersDefaultAppLocation20240813
    """

    type_field: typing_extensions.Required[str]
    """
    only available for team event types and the only allowed value for type is `organizersDefaultApp` - it refers to the default app defined by the organizer.
    """


class _SerializerBookingInputOrganizersDefaultAppLocation20240813(pydantic.BaseModel):
    """
    Serializer for BookingInputOrganizersDefaultAppLocation20240813 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    type_field: str = pydantic.Field(
        alias="type",
    )
