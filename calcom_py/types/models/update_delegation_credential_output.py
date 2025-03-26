import pydantic
import typing_extensions

from .delegation_credential_output import DelegationCredentialOutput


class UpdateDelegationCredentialOutput(pydantic.BaseModel):
    """
    UpdateDelegationCredentialOutput
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: DelegationCredentialOutput = pydantic.Field(
        alias="data",
    )
    status: typing_extensions.Literal["error", "success"] = pydantic.Field(
        alias="status",
    )
