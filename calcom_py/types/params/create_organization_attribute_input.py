import pydantic
import typing
import typing_extensions

from .create_organization_attribute_option_input import (
    CreateOrganizationAttributeOptionInput,
    _SerializerCreateOrganizationAttributeOptionInput,
)


class CreateOrganizationAttributeInput(typing_extensions.TypedDict):
    """
    CreateOrganizationAttributeInput
    """

    enabled: typing_extensions.NotRequired[bool]

    name: typing_extensions.Required[str]

    options: typing_extensions.Required[
        typing.List[CreateOrganizationAttributeOptionInput]
    ]

    slug: typing_extensions.Required[str]

    type_field: typing_extensions.Required[
        typing_extensions.Literal["MULTI_SELECT", "NUMBER", "SINGLE_SELECT", "TEXT"]
    ]


class _SerializerCreateOrganizationAttributeInput(pydantic.BaseModel):
    """
    Serializer for CreateOrganizationAttributeInput handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    enabled: typing.Optional[bool] = pydantic.Field(alias="enabled", default=None)
    name: str = pydantic.Field(
        alias="name",
    )
    options: typing.List[_SerializerCreateOrganizationAttributeOptionInput] = (
        pydantic.Field(
            alias="options",
        )
    )
    slug: str = pydantic.Field(
        alias="slug",
    )
    type_field: typing_extensions.Literal[
        "MULTI_SELECT", "NUMBER", "SINGLE_SELECT", "TEXT"
    ] = pydantic.Field(
        alias="type",
    )
