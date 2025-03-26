import pydantic
import typing_extensions


class Recurrence20240614(pydantic.BaseModel):
    """
    Recurrence20240614
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    frequency: typing_extensions.Literal["monthly", "weekly", "yearly"] = (
        pydantic.Field(
            alias="frequency",
        )
    )
    interval: float = pydantic.Field(
        alias="interval",
    )
    """
    Repeats every {count} week | month | year
    """
    occurrences: float = pydantic.Field(
        alias="occurrences",
    )
    """
    Repeats for a maximum of {count} events
    """
