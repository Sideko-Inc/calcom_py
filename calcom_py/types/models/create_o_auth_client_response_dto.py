import pydantic
import typing_extensions

from .create_o_auth_client_output import CreateOAuthClientOutput


class CreateOAuthClientResponseDto(pydantic.BaseModel):
    """
    CreateOAuthClientResponseDto
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: CreateOAuthClientOutput = pydantic.Field(
        alias="data",
    )
    status: typing_extensions.Literal["error", "success"] = pydantic.Field(
        alias="status",
    )
