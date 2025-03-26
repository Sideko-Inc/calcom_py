import pydantic
import typing_extensions


class NoticeThreshold20240614(typing_extensions.TypedDict):
    """
    NoticeThreshold20240614
    """

    count: typing_extensions.Required[float]
    """
    The time value for the notice threshold
    """

    unit: typing_extensions.Required[str]
    """
    The unit of time for the notice threshold (e.g., minutes, hours)
    """


class _SerializerNoticeThreshold20240614(pydantic.BaseModel):
    """
    Serializer for NoticeThreshold20240614 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    count: float = pydantic.Field(
        alias="count",
    )
    unit: str = pydantic.Field(
        alias="unit",
    )
