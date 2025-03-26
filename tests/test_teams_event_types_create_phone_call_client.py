import pydantic
import pytest

from calcom_py import AsyncClient, Client
from calcom_py.environment import Environment
from calcom_py.types import models


def test_create_201_success_default():
    """Tests a POST request to the /v2/teams/{teamId}/event-types/{eventTypeId}/create-phone-call endpoint.

    Operation: create
    Test Case ID: success_default
    Expected Status: 201
    Mode: Synchronous execution

    Response : models.CreatePhoneCallOutput

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(api_key="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.teams.event_types.create_phone_call.create(
        cal_api_key="string",
        enabled={},
        event_type_id=123.45,
        number_to_call="string",
        team_id=123.45,
        template_type="CHECK_IN_APPOINTMENT",
        your_phone_number="string",
    )
    try:
        pydantic.TypeAdapter(models.CreatePhoneCallOutput).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_create_201_success_default():
    """Tests a POST request to the /v2/teams/{teamId}/event-types/{eventTypeId}/create-phone-call endpoint.

    Operation: create
    Test Case ID: success_default
    Expected Status: 201
    Mode: Asynchronous execution

    Response : models.CreatePhoneCallOutput

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(api_key="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.teams.event_types.create_phone_call.create(
        cal_api_key="string",
        enabled={},
        event_type_id=123.45,
        number_to_call="string",
        team_id=123.45,
        template_type="CHECK_IN_APPOINTMENT",
        your_phone_number="string",
    )
    try:
        pydantic.TypeAdapter(models.CreatePhoneCallOutput).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"
