import pydantic
import typing_extensions

from .connected_calendars_data import ConnectedCalendarsData


class ConnectedCalendarsOutput(pydantic.BaseModel):
    """
    ConnectedCalendarsOutput
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: ConnectedCalendarsData = pydantic.Field(
        alias="data",
    )
    status: typing_extensions.Literal["error", "success"] = pydantic.Field(
        alias="status",
    )
