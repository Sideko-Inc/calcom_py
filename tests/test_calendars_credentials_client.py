import httpx
import pytest

from calcom_py import AsyncClient, Client
from calcom_py.environment import Environment


def test_create_201_generated_success():
    """Tests a POST request to the /v2/calendars/{calendar}/credentials endpoint.

    Operation: create
    Test Case ID: generated_success
    Expected Status: 201
    Mode: Synchronous execution

    Response : httpx.Response

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(api_key="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.calendars.credentials.create(calendar_field="apple")
    assert isinstance(response, httpx.Response)


@pytest.mark.asyncio
async def test_await_create_201_generated_success():
    """Tests a POST request to the /v2/calendars/{calendar}/credentials endpoint.

    Operation: create
    Test Case ID: generated_success
    Expected Status: 201
    Mode: Asynchronous execution

    Response : httpx.Response

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(api_key="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.calendars.credentials.create(calendar_field="apple")
    assert isinstance(response, httpx.Response)
