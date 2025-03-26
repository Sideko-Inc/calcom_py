import pydantic
import typing
import typing_extensions


class GuestsDefaultFieldInput20240614(typing_extensions.TypedDict):
    """
    GuestsDefaultFieldInput20240614
    """

    disable_on_prefill: typing_extensions.NotRequired[bool]
    """
    Disable this booking field if the URL contains query parameter with key equal to the slug and prefill it with the provided value.      For example, if URL contains query parameter `&guests=bob@cal.com`,      the guests field will be prefilled with this value and disabled.
    """

    hidden: typing_extensions.NotRequired[bool]
    """
    If true show under event type settings but don't show this booking field in the Booker. If false show in both.
    """

    label: typing_extensions.NotRequired[str]

    placeholder: typing_extensions.NotRequired[str]

    required: typing_extensions.NotRequired[bool]

    slug: typing_extensions.Required[str]
    """
    only allowed value for type is `guests`
    """


class _SerializerGuestsDefaultFieldInput20240614(pydantic.BaseModel):
    """
    Serializer for GuestsDefaultFieldInput20240614 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    disable_on_prefill: typing.Optional[bool] = pydantic.Field(
        alias="disableOnPrefill", default=None
    )
    hidden: typing.Optional[bool] = pydantic.Field(alias="hidden", default=None)
    label: typing.Optional[str] = pydantic.Field(alias="label", default=None)
    placeholder: typing.Optional[str] = pydantic.Field(
        alias="placeholder", default=None
    )
    required: typing.Optional[bool] = pydantic.Field(alias="required", default=None)
    slug: str = pydantic.Field(
        alias="slug",
    )
