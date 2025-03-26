import pydantic
import typing
import typing_extensions


class NameDefaultFieldInput20240614(typing_extensions.TypedDict):
    """
    NameDefaultFieldInput20240614
    """

    disable_on_prefill: typing_extensions.NotRequired[bool]
    """
    Disable this booking field if the URL contains query parameter with key equal to the slug and prefill it with the provided value.      For example, if URL contains query parameter `&name=bob`,      the name field will be prefilled with this value and disabled.
    """

    label: typing_extensions.Required[str]

    placeholder: typing_extensions.Required[str]

    type_field: typing_extensions.Required[str]
    """
    only allowed value for type is `name`. Used for having 1 booking field for both first name and last name.
    """


class _SerializerNameDefaultFieldInput20240614(pydantic.BaseModel):
    """
    Serializer for NameDefaultFieldInput20240614 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    disable_on_prefill: typing.Optional[bool] = pydantic.Field(
        alias="disableOnPrefill", default=None
    )
    label: str = pydantic.Field(
        alias="label",
    )
    placeholder: str = pydantic.Field(
        alias="placeholder",
    )
    type_field: str = pydantic.Field(
        alias="type",
    )
