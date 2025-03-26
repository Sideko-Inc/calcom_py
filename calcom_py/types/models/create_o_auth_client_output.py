import pydantic


class CreateOAuthClientOutput(pydantic.BaseModel):
    """
    CreateOAuthClientOutput
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    client_id: str = pydantic.Field(
        alias="clientId",
    )
    client_secret: str = pydantic.Field(
        alias="clientSecret",
    )
