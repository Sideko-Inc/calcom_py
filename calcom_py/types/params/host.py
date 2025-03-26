import pydantic
import typing
import typing_extensions


class Host(typing_extensions.TypedDict):
    """
    Host
    """

    mandatory: typing_extensions.NotRequired[bool]
    """
    Only relevant for round robin event types. If true then the user must attend round robin event always.
    """

    priority: typing_extensions.NotRequired[
        typing_extensions.Literal["high", "highest", "low", "lowest", "medium"]
    ]

    user_id: typing_extensions.Required[float]
    """
    Which user is the host of this event
    """


class _SerializerHost(pydantic.BaseModel):
    """
    Serializer for Host handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    mandatory: typing.Optional[bool] = pydantic.Field(alias="mandatory", default=None)
    priority: typing.Optional[
        typing_extensions.Literal["high", "highest", "low", "lowest", "medium"]
    ] = pydantic.Field(alias="priority", default=None)
    user_id: float = pydantic.Field(
        alias="userId",
    )
