import httpx
import pydantic
import pytest

from calcom_py import AsyncClient, Client
from calcom_py.environment import Environment
from calcom_py.types import models


def test_callback_200_generated_success():
    """Tests a GET request to the /v2/conferencing/{app}/oauth/callback endpoint.

    Operation: callback
    Test Case ID: generated_success
    Expected Status: 200
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
    response = client.conferencing.oauth.callback(
        app="msteams", code_field="string", state="string"
    )
    assert isinstance(response, httpx.Response)


@pytest.mark.asyncio
async def test_await_callback_200_generated_success():
    """Tests a GET request to the /v2/conferencing/{app}/oauth/callback endpoint.

    Operation: callback
    Test Case ID: generated_success
    Expected Status: 200
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
    response = await client.conferencing.oauth.callback(
        app="msteams", code_field="string", state="string"
    )
    assert isinstance(response, httpx.Response)


def test_auth_url_200_generated_success():
    """Tests a GET request to the /v2/conferencing/{app}/oauth/auth-url endpoint.

    Operation: auth_url
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.GetConferencingAppsOauthUrlResponseDto

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(api_key="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.conferencing.oauth.auth_url(
        app="msteams", on_error_return_to="string", return_to="string"
    )
    try:
        pydantic.TypeAdapter(
            models.GetConferencingAppsOauthUrlResponseDto
        ).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_auth_url_200_generated_success():
    """Tests a GET request to the /v2/conferencing/{app}/oauth/auth-url endpoint.

    Operation: auth_url
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.GetConferencingAppsOauthUrlResponseDto

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(api_key="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.conferencing.oauth.auth_url(
        app="msteams", on_error_return_to="string", return_to="string"
    )
    try:
        pydantic.TypeAdapter(
            models.GetConferencingAppsOauthUrlResponseDto
        ).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"
