import pydantic
import pytest

from calcom_py import AsyncClient, Client
from calcom_py.environment import Environment
from calcom_py.types import models


def test_refresh_200_success_default():
    """Tests a POST request to the /v2/oauth/{clientId}/refresh endpoint.

    Operation: refresh
    Test Case ID: success_default
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.KeysResponseDto

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(api_key="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.oauth.refresh(
        client_id="string", refresh_token="string", x_cal_secret_key="string"
    )
    try:
        pydantic.TypeAdapter(models.KeysResponseDto).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_refresh_200_success_default():
    """Tests a POST request to the /v2/oauth/{clientId}/refresh endpoint.

    Operation: refresh
    Test Case ID: success_default
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.KeysResponseDto

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(api_key="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.oauth.refresh(
        client_id="string", refresh_token="string", x_cal_secret_key="string"
    )
    try:
        pydantic.TypeAdapter(models.KeysResponseDto).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"
