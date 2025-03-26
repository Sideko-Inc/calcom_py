
### redirect <a name="redirect"></a>
Get stripe connect URL



**API Endpoint**: `GET /v2/stripe/connect`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.stripe.connect.redirect()
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.stripe.connect.redirect()
```
