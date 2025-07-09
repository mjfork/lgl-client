"""Gifts API for LGL client."""

from typing import Dict, List, Optional
from datetime import date

from ..lgl_api.client import LGLClient
from ..models.gift import Gift


class GiftsAPI:
    """API for managing gifts."""
    
    def __init__(self, client: LGLClient):
        self.client = client
    
    def list(
        self, 
        constituent_id: int,
        limit: Optional[int] = None, 
        offset: Optional[int] = None
    ) -> Dict:
        """List all gifts for a constituent.
        
        Args:
            constituent_id: The constituent ID
            limit: Number of entries to return
            offset: Start at given entry
        
        Returns:
            Paginated response with gift items
        """
        params = {}
        if limit is not None:
            params['limit'] = limit
        if offset is not None:
            params['offset'] = offset
        
        return self.client._get(f'constituents/{constituent_id}/gifts', **params)
    
    def search(
        self,
        constituent_id: Optional[int] = None,
        amount_from: Optional[float] = None,
        amount_to: Optional[float] = None,
        date_from: Optional[date] = None,
        date_to: Optional[date] = None,
        gift_type_id: Optional[int] = None,
        payment_type_id: Optional[int] = None,
        campaign_id: Optional[int] = None,
        fund_id: Optional[int] = None,
        appeal_id: Optional[int] = None,
        event_id: Optional[int] = None,
        acknowledged: Optional[bool] = None,
        external_gift_id: Optional[str] = None,
        check_number: Optional[str] = None,
        note: Optional[str] = None,
        sort: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> Dict:
        """Search for gifts with various criteria.
        
        Args:
            constituent_id: Filter by constituent ID
            amount_from: Minimum gift amount
            amount_to: Maximum gift amount
            date_from: Start date for gifts (YYYY-MM-DD)
            date_to: End date for gifts (YYYY-MM-DD)
            gift_type_id: Filter by gift type ID
            payment_type_id: Filter by payment type ID
            campaign_id: Filter by campaign ID
            fund_id: Filter by fund ID
            appeal_id: Filter by appeal ID
            event_id: Filter by event ID
            acknowledged: Filter by acknowledgment status
            external_gift_id: Search by external gift ID
            check_number: Search by check number
            note: Search in gift notes
            sort: Sort field with optional '!' for reverse order
            limit: Number of entries to return
            offset: Start at given entry
        
        Returns:
            Paginated response with gift items
        """
        params = {}
        
        if constituent_id is not None:
            params['constituent_id'] = constituent_id
        if amount_from is not None:
            params['amount_from'] = amount_from
        if amount_to is not None:
            params['amount_to'] = amount_to
        if date_from is not None:
            params['date_from'] = date_from.strftime('%Y-%m-%d')
        if date_to is not None:
            params['date_to'] = date_to.strftime('%Y-%m-%d')
        if gift_type_id is not None:
            params['gift_type_id'] = gift_type_id
        if payment_type_id is not None:
            params['payment_type_id'] = payment_type_id
        if campaign_id is not None:
            params['campaign_id'] = campaign_id
        if fund_id is not None:
            params['fund_id'] = fund_id
        if appeal_id is not None:
            params['appeal_id'] = appeal_id
        if event_id is not None:
            params['event_id'] = event_id
        if acknowledged is not None:
            params['acknowledged'] = acknowledged
        if external_gift_id is not None:
            params['external_gift_id'] = external_gift_id
        if check_number is not None:
            params['check_number'] = check_number
        if note is not None:
            params['note'] = note
        if sort is not None:
            params['sort'] = sort
        if limit is not None:
            params['limit'] = limit
        if offset is not None:
            params['offset'] = offset
        
        return self.client._get('gifts/search', **params)
    
    def fetch_all(self, constituent_id: int) -> List[Gift]:
        """Fetch all gifts for a constituent with automatic pagination.
        
        Args:
            constituent_id: The constituent ID
        
        Returns:
            List of all Gift objects
        """
        def _list_page(**kwargs):
            return self.list(constituent_id, **kwargs)
        
        items = list(self.client._paginate(_list_page))
        return [Gift(**item) for item in items]
    
    def search_gifts(
        self,
        constituent_id: Optional[int] = None,
        amount_from: Optional[float] = None,
        amount_to: Optional[float] = None,
        date_from: Optional[date] = None,
        date_to: Optional[date] = None,
        **kwargs
    ) -> List[Gift]:
        """Search for gifts and return as Gift objects.
        
        Args:
            constituent_id: Filter by constituent ID
            amount_from: Minimum gift amount
            amount_to: Maximum gift amount
            date_from: Start date for gifts
            date_to: End date for gifts
            **kwargs: Additional search parameters
        
        Returns:
            List of Gift objects
        """
        def _search_page(**search_kwargs):
            return self.search(
                constituent_id=constituent_id,
                amount_from=amount_from,
                amount_to=amount_to,
                date_from=date_from,
                date_to=date_to,
                **kwargs,
                **search_kwargs
            )
        
        items = list(self.client._paginate(_search_page))
        return [Gift(**item) for item in items]
    
    def retrieve(self, gift_id: int) -> Gift:
        """Retrieve a specific gift by ID.
        
        Args:
            gift_id: The gift ID
        
        Returns:
            Gift object
        """
        response = self.client._get(f'gifts/{gift_id}')
        return Gift(**response)
    
    def create(self, constituent_id: int, gift_data: Dict) -> Gift:
        """Create a new gift for a constituent.
        
        Args:
            constituent_id: The constituent ID
            gift_data: Dictionary containing gift data:
                - amount (required): Gift amount
                - date (required): Gift date (YYYY-MM-DD)
                - gift_type_id (required): Gift type ID
                - gift_category_id (optional): Gift category ID
                - payment_type_id (optional): Payment type ID
                - campaign_id (optional): Campaign ID
                - fund_id (optional): Fund ID
                - appeal_id (optional): Appeal ID
                - event_id (optional): Event ID
                - deductible_amount (optional): Tax-deductible amount
                - check_number (optional): Check number
                - check_date (optional): Check date
                - note (optional): Gift notes
                - external_gift_id (optional): External system ID
                - tribute (optional): Tribute information
                - custom_attrs (optional): Custom field data
        
        Returns:
            Created Gift object
        """
        response = self.client._post(f'constituents/{constituent_id}/gifts', gift_data)
        return Gift(**response)
    
    def update(self, gift_id: int, gift_data: Dict) -> Gift:
        """Update an existing gift.
        
        Args:
            gift_id: The gift ID
            gift_data: Dictionary containing updated gift data
        
        Returns:
            Updated Gift object
        """
        response = self.client._patch(f'gifts/{gift_id}', gift_data)
        return Gift(**response)
    
    def delete(self, gift_id: int) -> Dict:
        """Delete a gift.
        
        Args:
            gift_id: The gift ID
        
        Returns:
            Success response
        """
        self.client._delete(f'gifts/{gift_id}')
        return {"result": "success"}
    
    # Helper methods for common operations
    
    def create_donation(
        self, 
        constituent_id: int, 
        amount: float,
        gift_date: date,
        fund_id: Optional[int] = None,
        campaign_id: Optional[int] = None,
        appeal_id: Optional[int] = None,
        note: Optional[str] = None
    ) -> Gift:
        """Create a simple donation gift.
        
        Args:
            constituent_id: The constituent ID
            amount: Donation amount
            gift_date: Date of the gift
            fund_id: Fund to associate with (optional)
            campaign_id: Campaign to associate with (optional)
            appeal_id: Appeal to associate with (optional)
            note: Gift notes (optional)
        
        Returns:
            Created Gift object
        """
        data = {
            "amount": amount,
            "date": gift_date.strftime('%Y-%m-%d'),
            "gift_type_id": 1  # Assuming 1 is "Gift" type
        }
        
        if fund_id:
            data["fund_id"] = fund_id
        if campaign_id:
            data["campaign_id"] = campaign_id
        if appeal_id:
            data["appeal_id"] = appeal_id
        if note:
            data["note"] = note
        
        return self.create(constituent_id, data)
    
    def create_pledge(
        self, 
        constituent_id: int, 
        total_amount: float,
        pledge_date: date,
        installment_frequency: str,
        number_installments: int,
        fund_id: Optional[int] = None,
        campaign_id: Optional[int] = None
    ) -> Gift:
        """Create a pledge gift.
        
        Args:
            constituent_id: The constituent ID
            total_amount: Total pledge amount
            pledge_date: Date of the pledge
            installment_frequency: Frequency of payments (Monthly, Quarterly, etc.)
            number_installments: Number of installment payments
            fund_id: Fund to associate with (optional)
            campaign_id: Campaign to associate with (optional)
        
        Returns:
            Created Gift object
        """
        data = {
            "amount": total_amount,
            "date": pledge_date.strftime('%Y-%m-%d'),
            "gift_type_id": 3,  # Assuming 3 is "Pledge" type
            "installment_frequency": installment_frequency,
            "number_installments": number_installments
        }
        
        if fund_id:
            data["fund_id"] = fund_id
        if campaign_id:
            data["campaign_id"] = campaign_id
        
        return self.create(constituent_id, data)
    
    def acknowledge_gift(self, gift_id: int, acknowledge_date: Optional[date] = None) -> Gift:
        """Mark a gift as acknowledged.
        
        Args:
            gift_id: The gift ID
            acknowledge_date: Date of acknowledgment (defaults to today)
        
        Returns:
            Updated Gift object
        """
        if acknowledge_date is None:
            acknowledge_date = date.today()
        
        return self.update(gift_id, {
            "acknowledged": True,
            "acknowledged_date": acknowledge_date.strftime('%Y-%m-%d')
        })
    
    def add_note(self, gift_id: int, note: str) -> Gift:
        """Add or update a note on a gift.
        
        Args:
            gift_id: The gift ID
            note: Note text to add
        
        Returns:
            Updated Gift object
        """
        return self.update(gift_id, {"note": note})
    
    def set_deductible_amount(self, gift_id: int, deductible_amount: float) -> Gift:
        """Set the tax-deductible amount for a gift.
        
        Args:
            gift_id: The gift ID
            deductible_amount: Tax-deductible amount
        
        Returns:
            Updated Gift object
        """
        return self.update(gift_id, {"deductible_amount": deductible_amount})
    
    def get_unacknowledged_gifts(self, constituent_id: int) -> List[Gift]:
        """Get all unacknowledged gifts for a constituent.
        
        Args:
            constituent_id: The constituent ID
        
        Returns:
            List of unacknowledged Gift objects
        """
        all_gifts = self.fetch_all(constituent_id)
        return [gift for gift in all_gifts if not gift.acknowledged]
    
    def get_gifts_by_campaign(self, constituent_id: int, campaign_id: int) -> List[Gift]:
        """Get all gifts for a constituent associated with a specific campaign.
        
        Args:
            constituent_id: The constituent ID
            campaign_id: The campaign ID
        
        Returns:
            List of Gift objects for the campaign
        """
        all_gifts = self.fetch_all(constituent_id)
        return [gift for gift in all_gifts if gift.campaign_id == campaign_id]
    
    def get_gifts_by_date_range(
        self, 
        constituent_id: int, 
        start_date: date, 
        end_date: date
    ) -> List[Gift]:
        """Get all gifts for a constituent within a date range.
        
        Args:
            constituent_id: The constituent ID
            start_date: Start date for range
            end_date: End date for range
        
        Returns:
            List of Gift objects within the date range
        """
        all_gifts = self.fetch_all(constituent_id)
        return [gift for gift in all_gifts 
                if start_date <= gift.date <= end_date]