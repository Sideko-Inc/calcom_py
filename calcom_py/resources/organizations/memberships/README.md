
### delete <a name="delete"></a>
Delete a membership



**API Endpoint**: `DELETE /v2/organizations/{orgId}/memberships/{membershipId}`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.organizations.memberships.delete(membership_id=123.45, org_id=123.45)
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.organizations.memberships.delete(membership_id=123.45, org_id=123.45)
```

### list <a name="list"></a>
Get all memberships



**API Endpoint**: `GET /v2/organizations/{orgId}/memberships`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.organizations.memberships.list(org_id=123.45)
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.organizations.memberships.list(org_id=123.45)
```

### get <a name="get"></a>
Get a membership



**API Endpoint**: `GET /v2/organizations/{orgId}/memberships/{membershipId}`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.organizations.memberships.get(membership_id=123.45, org_id=123.45)
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.organizations.memberships.get(membership_id=123.45, org_id=123.45)
```

### patch <a name="patch"></a>
Update a membership



**API Endpoint**: `PATCH /v2/organizations/{orgId}/memberships/{membershipId}`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.organizations.memberships.patch(membership_id=123.45, org_id=123.45)
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.organizations.memberships.patch(membership_id=123.45, org_id=123.45)
```

### create <a name="create"></a>
Create a membership



**API Endpoint**: `POST /v2/organizations/{orgId}/memberships`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.organizations.memberships.create(
    org_id=123.45, role="ADMIN", user_id=123.45
)
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.organizations.memberships.create(
    org_id=123.45, role="ADMIN", user_id=123.45
)
```
