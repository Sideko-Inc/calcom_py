import pydantic
import typing
import typing_extensions

from .google_service_account_key_input import (
    GoogleServiceAccountKeyInput,
    _SerializerGoogleServiceAccountKeyInput,
)


class UpdateDelegationCredentialInput(typing_extensions.TypedDict):
    """
    UpdateDelegationCredentialInput
    """

    enabled: typing_extensions.NotRequired[bool]

    service_account_key: typing_extensions.NotRequired[
        typing.List[GoogleServiceAccountKeyInput]
    ]


class _SerializerUpdateDelegationCredentialInput(pydantic.BaseModel):
    """
    Serializer for UpdateDelegationCredentialInput handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    enabled: typing.Optional[bool] = pydantic.Field(alias="enabled", default=None)
    service_account_key: typing.Optional[
        typing.List[_SerializerGoogleServiceAccountKeyInput]
    ] = pydantic.Field(alias="serviceAccountKey", default=None)
