import pydantic
import typing
import typing_extensions


class DeclineBookingInput20240813(typing_extensions.TypedDict):
    """
    DeclineBookingInput20240813
    """

    reason: typing_extensions.NotRequired[str]
    """
    Reason for declining a booking that requires a confirmation
    """


class _SerializerDeclineBookingInput20240813(pydantic.BaseModel):
    """
    Serializer for DeclineBookingInput20240813 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    reason: typing.Optional[str] = pydantic.Field(alias="reason", default=None)
