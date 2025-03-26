
### delete <a name="delete"></a>
Delete an organization within an organization

Requires the user to have at least the 'ORG_ADMIN' role within the organization. Additionally, for platform, the plan must be 'SCALE' or higher to access this endpoint.

**API Endpoint**: `DELETE /v2/organizations/{orgId}/organizations/{managedOrganizationId}`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.organizations.delete(managed_organization_id=123.45, org_id=123.45)
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.organizations.delete(managed_organization_id=123.45, org_id=123.45)
```

### list <a name="list"></a>
Get all organizations within an organization

Requires the user to have at least the 'ORG_ADMIN' role within the organization. Additionally, for platform, the plan must be 'SCALE' or higher to access this endpoint.

**API Endpoint**: `GET /v2/organizations/{orgId}/organizations`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.organizations.list(org_id=123.45)
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.organizations.list(org_id=123.45)
```

### get <a name="get"></a>
Get an organization within an organization

Requires the user to have at least the 'ORG_ADMIN' role within the organization. Additionally, for platform, the plan must be 'SCALE' or higher to access this endpoint.

**API Endpoint**: `GET /v2/organizations/{orgId}/organizations/{managedOrganizationId}`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.organizations.get(managed_organization_id=123.45, org_id=123.45)
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.organizations.get(managed_organization_id=123.45, org_id=123.45)
```

### patch <a name="patch"></a>
Update an organization within an organization

Requires the user to have at least the 'ORG_ADMIN' role within the organization. Additionally, for platform, the plan must be 'SCALE' or higher to access this endpoint.

**API Endpoint**: `PATCH /v2/organizations/{orgId}/organizations/{managedOrganizationId}`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.organizations.patch(
    managed_organization_id=123.45,
    org_id=123.45,
    metadata={"key": "value"},
    name="CalTeam",
)
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.organizations.patch(
    managed_organization_id=123.45,
    org_id=123.45,
    metadata={"key": "value"},
    name="CalTeam",
)
```

### create <a name="create"></a>
Create an organization within an organization

Requires the user to have at least the 'ORG_ADMIN' role within the organization. Additionally, for platform, the plan must be 'SCALE' or higher to access this endpoint.

**API Endpoint**: `POST /v2/organizations/{orgId}/organizations`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.organizations.create(
    name="CalTeam",
    org_id=123.45,
    api_key_days_valid=60.0,
    api_key_never_expires=True,
    metadata={"key": "value"},
)
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.organizations.create(
    name="CalTeam",
    org_id=123.45,
    api_key_days_valid=60.0,
    api_key_never_expires=True,
    metadata={"key": "value"},
)
```
