import pydantic
import typing
import typing_extensions


class RangeWindow20240614(pydantic.BaseModel):
    """
    RangeWindow20240614
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    type_field: typing_extensions.Literal["businessDays", "calendarDays", "range"] = (
        pydantic.Field(
            alias="type",
        )
    )
    """
    Whether the window should be business days, calendar days or a range of dates
    """
    value: typing.List[str] = pydantic.Field(
        alias="value",
    )
    """
    Date range for when this event can be booked.
    """
