
### delete <a name="delete"></a>
Delete a schedule



**API Endpoint**: `DELETE /v2/schedules/{scheduleId}`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.schedules.delete(cal_api_version="string", schedule_id=123.45)
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.schedules.delete(cal_api_version="string", schedule_id=123.45)
```

### list <a name="list"></a>
Get all schedules

Get all schedules of the authenticated user.

**API Endpoint**: `GET /v2/schedules`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.schedules.list(cal_api_version="string")
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.schedules.list(cal_api_version="string")
```

### get <a name="get"></a>
Get a schedule



**API Endpoint**: `GET /v2/schedules/{scheduleId}`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.schedules.get(cal_api_version="string", schedule_id=123.45)
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.schedules.get(cal_api_version="string", schedule_id=123.45)
```

### patch <a name="patch"></a>
Update a schedule



**API Endpoint**: `PATCH /v2/schedules/{scheduleId}`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.schedules.patch(
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
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.schedules.patch(
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
```

### create <a name="create"></a>
Create a schedule


      Create a schedule for the authenticated user.

      The point of creating schedules is for event types to be available at specific times.

      The first goal of schedules is to have a default schedule. If you are platform customer and created managed users, then it is important to note that each managed user should have a default schedule.
      1. If you passed `timeZone` when creating managed user, then the default schedule from Monday to Friday from 9AM to 5PM will be created with that timezone. The managed user can then change the default schedule via the `AvailabilitySettings` atom.
      2. If you did not, then we assume you want the user to have this specific schedule right away. You should create a default schedule by specifying
      `"isDefault": true` in the request body. Until the user has a default schedule the user can't be booked nor manage their schedule via the AvailabilitySettings atom.

      The second goal of schedules is to create another schedule that event types can point to. This is useful for when an event is booked because availability is not checked against the default schedule but instead against that specific schedule.
      After creating a non-default schedule, you can update an event type to point to that schedule via the PATCH `event-types/{eventTypeId}` endpoint.

      When specifying start time and end time for each day use the 24 hour format e.g. 08:00, 15:00 etc.
      

**API Endpoint**: `POST /v2/schedules`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.schedules.create(
    cal_api_version="string",
    is_default=True,
    name="Catch up hours",
    time_zone="Europe/Rome",
    availability=[
        {"days": ["Monday", "Tuesday"], "end_time": "19:00", "start_time": "17:00"},
        {"days": ["Wednesday", "Thursday"], "end_time": "20:00", "start_time": "16:00"},
    ],
    overrides=[{"date": "2024-05-20", "end_time": "21:00", "start_time": "18:00"}],
)
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.schedules.create(
    cal_api_version="string",
    is_default=True,
    name="Catch up hours",
    time_zone="Europe/Rome",
    availability=[
        {"days": ["Monday", "Tuesday"], "end_time": "19:00", "start_time": "17:00"},
        {"days": ["Wednesday", "Thursday"], "end_time": "20:00", "start_time": "16:00"},
    ],
    overrides=[{"date": "2024-05-20", "end_time": "21:00", "start_time": "18:00"}],
)
```
