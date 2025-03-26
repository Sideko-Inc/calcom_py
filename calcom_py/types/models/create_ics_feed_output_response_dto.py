import pydantic
import typing_extensions

from .create_ics_feed_output import CreateIcsFeedOutput


class CreateIcsFeedOutputResponseDto(pydantic.BaseModel):
    """
    CreateIcsFeedOutputResponseDto
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: CreateIcsFeedOutput = pydantic.Field(
        alias="data",
    )
    status: typing_extensions.Literal["error", "success"] = pydantic.Field(
        alias="status",
    )
