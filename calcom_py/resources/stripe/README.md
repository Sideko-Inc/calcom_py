
### save <a name="save"></a>
Save stripe credentials



**API Endpoint**: `GET /v2/stripe/save`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.stripe.save(code_field="string", state="string")
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.stripe.save(code_field="string", state="string")
```
