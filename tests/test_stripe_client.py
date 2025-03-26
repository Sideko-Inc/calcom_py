import pydantic
import pytest

from calcom_py import AsyncClient, Client
from calcom_py.environment import Environment
from calcom_py.types import models


def test_save_200_generated_success():
    """Tests a GET request to the /v2/stripe/save endpoint.

    Operation: save
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.StripCredentialsSaveOutputResponseDto

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(api_key="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.stripe.save(code_field="string", state="string")
    try:
        pydantic.TypeAdapter(
            models.StripCredentialsSaveOutputResponseDto
        ).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_save_200_generated_success():
    """Tests a GET request to the /v2/stripe/save endpoint.

    Operation: save
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.StripCredentialsSaveOutputResponseDto

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(api_key="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.stripe.save(code_field="string", state="string")
    try:
        pydantic.TypeAdapter(
            models.StripCredentialsSaveOutputResponseDto
        ).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"
