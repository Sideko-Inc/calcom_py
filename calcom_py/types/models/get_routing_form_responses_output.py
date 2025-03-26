import pydantic
import typing
import typing_extensions

from .routing_form_response_output import RoutingFormResponseOutput


class GetRoutingFormResponsesOutput(pydantic.BaseModel):
    """
    GetRoutingFormResponsesOutput
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.List[RoutingFormResponseOutput] = pydantic.Field(
        alias="data",
    )
    status: typing_extensions.Literal["error", "success"] = pydantic.Field(
        alias="status",
    )
