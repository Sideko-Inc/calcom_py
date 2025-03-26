import pydantic
import typing_extensions


class CreateOrganizationAttributeOptionInput(typing_extensions.TypedDict):
    """
    CreateOrganizationAttributeOptionInput
    """

    slug: typing_extensions.Required[str]

    value: typing_extensions.Required[str]


class _SerializerCreateOrganizationAttributeOptionInput(pydantic.BaseModel):
    """
    Serializer for CreateOrganizationAttributeOptionInput handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    slug: str = pydantic.Field(
        alias="slug",
    )
    value: str = pydantic.Field(
        alias="value",
    )
