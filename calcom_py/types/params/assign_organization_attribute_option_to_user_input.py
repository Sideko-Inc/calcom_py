import pydantic
import typing
import typing_extensions


class AssignOrganizationAttributeOptionToUserInput(typing_extensions.TypedDict):
    """
    AssignOrganizationAttributeOptionToUserInput
    """

    attribute_id: typing_extensions.Required[str]

    attribute_option_id: typing_extensions.NotRequired[str]

    value: typing_extensions.NotRequired[str]


class _SerializerAssignOrganizationAttributeOptionToUserInput(pydantic.BaseModel):
    """
    Serializer for AssignOrganizationAttributeOptionToUserInput handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    attribute_id: str = pydantic.Field(
        alias="attributeId",
    )
    attribute_option_id: typing.Optional[str] = pydantic.Field(
        alias="attributeOptionId", default=None
    )
    value: typing.Optional[str] = pydantic.Field(alias="value", default=None)
