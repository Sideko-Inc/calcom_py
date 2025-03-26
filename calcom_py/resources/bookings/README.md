
### list <a name="list"></a>
Get all bookings



**API Endpoint**: `GET /v2/bookings`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.bookings.list(cal_api_version="string")
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.bookings.list(cal_api_version="string")
```

### get <a name="get"></a>
Get a booking

`:bookingUid` can be

      1. uid of a normal booking

      2. uid of one of the recurring booking recurrences

      3. uid of recurring booking which will return an array of all recurring booking recurrences (stored as recurringBookingUid on one of the individual recurrences).

**API Endpoint**: `GET /v2/bookings/{bookingUid}`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.bookings.get(booking_uid="string", cal_api_version="string")
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.bookings.get(booking_uid="string", cal_api_version="string")
```

### create <a name="create"></a>
Create a booking


      POST /v2/bookings is used to create regular bookings, recurring bookings and instant bookings. The request bodies for all 3 are almost the same except:
      If eventTypeId in the request body is id of a regular event, then regular booking is created.

      If it is an id of a recurring event type, then recurring booking is created.

      Meaning that the request bodies are equal but the outcome depends on what kind of event type it is with the goal of making it as seamless for developers as possible.

      For team event types it is possible to create instant meeting. To do that just pass `"instant": true` to the request body.

      The start needs to be in UTC aka if the timezone is GMT+2 in Rome and meeting should start at 11, then UTC time should have hours 09:00 aka without time zone.
      

**API Endpoint**: `POST /v2/bookings`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.bookings.create(
    cal_api_version="string",
    data={
        "attendee": {"name": "John Doe", "time_zone": "America/New_York"},
        "event_type_id": 123.0,
        "start": "2024-08-13T09:00:00Z",
    },
)
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.bookings.create(
    cal_api_version="string",
    data={
        "attendee": {"name": "John Doe", "time_zone": "America/New_York"},
        "event_type_id": 123.0,
        "start": "2024-08-13T09:00:00Z",
    },
)
```

### cancel <a name="cancel"></a>
Cancel a booking

:bookingUid can be :bookingUid of an usual booking, individual recurrence or recurring booking to cancel all recurrences.
    For seated bookings to cancel one individual booking provide :bookingUid and :seatUid in the request body. For recurring seated bookings it is not possible to cancel all of them with 1 call
    like with non-seated recurring bookings by providing recurring bookind uid - you have to cancel each recurrence booking by its bookingUid + seatUid.

**API Endpoint**: `POST /v2/bookings/{bookingUid}/cancel`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.bookings.cancel(booking_uid="string", cal_api_version="string", data={})
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.bookings.cancel(
    booking_uid="string", cal_api_version="string", data={}
)
```

### confirm <a name="confirm"></a>
Confirm booking that requires a confirmation



**API Endpoint**: `POST /v2/bookings/{bookingUid}/confirm`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.bookings.confirm(booking_uid="string", cal_api_version="string")
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.bookings.confirm(booking_uid="string", cal_api_version="string")
```

### decline <a name="decline"></a>
Decline booking that requires a confirmation



**API Endpoint**: `POST /v2/bookings/{bookingUid}/decline`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.bookings.decline(
    booking_uid="string",
    cal_api_version="string",
    reason="Host has to take another call",
)
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.bookings.decline(
    booking_uid="string",
    cal_api_version="string",
    reason="Host has to take another call",
)
```

### mark_absent <a name="mark_absent"></a>
Mark a booking absence



**API Endpoint**: `POST /v2/bookings/{bookingUid}/mark-absent`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.bookings.mark_absent(
    booking_uid="string", cal_api_version="string", host=False
)
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.bookings.mark_absent(
    booking_uid="string", cal_api_version="string", host=False
)
```

### reassign <a name="reassign"></a>
Automatically reassign booking to a new host



**API Endpoint**: `POST /v2/bookings/{bookingUid}/reassign`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.bookings.reassign(booking_uid="string", cal_api_version="string")
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.bookings.reassign(booking_uid="string", cal_api_version="string")
```

### reassign_to_user <a name="reassign_to_user"></a>
Reassign a booking to a specific user



**API Endpoint**: `POST /v2/bookings/{bookingUid}/reassign/{userId}`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.bookings.reassign_to_user(
    booking_uid="string",
    cal_api_version="string",
    user_id=123.45,
    reason="Host has to take another call",
)
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.bookings.reassign_to_user(
    booking_uid="string",
    cal_api_version="string",
    user_id=123.45,
    reason="Host has to take another call",
)
```

### reschedule <a name="reschedule"></a>
Reschedule a booking

Reschedule a booking or seated booking

**API Endpoint**: `POST /v2/bookings/{bookingUid}/reschedule`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.bookings.reschedule(
    booking_uid="string",
    cal_api_version="string",
    data={"start": "2024-08-13T10:00:00Z"},
)
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.bookings.reschedule(
    booking_uid="string",
    cal_api_version="string",
    data={"start": "2024-08-13T10:00:00Z"},
)
```
