import pydantic
import typing
import typing_extensions


class UpdateWebhookInputDto(typing_extensions.TypedDict):
    """
    UpdateWebhookInputDto
    """

    active: typing_extensions.NotRequired[bool]

    payload_template: typing_extensions.NotRequired[str]
    """
    The template of the payload that will be sent to the subscriberUrl, check cal.com/docs/core-features/webhooks for more information
    """

    secret: typing_extensions.NotRequired[str]

    subscriber_url: typing_extensions.NotRequired[str]

    triggers: typing_extensions.NotRequired[
        typing_extensions.Literal[
            "AFTER_GUESTS_CAL_VIDEO_NO_SHOW",
            "AFTER_HOSTS_CAL_VIDEO_NO_SHOW",
            "BOOKING_CANCELLED",
            "BOOKING_CREATED",
            "BOOKING_NO_SHOW_UPDATED",
            "BOOKING_PAID",
            "BOOKING_PAYMENT_INITIATED",
            "BOOKING_REJECTED",
            "BOOKING_REQUESTED",
            "BOOKING_RESCHEDULED",
            "FORM_SUBMITTED",
            "FORM_SUBMITTED_NO_EVENT",
            "INSTANT_MEETING",
            "MEETING_ENDED",
            "MEETING_STARTED",
            "OOO_CREATED",
            "RECORDING_READY",
            "RECORDING_TRANSCRIPTION_GENERATED",
        ]
    ]


class _SerializerUpdateWebhookInputDto(pydantic.BaseModel):
    """
    Serializer for UpdateWebhookInputDto handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    active: typing.Optional[bool] = pydantic.Field(alias="active", default=None)
    payload_template: typing.Optional[str] = pydantic.Field(
        alias="payloadTemplate", default=None
    )
    secret: typing.Optional[str] = pydantic.Field(alias="secret", default=None)
    subscriber_url: typing.Optional[str] = pydantic.Field(
        alias="subscriberUrl", default=None
    )
    triggers: typing.Optional[
        typing_extensions.Literal[
            "AFTER_GUESTS_CAL_VIDEO_NO_SHOW",
            "AFTER_HOSTS_CAL_VIDEO_NO_SHOW",
            "BOOKING_CANCELLED",
            "BOOKING_CREATED",
            "BOOKING_NO_SHOW_UPDATED",
            "BOOKING_PAID",
            "BOOKING_PAYMENT_INITIATED",
            "BOOKING_REJECTED",
            "BOOKING_REQUESTED",
            "BOOKING_RESCHEDULED",
            "FORM_SUBMITTED",
            "FORM_SUBMITTED_NO_EVENT",
            "INSTANT_MEETING",
            "MEETING_ENDED",
            "MEETING_STARTED",
            "OOO_CREATED",
            "RECORDING_READY",
            "RECORDING_TRANSCRIPTION_GENERATED",
        ]
    ] = pydantic.Field(alias="triggers", default=None)
