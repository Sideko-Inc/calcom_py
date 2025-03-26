import pydantic
import typing
import typing_extensions

from .notice_threshold20240614 import (
    NoticeThreshold20240614,
    _SerializerNoticeThreshold20240614,
)


class BaseConfirmationPolicy20240614(typing_extensions.TypedDict):
    """
    BaseConfirmationPolicy20240614
    """

    block_unconfirmed_bookings_in_booker: typing_extensions.Required[bool]
    """
    Unconfirmed bookings still block calendar slots.
    """

    notice_threshold: typing_extensions.NotRequired[NoticeThreshold20240614]

    type_field: typing_extensions.Required[typing_extensions.Literal["always", "time"]]
    """
    The policy that determines when confirmation is required
    """


class _SerializerBaseConfirmationPolicy20240614(pydantic.BaseModel):
    """
    Serializer for BaseConfirmationPolicy20240614 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    block_unconfirmed_bookings_in_booker: bool = pydantic.Field(
        alias="blockUnconfirmedBookingsInBooker",
    )
    notice_threshold: typing.Optional[_SerializerNoticeThreshold20240614] = (
        pydantic.Field(alias="noticeThreshold", default=None)
    )
    type_field: typing_extensions.Literal["always", "time"] = pydantic.Field(
        alias="type",
    )
