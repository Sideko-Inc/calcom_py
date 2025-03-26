import pydantic
import pytest

from calcom_py import AsyncClient, Client
from calcom_py.environment import Environment
from calcom_py.types import models


def test_reschedule_201_success_default():
    """Tests a POST request to the /v2/bookings/{bookingUid}/reschedule endpoint.

    Operation: reschedule
    Test Case ID: success_default
    Expected Status: 201
    Mode: Synchronous execution

    Response : models.RescheduleBookingOutput20240813

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(api_key="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.bookings.reschedule(
        booking_uid="string",
        cal_api_version="string",
        data={"start": "2024-08-13T10:00:00Z"},
    )
    try:
        pydantic.TypeAdapter(models.RescheduleBookingOutput20240813).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_reschedule_201_success_default():
    """Tests a POST request to the /v2/bookings/{bookingUid}/reschedule endpoint.

    Operation: reschedule
    Test Case ID: success_default
    Expected Status: 201
    Mode: Asynchronous execution

    Response : models.RescheduleBookingOutput20240813

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(api_key="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.bookings.reschedule(
        booking_uid="string",
        cal_api_version="string",
        data={"start": "2024-08-13T10:00:00Z"},
    )
    try:
        pydantic.TypeAdapter(models.RescheduleBookingOutput20240813).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_reassign_to_user_200_success_default():
    """Tests a POST request to the /v2/bookings/{bookingUid}/reassign/{userId} endpoint.

    Operation: reassign_to_user
    Test Case ID: success_default
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.ReassignBookingOutput20240813

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(api_key="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.bookings.reassign_to_user(
        booking_uid="string",
        cal_api_version="string",
        user_id=123.45,
        reason="Host has to take another call",
    )
    try:
        pydantic.TypeAdapter(models.ReassignBookingOutput20240813).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_reassign_to_user_200_success_default():
    """Tests a POST request to the /v2/bookings/{bookingUid}/reassign/{userId} endpoint.

    Operation: reassign_to_user
    Test Case ID: success_default
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.ReassignBookingOutput20240813

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(api_key="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.bookings.reassign_to_user(
        booking_uid="string",
        cal_api_version="string",
        user_id=123.45,
        reason="Host has to take another call",
    )
    try:
        pydantic.TypeAdapter(models.ReassignBookingOutput20240813).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_reassign_200_generated_success():
    """Tests a POST request to the /v2/bookings/{bookingUid}/reassign endpoint.

    Operation: reassign
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.ReassignBookingOutput20240813

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(api_key="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.bookings.reassign(booking_uid="string", cal_api_version="string")
    try:
        pydantic.TypeAdapter(models.ReassignBookingOutput20240813).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_reassign_200_generated_success():
    """Tests a POST request to the /v2/bookings/{bookingUid}/reassign endpoint.

    Operation: reassign
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.ReassignBookingOutput20240813

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(api_key="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.bookings.reassign(
        booking_uid="string", cal_api_version="string"
    )
    try:
        pydantic.TypeAdapter(models.ReassignBookingOutput20240813).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_mark_absent_200_success_default():
    """Tests a POST request to the /v2/bookings/{bookingUid}/mark-absent endpoint.

    Operation: mark_absent
    Test Case ID: success_default
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.MarkAbsentBookingOutput20240813

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(api_key="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.bookings.mark_absent(
        booking_uid="string", cal_api_version="string", host=False
    )
    try:
        pydantic.TypeAdapter(models.MarkAbsentBookingOutput20240813).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_mark_absent_200_success_default():
    """Tests a POST request to the /v2/bookings/{bookingUid}/mark-absent endpoint.

    Operation: mark_absent
    Test Case ID: success_default
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.MarkAbsentBookingOutput20240813

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(api_key="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.bookings.mark_absent(
        booking_uid="string", cal_api_version="string", host=False
    )
    try:
        pydantic.TypeAdapter(models.MarkAbsentBookingOutput20240813).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_decline_200_success_default():
    """Tests a POST request to the /v2/bookings/{bookingUid}/decline endpoint.

    Operation: decline
    Test Case ID: success_default
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.GetBookingOutput20240813

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(api_key="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.bookings.decline(
        booking_uid="string",
        cal_api_version="string",
        reason="Host has to take another call",
    )
    try:
        pydantic.TypeAdapter(models.GetBookingOutput20240813).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_decline_200_success_default():
    """Tests a POST request to the /v2/bookings/{bookingUid}/decline endpoint.

    Operation: decline
    Test Case ID: success_default
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.GetBookingOutput20240813

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(api_key="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.bookings.decline(
        booking_uid="string",
        cal_api_version="string",
        reason="Host has to take another call",
    )
    try:
        pydantic.TypeAdapter(models.GetBookingOutput20240813).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_confirm_200_generated_success():
    """Tests a POST request to the /v2/bookings/{bookingUid}/confirm endpoint.

    Operation: confirm
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.GetBookingOutput20240813

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(api_key="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.bookings.confirm(booking_uid="string", cal_api_version="string")
    try:
        pydantic.TypeAdapter(models.GetBookingOutput20240813).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_confirm_200_generated_success():
    """Tests a POST request to the /v2/bookings/{bookingUid}/confirm endpoint.

    Operation: confirm
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.GetBookingOutput20240813

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(api_key="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.bookings.confirm(
        booking_uid="string", cal_api_version="string"
    )
    try:
        pydantic.TypeAdapter(models.GetBookingOutput20240813).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_cancel_200_success_default():
    """Tests a POST request to the /v2/bookings/{bookingUid}/cancel endpoint.

    Operation: cancel
    Test Case ID: success_default
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.CancelBookingOutput20240813

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(api_key="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.bookings.cancel(
        booking_uid="string", cal_api_version="string", data={}
    )
    try:
        pydantic.TypeAdapter(models.CancelBookingOutput20240813).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_cancel_200_success_default():
    """Tests a POST request to the /v2/bookings/{bookingUid}/cancel endpoint.

    Operation: cancel
    Test Case ID: success_default
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.CancelBookingOutput20240813

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(api_key="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.bookings.cancel(
        booking_uid="string", cal_api_version="string", data={}
    )
    try:
        pydantic.TypeAdapter(models.CancelBookingOutput20240813).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_create_201_success_default():
    """Tests a POST request to the /v2/bookings endpoint.

    Operation: create
    Test Case ID: success_default
    Expected Status: 201
    Mode: Synchronous execution

    Response : models.CreateBookingOutput20240813

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(api_key="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.bookings.create(
        cal_api_version="string",
        data={
            "attendee": {"name": "John Doe", "time_zone": "America/New_York"},
            "event_type_id": 123.0,
            "start": "2024-08-13T09:00:00Z",
        },
    )
    try:
        pydantic.TypeAdapter(models.CreateBookingOutput20240813).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_create_201_success_default():
    """Tests a POST request to the /v2/bookings endpoint.

    Operation: create
    Test Case ID: success_default
    Expected Status: 201
    Mode: Asynchronous execution

    Response : models.CreateBookingOutput20240813

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(api_key="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.bookings.create(
        cal_api_version="string",
        data={
            "attendee": {"name": "John Doe", "time_zone": "America/New_York"},
            "event_type_id": 123.0,
            "start": "2024-08-13T09:00:00Z",
        },
    )
    try:
        pydantic.TypeAdapter(models.CreateBookingOutput20240813).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_get_200_generated_success():
    """Tests a GET request to the /v2/bookings/{bookingUid} endpoint.

    Operation: get
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.GetBookingOutput20240813

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(api_key="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.bookings.get(booking_uid="string", cal_api_version="string")
    try:
        pydantic.TypeAdapter(models.GetBookingOutput20240813).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_get_200_generated_success():
    """Tests a GET request to the /v2/bookings/{bookingUid} endpoint.

    Operation: get
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.GetBookingOutput20240813

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(api_key="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.bookings.get(booking_uid="string", cal_api_version="string")
    try:
        pydantic.TypeAdapter(models.GetBookingOutput20240813).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_list_200_generated_success():
    """Tests a GET request to the /v2/bookings endpoint.

    Operation: list
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.GetBookingsOutput20240813

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(api_key="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.bookings.list(cal_api_version="string")
    try:
        pydantic.TypeAdapter(models.GetBookingsOutput20240813).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_list_200_generated_success():
    """Tests a GET request to the /v2/bookings endpoint.

    Operation: list
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.GetBookingsOutput20240813

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(api_key="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.bookings.list(cal_api_version="string")
    try:
        pydantic.TypeAdapter(models.GetBookingsOutput20240813).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"
