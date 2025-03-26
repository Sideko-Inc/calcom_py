import pydantic
import typing
import typing_extensions


class RangeWindow20240614(typing_extensions.TypedDict):
    """
    RangeWindow20240614
    """

    type_field: typing_extensions.Required[
        typing_extensions.Literal["businessDays", "calendarDays", "range"]
    ]
    """
    Whether the window should be business days, calendar days or a range of dates
    """

    value: typing_extensions.Required[typing.List[str]]
    """
    Date range for when this event can be booked.
    """


class _SerializerRangeWindow20240614(pydantic.BaseModel):
    """
    Serializer for RangeWindow20240614 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    type_field: typing_extensions.Literal["businessDays", "calendarDays", "range"] = (
        pydantic.Field(
            alias="type",
        )
    )
    value: typing.List[str] = pydantic.Field(
        alias="value",
    )
