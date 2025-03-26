import pydantic
import typing_extensions

from .destination_calendars_output_dto import DestinationCalendarsOutputDto


class DestinationCalendarsOutputResponseDto(pydantic.BaseModel):
    """
    DestinationCalendarsOutputResponseDto
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: DestinationCalendarsOutputDto = pydantic.Field(
        alias="data",
    )
    status: typing_extensions.Literal["error", "success"] = pydantic.Field(
        alias="status",
    )
