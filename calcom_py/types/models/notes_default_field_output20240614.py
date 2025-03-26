import pydantic
import typing
import typing_extensions


class NotesDefaultFieldOutput20240614(pydantic.BaseModel):
    """
    NotesDefaultFieldOutput20240614
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    disable_on_prefill: typing.Optional[bool] = pydantic.Field(
        alias="disableOnPrefill", default=None
    )
    """
    Disable this booking field if the URL contains query parameter with key equal to the slug and prefill it with the provided value.      For example, if URL contains query parameter `&notes=hello`,      the notes field will be prefilled with this value and disabled.
    """
    hidden: typing.Optional[bool] = pydantic.Field(alias="hidden", default=None)
    """
    If true show under event type settings but don't show this booking field in the Booker. If false show in both.
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
    required: typing.Optional[bool] = pydantic.Field(alias="required", default=None)
    slug: typing_extensions.Literal["email", "guests", "name", "notes", "title"] = (
        pydantic.Field(
            alias="slug",
        )
    )
    """
    only allowed value for type is `notes`
    """
    type_field: str = pydantic.Field(
        alias="type",
    )
