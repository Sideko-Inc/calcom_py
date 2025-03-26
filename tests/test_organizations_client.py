import pydantic
import pytest

from calcom_py import AsyncClient, Client
from calcom_py.environment import Environment
from calcom_py.types import models


def test_create_201_success_default():
    """Tests a POST request to the /v2/organizations/{orgId}/organizations endpoint.

    Operation: create
    Test Case ID: success_default
    Expected Status: 201
    Mode: Synchronous execution

    Response : models.CreateManagedOrganizationOutput

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(api_key="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.organizations.create(
        name="CalTeam",
        org_id=123.45,
        api_key_days_valid=60.0,
        api_key_never_expires=True,
        metadata={"key": "value"},
    )
    try:
        pydantic.TypeAdapter(models.CreateManagedOrganizationOutput).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_create_201_success_default():
    """Tests a POST request to the /v2/organizations/{orgId}/organizations endpoint.

    Operation: create
    Test Case ID: success_default
    Expected Status: 201
    Mode: Asynchronous execution

    Response : models.CreateManagedOrganizationOutput

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(api_key="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.organizations.create(
        name="CalTeam",
        org_id=123.45,
        api_key_days_valid=60.0,
        api_key_never_expires=True,
        metadata={"key": "value"},
    )
    try:
        pydantic.TypeAdapter(models.CreateManagedOrganizationOutput).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_patch_200_success_default():
    """Tests a PATCH request to the /v2/organizations/{orgId}/organizations/{managedOrganizationId} endpoint.

    Operation: patch
    Test Case ID: success_default
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.GetManagedOrganizationOutput

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(api_key="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.organizations.patch(
        managed_organization_id=123.45,
        org_id=123.45,
        metadata={"key": "value"},
        name="CalTeam",
    )
    try:
        pydantic.TypeAdapter(models.GetManagedOrganizationOutput).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_patch_200_success_default():
    """Tests a PATCH request to the /v2/organizations/{orgId}/organizations/{managedOrganizationId} endpoint.

    Operation: patch
    Test Case ID: success_default
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.GetManagedOrganizationOutput

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(api_key="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.organizations.patch(
        managed_organization_id=123.45,
        org_id=123.45,
        metadata={"key": "value"},
        name="CalTeam",
    )
    try:
        pydantic.TypeAdapter(models.GetManagedOrganizationOutput).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_get_200_generated_success():
    """Tests a GET request to the /v2/organizations/{orgId}/organizations/{managedOrganizationId} endpoint.

    Operation: get
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.GetManagedOrganizationOutput

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(api_key="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.organizations.get(managed_organization_id=123.45, org_id=123.45)
    try:
        pydantic.TypeAdapter(models.GetManagedOrganizationOutput).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_get_200_generated_success():
    """Tests a GET request to the /v2/organizations/{orgId}/organizations/{managedOrganizationId} endpoint.

    Operation: get
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.GetManagedOrganizationOutput

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(api_key="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.organizations.get(
        managed_organization_id=123.45, org_id=123.45
    )
    try:
        pydantic.TypeAdapter(models.GetManagedOrganizationOutput).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_list_200_generated_success():
    """Tests a GET request to the /v2/organizations/{orgId}/organizations endpoint.

    Operation: list
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.GetManagedOrganizationsOutput

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(api_key="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.organizations.list(org_id=123.45)
    try:
        pydantic.TypeAdapter(models.GetManagedOrganizationsOutput).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_list_200_generated_success():
    """Tests a GET request to the /v2/organizations/{orgId}/organizations endpoint.

    Operation: list
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.GetManagedOrganizationsOutput

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(api_key="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.organizations.list(org_id=123.45)
    try:
        pydantic.TypeAdapter(models.GetManagedOrganizationsOutput).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_delete_200_generated_success():
    """Tests a DELETE request to the /v2/organizations/{orgId}/organizations/{managedOrganizationId} endpoint.

    Operation: delete
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.GetManagedOrganizationOutput

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(api_key="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.organizations.delete(
        managed_organization_id=123.45, org_id=123.45
    )
    try:
        pydantic.TypeAdapter(models.GetManagedOrganizationOutput).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_delete_200_generated_success():
    """Tests a DELETE request to the /v2/organizations/{orgId}/organizations/{managedOrganizationId} endpoint.

    Operation: delete
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.GetManagedOrganizationOutput

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(api_key="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.organizations.delete(
        managed_organization_id=123.45, org_id=123.45
    )
    try:
        pydantic.TypeAdapter(models.GetManagedOrganizationOutput).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"
