import pydantic
import typing
import typing_extensions


class BooleanFieldInput20240614(typing_extensions.TypedDict):
    """
    BooleanFieldInput20240614
    """

    disable_on_prefill: typing_extensions.NotRequired[bool]

    hidden: typing_extensions.Required[bool]
    """
    If true show under event type settings but don't show this booking field in the Booker. If false show in both.
    """

    label: typing_extensions.Required[str]

    required: typing_extensions.Required[bool]

    slug: typing_extensions.Required[str]
    """
    Unique identifier for the field in format `some-slug`. It is used to access response to this booking field during the booking
    """

    type_field: typing_extensions.Required[str]
    """
    only allowed value for type is `boolean`
    """


class _SerializerBooleanFieldInput20240614(pydantic.BaseModel):
    """
    Serializer for BooleanFieldInput20240614 handling case conversions
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
    required: bool = pydantic.Field(
        alias="required",
    )
    slug: str = pydantic.Field(
        alias="slug",
    )
    type_field: str = pydantic.Field(
        alias="type",
    )
