"""Constituent Relationships API for LGL client."""

from typing import Dict, List, Optional

from ..lgl_api.client import LGLClient
from ..models.constituent import ConstituentRelationship


class ConstituentRelationshipsAPI:
    """API for managing constituent relationships."""
    
    def __init__(self, client: LGLClient):
        self.client = client
    
    def list(
        self, 
        constituent_id: int,
        limit: Optional[int] = None, 
        offset: Optional[int] = None
    ) -> Dict:
        """List all constituent relationships for a constituent.
        
        Args:
            constituent_id: The constituent ID
            limit: Number of entries to return
            offset: Start at given entry
        
        Returns:
            Paginated response with constituent relationship items
        """
        params = {}
        if limit is not None:
            params['limit'] = limit
        if offset is not None:
            params['offset'] = offset
        
        return self.client._get(f'constituents/{constituent_id}/constituent_relationships', **params)
    
    def fetch_all(self, constituent_id: int) -> List[ConstituentRelationship]:
        """Fetch all constituent relationships for a constituent with automatic pagination.
        
        Args:
            constituent_id: The constituent ID
        
        Returns:
            List of all ConstituentRelationship objects
        """
        def _list_page(**kwargs):
            return self.list(constituent_id, **kwargs)
        
        items = list(self.client._paginate(_list_page))
        return [ConstituentRelationship(**item) for item in items]
    
    def retrieve(self, relationship_id: int) -> ConstituentRelationship:
        """Retrieve a specific constituent relationship by ID.
        
        Args:
            relationship_id: The constituent relationship ID
        
        Returns:
            ConstituentRelationship object
        """
        response = self.client._get(f'constituent_relationships/{relationship_id}')
        return ConstituentRelationship(**response)
    
    def create(self, constituent_id: int, relationship_data: Dict) -> ConstituentRelationship:
        """Create a new constituent relationship.
        
        Args:
            constituent_id: The constituent ID
            relationship_data: Dictionary containing relationship data:
                - relationship_type_id (required): Relationship type ID
                - related_constituent_id (required): ID of related constituent
                - name (required): Name of the related constituent
                - description (optional): Description of the relationship
                - auto_soft_credit (optional): Auto soft credit flag
                - also_acknowledge (optional): Also acknowledge flag
                - share_address (optional): Share address flag
                - share_phone (optional): Share phone flag
        
        Returns:
            Created ConstituentRelationship object
        """
        response = self.client._post(f'constituents/{constituent_id}/constituent_relationships', relationship_data)
        return ConstituentRelationship(**response)
    
    def update(self, relationship_id: int, relationship_data: Dict) -> ConstituentRelationship:
        """Update an existing constituent relationship.
        
        Args:
            relationship_id: The constituent relationship ID
            relationship_data: Dictionary containing updated relationship data
        
        Returns:
            Updated ConstituentRelationship object
        """
        response = self.client._patch(f'constituent_relationships/{relationship_id}', relationship_data)
        return ConstituentRelationship(**response)
    
    def delete(self, relationship_id: int) -> Dict:
        """Delete a constituent relationship.
        
        Args:
            relationship_id: The constituent relationship ID
        
        Returns:
            Success response
        """
        self.client._delete(f'constituent_relationships/{relationship_id}')
        return {"result": "success"}
    
    # Helper methods for common operations
    
    def create_family_relationship(
        self, 
        constituent_id: int, 
        related_constituent_id: int,
        relationship_type_id: int,
        related_name: str,
        description: Optional[str] = None,
        auto_soft_credit: bool = False,
        share_address: bool = False
    ) -> ConstituentRelationship:
        """Create a family relationship.
        
        Args:
            constituent_id: The constituent ID
            related_constituent_id: ID of related family member
            relationship_type_id: Family relationship type ID
            related_name: Name of the related constituent
            description: Description of the relationship
            auto_soft_credit: Enable auto soft credit
            share_address: Share address information
        
        Returns:
            Created ConstituentRelationship object
        """
        return self.create(constituent_id, {
            "relationship_type_id": relationship_type_id,
            "related_constituent_id": related_constituent_id,
            "name": related_name,
            "description": description,
            "auto_soft_credit": auto_soft_credit,
            "share_address": share_address
        })
    
    def create_spouse_relationship(
        self, 
        constituent_id: int, 
        spouse_constituent_id: int,
        spouse_name: str,
        auto_soft_credit: bool = True,
        share_address: bool = True,
        also_acknowledge: bool = True
    ) -> ConstituentRelationship:
        """Create a spouse/partner relationship.
        
        Args:
            constituent_id: The constituent ID
            spouse_constituent_id: ID of spouse/partner
            spouse_name: Name of the spouse/partner
            auto_soft_credit: Enable auto soft credit
            share_address: Share address information
            also_acknowledge: Also acknowledge spouse in communications
        
        Returns:
            Created ConstituentRelationship object
        """
        return self.create(constituent_id, {
            "relationship_type_id": 1,  # Assuming 1 is spouse/partner type
            "related_constituent_id": spouse_constituent_id,
            "name": spouse_name,
            "auto_soft_credit": auto_soft_credit,
            "also_acknowledge": also_acknowledge,
            "share_address": share_address,
            "share_phone": True
        })
    
    def create_parent_child_relationship(
        self, 
        parent_id: int, 
        child_id: int,
        child_name: str,
        auto_soft_credit: bool = True
    ) -> ConstituentRelationship:
        """Create a parent-child relationship.
        
        Args:
            parent_id: The parent constituent ID
            child_id: The child constituent ID
            child_name: Name of the child
            auto_soft_credit: Enable auto soft credit from child to parent
        
        Returns:
            Created ConstituentRelationship object
        """
        return self.create(parent_id, {
            "relationship_type_id": 2,  # Assuming 2 is parent-child type
            "related_constituent_id": child_id,
            "name": child_name,
            "auto_soft_credit": auto_soft_credit
        })
    
    def create_employer_relationship(
        self, 
        employee_id: int, 
        employer_id: int,
        employer_name: str,
        description: Optional[str] = None
    ) -> ConstituentRelationship:
        """Create an employer-employee relationship.
        
        Args:
            employee_id: The employee constituent ID
            employer_id: The employer constituent ID
            employer_name: Name of the employer
            description: Job title or description
        
        Returns:
            Created ConstituentRelationship object
        """
        return self.create(employee_id, {
            "relationship_type_id": 3,  # Assuming 3 is employer type
            "related_constituent_id": employer_id,
            "name": employer_name,
            "description": description
        })
    
    def enable_auto_soft_credit(self, relationship_id: int) -> ConstituentRelationship:
        """Enable auto soft credit for a relationship.
        
        Args:
            relationship_id: The constituent relationship ID
        
        Returns:
            Updated ConstituentRelationship object
        """
        return self.update(relationship_id, {"auto_soft_credit": True})
    
    def disable_auto_soft_credit(self, relationship_id: int) -> ConstituentRelationship:
        """Disable auto soft credit for a relationship.
        
        Args:
            relationship_id: The constituent relationship ID
        
        Returns:
            Updated ConstituentRelationship object
        """
        return self.update(relationship_id, {"auto_soft_credit": False})
    
    def enable_address_sharing(self, relationship_id: int) -> ConstituentRelationship:
        """Enable address sharing for a relationship.
        
        Args:
            relationship_id: The constituent relationship ID
        
        Returns:
            Updated ConstituentRelationship object
        """
        return self.update(relationship_id, {"share_address": True})
    
    def enable_phone_sharing(self, relationship_id: int) -> ConstituentRelationship:
        """Enable phone sharing for a relationship.
        
        Args:
            relationship_id: The constituent relationship ID
        
        Returns:
            Updated ConstituentRelationship object
        """
        return self.update(relationship_id, {"share_phone": True})
    
    def update_description(self, relationship_id: int, description: str) -> ConstituentRelationship:
        """Update the description of a relationship.
        
        Args:
            relationship_id: The constituent relationship ID
            description: New description
        
        Returns:
            Updated ConstituentRelationship object
        """
        return self.update(relationship_id, {"description": description})
    
    def get_family_relationships(self, constituent_id: int) -> List[ConstituentRelationship]:
        """Get all family relationships for a constituent.
        
        Args:
            constituent_id: The constituent ID
        
        Returns:
            List of family ConstituentRelationship objects
        """
        # This would need to be refined based on actual relationship type IDs
        # for family relationships in the system
        all_relationships = self.fetch_all(constituent_id)
        family_type_ids = [1, 2, 4, 5, 6, 7]  # Example family type IDs
        return [rel for rel in all_relationships 
                if rel.relationship_type_id in family_type_ids]
    
    def get_relationships_with_soft_credit(self, constituent_id: int) -> List[ConstituentRelationship]:
        """Get all relationships with auto soft credit enabled.
        
        Args:
            constituent_id: The constituent ID
        
        Returns:
            List of ConstituentRelationship objects with auto soft credit
        """
        all_relationships = self.fetch_all(constituent_id)
        return [rel for rel in all_relationships if rel.auto_soft_credit]
    
    def get_relationships_by_type(self, constituent_id: int, relationship_type_id: int) -> List[ConstituentRelationship]:
        """Get all relationships of a specific type for a constituent.
        
        Args:
            constituent_id: The constituent ID
            relationship_type_id: The relationship type ID to filter by
        
        Returns:
            List of ConstituentRelationship objects of the specified type
        """
        all_relationships = self.fetch_all(constituent_id)
        return [rel for rel in all_relationships 
                if rel.relationship_type_id == relationship_type_id]