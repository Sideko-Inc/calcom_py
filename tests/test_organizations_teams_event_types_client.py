import pydantic
import pytest

from calcom_py import AsyncClient, Client
from calcom_py.environment import Environment
from calcom_py.types import models


def test_create_phone_call_201_success_default():
    """Tests a POST request to the /v2/organizations/{orgId}/teams/{teamId}/event-types/{eventTypeId}/create-phone-call endpoint.

    Operation: create_phone_call
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
    response = client.organizations.teams.event_types.create_phone_call(
        cal_api_key="string",
        enabled={},
        event_type_id=123.45,
        number_to_call="string",
        org_id=123.45,
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
async def test_await_create_phone_call_201_success_default():
    """Tests a POST request to the /v2/organizations/{orgId}/teams/{teamId}/event-types/{eventTypeId}/create-phone-call endpoint.

    Operation: create_phone_call
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
    response = await client.organizations.teams.event_types.create_phone_call(
        cal_api_key="string",
        enabled={},
        event_type_id=123.45,
        number_to_call="string",
        org_id=123.45,
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


def test_create_201_success_default():
    """Tests a POST request to the /v2/organizations/{orgId}/teams/{teamId}/event-types endpoint.

    Operation: create
    Test Case ID: success_default
    Expected Status: 201
    Mode: Synchronous execution

    Response : models.CreateTeamEventTypeOutput

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(api_key="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.organizations.teams.event_types.create(
        hosts=[{"user_id": 123.45}],
        length_in_minutes=60.0,
        org_id=123.45,
        scheduling_type="collective",
        slug="learn-the-secrets-of-masterchief",
        team_id=123.45,
        title="Learn the secrets of masterchief!",
        custom_name="{Event type title} between {Organiser} and {Scheduler}",
        description="Discover the culinary wonders of the Argentina by making the best flan ever!",
        length_in_minutes_options=["string", "string", "string"],
        success_redirect_url="https://masterchief.com/argentina/flan/video/9129412",
    )
    try:
        pydantic.TypeAdapter(models.CreateTeamEventTypeOutput).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_create_201_success_default():
    """Tests a POST request to the /v2/organizations/{orgId}/teams/{teamId}/event-types endpoint.

    Operation: create
    Test Case ID: success_default
    Expected Status: 201
    Mode: Asynchronous execution

    Response : models.CreateTeamEventTypeOutput

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(api_key="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.organizations.teams.event_types.create(
        hosts=[{"user_id": 123.45}],
        length_in_minutes=60.0,
        org_id=123.45,
        scheduling_type="collective",
        slug="learn-the-secrets-of-masterchief",
        team_id=123.45,
        title="Learn the secrets of masterchief!",
        custom_name="{Event type title} between {Organiser} and {Scheduler}",
        description="Discover the culinary wonders of the Argentina by making the best flan ever!",
        length_in_minutes_options=["string", "string", "string"],
        success_redirect_url="https://masterchief.com/argentina/flan/video/9129412",
    )
    try:
        pydantic.TypeAdapter(models.CreateTeamEventTypeOutput).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_patch_200_success_default():
    """Tests a PATCH request to the /v2/organizations/{orgId}/teams/{teamId}/event-types/{eventTypeId} endpoint.

    Operation: patch
    Test Case ID: success_default
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.UpdateTeamEventTypeOutput

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(api_key="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.organizations.teams.event_types.patch(
        event_type_id=123.45,
        org_id=123.45,
        team_id=123.45,
        custom_name="{Event type title} between {Organiser} and {Scheduler}",
        description="Discover the culinary wonders of the Argentina by making the best flan ever!",
        length_in_minutes=60.0,
        length_in_minutes_options=["string", "string", "string"],
        slug="learn-the-secrets-of-masterchief",
        success_redirect_url="https://masterchief.com/argentina/flan/video/9129412",
        title="Learn the secrets of masterchief!",
    )
    try:
        pydantic.TypeAdapter(models.UpdateTeamEventTypeOutput).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_patch_200_success_default():
    """Tests a PATCH request to the /v2/organizations/{orgId}/teams/{teamId}/event-types/{eventTypeId} endpoint.

    Operation: patch
    Test Case ID: success_default
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.UpdateTeamEventTypeOutput

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(api_key="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.organizations.teams.event_types.patch(
        event_type_id=123.45,
        org_id=123.45,
        team_id=123.45,
        custom_name="{Event type title} between {Organiser} and {Scheduler}",
        description="Discover the culinary wonders of the Argentina by making the best flan ever!",
        length_in_minutes=60.0,
        length_in_minutes_options=["string", "string", "string"],
        slug="learn-the-secrets-of-masterchief",
        success_redirect_url="https://masterchief.com/argentina/flan/video/9129412",
        title="Learn the secrets of masterchief!",
    )
    try:
        pydantic.TypeAdapter(models.UpdateTeamEventTypeOutput).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_get_one_200_generated_success():
    """Tests a GET request to the /v2/organizations/{orgId}/teams/{teamId}/event-types/{eventTypeId} endpoint.

    Operation: get_one
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.GetTeamEventTypeOutput

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(api_key="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.organizations.teams.event_types.get_one(
        event_type_id=123.45, org_id=123.45, team_id=123.45
    )
    try:
        pydantic.TypeAdapter(models.GetTeamEventTypeOutput).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_get_one_200_generated_success():
    """Tests a GET request to the /v2/organizations/{orgId}/teams/{teamId}/event-types/{eventTypeId} endpoint.

    Operation: get_one
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.GetTeamEventTypeOutput

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(api_key="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.organizations.teams.event_types.get_one(
        event_type_id=123.45, org_id=123.45, team_id=123.45
    )
    try:
        pydantic.TypeAdapter(models.GetTeamEventTypeOutput).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_list_200_generated_success():
    """Tests a GET request to the /v2/organizations/{orgId}/teams/{teamId}/event-types endpoint.

    Operation: list
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.GetTeamEventTypesOutput

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(api_key="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.organizations.teams.event_types.list(
        org_id=123.45, team_id=123.45
    )
    try:
        pydantic.TypeAdapter(models.GetTeamEventTypesOutput).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_list_200_generated_success():
    """Tests a GET request to the /v2/organizations/{orgId}/teams/{teamId}/event-types endpoint.

    Operation: list
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.GetTeamEventTypesOutput

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(api_key="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.organizations.teams.event_types.list(
        org_id=123.45, team_id=123.45
    )
    try:
        pydantic.TypeAdapter(models.GetTeamEventTypesOutput).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_list_for_team_200_generated_success():
    """Tests a GET request to the /v2/organizations/{orgId}/teams/event-types endpoint.

    Operation: list_for_team
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.GetTeamEventTypesOutput

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(api_key="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.organizations.teams.event_types.list_for_team(org_id=123.45)
    try:
        pydantic.TypeAdapter(models.GetTeamEventTypesOutput).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_list_for_team_200_generated_success():
    """Tests a GET request to the /v2/organizations/{orgId}/teams/event-types endpoint.

    Operation: list_for_team
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.GetTeamEventTypesOutput

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(api_key="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.organizations.teams.event_types.list_for_team(org_id=123.45)
    try:
        pydantic.TypeAdapter(models.GetTeamEventTypesOutput).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_delete_200_generated_success():
    """Tests a DELETE request to the /v2/organizations/{orgId}/teams/{teamId}/event-types/{eventTypeId} endpoint.

    Operation: delete
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.DeleteTeamEventTypeOutput

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(api_key="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.organizations.teams.event_types.delete(
        event_type_id=123.45, org_id=123.45, team_id=123.45
    )
    try:
        pydantic.TypeAdapter(models.DeleteTeamEventTypeOutput).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_delete_200_generated_success():
    """Tests a DELETE request to the /v2/organizations/{orgId}/teams/{teamId}/event-types/{eventTypeId} endpoint.

    Operation: delete
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.DeleteTeamEventTypeOutput

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(api_key="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.organizations.teams.event_types.delete(
        event_type_id=123.45, org_id=123.45, team_id=123.45
    )
    try:
        pydantic.TypeAdapter(models.DeleteTeamEventTypeOutput).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"
