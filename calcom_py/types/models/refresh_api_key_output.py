import pydantic
import typing_extensions

from .api_key_output import ApiKeyOutput


class RefreshApiKeyOutput(pydantic.BaseModel):
    """
    RefreshApiKeyOutput
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: ApiKeyOutput = pydantic.Field(
        alias="data",
    )
    status: typing_extensions.Literal["error", "success"] = pydantic.Field(
        alias="status",
    )
