import pydantic
import typing
import typing_extensions


class AddressFieldInput20240614(typing_extensions.TypedDict):
    """
    AddressFieldInput20240614
    """

    disable_on_prefill: typing_extensions.NotRequired[bool]
    """
    Disable this booking field if the URL contains query parameter with key equal to the slug and prefill it with the provided value.      For example, if the slug is `address` and the URL contains query parameter `&address=1234 Main St, London`,      the address field will be prefilled with this value and disabled.
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
    Unique identifier for the field in format `some-slug`. It is used to access response to this booking field during the booking
    """

    type_field: typing_extensions.Required[str]
    """
    only allowed value for type is `address`
    """


class _SerializerAddressFieldInput20240614(pydantic.BaseModel):
    """
    Serializer for AddressFieldInput20240614 handling case conversions
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
