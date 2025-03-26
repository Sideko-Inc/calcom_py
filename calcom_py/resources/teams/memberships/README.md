
### delete <a name="delete"></a>
Delete a membership



**API Endpoint**: `DELETE /v2/teams/{teamId}/memberships/{membershipId}`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.teams.memberships.delete(membership_id=123.45, team_id=123.45)
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.teams.memberships.delete(membership_id=123.45, team_id=123.45)
```

### list <a name="list"></a>
Get all memberships



**API Endpoint**: `GET /v2/teams/{teamId}/memberships`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.teams.memberships.list(team_id=123.45)
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.teams.memberships.list(team_id=123.45)
```

### get <a name="get"></a>
Get a membership



**API Endpoint**: `GET /v2/teams/{teamId}/memberships/{membershipId}`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.teams.memberships.get(membership_id=123.45, team_id=123.45)
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.teams.memberships.get(membership_id=123.45, team_id=123.45)
```

### patch <a name="patch"></a>
Create a membership



**API Endpoint**: `PATCH /v2/teams/{teamId}/memberships/{membershipId}`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.teams.memberships.patch(membership_id=123.45, team_id=123.45)
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.teams.memberships.patch(membership_id=123.45, team_id=123.45)
```

### create <a name="create"></a>
Create a membership



**API Endpoint**: `POST /v2/teams/{teamId}/memberships`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.teams.memberships.create(team_id=123.45, user_id=123.45)
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.teams.memberships.create(team_id=123.45, user_id=123.45)
```
