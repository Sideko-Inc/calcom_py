
### check <a name="check"></a>
Check stripe connection



**API Endpoint**: `GET /v2/stripe/check`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.stripe.check.check()
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.stripe.check.check()
```

### get <a name="get"></a>
Check team stripe connection



**API Endpoint**: `GET /v2/stripe/check/{teamId}`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.stripe.check.get(team_id="string")
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.stripe.check.get(team_id="string")
```
