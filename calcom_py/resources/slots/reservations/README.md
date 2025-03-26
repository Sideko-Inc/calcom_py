
### delete <a name="delete"></a>
DELETE /v2/slots/reservations/{uid}



**API Endpoint**: `DELETE /v2/slots/reservations/{uid}`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.slots.reservations.delete(cal_api_version="string", uid="string")
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.slots.reservations.delete(cal_api_version="string", uid="string")
```

### get <a name="get"></a>
Get reserved slot



**API Endpoint**: `GET /v2/slots/reservations/{uid}`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.slots.reservations.get(cal_api_version="string", uid="string")
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.slots.reservations.get(cal_api_version="string", uid="string")
```

### patch <a name="patch"></a>
Updated reserved a slot



**API Endpoint**: `PATCH /v2/slots/reservations/{uid}`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.slots.reservations.patch(
    cal_api_version="string",
    event_type_id=1.0,
    slot_start="2024-09-04T09:00:00Z",
    uid="string",
    reservation_duration=5.0,
    slot_duration=123.45,
)
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.slots.reservations.patch(
    cal_api_version="string",
    event_type_id=1.0,
    slot_start="2024-09-04T09:00:00Z",
    uid="string",
    reservation_duration=5.0,
    slot_duration=123.45,
)
```

### create <a name="create"></a>
Reserve a slot

Make a slot not available for others to book for a certain period of time.

**API Endpoint**: `POST /v2/slots/reservations`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.slots.reservations.create(
    cal_api_version="string",
    event_type_id=1.0,
    slot_start="2024-09-04T09:00:00Z",
    reservation_duration=5.0,
    slot_duration=123.45,
)
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.slots.reservations.create(
    cal_api_version="string",
    event_type_id=1.0,
    slot_start="2024-09-04T09:00:00Z",
    reservation_duration=5.0,
    slot_duration=123.45,
)
```
