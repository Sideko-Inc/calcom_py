import pydantic


class CalendarLink(pydantic.BaseModel):
    """
    CalendarLink
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    label: str = pydantic.Field(
        alias="label",
    )
    """
    The label of the calendar link
    """
    link: str = pydantic.Field(
        alias="link",
    )
    """
    The link to the calendar
    """
