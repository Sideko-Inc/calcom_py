import pydantic
import typing_extensions

from .strip_connect_output_dto import StripConnectOutputDto


class StripConnectOutputResponseDto(pydantic.BaseModel):
    """
    StripConnectOutputResponseDto
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: StripConnectOutputDto = pydantic.Field(
        alias="data",
    )
    status: typing_extensions.Literal["error", "success"] = pydantic.Field(
        alias="status",
    )
