import pydantic
import typing
import typing_extensions


class CreateOrganizationInput(typing_extensions.TypedDict):
    """
    CreateOrganizationInput
    """

    api_key_days_valid: typing_extensions.NotRequired[float]
    """
    For how many days is managed organization api key valid. Defaults to 30 days.
    """

    api_key_never_expires: typing_extensions.NotRequired[bool]
    """
    If true, organization api key never expires.
    """

    metadata: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]
    """
    You can store any additional data you want here.
    Metadata must have at most 50 keys, each key up to 40 characters.
    Values can be strings (up to 500 characters), numbers, or booleans.
    """

    name: typing_extensions.Required[str]
    """
    Name of the organization
    """


class _SerializerCreateOrganizationInput(pydantic.BaseModel):
    """
    Serializer for CreateOrganizationInput handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    api_key_days_valid: typing.Optional[float] = pydantic.Field(
        alias="apiKeyDaysValid", default=None
    )
    api_key_never_expires: typing.Optional[bool] = pydantic.Field(
        alias="apiKeyNeverExpires", default=None
    )
    metadata: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="metadata", default=None
    )
    name: str = pydantic.Field(
        alias="name",
    )
