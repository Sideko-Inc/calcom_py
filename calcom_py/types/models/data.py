import pydantic
import typing


class Data(pydantic.BaseModel):
    """
    Data
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    agent_id: typing.Optional[str] = pydantic.Field(alias="agentId", default=None)
    call_id: str = pydantic.Field(
        alias="callId",
    )
