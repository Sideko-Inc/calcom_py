import pydantic
import typing_extensions

from .event_type_output20240614 import EventTypeOutput20240614


class UpdateEventTypeOutput20240614(pydantic.BaseModel):
    """
    UpdateEventTypeOutput20240614
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: EventTypeOutput20240614 = pydantic.Field(
        alias="data",
    )
    status: typing_extensions.Literal["error", "success"] = pydantic.Field(
        alias="status",
    )
