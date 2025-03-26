import pydantic
import typing_extensions

from .provider_verify_client_data import ProviderVerifyClientData


class ProviderVerifyClientOutput(pydantic.BaseModel):
    """
    ProviderVerifyClientOutput
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: ProviderVerifyClientData = pydantic.Field(
        alias="data",
    )
    status: typing_extensions.Literal["error", "success"] = pydantic.Field(
        alias="status",
    )
