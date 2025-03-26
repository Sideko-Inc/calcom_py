import pydantic
import typing_extensions

from .selected_calendar_output_dto import SelectedCalendarOutputDto


class SelectedCalendarOutputResponseDto(pydantic.BaseModel):
    """
    SelectedCalendarOutputResponseDto
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: SelectedCalendarOutputDto = pydantic.Field(
        alias="data",
    )
    status: typing_extensions.Literal["error", "success"] = pydantic.Field(
        alias="status",
    )
