import pydantic
import typing_extensions

from .user_webhook_output_dto import UserWebhookOutputDto


class UserWebhookOutputResponseDto(pydantic.BaseModel):
    """
    UserWebhookOutputResponseDto
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: UserWebhookOutputDto = pydantic.Field(
        alias="data",
    )
    status: typing_extensions.Literal["error", "success"] = pydantic.Field(
        alias="status",
    )
