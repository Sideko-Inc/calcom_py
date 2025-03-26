import pydantic
import typing
import typing_extensions


class NameDefaultFieldOutput20240614(pydantic.BaseModel):
    """
    NameDefaultFieldOutput20240614
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    disable_on_prefill: typing.Optional[bool] = pydantic.Field(
        alias="disableOnPrefill", default=None
    )
    """
    Disable this booking field if the URL contains query parameter with key equal to the slug and prefill it with the provided value.      For example, if URL contains query parameter `&name=bob`,      the name field will be prefilled with this value and disabled.
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
    required: bool = pydantic.Field(
        alias="required",
    )
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
    only allowed value for type is `name`. Used for having 1 booking field for both first name and last name.
    """
