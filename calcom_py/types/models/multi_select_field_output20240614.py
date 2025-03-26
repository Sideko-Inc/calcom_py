import pydantic
import typing
import typing_extensions


class MultiSelectFieldOutput20240614(pydantic.BaseModel):
    """
    MultiSelectFieldOutput20240614
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    disable_on_prefill: typing.Optional[bool] = pydantic.Field(
        alias="disableOnPrefill", default=None
    )
    """
    Disable this booking field if the URL contains query parameter with key equal to the slug and prefill it with the provided value.      For example, if the slug is `consultants` and the URL contains query parameter `&consultants=en&language=it`,      the 'en' and 'it' will be selected and the select field will be disabled.
    """
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
    options: typing.List[str] = pydantic.Field(
        alias="options",
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
    only allowed value for type is `multiselect`
    """
