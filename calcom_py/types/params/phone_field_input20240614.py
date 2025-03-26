import pydantic
import typing
import typing_extensions


class PhoneFieldInput20240614(typing_extensions.TypedDict):
    """
    PhoneFieldInput20240614
    """

    disable_on_prefill: typing_extensions.NotRequired[bool]
    """
    Disable this booking field if the URL contains query parameter with key equal to the slug and prefill it with the provided value.      For example, if the slug is `phone` and the URL contains query parameter `&phone=1234567890`,      the phone field will be prefilled with this value and disabled.
    """

    hidden: typing_extensions.Required[bool]
    """
    If true show under event type settings but don't show this booking field in the Booker. If false show in both.
    """

    label: typing_extensions.Required[str]

    placeholder: typing_extensions.Required[str]

    required: typing_extensions.Required[bool]

    slug: typing_extensions.Required[str]
    """
    Unique identifier for the field in format `some-slug`. It is used to access response to this booking field during the booking. Special slug is `attendeePhoneNumber` - if you create
          a phone input field with this slug for organization team event type you can create an organization team event type that can be booked using phone without requiring an email by setting {"type": "email", "required": false, "hidden": true} to the email booking field input in the request body.
    """

    type_field: typing_extensions.Required[str]
    """
    only allowed value for type is `phone`
    """


class _SerializerPhoneFieldInput20240614(pydantic.BaseModel):
    """
    Serializer for PhoneFieldInput20240614 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    disable_on_prefill: typing.Optional[bool] = pydantic.Field(
        alias="disableOnPrefill", default=None
    )
    hidden: bool = pydantic.Field(
        alias="hidden",
    )
    label: str = pydantic.Field(
        alias="label",
    )
    placeholder: str = pydantic.Field(
        alias="placeholder",
    )
    required: bool = pydantic.Field(
        alias="required",
    )
    slug: str = pydantic.Field(
        alias="slug",
    )
    type_field: str = pydantic.Field(
        alias="type",
    )
