import pydantic


class ApiKeyOutput(pydantic.BaseModel):
    """
    ApiKeyOutput
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    api_key: str = pydantic.Field(
        alias="apiKey",
    )
