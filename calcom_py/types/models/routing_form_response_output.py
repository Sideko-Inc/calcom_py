import pydantic
import typing


class RoutingFormResponseOutput(pydantic.BaseModel):
    """
    RoutingFormResponseOutput
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    created_at: str = pydantic.Field(
        alias="createdAt",
    )
    form_filler_id: str = pydantic.Field(
        alias="formFillerId",
    )
    form_id: str = pydantic.Field(
        alias="formId",
    )
    id: str = pydantic.Field(
        alias="id",
    )
    response: typing.Dict[str, typing.Any] = pydantic.Field(
        alias="response",
    )
    routed_to_booking_uid: str = pydantic.Field(
        alias="routedToBookingUid",
    )
