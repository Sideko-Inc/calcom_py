import pydantic
import typing
import typing_extensions

from .google_service_account_key_input import (
    GoogleServiceAccountKeyInput,
    _SerializerGoogleServiceAccountKeyInput,
)


class CreateDelegationCredentialInput(typing_extensions.TypedDict):
    """
    CreateDelegationCredentialInput
    """

    domain: typing_extensions.Required[str]

    service_account_key: typing_extensions.Required[
        typing.List[GoogleServiceAccountKeyInput]
    ]

    workspace_platform_slug: typing_extensions.Required[str]


class _SerializerCreateDelegationCredentialInput(pydantic.BaseModel):
    """
    Serializer for CreateDelegationCredentialInput handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    domain: str = pydantic.Field(
        alias="domain",
    )
    service_account_key: typing.List[_SerializerGoogleServiceAccountKeyInput] = (
        pydantic.Field(
            alias="serviceAccountKey",
        )
    )
    workspace_platform_slug: str = pydantic.Field(
        alias="workspacePlatformSlug",
    )
