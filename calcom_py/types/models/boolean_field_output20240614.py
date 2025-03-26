import pydantic
import typing
import typing_extensions


class BooleanFieldOutput20240614(pydantic.BaseModel):
    """
    BooleanFieldOutput20240614
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    disable_on_prefill: typing.Optional[bool] = pydantic.Field(
        alias="disableOnPrefill", default=None
    )
    hidden: bool = pydantic.Field(
        alias="hidden",
    )
    """
    If true show under event type settings but don't show this booking field in the Booker. If false show in both.
    """
    is_default: typing.Dict[str, typing.Any] = pydantic.Field(
        alias="isDefault",
    )
    """
    This property is always false because it's not default field but custom field
    """
    label: str = pydantic.Field(
        alias="label",
    )
    required: bool = pydantic.Field(
        alias="required",
    )
    slug: str = pydantic.Field(
        alias="slug",
    )
    """
    Unique identifier for the field in format `some-slug`. It is used to access response to this booking field during the booking
    """
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
    only allowed value for type is `boolean`
    """
