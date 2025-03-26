import pydantic
import typing
import typing_extensions


class EmailDefaultFieldOutput20240614(pydantic.BaseModel):
    """
    EmailDefaultFieldOutput20240614
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    disable_on_prefill: typing.Optional[bool] = pydantic.Field(
        alias="disableOnPrefill", default=None
    )
    """
    Disable this booking field if the URL contains query parameter with key equal to the slug and prefill it with the provided value.      For example, if URL contains query parameter `&email=bob@gmail.com`,      the email field will be prefilled with this value and disabled.
    """
    hidden: typing.Optional[bool] = pydantic.Field(alias="hidden", default=None)
    """
    If true show under event type settings but don't show this booking field in the Booker. If false show in both. Can only be hidden
          for organization team event types when also providing attendee phone number booking field.
    """
    is_default: typing.Dict[str, typing.Any] = pydantic.Field(
        alias="isDefault",
    )
    """
    This property is always true because it's a default field
    """
    label: typing.Optional[str] = pydantic.Field(alias="label", default=None)
    placeholder: typing.Optional[str] = pydantic.Field(
        alias="placeholder", default=None
    )
    required: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="required", default=None
    )
    """
    Can be set to false only for organization team event types and if you also pass booking field {type: "phone", slug: "attendeePhoneNumber", required: true, hidden: false, label: "whatever label"} of booking field type PhoneFieldInput_2024_06_14 - this is done
          to enable phone only bookings where during the booking attendee can provide only their phone number and not provide email, so you must pass to the email booking field {hidden: true, required: false}.
          If true show under event type settings but don't show this booking field in the Booker. If false show in both.
    """
    slug: str = pydantic.Field(
        alias="slug",
    )
    type_field: typing_extensions.Literal[
        "address",
        "boolean",
        "checkbox",
        "email",
        "multiemail",
        "multiselect",
        "name",
        "number",
        "phone",
        "radio",
        "select",
        "text",
        "textarea",
        "url",
    ] = pydantic.Field(
        alias="type",
    )
    """
    only allowed value for type is `email`
    """
