import pydantic
import typing_extensions


class Recurrence20240614(typing_extensions.TypedDict):
    """
    Recurrence20240614
    """

    frequency: typing_extensions.Required[
        typing_extensions.Literal["monthly", "weekly", "yearly"]
    ]

    interval: typing_extensions.Required[float]
    """
    Repeats every {count} week | month | year
    """

    occurrences: typing_extensions.Required[float]
    """
    Repeats for a maximum of {count} events
    """


class _SerializerRecurrence20240614(pydantic.BaseModel):
    """
    Serializer for Recurrence20240614 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
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
    occurrences: float = pydantic.Field(
        alias="occurrences",
    )
