import pydantic
import typing_extensions


class GoogleServiceAccountKeyInput(typing_extensions.TypedDict):
    """
    GoogleServiceAccountKeyInput
    """

    client_email: typing_extensions.Required[str]

    client_id: typing_extensions.Required[str]

    private_key: typing_extensions.Required[str]


class _SerializerGoogleServiceAccountKeyInput(pydantic.BaseModel):
    """
    Serializer for GoogleServiceAccountKeyInput handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    client_email: str = pydantic.Field(
        alias="client_email",
    )
    client_id: str = pydantic.Field(
        alias="client_id",
    )
    private_key: str = pydantic.Field(
        alias="private_key",
    )
