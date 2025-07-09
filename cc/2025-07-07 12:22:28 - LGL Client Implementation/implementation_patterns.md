# Implementation Patterns & Standards

## Model Field Type Mapping

### Based on API Documentation Analysis:

1. **ID Fields**: Always `int` (never null)
   - `id: int`

2. **Name/Title Fields**: Always `str` (never null) 
   - `name: str`

3. **Description Fields**: Always optional
   - `description: Optional[str] = None`

4. **Code Fields**: Always optional
   - `code: Optional[str] = None`

5. **Date Fields**: Use string for now (TO FIX LATER)
   - `date: Optional[str] = None`
   - `start_date: Optional[str] = None`
   - `end_date: Optional[str] = None`

6. **Financial Fields**: Use Decimal, always optional
   - `financial_goal: Optional[Decimal] = None`
   - `projected_amount: Optional[Decimal] = None`

7. **Boolean Fields**: Check API docs, usually optional
   - `removable: Optional[bool] = None`

8. **Ordinal/Order Fields**: Usually optional int
   - `ordinal: Optional[int] = None`

## API Class Patterns

### Standard Methods for All Resources:
```python
def list(self, *, limit: int = 25, offset: int = 0) -> List[Model]:
def fetch_all(self) -> List[Model]:
def retrieve(self, resource_id: int) -> Model:
def create(self, resource: Model) -> Model:
def update(self, resource_id: int, resource: Model) -> Model:
def delete(self, resource_id: int) -> None:
```

### Pagination Pattern:
```python
def fetch_all(self) -> List[Model]:
    def _list_page(**kwargs: Any) -> List[Model]:
        return self.list(**kwargs)
    items = list(self._client._paginate(_list_page))
    return [Model.from_dict(item) if isinstance(item, dict) else item for item in items]
```

## Import Pattern:
1. Update `lgl_client/__init__.py` imports
2. Add to LGL class constructor
3. Test immediately

## Testing Pattern:
Always test with: 
```bash
python -c "import os; from lgl_client import new_client; client = new_client(os.environ['LGL_API_KEY']); print(client.{resource}.list())"
```

This ensures consistent implementation across all 31 resources.