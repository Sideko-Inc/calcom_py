
### delete <a name="delete"></a>
Delete an attribute



**API Endpoint**: `DELETE /v2/organizations/{orgId}/attributes/{attributeId}`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.organizations.attributes.delete(attribute_id="string", org_id=123.45)
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.organizations.attributes.delete(attribute_id="string", org_id=123.45)
```

### list <a name="list"></a>
Get all attributes



**API Endpoint**: `GET /v2/organizations/{orgId}/attributes`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.organizations.attributes.list(org_id=123.45)
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.organizations.attributes.list(org_id=123.45)
```

### get <a name="get"></a>
Get an attribute



**API Endpoint**: `GET /v2/organizations/{orgId}/attributes/{attributeId}`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.organizations.attributes.get(attribute_id="string", org_id=123.45)
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.organizations.attributes.get(attribute_id="string", org_id=123.45)
```

### patch <a name="patch"></a>
Update an attribute



**API Endpoint**: `PATCH /v2/organizations/{orgId}/attributes/{attributeId}`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.organizations.attributes.patch(attribute_id="string", org_id=123.45)
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.organizations.attributes.patch(attribute_id="string", org_id=123.45)
```

### create <a name="create"></a>
Create an attribute



**API Endpoint**: `POST /v2/organizations/{orgId}/attributes`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.organizations.attributes.create(
    name="string",
    options=[{"slug": "string", "value": "string"}],
    org_id=123.45,
    slug="string",
    type_field="MULTI_SELECT",
)
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.organizations.attributes.create(
    name="string",
    options=[{"slug": "string", "value": "string"}],
    org_id=123.45,
    slug="string",
    type_field="MULTI_SELECT",
)
```
