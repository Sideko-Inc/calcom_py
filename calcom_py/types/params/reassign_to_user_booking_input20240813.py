import pydantic
import typing
import typing_extensions


class ReassignToUserBookingInput20240813(typing_extensions.TypedDict):
    """
    ReassignToUserBookingInput20240813
    """

    reason: typing_extensions.NotRequired[str]
    """
    Reason for reassigning the booking
    """


class _SerializerReassignToUserBookingInput20240813(pydantic.BaseModel):
    """
    Serializer for ReassignToUserBookingInput20240813 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    reason: typing.Optional[str] = pydantic.Field(alias="reason", default=None)
