import pydantic
import typing
import typing_extensions


class CreateIcsFeedInputDto(typing_extensions.TypedDict):
    """
    CreateIcsFeedInputDto
    """

    read_only: typing_extensions.NotRequired[bool]
    """
    Whether to allowing writing to the calendar or not
    """

    urls: typing_extensions.Required[typing.List[str]]
    """
    An array of ICS URLs
    """


class _SerializerCreateIcsFeedInputDto(pydantic.BaseModel):
    """
    Serializer for CreateIcsFeedInputDto handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    read_only: typing.Optional[bool] = pydantic.Field(alias="readOnly", default=None)
    urls: typing.List[str] = pydantic.Field(
        alias="urls",
    )
