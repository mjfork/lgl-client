"""Payment Type model for LGL API."""

from typing import Optional

from ..models import LGLModel


class PaymentType(LGLModel):
    """Payment Type resource model.
    
    Payment types define the different methods of payment that can be used
    for gifts (e.g., Cash, Check, Credit Card, Stock).
    """
    
    id: int
    name: str
    key: str
    ordinal: Optional[int] = None