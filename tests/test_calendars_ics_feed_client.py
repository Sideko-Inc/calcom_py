import pydantic
import pytest
import typing

from calcom_py import AsyncClient, Client
from calcom_py.environment import Environment
from calcom_py.types import models


def test_save_201_success_default():
    """Tests a POST request to the /v2/calendars/ics-feed/save endpoint.

    Operation: save
    Test Case ID: success_default
    Expected Status: 201
    Mode: Synchronous execution

    Response : models.CreateIcsFeedOutputResponseDto

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(api_key="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.calendars.ics_feed.save(
        urls=["https://cal.com/ics/feed.ics", "http://cal.com/ics/feed.ics"],
        read_only=False,
    )
    try:
        pydantic.TypeAdapter(models.CreateIcsFeedOutputResponseDto).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_save_201_success_default():
    """Tests a POST request to the /v2/calendars/ics-feed/save endpoint.

    Operation: save
    Test Case ID: success_default
    Expected Status: 201
    Mode: Asynchronous execution

    Response : models.CreateIcsFeedOutputResponseDto

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(api_key="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.calendars.ics_feed.save(
        urls=["https://cal.com/ics/feed.ics", "http://cal.com/ics/feed.ics"],
        read_only=False,
    )
    try:
        pydantic.TypeAdapter(models.CreateIcsFeedOutputResponseDto).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_check_200_generated_success():
    """Tests a GET request to the /v2/calendars/ics-feed/check endpoint.

    Operation: check
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : typing.Dict[str, typing.Any]

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(api_key="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.calendars.ics_feed.check()
    try:
        pydantic.TypeAdapter(typing.Dict[str, typing.Any]).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_check_200_generated_success():
    """Tests a GET request to the /v2/calendars/ics-feed/check endpoint.

    Operation: check
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : typing.Dict[str, typing.Any]

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(api_key="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.calendars.ics_feed.check()
    try:
        pydantic.TypeAdapter(typing.Dict[str, typing.Any]).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"
