import pydantic
import typing
import typing_extensions


class CreatePhoneCallInput(typing_extensions.TypedDict):
    """
    CreatePhoneCallInput
    """

    begin_message: typing_extensions.NotRequired[str]
    """
    Begin message
    """

    cal_api_key: typing_extensions.Required[str]
    """
    CAL API Key
    """

    enabled: typing_extensions.Required[typing.Dict[str, typing.Any]]
    """
    Enabled status
    """

    general_prompt: typing_extensions.NotRequired[str]
    """
    General prompt
    """

    guest_company: typing_extensions.NotRequired[str]
    """
    Guest company
    """

    guest_email: typing_extensions.NotRequired[str]
    """
    Guest email
    """

    guest_name: typing_extensions.NotRequired[str]
    """
    Guest name
    """

    number_to_call: typing_extensions.Required[str]
    """
    Number to call
    """

    scheduler_name: typing_extensions.NotRequired[str]
    """
    Scheduler name
    """

    template_type: typing_extensions.Required[
        typing_extensions.Literal["CHECK_IN_APPOINTMENT", "CUSTOM_TEMPLATE"]
    ]
    """
    Template type
    """

    your_phone_number: typing_extensions.Required[str]
    """
    Your phone number
    """


class _SerializerCreatePhoneCallInput(pydantic.BaseModel):
    """
    Serializer for CreatePhoneCallInput handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    begin_message: typing.Optional[str] = pydantic.Field(
        alias="beginMessage", default=None
    )
    cal_api_key: str = pydantic.Field(
        alias="calApiKey",
    )
    enabled: typing.Dict[str, typing.Any] = pydantic.Field(
        alias="enabled",
    )
    general_prompt: typing.Optional[str] = pydantic.Field(
        alias="generalPrompt", default=None
    )
    guest_company: typing.Optional[str] = pydantic.Field(
        alias="guestCompany", default=None
    )
    guest_email: typing.Optional[str] = pydantic.Field(alias="guestEmail", default=None)
    guest_name: typing.Optional[str] = pydantic.Field(alias="guestName", default=None)
    number_to_call: str = pydantic.Field(
        alias="numberToCall",
    )
    scheduler_name: typing.Optional[str] = pydantic.Field(
        alias="schedulerName", default=None
    )
    template_type: typing_extensions.Literal[
        "CHECK_IN_APPOINTMENT", "CUSTOM_TEMPLATE"
    ] = pydantic.Field(
        alias="templateType",
    )
    your_phone_number: str = pydantic.Field(
        alias="yourPhoneNumber",
    )
