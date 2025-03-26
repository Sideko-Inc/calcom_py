import pydantic
import pytest

from calcom_py import AsyncClient, Client
from calcom_py.environment import Environment
from calcom_py.types import models


def test_create_201_success_default():
    """Tests a POST request to the /v2/event-types endpoint.

    Operation: create
    Test Case ID: success_default
    Expected Status: 201
    Mode: Synchronous execution

    Response : models.CreateEventTypeOutput20240614

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(api_key="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.event_types.create(
        cal_api_version="string",
        length_in_minutes=60.0,
        slug="learn-the-secrets-of-masterchief",
        title="Learn the secrets of masterchief!",
        custom_name="{Event type title} between {Organiser} and {Scheduler}",
        description="Discover the culinary wonders of the Argentina by making the best flan ever!",
        length_in_minutes_options=["string", "string", "string"],
        success_redirect_url="https://masterchief.com/argentina/flan/video/9129412",
    )
    try:
        pydantic.TypeAdapter(models.CreateEventTypeOutput20240614).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_create_201_success_default():
    """Tests a POST request to the /v2/event-types endpoint.

    Operation: create
    Test Case ID: success_default
    Expected Status: 201
    Mode: Asynchronous execution

    Response : models.CreateEventTypeOutput20240614

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(api_key="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.event_types.create(
        cal_api_version="string",
        length_in_minutes=60.0,
        slug="learn-the-secrets-of-masterchief",
        title="Learn the secrets of masterchief!",
        custom_name="{Event type title} between {Organiser} and {Scheduler}",
        description="Discover the culinary wonders of the Argentina by making the best flan ever!",
        length_in_minutes_options=["string", "string", "string"],
        success_redirect_url="https://masterchief.com/argentina/flan/video/9129412",
    )
    try:
        pydantic.TypeAdapter(models.CreateEventTypeOutput20240614).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_patch_200_success_default():
    """Tests a PATCH request to the /v2/event-types/{eventTypeId} endpoint.

    Operation: patch
    Test Case ID: success_default
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.UpdateEventTypeOutput20240614

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(api_key="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.event_types.patch(
        cal_api_version="string",
        event_type_id=123.45,
        custom_name="{Event type title} between {Organiser} and {Scheduler}",
        description="Discover the culinary wonders of the Argentina by making the best flan ever!",
        length_in_minutes=60.0,
        length_in_minutes_options=["string", "string", "string"],
        slug="learn-the-secrets-of-masterchief",
        success_redirect_url="https://masterchief.com/argentina/flan/video/9129412",
        title="Learn the secrets of masterchief!",
    )
    try:
        pydantic.TypeAdapter(models.UpdateEventTypeOutput20240614).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_patch_200_success_default():
    """Tests a PATCH request to the /v2/event-types/{eventTypeId} endpoint.

    Operation: patch
    Test Case ID: success_default
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.UpdateEventTypeOutput20240614

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(api_key="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.event_types.patch(
        cal_api_version="string",
        event_type_id=123.45,
        custom_name="{Event type title} between {Organiser} and {Scheduler}",
        description="Discover the culinary wonders of the Argentina by making the best flan ever!",
        length_in_minutes=60.0,
        length_in_minutes_options=["string", "string", "string"],
        slug="learn-the-secrets-of-masterchief",
        success_redirect_url="https://masterchief.com/argentina/flan/video/9129412",
        title="Learn the secrets of masterchief!",
    )
    try:
        pydantic.TypeAdapter(models.UpdateEventTypeOutput20240614).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_get_200_generated_success():
    """Tests a GET request to the /v2/event-types/{eventTypeId} endpoint.

    Operation: get
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.GetEventTypeOutput20240614

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(api_key="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.event_types.get(cal_api_version="string", event_type_id="string")
    try:
        pydantic.TypeAdapter(models.GetEventTypeOutput20240614).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_get_200_generated_success():
    """Tests a GET request to the /v2/event-types/{eventTypeId} endpoint.

    Operation: get
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.GetEventTypeOutput20240614

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(api_key="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.event_types.get(
        cal_api_version="string", event_type_id="string"
    )
    try:
        pydantic.TypeAdapter(models.GetEventTypeOutput20240614).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_list_200_generated_success():
    """Tests a GET request to the /v2/event-types endpoint.

    Operation: list
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.GetEventTypesOutput20240614

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(api_key="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.event_types.list(cal_api_version="string")
    try:
        pydantic.TypeAdapter(models.GetEventTypesOutput20240614).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_list_200_generated_success():
    """Tests a GET request to the /v2/event-types endpoint.

    Operation: list
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.GetEventTypesOutput20240614

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(api_key="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.event_types.list(cal_api_version="string")
    try:
        pydantic.TypeAdapter(models.GetEventTypesOutput20240614).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_delete_200_generated_success():
    """Tests a DELETE request to the /v2/event-types/{eventTypeId} endpoint.

    Operation: delete
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.DeleteEventTypeOutput20240614

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(api_key="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.event_types.delete(cal_api_version="string", event_type_id=123.45)
    try:
        pydantic.TypeAdapter(models.DeleteEventTypeOutput20240614).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_delete_200_generated_success():
    """Tests a DELETE request to the /v2/event-types/{eventTypeId} endpoint.

    Operation: delete
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.DeleteEventTypeOutput20240614

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(api_key="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.event_types.delete(
        cal_api_version="string", event_type_id=123.45
    )
    try:
        pydantic.TypeAdapter(models.DeleteEventTypeOutput20240614).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"
