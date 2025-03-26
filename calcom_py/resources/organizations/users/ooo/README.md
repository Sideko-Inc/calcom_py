
### delete <a name="delete"></a>
Delete ooo entry of a user



**API Endpoint**: `DELETE /v2/organizations/{orgId}/users/{userId}/ooo/{oooId}`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.organizations.users.ooo.delete(
    ooo_id=123.45, org_id=123.45, user_id=123.45
)
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.organizations.users.ooo.delete(
    ooo_id=123.45, org_id=123.45, user_id=123.45
)
```

### list <a name="list"></a>
Get all ooo entries of a user



**API Endpoint**: `GET /v2/organizations/{orgId}/users/{userId}/ooo`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.organizations.users.ooo.list(org_id=123.45, user_id=123.45)
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.organizations.users.ooo.list(org_id=123.45, user_id=123.45)
```

### patch <a name="patch"></a>
Update ooo entry of a user



**API Endpoint**: `PATCH /v2/organizations/{orgId}/users/{userId}/ooo/{oooId}`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.organizations.users.ooo.patch(
    ooo_id=123.45,
    org_id=123.45,
    user_id=123.45,
    end="2023-05-10T23:59:59.999Z",
    notes="Vacation in Hawaii",
    reason="vacation",
    start="2023-05-01T00:00:00.000Z",
    to_user_id=2.0,
)
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.organizations.users.ooo.patch(
    ooo_id=123.45,
    org_id=123.45,
    user_id=123.45,
    end="2023-05-10T23:59:59.999Z",
    notes="Vacation in Hawaii",
    reason="vacation",
    start="2023-05-01T00:00:00.000Z",
    to_user_id=2.0,
)
```

### create <a name="create"></a>
Create an ooo entry for user



**API Endpoint**: `POST /v2/organizations/{orgId}/users/{userId}/ooo`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.organizations.users.ooo.create(
    end="2023-05-10T23:59:59.999Z",
    org_id=123.45,
    start="2023-05-01T00:00:00.000Z",
    user_id=123.45,
    notes="Vacation in Hawaii",
    reason="vacation",
    to_user_id=2.0,
)
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.organizations.users.ooo.create(
    end="2023-05-10T23:59:59.999Z",
    org_id=123.45,
    start="2023-05-01T00:00:00.000Z",
    user_id=123.45,
    notes="Vacation in Hawaii",
    reason="vacation",
    to_user_id=2.0,
)
```
