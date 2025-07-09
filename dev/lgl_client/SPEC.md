# Little Green Light Python Client – Technical Specification  
_A modular, type-safe, test-driven DAO layer for internal web-app services._

---

## 1. Purpose & Scope  
Provide a reusable **sync** Python library that wraps the Little Green Light (LGL) REST API and hides networking, pagination, error handling, and JSON ↔︎ object mapping behind clean, resource-oriented interfaces.  
The client will live in **`src/lgl_client/lgl_api/`** and be imported by multiple services throughout the web app (acting like a Spring-style DAO layer).

---

## 2. Directory Layout  
```
dev/                           # design & docs
└── lgl_client/
    └── SPEC.md                # <-- this file

src/
└── lgl_client/
    └── lgl_api/
        __init__.py            # optional re-exports
        client.py              # base HTTP client
        exceptions.py
        models.py              # cross-resource data models & mix-ins
        <resource>.py          # one per API group (appeal_requests.py, constituents.py, …)

tests/
└── lgl_api/
    test_<resource>.py         # one per resource module
```

---

## 3. External Dependencies  
| Package | Purpose | Version |
|---------|---------|---------|
| **httpx** | Sync HTTP client | `^0.27` |
| **pydantic** | Data modelling / validation | `^2.0` |
| **pytest** | Unit tests | latest |
| **httpx[httpx-mock]** | Transport mock in tests | latest |
| **ruff**, **black**, **mypy** | Lint, format, type-check | latest |

Python ≥ **3.9** (use `typing.Annotated`, `list[str]`, etc.).

---

## 4. Base HTTP Client (`client.py`)  

```py
class LGLClient:
    BASE_URL = "https://api.littlegreenlight.com/api/v1/"

    def __init__(self, api_key: str, *, timeout: float = 10.0):
        self._client = httpx.Client(
            base_url=self.BASE_URL,
            headers={"Authorization": f"Bearer {api_key}"},
            timeout=timeout,
        )

    # ---- Internal helpers --------------------------------------------------
    def _get(self, path: str, **params) -> dict: ...
    def _post(self, path: str, json: dict) -> dict: ...
    def _patch(self, path: str, json: dict) -> dict: ...
    def _delete(self, path: str) -> None: ...
```

* Helpers centralise logging & error mapping (see §7).  
* **Pagination**: add a staticmethod `def _paginate(...) -> Iterable[dict]` used by `fetch_all()` convenience wrappers in each resource.

---

## 5. Data Modelling (`models.py`)  

* Base class `class LGLModel(BaseModel):` provides:
  ```py
  @classmethod
  def from_dict(cls, data: dict) -> "Self": ...
  def dict(self, *, by_alias=True, exclude_none=True) -> dict:
      return super().dict(...)
  ```
* Create one subclass per major resource with clear attribute/JSON-field mapping, e.g.:

```py
class Constituent(LGLModel):
    id: int
    first_name: str | None
    last_name: str | None
    email: str | None
    # ...

class AppealRequest(LGLModel):
    id: int
    appeal_id: int
    amount: Decimal
    # ...
```

---

## 6. Resource Modules (`<resource>.py`)  

Pattern for **every** API group:

```py
class ConstituentsAPI:
    _resource = "constituents"

    def __init__(self, client: LGLClient):  # dependency inject
        self._c = client

    def list(
        self,
        *,
        limit: int = 100,
        offset: int = 0,
        **filters,
    ) -> list[Constituent]:
        data = self._c._get(self._resource, limit=limit, offset=offset, **filters)
        return [Constituent.from_dict(d) for d in data["items"]]

    def fetch_all(self, **filters) -> list[Constituent]:
        return list(self._c._paginate(self.list, **filters))

    def retrieve(self, constituent_id: int) -> Constituent: ...
    def create(self, payload: Constituent) -> Constituent: ...
    def update(self, constituent_id: int, payload: Constituent) -> Constituent: ...
    def delete(self, constituent_id: int) -> None: ...
```

Expose convenience factory in `__init__.py` (optional):

```py
def new_client(api_key: str) -> "LGL":
    base = LGLClient(api_key)
    return LGL(
        constituents=ConstituentsAPI(base),
        appeal_requests=AppealRequestsAPI(base),
        # ...
    )
```

---

## 7. Error Handling (`exceptions.py`)  

```py
class LGLAPIError(Exception):
    def __init__(self, msg: str, *, status_code: int, url: str, payload: dict | None = None): ...

class UnauthorizedError(LGLAPIError): ...
class NotFoundError(LGLAPIError): ...
class ValidationError(LGLAPIError): ...
```

* `_get/_post/...` raise mapped exceptions on **any** non-2xx status.  
* Include response body (if JSON) and request ID header (if provided).

---

## 8. Pagination Helper  

```py
def _paginate(call: Callable[..., list[T]], **kwargs) -> Iterator[T]:
    offset = 0
    while True:
        items = call(offset=offset, **kwargs)
        if not items:
            break
        yield from items
        offset += len(items)
```

---

## 9. Testing Strategy  

* **Location**: `tests/lgl_api/`
* Use `httpx.MockTransport` (or `respx`) to stub endpoints.  
* Every public method gets:
  1. **Success path** (happy case)
  2. **Pagination** coverage (`fetch_all`)
  3. **Error** path (e.g. 401 → `UnauthorizedError`)
* `pytest -q` must pass with **100 % coverage** for implemented modules.

Example skeleton:

```py
@pytest.fixture
def mock_client(mock_transport):
    client = LGLClient("token", transport=mock_transport)
    return ConstituentsAPI(client)

def test_retrieve_ok(mock_client, mock_transport):
    mock_transport.add("GET", ".../constituents/1", json={"id": 1})
    c = mock_client.retrieve(1)
    assert c.id == 1
```

---

## 10. Coding & Style Conventions  

* **PEP 484** type hints everywhere.  
* Run `black`, `ruff --fix`, `mypy --strict`.  
* No YAGNI abstractions (keep code thin and explicit).  
* Docstrings follow [Google style].  
* Each public method documents endpoint path & required LGL scopes.

---

## 11. Implementation Roadmap  

| Phase | Deliverable | File(s) |
|-------|-------------|---------|
| **0** | Skeleton dirs + `pyproject.toml` with deps | _init commit_ |
| **1** | `client.py`, `exceptions.py` | core |
| **2** | `models.py` with **Constituent** & **AppealRequest** | models |
| **3** | `appeal_requests.py` implementation | resource |
| **4** | `tests/lgl_api/test_appeal_requests.py` (full coverage) | tests |
| **5+**| Iterate: add one resource module + matching tests each cycle | all |

Follow the same blueprint until every markdown-listed resource is covered.

---

## 12. Future Enhancements (out-of-scope but anticipated)  

* **Async variant** (`httpx.AsyncClient`) behind a shared interface.  
* **Retry & back-off** with [tenacity].  
* **Caching** via local LRU or Redis for GET endpoints.  
* **CLI** wrapper for ops tasks.  
* **Pagination streaming** (yielding models instead of list).  

---

**End of SPEC**
