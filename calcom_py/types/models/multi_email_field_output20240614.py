import pydantic
import typing
import typing_extensions


class MultiEmailFieldOutput20240614(pydantic.BaseModel):
    """
    MultiEmailFieldOutput20240614
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    disable_on_prefill: typing.Optional[bool] = pydantic.Field(
        alias="disableOnPrefill", default=None
    )
    """
    Disable this booking field if the URL contains query parameter with key equal to the slug and prefill it with the provided value.      For example, if the slug is `consultants` and the URL contains query parameter `&consultants=alice@gmail.com&consultants=bob@gmail.com`,      the these emails will be added and none more can be added.
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
    placeholder: typing.Optional[str] = pydantic.Field(
        alias="placeholder", default=None
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
    only allowed value for type is `multiemail`
    """
