import pydantic
import typing
import typing_extensions


class UpdateOutOfOfficeEntryDto(typing_extensions.TypedDict):
    """
    UpdateOutOfOfficeEntryDto
    """

    end: typing_extensions.NotRequired[str]
    """
    The end date and time of the out of office period in ISO 8601 format in UTC timezone.
    """

    notes: typing_extensions.NotRequired[str]
    """
    Optional notes for the out of office entry.
    """

    reason: typing_extensions.NotRequired[
        typing_extensions.Literal[
            "public_holiday", "sick", "travel", "unspecified", "vacation"
        ]
    ]
    """
    the reason for the out of office entry, if applicable
    """

    start: typing_extensions.NotRequired[str]
    """
    The start date and time of the out of office period in ISO 8601 format in UTC timezone.
    """

    to_user_id: typing_extensions.NotRequired[float]
    """
    The ID of the user covering for the out of office period, if applicable.
    """


class _SerializerUpdateOutOfOfficeEntryDto(pydantic.BaseModel):
    """
    Serializer for UpdateOutOfOfficeEntryDto handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    end: typing.Optional[str] = pydantic.Field(alias="end", default=None)
    notes: typing.Optional[str] = pydantic.Field(alias="notes", default=None)
    reason: typing.Optional[
        typing_extensions.Literal[
            "public_holiday", "sick", "travel", "unspecified", "vacation"
        ]
    ] = pydantic.Field(alias="reason", default=None)
    start: typing.Optional[str] = pydantic.Field(alias="start", default=None)
    to_user_id: typing.Optional[float] = pydantic.Field(alias="toUserId", default=None)
