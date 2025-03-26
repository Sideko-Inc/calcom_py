import pydantic
import typing_extensions


class DisconnectConferencingAppOutputResponseDto(pydantic.BaseModel):
    """
    DisconnectConferencingAppOutputResponseDto
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    status: typing_extensions.Literal["error", "success"] = pydantic.Field(
        alias="status",
    )
