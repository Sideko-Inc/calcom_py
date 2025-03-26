import httpx
import pytest

from calcom_py import AsyncClient, Client
from calcom_py.environment import Environment


def test_create_201_success_default():
    """Tests a POST request to the /v2/organizations/{orgId}/users/{userId}/ooo endpoint.

    Operation: create
    Test Case ID: success_default
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
    response = client.organizations.users.ooo.create(
        end="2023-05-10T23:59:59.999Z",
        org_id=123.45,
        start="2023-05-01T00:00:00.000Z",
        user_id=123.45,
        notes="Vacation in Hawaii",
        reason="vacation",
        to_user_id=2.0,
    )
    assert isinstance(response, httpx.Response)


@pytest.mark.asyncio
async def test_await_create_201_success_default():
    """Tests a POST request to the /v2/organizations/{orgId}/users/{userId}/ooo endpoint.

    Operation: create
    Test Case ID: success_default
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
    response = await client.organizations.users.ooo.create(
        end="2023-05-10T23:59:59.999Z",
        org_id=123.45,
        start="2023-05-01T00:00:00.000Z",
        user_id=123.45,
        notes="Vacation in Hawaii",
        reason="vacation",
        to_user_id=2.0,
    )
    assert isinstance(response, httpx.Response)


def test_patch_200_success_default():
    """Tests a PATCH request to the /v2/organizations/{orgId}/users/{userId}/ooo/{oooId} endpoint.

    Operation: patch
    Test Case ID: success_default
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
    response = client.organizations.users.ooo.patch(
        ooo_id=123.45,
        org_id=123.45,
        user_id=123.45,
        end="2023-05-10T23:59:59.999Z",
        notes="Vacation in Hawaii",
        reason="vacation",
        start="2023-05-01T00:00:00.000Z",
        to_user_id=2.0,
    )
    assert isinstance(response, httpx.Response)


@pytest.mark.asyncio
async def test_await_patch_200_success_default():
    """Tests a PATCH request to the /v2/organizations/{orgId}/users/{userId}/ooo/{oooId} endpoint.

    Operation: patch
    Test Case ID: success_default
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
    response = await client.organizations.users.ooo.patch(
        ooo_id=123.45,
        org_id=123.45,
        user_id=123.45,
        end="2023-05-10T23:59:59.999Z",
        notes="Vacation in Hawaii",
        reason="vacation",
        start="2023-05-01T00:00:00.000Z",
        to_user_id=2.0,
    )
    assert isinstance(response, httpx.Response)


def test_list_200_generated_success():
    """Tests a GET request to the /v2/organizations/{orgId}/users/{userId}/ooo endpoint.

    Operation: list
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
    response = client.organizations.users.ooo.list(org_id=123.45, user_id=123.45)
    assert isinstance(response, httpx.Response)


@pytest.mark.asyncio
async def test_await_list_200_generated_success():
    """Tests a GET request to the /v2/organizations/{orgId}/users/{userId}/ooo endpoint.

    Operation: list
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
    response = await client.organizations.users.ooo.list(org_id=123.45, user_id=123.45)
    assert isinstance(response, httpx.Response)


def test_delete_200_generated_success():
    """Tests a DELETE request to the /v2/organizations/{orgId}/users/{userId}/ooo/{oooId} endpoint.

    Operation: delete
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
    response = client.organizations.users.ooo.delete(
        ooo_id=123.45, org_id=123.45, user_id=123.45
    )
    assert isinstance(response, httpx.Response)


@pytest.mark.asyncio
async def test_await_delete_200_generated_success():
    """Tests a DELETE request to the /v2/organizations/{orgId}/users/{userId}/ooo/{oooId} endpoint.

    Operation: delete
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
    response = await client.organizations.users.ooo.delete(
        ooo_id=123.45, org_id=123.45, user_id=123.45
    )
    assert isinstance(response, httpx.Response)
