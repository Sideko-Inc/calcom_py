import pydantic
import typing
import typing_extensions

from .o_auth_client_webhook_output_dto import OAuthClientWebhookOutputDto


class OAuthClientWebhooksOutputResponseDto(pydantic.BaseModel):
    """
    OAuthClientWebhooksOutputResponseDto
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.List[OAuthClientWebhookOutputDto] = pydantic.Field(
        alias="data",
    )
    status: typing_extensions.Literal["error", "success"] = pydantic.Field(
        alias="status",
    )
