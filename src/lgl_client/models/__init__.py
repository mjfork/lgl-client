"""Base model classes and utilities."""

from typing import Any, Dict, Type, TypeVar

from pydantic import BaseModel, ConfigDict

T = TypeVar('T', bound='LGLModel')


class LGLModel(BaseModel):
    """Base model for all LGL API resources.
    
    Provides common functionality for data validation, serialization,
    and deserialization using Pydantic.
    """
    
    model_config = ConfigDict(
        # Allow extra fields for forward compatibility
        extra='allow',
        # Use aliases for field names (API uses snake_case)
        populate_by_name=True,
        # Validate assignment
        validate_assignment=True,
        # Use enum values
        use_enum_values=True,
    )
    
    @classmethod
    def from_dict(cls: Type[T], data: Dict[str, Any]) -> T:
        """Create model instance from dictionary data.
        
        Args:
            data: Dictionary containing model data
            
        Returns:
            Model instance
        """
        return cls.model_validate(data)
    
    def to_dict(self, *, by_alias: bool = True, exclude_none: bool = True) -> Dict[str, Any]:
        """Convert model to dictionary.
        
        Args:
            by_alias: Use field aliases (recommended for API compatibility)
            exclude_none: Exclude None values from output
            
        Returns:
            Dictionary representation of the model
        """
        return self.model_dump(
            by_alias=by_alias,
            exclude_none=exclude_none,
        )