import pydantic
import typing
import typing_extensions

from .event_type_webhook_output_dto import EventTypeWebhookOutputDto


class EventTypeWebhooksOutputResponseDto(pydantic.BaseModel):
    """
    EventTypeWebhooksOutputResponseDto
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.List[EventTypeWebhookOutputDto] = pydantic.Field(
        alias="data",
    )
    status: typing_extensions.Literal["error", "success"] = pydantic.Field(
        alias="status",
    )
