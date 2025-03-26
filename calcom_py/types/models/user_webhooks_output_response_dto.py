import pydantic
import typing
import typing_extensions

from .user_webhook_output_dto import UserWebhookOutputDto


class UserWebhooksOutputResponseDto(pydantic.BaseModel):
    """
    UserWebhooksOutputResponseDto
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.List[UserWebhookOutputDto] = pydantic.Field(
        alias="data",
    )
    status: typing_extensions.Literal["error", "success"] = pydantic.Field(
        alias="status",
    )
