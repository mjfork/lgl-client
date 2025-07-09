"""Notes API for LGL client."""

from typing import Dict, List, Optional
from datetime import date

from ..lgl_api.client import LGLClient
from ..models.note import Note


class NotesAPI:
    """API for managing constituent notes."""
    
    def __init__(self, client: LGLClient):
        self.client = client
    
    def list(
        self, 
        constituent_id: int,
        limit: Optional[int] = None, 
        offset: Optional[int] = None
    ) -> Dict:
        """List all notes for a constituent.
        
        Args:
            constituent_id: The constituent ID
            limit: Number of entries to return
            offset: Start at given entry
        
        Returns:
            Paginated response with note items
        """
        params = {}
        if limit is not None:
            params['limit'] = limit
        if offset is not None:
            params['offset'] = offset
        
        return self.client._get(f'constituents/{constituent_id}/notes', **params)
    
    def list_all(
        self,
        limit: Optional[int] = None, 
        offset: Optional[int] = None
    ) -> Dict:
        """List all notes for the account.
        
        Args:
            limit: Number of entries to return
            offset: Start at given entry
        
        Returns:
            Paginated response with note items
        """
        params = {}
        if limit is not None:
            params['limit'] = limit
        if offset is not None:
            params['offset'] = offset
        
        return self.client._get('notes', **params)
    
    def fetch_all(self, constituent_id: int) -> List[Note]:
        """Fetch all notes for a constituent with automatic pagination.
        
        Args:
            constituent_id: The constituent ID
        
        Returns:
            List of all Note objects
        """
        def _list_page(**kwargs):
            return self.list(constituent_id, **kwargs)
        
        items = list(self.client._paginate(_list_page))
        return [Note(**item) for item in items]
    
    def fetch_all_account_notes(self) -> List[Note]:
        """Fetch all notes for the account with automatic pagination.
        
        Returns:
            List of all Note objects in the account
        """
        def _list_page(**kwargs):
            return self.list_all(**kwargs)
        
        items = list(self.client._paginate(_list_page))
        return [Note(**item) for item in items]
    
    def retrieve(self, note_id: int) -> Note:
        """Retrieve a specific note by ID.
        
        Args:
            note_id: The note ID
        
        Returns:
            Note object
        """
        response = self.client._get(f'notes/{note_id}')
        return Note(**response)
    
    def create(self, constituent_id: int, note_data: Dict) -> Note:
        """Create a new note for a constituent.
        
        Args:
            constituent_id: The constituent ID
            note_data: Dictionary containing note data:
                - text (required): The note content
                - original_date (required): Date note was originally created (YYYY-MM-DD)
                - note_type_id (optional): Note type ID
                - note_type_name (optional): Note type name
                - external_id (optional): External system reference
        
        Returns:
            Created Note object
        """
        response = self.client._post(f'constituents/{constituent_id}/notes', note_data)
        return Note(**response)
    
    def update(self, note_id: int, note_data: Dict) -> Note:
        """Update an existing note.
        
        Args:
            note_id: The note ID
            note_data: Dictionary containing updated note data:
                - text (required): The note content
                - original_date (required): Date note was originally created (YYYY-MM-DD)
                - note_type_id (optional): Note type ID
                - note_type_name (optional): Note type name
                - external_id (optional): External system reference
        
        Returns:
            Updated Note object
        """
        response = self.client._patch(f'notes/{note_id}', note_data)
        return Note(**response)
    
    def delete(self, note_id: int) -> Dict:
        """Delete a note.
        
        Args:
            note_id: The note ID
        
        Returns:
            Success response
        """
        self.client._delete(f'notes/{note_id}')
        return {"result": "success"}
    
    # Helper methods for common operations
    
    def create_general_note(self, constituent_id: int, text: str, original_date: date) -> Note:
        """Create a general note for a constituent.
        
        Args:
            constituent_id: The constituent ID
            text: The note content
            original_date: Date the note was originally created
        
        Returns:
            Created Note object
        """
        return self.create(constituent_id, {
            "text": text,
            "original_date": original_date.strftime('%Y-%m-%d'),
            "note_type_name": "General"
        })
    
    def create_contact_note(self, constituent_id: int, text: str, original_date: date) -> Note:
        """Create a contact note for a constituent.
        
        Args:
            constituent_id: The constituent ID
            text: The note content
            original_date: Date the note was originally created
        
        Returns:
            Created Note object
        """
        return self.create(constituent_id, {
            "text": text,
            "original_date": original_date.strftime('%Y-%m-%d'),
            "note_type_name": "Contact"
        })
    
    def create_meeting_note(self, constituent_id: int, text: str, original_date: date) -> Note:
        """Create a meeting note for a constituent.
        
        Args:
            constituent_id: The constituent ID
            text: The note content
            original_date: Date the note was originally created
        
        Returns:
            Created Note object
        """
        return self.create(constituent_id, {
            "text": text,
            "original_date": original_date.strftime('%Y-%m-%d'),
            "note_type_name": "Meeting"
        })
    
    def create_phone_call_note(self, constituent_id: int, text: str, original_date: date) -> Note:
        """Create a phone call note for a constituent.
        
        Args:
            constituent_id: The constituent ID
            text: The note content
            original_date: Date the note was originally created
        
        Returns:
            Created Note object
        """
        return self.create(constituent_id, {
            "text": text,
            "original_date": original_date.strftime('%Y-%m-%d'),
            "note_type_name": "Phone Call"
        })