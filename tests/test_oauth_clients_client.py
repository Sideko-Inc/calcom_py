import pydantic
import pytest

from calcom_py import AsyncClient, Client
from calcom_py.environment import Environment
from calcom_py.types import models


def test_create_201_success_default():
    """Tests a POST request to the /v2/oauth-clients endpoint.

    Operation: create
    Test Case ID: success_default
    Expected Status: 201
    Mode: Synchronous execution

    Response : models.CreateOAuthClientResponseDto

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(api_key="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.oauth_clients.create(
        name="string", permissions=["*"], redirect_uris=["string"]
    )
    try:
        pydantic.TypeAdapter(models.CreateOAuthClientResponseDto).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_create_201_success_default():
    """Tests a POST request to the /v2/oauth-clients endpoint.

    Operation: create
    Test Case ID: success_default
    Expected Status: 201
    Mode: Asynchronous execution

    Response : models.CreateOAuthClientResponseDto

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(api_key="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.oauth_clients.create(
        name="string", permissions=["*"], redirect_uris=["string"]
    )
    try:
        pydantic.TypeAdapter(models.CreateOAuthClientResponseDto).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_patch_200_success_default():
    """Tests a PATCH request to the /v2/oauth-clients/{clientId} endpoint.

    Operation: patch
    Test Case ID: success_default
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.GetOAuthClientResponseDto

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(api_key="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.oauth_clients.patch(client_id="string")
    try:
        pydantic.TypeAdapter(models.GetOAuthClientResponseDto).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_patch_200_success_default():
    """Tests a PATCH request to the /v2/oauth-clients/{clientId} endpoint.

    Operation: patch
    Test Case ID: success_default
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.GetOAuthClientResponseDto

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(api_key="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.oauth_clients.patch(client_id="string")
    try:
        pydantic.TypeAdapter(models.GetOAuthClientResponseDto).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_get_200_generated_success():
    """Tests a GET request to the /v2/oauth-clients/{clientId} endpoint.

    Operation: get
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.GetOAuthClientResponseDto

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(api_key="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.oauth_clients.get(client_id="string")
    try:
        pydantic.TypeAdapter(models.GetOAuthClientResponseDto).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_get_200_generated_success():
    """Tests a GET request to the /v2/oauth-clients/{clientId} endpoint.

    Operation: get
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.GetOAuthClientResponseDto

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(api_key="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.oauth_clients.get(client_id="string")
    try:
        pydantic.TypeAdapter(models.GetOAuthClientResponseDto).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_list_200_generated_success():
    """Tests a GET request to the /v2/oauth-clients endpoint.

    Operation: list
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.GetOAuthClientsResponseDto

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(api_key="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.oauth_clients.list()
    try:
        pydantic.TypeAdapter(models.GetOAuthClientsResponseDto).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_list_200_generated_success():
    """Tests a GET request to the /v2/oauth-clients endpoint.

    Operation: list
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.GetOAuthClientsResponseDto

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(api_key="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.oauth_clients.list()
    try:
        pydantic.TypeAdapter(models.GetOAuthClientsResponseDto).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_delete_200_generated_success():
    """Tests a DELETE request to the /v2/oauth-clients/{clientId} endpoint.

    Operation: delete
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.GetOAuthClientResponseDto

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(api_key="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.oauth_clients.delete(client_id="string")
    try:
        pydantic.TypeAdapter(models.GetOAuthClientResponseDto).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_delete_200_generated_success():
    """Tests a DELETE request to the /v2/oauth-clients/{clientId} endpoint.

    Operation: delete
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.GetOAuthClientResponseDto

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(api_key="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.oauth_clients.delete(client_id="string")
    try:
        pydantic.TypeAdapter(models.GetOAuthClientResponseDto).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"
