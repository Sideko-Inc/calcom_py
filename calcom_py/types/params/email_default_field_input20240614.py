import pydantic
import typing
import typing_extensions


class EmailDefaultFieldInput20240614(typing_extensions.TypedDict):
    """
    EmailDefaultFieldInput20240614
    """

    disable_on_prefill: typing_extensions.NotRequired[bool]
    """
    Disable this booking field if the URL contains query parameter with key equal to the slug and prefill it with the provided value.      For example, if URL contains query parameter `&email=bob@gmail.com`,      the email field will be prefilled with this value and disabled.
    """

    hidden: typing_extensions.NotRequired[bool]
    """
    Can be set to true only for organization team event types and if you also pass booking field {type: "phone", slug: "attendeePhoneNumber", required: true, hidden: false, label: "whatever label"} of booking field type PhoneFieldInput_2024_06_14 - this is done
          to enable phone only bookings where during the booking attendee can provide only their phone number and not provide email, so you must pass to the email booking field {hidden: true, required: false}.
          If true show under event type settings but don't show this booking field in the Booker. If false show in both.
    """

    label: typing_extensions.Required[str]

    placeholder: typing_extensions.Required[str]

    required: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]
    """
    Can be set to false only for organization team event types and if you also pass booking field {type: "phone", slug: "attendeePhoneNumber", required: true, hidden: false, label: "whatever label"} of booking field type PhoneFieldInput_2024_06_14 - this is done
          to enable phone only bookings where during the booking attendee can provide only their phone number and not provide email, so you must pass to the email booking field {hidden: true, required: false}.
          If true show under event type settings but don't show this booking field in the Booker. If false show in both.
    """

    type_field: typing_extensions.Required[str]
    """
    only allowed value for type is `email`
    """


class _SerializerEmailDefaultFieldInput20240614(pydantic.BaseModel):
    """
    Serializer for EmailDefaultFieldInput20240614 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    disable_on_prefill: typing.Optional[bool] = pydantic.Field(
        alias="disableOnPrefill", default=None
    )
    hidden: typing.Optional[bool] = pydantic.Field(alias="hidden", default=None)
    label: str = pydantic.Field(
        alias="label",
    )
    placeholder: str = pydantic.Field(
        alias="placeholder",
    )
    required: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="required", default=None
    )
    type_field: str = pydantic.Field(
        alias="type",
    )
