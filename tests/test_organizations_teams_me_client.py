import pydantic
import pytest

from calcom_py import AsyncClient, Client
from calcom_py.environment import Environment
from calcom_py.types import models


def test_get_200_generated_success():
    """Tests a GET request to the /v2/organizations/{orgId}/teams/me endpoint.

    Operation: get
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.OrgMeTeamsOutputResponseDto

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(api_key="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.organizations.teams.me.get(org_id=123.45)
    try:
        pydantic.TypeAdapter(models.OrgMeTeamsOutputResponseDto).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_get_200_generated_success():
    """Tests a GET request to the /v2/organizations/{orgId}/teams/me endpoint.

    Operation: get
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.OrgMeTeamsOutputResponseDto

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(api_key="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.organizations.teams.me.get(org_id=123.45)
    try:
        pydantic.TypeAdapter(models.OrgMeTeamsOutputResponseDto).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"
