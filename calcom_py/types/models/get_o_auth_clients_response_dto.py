import pydantic
import typing
import typing_extensions

from .platform_o_auth_client_dto import PlatformOAuthClientDto


class GetOAuthClientsResponseDto(pydantic.BaseModel):
    """
    GetOAuthClientsResponseDto
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.List[PlatformOAuthClientDto] = pydantic.Field(
        alias="data",
    )
    status: typing_extensions.Literal["error", "success"] = pydantic.Field(
        alias="status",
    )
