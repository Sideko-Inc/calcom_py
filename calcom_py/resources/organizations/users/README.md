
### delete <a name="delete"></a>
Delete a user



**API Endpoint**: `DELETE /v2/organizations/{orgId}/users/{userId}`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.organizations.users.delete(org_id=123.45, user_id=123.45)
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.organizations.users.delete(org_id=123.45, user_id=123.45)
```

### list <a name="list"></a>
Get all users



**API Endpoint**: `GET /v2/organizations/{orgId}/users`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.organizations.users.list(org_id=123.45)
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.organizations.users.list(org_id=123.45)
```

### patch <a name="patch"></a>
Update a user



**API Endpoint**: `PATCH /v2/organizations/{orgId}/users/{userId}`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.organizations.users.patch(data={}, org_id=123.45, user_id=123.45)
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.organizations.users.patch(data={}, org_id=123.45, user_id=123.45)
```

### create <a name="create"></a>
Create a user



**API Endpoint**: `POST /v2/organizations/{orgId}/users`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.organizations.users.create(
    email_field="user@example.com",
    org_id=123.45,
    app_theme="light",
    avatar_url="https://example.com/avatar.jpg",
    brand_color="#FFFFFF",
    dark_brand_color="#000000",
    default_schedule_id=1.0,
    hide_branding=False,
    locale_field="en",
    theme="dark",
    time_format=24.0,
    time_zone="America/New_York",
    username="user123",
    weekday="Monday",
)
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.organizations.users.create(
    email_field="user@example.com",
    org_id=123.45,
    app_theme="light",
    avatar_url="https://example.com/avatar.jpg",
    brand_color="#FFFFFF",
    dark_brand_color="#000000",
    default_schedule_id=1.0,
    hide_branding=False,
    locale_field="en",
    theme="dark",
    time_format=24.0,
    time_zone="America/New_York",
    username="user123",
    weekday="Monday",
)
```
