import pydantic
import typing_extensions

from .deleted_calendar_credentials_output_dto import DeletedCalendarCredentialsOutputDto


class DeletedCalendarCredentialsOutputResponseDto(pydantic.BaseModel):
    """
    DeletedCalendarCredentialsOutputResponseDto
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: DeletedCalendarCredentialsOutputDto = pydantic.Field(
        alias="data",
    )
    status: typing_extensions.Literal["error", "success"] = pydantic.Field(
        alias="status",
    )
