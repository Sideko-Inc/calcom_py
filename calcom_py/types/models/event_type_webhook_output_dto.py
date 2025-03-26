import pydantic
import typing


class EventTypeWebhookOutputDto(pydantic.BaseModel):
    """
    EventTypeWebhookOutputDto
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    active: bool = pydantic.Field(
        alias="active",
    )
    event_type_id: float = pydantic.Field(
        alias="eventTypeId",
    )
    id: float = pydantic.Field(
        alias="id",
    )
    payload_template: str = pydantic.Field(
        alias="payloadTemplate",
    )
    """
    The template of the payload that will be sent to the subscriberUrl, check cal.com/docs/core-features/webhooks for more information
    """
    secret: typing.Optional[str] = pydantic.Field(alias="secret", default=None)
    subscriber_url: str = pydantic.Field(
        alias="subscriberUrl",
    )
    triggers: typing.List[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="triggers",
    )
