
### list <a name="list"></a>
Get all calendars



**API Endpoint**: `GET /v2/calendars`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.calendars.list()
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.calendars.list()
```

### get_busy <a name="get_busy"></a>
Get busy times

Get busy times from a calendar. Example request URL is `https://api.cal.com/v2/calendars/busy-times?loggedInUsersTz=Europe%2FMadrid&dateFrom=2024-12-18&dateTo=2024-12-18&calendarsToLoad[0][credentialId]=135&calendarsToLoad[0][externalId]=skrauciz%40gmail.com`

**API Endpoint**: `GET /v2/calendars/busy-times`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.calendars.get_busy(
    credential_id=123.45, external_id="string", logged_in_users_tz="string"
)
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.calendars.get_busy(
    credential_id=123.45, external_id="string", logged_in_users_tz="string"
)
```

### check <a name="check"></a>
Check a calendar connection



**API Endpoint**: `GET /v2/calendars/{calendar}/check`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.calendars.check(calendar_field="apple")
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.calendars.check(calendar_field="apple")
```

### connect <a name="connect"></a>
Get oAuth connect URL



**API Endpoint**: `GET /v2/calendars/{calendar}/connect`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.calendars.connect(calendar_field="google")
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.calendars.connect(calendar_field="google")
```

### save <a name="save"></a>
Save an oAuth calendar credentials



**API Endpoint**: `GET /v2/calendars/{calendar}/save`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.calendars.save(
    calendar_field="google", code_field="string", state="string"
)
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.calendars.save(
    calendar_field="google", code_field="string", state="string"
)
```

### disconnect <a name="disconnect"></a>
Disconnect a calendar



**API Endpoint**: `POST /v2/calendars/{calendar}/disconnect`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.calendars.disconnect(calendar_field="apple", id=10)
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.calendars.disconnect(calendar_field="apple", id=10)
```
