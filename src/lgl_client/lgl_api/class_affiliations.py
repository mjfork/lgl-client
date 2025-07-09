"""Class Affiliations API for LGL client."""

from typing import Dict, List, Optional

from ..lgl_api.client import LGLClient
from ..models.constituent import ClassAffiliation


class ClassAffiliationsAPI:
    """API for managing constituent class affiliations."""
    
    def __init__(self, client: LGLClient):
        self.client = client
    
    def list(
        self, 
        constituent_id: int,
        limit: Optional[int] = None, 
        offset: Optional[int] = None
    ) -> Dict:
        """List all class affiliations for a constituent.
        
        Args:
            constituent_id: The constituent ID
            limit: Number of entries to return
            offset: Start at given entry
        
        Returns:
            Paginated response with class affiliation items
        """
        params = {}
        if limit is not None:
            params['limit'] = limit
        if offset is not None:
            params['offset'] = offset
        
        return self.client._get(f'constituents/{constituent_id}/class_affiliations', **params)
    
    def fetch_all(self, constituent_id: int) -> List[ClassAffiliation]:
        """Fetch all class affiliations for a constituent with automatic pagination.
        
        Args:
            constituent_id: The constituent ID
        
        Returns:
            List of all ClassAffiliation objects
        """
        def _list_page(**kwargs):
            return self.list(constituent_id, **kwargs)
        
        items = list(self.client._paginate(_list_page))
        return [ClassAffiliation(**item) for item in items]
    
    def retrieve(self, class_affiliation_id: int) -> ClassAffiliation:
        """Retrieve a specific class affiliation by ID.
        
        Args:
            class_affiliation_id: The class affiliation ID
        
        Returns:
            ClassAffiliation object
        """
        response = self.client._get(f'class_affiliations/{class_affiliation_id}')
        return ClassAffiliation(**response)
    
    def create(self, constituent_id: int, class_affiliation_data: Dict) -> ClassAffiliation:
        """Create a new class affiliation for a constituent.
        
        Args:
            constituent_id: The constituent ID
            class_affiliation_data: Dictionary containing class affiliation data:
                - class_affiliation_type_id (required): Class affiliation type ID
                - year (required): Year associated with the affiliation
                - note (optional): Additional notes about the affiliation
        
        Returns:
            Created ClassAffiliation object
        """
        response = self.client._post(f'constituents/{constituent_id}/class_affiliations', class_affiliation_data)
        return ClassAffiliation(**response)
    
    def update(self, class_affiliation_id: int, class_affiliation_data: Dict) -> ClassAffiliation:
        """Update an existing class affiliation.
        
        Args:
            class_affiliation_id: The class affiliation ID
            class_affiliation_data: Dictionary containing updated class affiliation data:
                - class_affiliation_type_id (optional): Class affiliation type ID
                - year (optional): Year associated with the affiliation
                - note (optional): Additional notes about the affiliation
        
        Returns:
            Updated ClassAffiliation object
        """
        response = self.client._patch(f'class_affiliations/{class_affiliation_id}', class_affiliation_data)
        return ClassAffiliation(**response)
    
    def delete(self, class_affiliation_id: int) -> Dict:
        """Delete a class affiliation.
        
        Args:
            class_affiliation_id: The class affiliation ID
        
        Returns:
            Success response
        """
        self.client._delete(f'class_affiliations/{class_affiliation_id}')
        return {"result": "success"}
    
    # Helper methods for common operations
    
    def create_student_affiliation(
        self, 
        constituent_id: int, 
        year: int,
        note: Optional[str] = None
    ) -> ClassAffiliation:
        """Create a student class affiliation.
        
        Args:
            constituent_id: The constituent ID
            year: Graduation or attendance year
            note: Optional notes about the affiliation
        
        Returns:
            Created ClassAffiliation object
        """
        return self.create(constituent_id, {
            "class_affiliation_type_id": 1,  # Assuming 1 is Student type
            "year": year,
            "note": note
        })
    
    def create_parent_affiliation(
        self, 
        constituent_id: int, 
        year: int,
        note: Optional[str] = None
    ) -> ClassAffiliation:
        """Create a parent class affiliation.
        
        Args:
            constituent_id: The constituent ID
            year: Year of child's graduation or attendance
            note: Optional notes about the affiliation
        
        Returns:
            Created ClassAffiliation object
        """
        return self.create(constituent_id, {
            "class_affiliation_type_id": 2,  # Assuming 2 is Parent type
            "year": year,
            "note": note
        })
    
    def create_custom_affiliation(
        self, 
        constituent_id: int, 
        affiliation_type_id: int,
        year: int,
        note: Optional[str] = None
    ) -> ClassAffiliation:
        """Create a class affiliation with custom type.
        
        Args:
            constituent_id: The constituent ID
            affiliation_type_id: The class affiliation type ID
            year: Year associated with the affiliation
            note: Optional notes about the affiliation
        
        Returns:
            Created ClassAffiliation object
        """
        return self.create(constituent_id, {
            "class_affiliation_type_id": affiliation_type_id,
            "year": year,
            "note": note
        })
    
    def update_year(self, class_affiliation_id: int, new_year: int) -> ClassAffiliation:
        """Update the year for a class affiliation.
        
        Args:
            class_affiliation_id: The class affiliation ID
            new_year: New year for the affiliation
        
        Returns:
            Updated ClassAffiliation object
        """
        return self.update(class_affiliation_id, {"year": new_year})
    
    def add_note(self, class_affiliation_id: int, note: str) -> ClassAffiliation:
        """Add or update a note on a class affiliation.
        
        Args:
            class_affiliation_id: The class affiliation ID
            note: Note text to add
        
        Returns:
            Updated ClassAffiliation object
        """
        return self.update(class_affiliation_id, {"note": note})
    
    def change_type(self, class_affiliation_id: int, new_type_id: int) -> ClassAffiliation:
        """Change the affiliation type.
        
        Args:
            class_affiliation_id: The class affiliation ID
            new_type_id: New class affiliation type ID
        
        Returns:
            Updated ClassAffiliation object
        """
        return self.update(class_affiliation_id, {"class_affiliation_type_id": new_type_id})
    
    def get_affiliations_by_year(self, constituent_id: int, year: int) -> List[ClassAffiliation]:
        """Get all class affiliations for a constituent in a specific year.
        
        Args:
            constituent_id: The constituent ID
            year: The year to filter by
        
        Returns:
            List of ClassAffiliation objects for the specified year
        """
        all_affiliations = self.fetch_all(constituent_id)
        return [affiliation for affiliation in all_affiliations if affiliation.year == year]
    
    def get_affiliations_by_type(self, constituent_id: int, type_id: int) -> List[ClassAffiliation]:
        """Get all class affiliations for a constituent of a specific type.
        
        Args:
            constituent_id: The constituent ID
            type_id: The class affiliation type ID to filter by
        
        Returns:
            List of ClassAffiliation objects of the specified type
        """
        all_affiliations = self.fetch_all(constituent_id)
        return [affiliation for affiliation in all_affiliations 
                if affiliation.class_affiliation_type_id == type_id]