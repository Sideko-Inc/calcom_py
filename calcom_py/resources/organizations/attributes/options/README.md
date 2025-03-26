
### delete_from_user <a name="delete_from_user"></a>
Unassign an attribute from a user



**API Endpoint**: `DELETE /v2/organizations/{orgId}/attributes/options/{userId}/{attributeOptionId}`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.organizations.attributes.options.delete_from_user(
    attribute_option_id="string", org_id=123.45, user_id=123.45
)
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.organizations.attributes.options.delete_from_user(
    attribute_option_id="string", org_id=123.45, user_id=123.45
)
```

### delete <a name="delete"></a>
Delete an attribute option



**API Endpoint**: `DELETE /v2/organizations/{orgId}/attributes/{attributeId}/options/{optionId}`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.organizations.attributes.options.delete(
    attribute_id="string", option_id="string", org_id=123.45
)
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.organizations.attributes.options.delete(
    attribute_id="string", option_id="string", org_id=123.45
)
```

### get <a name="get"></a>
Get all attribute options for a user



**API Endpoint**: `GET /v2/organizations/{orgId}/attributes/options/{userId}`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.organizations.attributes.options.get(org_id=123.45, user_id=123.45)
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.organizations.attributes.options.get(org_id=123.45, user_id=123.45)
```

### list <a name="list"></a>
Get all attribute options



**API Endpoint**: `GET /v2/organizations/{orgId}/attributes/{attributeId}/options`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.organizations.attributes.options.list(attribute_id="string", org_id=123.45)
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.organizations.attributes.options.list(
    attribute_id="string", org_id=123.45
)
```

### patch <a name="patch"></a>
Update an attribute option



**API Endpoint**: `PATCH /v2/organizations/{orgId}/attributes/{attributeId}/options/{optionId}`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.organizations.attributes.options.patch(
    attribute_id="string", option_id="string", org_id=123.45
)
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.organizations.attributes.options.patch(
    attribute_id="string", option_id="string", org_id=123.45
)
```

### create_to_user <a name="create_to_user"></a>
Assign an attribute to a user



**API Endpoint**: `POST /v2/organizations/{orgId}/attributes/options/{userId}`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.organizations.attributes.options.create_to_user(
    attribute_id="string", org_id=123.45, user_id=123.45
)
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.organizations.attributes.options.create_to_user(
    attribute_id="string", org_id=123.45, user_id=123.45
)
```

### create <a name="create"></a>
Create an attribute option



**API Endpoint**: `POST /v2/organizations/{orgId}/attributes/{attributeId}/options`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.organizations.attributes.options.create(
    attribute_id="string", org_id=123.45, slug="string", value="string"
)
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.organizations.attributes.options.create(
    attribute_id="string", org_id=123.45, slug="string", value="string"
)
```
