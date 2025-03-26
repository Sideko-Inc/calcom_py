import pydantic
import pytest

from calcom_py import AsyncClient, Client
from calcom_py.environment import Environment
from calcom_py.types import models


def test_create_201_success_default():
    """Tests a POST request to the /v2/schedules endpoint.

    Operation: create
    Test Case ID: success_default
    Expected Status: 201
    Mode: Synchronous execution

    Response : models.CreateScheduleOutput20240611

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(api_key="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.schedules.create(
        cal_api_version="string",
        is_default=True,
        name="Catch up hours",
        time_zone="Europe/Rome",
        availability=[
            {"days": ["Monday", "Tuesday"], "end_time": "19:00", "start_time": "17:00"},
            {
                "days": ["Wednesday", "Thursday"],
                "end_time": "20:00",
                "start_time": "16:00",
            },
        ],
        overrides=[{"date": "2024-05-20", "end_time": "21:00", "start_time": "18:00"}],
    )
    try:
        pydantic.TypeAdapter(models.CreateScheduleOutput20240611).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_create_201_success_default():
    """Tests a POST request to the /v2/schedules endpoint.

    Operation: create
    Test Case ID: success_default
    Expected Status: 201
    Mode: Asynchronous execution

    Response : models.CreateScheduleOutput20240611

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(api_key="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.schedules.create(
        cal_api_version="string",
        is_default=True,
        name="Catch up hours",
        time_zone="Europe/Rome",
        availability=[
            {"days": ["Monday", "Tuesday"], "end_time": "19:00", "start_time": "17:00"},
            {
                "days": ["Wednesday", "Thursday"],
                "end_time": "20:00",
                "start_time": "16:00",
            },
        ],
        overrides=[{"date": "2024-05-20", "end_time": "21:00", "start_time": "18:00"}],
    )
    try:
        pydantic.TypeAdapter(models.CreateScheduleOutput20240611).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_patch_200_success_default():
    """Tests a PATCH request to the /v2/schedules/{scheduleId} endpoint.

    Operation: patch
    Test Case ID: success_default
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.UpdateScheduleOutput20240611

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(api_key="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.schedules.patch(
        cal_api_version="string",
        schedule_id="string",
        availability=[
            {"days": ["Monday", "Tuesday"], "end_time": "10:00", "start_time": "09:00"}
        ],
        is_default=True,
        name="One-on-one coaching",
        overrides=[{"date": "2024-05-20", "end_time": "14:00", "start_time": "12:00"}],
        time_zone="Europe/Rome",
    )
    try:
        pydantic.TypeAdapter(models.UpdateScheduleOutput20240611).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_patch_200_success_default():
    """Tests a PATCH request to the /v2/schedules/{scheduleId} endpoint.

    Operation: patch
    Test Case ID: success_default
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.UpdateScheduleOutput20240611

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(api_key="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.schedules.patch(
        cal_api_version="string",
        schedule_id="string",
        availability=[
            {"days": ["Monday", "Tuesday"], "end_time": "10:00", "start_time": "09:00"}
        ],
        is_default=True,
        name="One-on-one coaching",
        overrides=[{"date": "2024-05-20", "end_time": "14:00", "start_time": "12:00"}],
        time_zone="Europe/Rome",
    )
    try:
        pydantic.TypeAdapter(models.UpdateScheduleOutput20240611).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_get_200_generated_success():
    """Tests a GET request to the /v2/schedules/{scheduleId} endpoint.

    Operation: get
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.GetScheduleOutput20240611

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(api_key="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.schedules.get(cal_api_version="string", schedule_id=123.45)
    try:
        pydantic.TypeAdapter(models.GetScheduleOutput20240611).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_get_200_generated_success():
    """Tests a GET request to the /v2/schedules/{scheduleId} endpoint.

    Operation: get
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.GetScheduleOutput20240611

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(api_key="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.schedules.get(cal_api_version="string", schedule_id=123.45)
    try:
        pydantic.TypeAdapter(models.GetScheduleOutput20240611).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_list_200_generated_success():
    """Tests a GET request to the /v2/schedules endpoint.

    Operation: list
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.GetSchedulesOutput20240611

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(api_key="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.schedules.list(cal_api_version="string")
    try:
        pydantic.TypeAdapter(models.GetSchedulesOutput20240611).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_list_200_generated_success():
    """Tests a GET request to the /v2/schedules endpoint.

    Operation: list
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.GetSchedulesOutput20240611

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(api_key="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.schedules.list(cal_api_version="string")
    try:
        pydantic.TypeAdapter(models.GetSchedulesOutput20240611).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_delete_200_generated_success():
    """Tests a DELETE request to the /v2/schedules/{scheduleId} endpoint.

    Operation: delete
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.DeleteScheduleOutput20240611

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(api_key="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.schedules.delete(cal_api_version="string", schedule_id=123.45)
    try:
        pydantic.TypeAdapter(models.DeleteScheduleOutput20240611).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_delete_200_generated_success():
    """Tests a DELETE request to the /v2/schedules/{scheduleId} endpoint.

    Operation: delete
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.DeleteScheduleOutput20240611

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(api_key="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.schedules.delete(
        cal_api_version="string", schedule_id=123.45
    )
    try:
        pydantic.TypeAdapter(models.DeleteScheduleOutput20240611).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"
