"""Appeal Requests API for LGL client."""

from typing import Dict, List, Optional

from ..lgl_api.client import LGLClient
from ..models.appeal_request import AppealRequest


class AppealRequestsAPI:
    """API for managing appeal requests."""
    
    def __init__(self, client: LGLClient):
        self.client = client
    
    def list_by_appeal(
        self, 
        appeal_id: int,
        limit: Optional[int] = None, 
        offset: Optional[int] = None
    ) -> Dict:
        """List all appeal requests for a specific appeal.
        
        Args:
            appeal_id: The appeal ID
            limit: Number of entries to return
            offset: Start at given entry
        
        Returns:
            Paginated response with appeal request items
        """
        params = {}
        if limit is not None:
            params['limit'] = limit
        if offset is not None:
            params['offset'] = offset
        
        return self.client._get(f'appeals/{appeal_id}/appeal_requests', **params)
    
    def list_by_constituent(
        self, 
        constituent_id: int,
        limit: Optional[int] = None, 
        offset: Optional[int] = None
    ) -> Dict:
        """List all appeal requests for a specific constituent.
        
        Args:
            constituent_id: The constituent ID
            limit: Number of entries to return
            offset: Start at given entry
        
        Returns:
            Paginated response with appeal request items
        """
        params = {}
        if limit is not None:
            params['limit'] = limit
        if offset is not None:
            params['offset'] = offset
        
        return self.client._get(f'constituents/{constituent_id}/appeal_requests', **params)
    
    def fetch_all_by_appeal(self, appeal_id: int) -> List[AppealRequest]:
        """Fetch all appeal requests for an appeal with automatic pagination.
        
        Args:
            appeal_id: The appeal ID
        
        Returns:
            List of all AppealRequest objects
        """
        def _list_page(**kwargs):
            return self.list_by_appeal(appeal_id, **kwargs)
        
        items = list(self.client._paginate(_list_page))
        return [AppealRequest(**item) for item in items]
    
    def fetch_all_by_constituent(self, constituent_id: int) -> List[AppealRequest]:
        """Fetch all appeal requests for a constituent with automatic pagination.
        
        Args:
            constituent_id: The constituent ID
        
        Returns:
            List of all AppealRequest objects
        """
        def _list_page(**kwargs):
            return self.list_by_constituent(constituent_id, **kwargs)
        
        items = list(self.client._paginate(_list_page))
        return [AppealRequest(**item) for item in items]
    
    def retrieve(self, appeal_request_id: int) -> AppealRequest:
        """Retrieve a specific appeal request by ID.
        
        Args:
            appeal_request_id: The appeal request ID
        
        Returns:
            AppealRequest object
        """
        response = self.client._get(f'appeal_requests/{appeal_request_id}')
        return AppealRequest(**response)
    
    def create_for_appeal(self, appeal_id: int, appeal_request_data: Dict) -> AppealRequest:
        """Create a new appeal request for a specific appeal.
        
        Args:
            appeal_id: The appeal ID
            appeal_request_data: Dictionary containing appeal request data:
                - constituent_id (required): Constituent ID for this request
                - ask_amount (optional): Amount to request from constituent
                - status (optional): Request status
                - assigned_to (optional): Person assigned to this request
                - custom_attrs (optional): Custom field data
        
        Returns:
            Created AppealRequest object
        """
        response = self.client._post(f'appeals/{appeal_id}/appeal_requests', appeal_request_data)
        return AppealRequest(**response)
    
    def create_for_constituent(self, constituent_id: int, appeal_request_data: Dict) -> AppealRequest:
        """Create a new appeal request for a specific constituent.
        
        Args:
            constituent_id: The constituent ID
            appeal_request_data: Dictionary containing appeal request data:
                - appeal_id (required): Appeal ID for this request
                - ask_amount (optional): Amount to request from constituent
                - status (optional): Request status
                - assigned_to (optional): Person assigned to this request
                - custom_attrs (optional): Custom field data
        
        Returns:
            Created AppealRequest object
        """
        response = self.client._post(f'constituents/{constituent_id}/appeal_requests', appeal_request_data)
        return AppealRequest(**response)
    
    def update(self, appeal_request_id: int, appeal_request_data: Dict) -> AppealRequest:
        """Update an existing appeal request.
        
        Args:
            appeal_request_id: The appeal request ID
            appeal_request_data: Dictionary containing updated appeal request data
        
        Returns:
            Updated AppealRequest object
        """
        response = self.client._patch(f'appeal_requests/{appeal_request_id}', appeal_request_data)
        return AppealRequest(**response)
    
    def delete(self, appeal_request_id: int) -> Dict:
        """Delete an appeal request.
        
        Args:
            appeal_request_id: The appeal request ID
        
        Returns:
            Success response
        """
        self.client._delete(f'appeal_requests/{appeal_request_id}')
        return {"result": "success"}
    
    # Helper methods for common operations
    
    def create_simple_request(
        self, 
        appeal_id: int, 
        constituent_id: int,
        ask_amount: float,
        assigned_to: Optional[str] = None,
        status: str = "Pending"
    ) -> AppealRequest:
        """Create a simple appeal request with common parameters.
        
        Args:
            appeal_id: The appeal ID
            constituent_id: The constituent ID
            ask_amount: Amount to request
            assigned_to: Person assigned to this request
            status: Request status
        
        Returns:
            Created AppealRequest object
        """
        data = {
            "constituent_id": constituent_id,
            "ask_amount": ask_amount,
            "status": status
        }
        
        if assigned_to:
            data["assigned_to"] = assigned_to
        
        return self.create_for_appeal(appeal_id, data)
    
    def assign_request(self, appeal_request_id: int, assigned_to: str) -> AppealRequest:
        """Assign an appeal request to someone.
        
        Args:
            appeal_request_id: The appeal request ID
            assigned_to: Person to assign the request to
        
        Returns:
            Updated AppealRequest object
        """
        return self.update(appeal_request_id, {"assigned_to": assigned_to})
    
    def update_status(self, appeal_request_id: int, status: str) -> AppealRequest:
        """Update the status of an appeal request.
        
        Args:
            appeal_request_id: The appeal request ID
            status: New status (e.g., "Pending", "Completed", "Declined")
        
        Returns:
            Updated AppealRequest object
        """
        return self.update(appeal_request_id, {"status": status})
    
    def update_ask_amount(self, appeal_request_id: int, ask_amount: float) -> AppealRequest:
        """Update the ask amount for an appeal request.
        
        Args:
            appeal_request_id: The appeal request ID
            ask_amount: New ask amount
        
        Returns:
            Updated AppealRequest object
        """
        return self.update(appeal_request_id, {"ask_amount": ask_amount})
    
    def mark_completed(self, appeal_request_id: int, raised_amount: Optional[float] = None) -> AppealRequest:
        """Mark an appeal request as completed.
        
        Args:
            appeal_request_id: The appeal request ID
            raised_amount: Amount actually raised (optional)
        
        Returns:
            Updated AppealRequest object
        """
        data = {"status": "Completed"}
        if raised_amount is not None:
            data["raised"] = raised_amount
        
        return self.update(appeal_request_id, data)
    
    def get_pending_requests_by_appeal(self, appeal_id: int) -> List[AppealRequest]:
        """Get all pending appeal requests for an appeal.
        
        Args:
            appeal_id: The appeal ID
        
        Returns:
            List of pending AppealRequest objects
        """
        all_requests = self.fetch_all_by_appeal(appeal_id)
        return [req for req in all_requests if req.status == "Pending"]
    
    def get_requests_by_assignee(self, appeal_id: int, assigned_to: str) -> List[AppealRequest]:
        """Get all appeal requests assigned to a specific person.
        
        Args:
            appeal_id: The appeal ID
            assigned_to: Person the requests are assigned to
        
        Returns:
            List of AppealRequest objects assigned to the person
        """
        all_requests = self.fetch_all_by_appeal(appeal_id)
        return [req for req in all_requests if req.assigned_to == assigned_to]