
### delete <a name="delete"></a>
Delete a schedule



**API Endpoint**: `DELETE /v2/organizations/{orgId}/users/{userId}/schedules/{scheduleId}`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.organizations.users.schedules.delete(
    org_id=123.45, schedule_id=123.45, user_id=123.45
)
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.organizations.users.schedules.delete(
    org_id=123.45, schedule_id=123.45, user_id=123.45
)
```

### list <a name="list"></a>
Get all schedules



**API Endpoint**: `GET /v2/organizations/{orgId}/users/{userId}/schedules`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.organizations.users.schedules.list(org_id=123.45, user_id=123.45)
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.organizations.users.schedules.list(org_id=123.45, user_id=123.45)
```

### get <a name="get"></a>
Get a schedule



**API Endpoint**: `GET /v2/organizations/{orgId}/users/{userId}/schedules/{scheduleId}`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.organizations.users.schedules.get(
    org_id=123.45, schedule_id=123.45, user_id=123.45
)
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.organizations.users.schedules.get(
    org_id=123.45, schedule_id=123.45, user_id=123.45
)
```

### patch <a name="patch"></a>
Update a schedule



**API Endpoint**: `PATCH /v2/organizations/{orgId}/users/{userId}/schedules/{scheduleId}`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.organizations.users.schedules.patch(
    org_id=123.45,
    schedule_id=123.45,
    user_id=123.45,
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
res = await client.organizations.users.schedules.patch(
    org_id=123.45,
    schedule_id=123.45,
    user_id=123.45,
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



**API Endpoint**: `POST /v2/organizations/{orgId}/users/{userId}/schedules`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.organizations.users.schedules.create(
    is_default=True,
    name="Catch up hours",
    org_id=123.45,
    time_zone="Europe/Rome",
    user_id=123.45,
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
res = await client.organizations.users.schedules.create(
    is_default=True,
    name="Catch up hours",
    org_id=123.45,
    time_zone="Europe/Rome",
    user_id=123.45,
    availability=[
        {"days": ["Monday", "Tuesday"], "end_time": "19:00", "start_time": "17:00"},
        {"days": ["Wednesday", "Thursday"], "end_time": "20:00", "start_time": "16:00"},
    ],
    overrides=[{"date": "2024-05-20", "end_time": "21:00", "start_time": "18:00"}],
)
```
