import pydantic
import typing
import typing_extensions


class UpdateOrganizationInput(typing_extensions.TypedDict):
    """
    UpdateOrganizationInput
    """

    metadata: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]
    """
    You can store any additional data you want here.
    Metadata must have at most 50 keys, each key up to 40 characters.
    Values can be strings (up to 500 characters), numbers, or booleans.
    """

    name: typing_extensions.NotRequired[str]
    """
    Name of the organization
    """


class _SerializerUpdateOrganizationInput(pydantic.BaseModel):
    """
    Serializer for UpdateOrganizationInput handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    metadata: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="metadata", default=None
    )
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
