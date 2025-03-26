
### delete <a name="delete"></a>
Delete a team



**API Endpoint**: `DELETE /v2/organizations/{orgId}/teams/{teamId}`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.organizations.teams.delete(org_id=123.45, team_id=123.45)
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.organizations.teams.delete(org_id=123.45, team_id=123.45)
```

### list <a name="list"></a>
Get all teams



**API Endpoint**: `GET /v2/organizations/{orgId}/teams`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.organizations.teams.list(org_id=123.45)
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.organizations.teams.list(org_id=123.45)
```

### get <a name="get"></a>
Get a team



**API Endpoint**: `GET /v2/organizations/{orgId}/teams/{teamId}`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.organizations.teams.get(org_id=123.45, team_id=123.45)
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.organizations.teams.get(org_id=123.45, team_id=123.45)
```

### patch <a name="patch"></a>
Update a team



**API Endpoint**: `PATCH /v2/organizations/{orgId}/teams/{teamId}`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.organizations.teams.patch(
    org_id=123.45,
    team_id=123.45,
    banner_url="https://i.cal.com/api/avatar/949be534-7a88-4185-967c-c020b0c0bef3.png",
    logo_url="https://i.cal.com/api/avatar/b0b58752-68ad-4c0d-8024-4fa382a77752.png",
    metadata={"key": "value"},
    name="CalTeam",
    slug="caltel",
    time_zone="America/New_York",
    week_start="Monday",
)
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.organizations.teams.patch(
    org_id=123.45,
    team_id=123.45,
    banner_url="https://i.cal.com/api/avatar/949be534-7a88-4185-967c-c020b0c0bef3.png",
    logo_url="https://i.cal.com/api/avatar/b0b58752-68ad-4c0d-8024-4fa382a77752.png",
    metadata={"key": "value"},
    name="CalTeam",
    slug="caltel",
    time_zone="America/New_York",
    week_start="Monday",
)
```

### create <a name="create"></a>
Create a team



**API Endpoint**: `POST /v2/organizations/{orgId}/teams`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.organizations.teams.create(
    name="CalTeam",
    org_id=123.45,
    x_cal_client_id="string",
    banner_url="https://i.cal.com/api/avatar/949be534-7a88-4185-967c-c020b0c0bef3.png",
    logo_url="https://i.cal.com/api/avatar/b0b58752-68ad-4c0d-8024-4fa382a77752.png",
    metadata={"key": "value"},
    slug="caltel",
    time_zone="America/New_York",
    week_start="Monday",
)
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.organizations.teams.create(
    name="CalTeam",
    org_id=123.45,
    x_cal_client_id="string",
    banner_url="https://i.cal.com/api/avatar/949be534-7a88-4185-967c-c020b0c0bef3.png",
    logo_url="https://i.cal.com/api/avatar/b0b58752-68ad-4c0d-8024-4fa382a77752.png",
    metadata={"key": "value"},
    slug="caltel",
    time_zone="America/New_York",
    week_start="Monday",
)
```
