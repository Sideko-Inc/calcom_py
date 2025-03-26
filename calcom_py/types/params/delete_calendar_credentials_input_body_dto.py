import pydantic
import typing_extensions


class DeleteCalendarCredentialsInputBodyDto(typing_extensions.TypedDict):
    """
    DeleteCalendarCredentialsInputBodyDto
    """

    id: typing_extensions.Required[int]
    """
    Credential ID of the calendar to delete, as returned by the /calendars endpoint
    """


class _SerializerDeleteCalendarCredentialsInputBodyDto(pydantic.BaseModel):
    """
    Serializer for DeleteCalendarCredentialsInputBodyDto handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    id: int = pydantic.Field(
        alias="id",
    )
