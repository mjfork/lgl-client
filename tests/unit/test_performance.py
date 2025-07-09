"""Performance benchmark tests for the LGL client."""
import pytest
import time
from unittest.mock import patch
from typing import List, Dict, Any
import statistics

from lgl_client import new_client
from tests.fixtures import APIResponseMocker


class TestPerformance:
    """Performance benchmark tests."""

    @pytest.fixture
    def client(self):
        """Create test client."""
        return new_client(api_key="test_key")

    @pytest.fixture
    def large_dataset(self):
        """Generate large dataset for performance testing."""
        return [
            {
                "id": i,
                "name": f"Item {i}",
                "item_type": "Constituent",
                "description": f"This is a longer description for item {i} " * 5,
                "created_at": "2025-01-01T10:00:00Z",
                "updated_at": "2025-01-01T10:00:00Z"
            }
            for i in range(1, 1001)  # 1000 items
        ]

    def test_model_creation_performance(self, large_dataset):
        """Test performance of model creation with large datasets."""
        from lgl_client.models.category import Category
        
        start_time = time.time()
        
        categories = []
        for item_data in large_dataset[:100]:  # Test with 100 items
            category = Category(**item_data)
            categories.append(category)
        
        end_time = time.time()
        creation_time = end_time - start_time
        
        # Should create 100 models in reasonable time (under 1 second)
        assert creation_time < 1.0, f"Model creation took {creation_time:.3f}s for 100 items"
        assert len(categories) == 100
        
        # Test average creation time per model
        avg_time = creation_time / 100
        assert avg_time < 0.01, f"Average model creation time {avg_time:.6f}s too slow"

    def test_pagination_performance(self, client, large_dataset):
        """Test pagination performance with large datasets."""
        # Split dataset into pages
        page_size = 100
        pages = [
            large_dataset[i:i + page_size] 
            for i in range(0, len(large_dataset), page_size)
        ]
        
        def mock_get_side_effect(*args, **kwargs):
            offset = kwargs.get('offset', 0)
            limit = kwargs.get('limit', 100)
            page_index = offset // limit
            
            if page_index < len(pages):
                items = pages[page_index]
            else:
                items = []
            
            return APIResponseMocker.paginated_response(
                items=items,
                total=len(large_dataset),
                page=page_index + 1,
                per_page=limit
            )
        
        with patch.object(client.categories._client, '_get', side_effect=mock_get_side_effect):
            start_time = time.time()
            all_items = client.categories.fetch_all()
            end_time = time.time()
            
            pagination_time = end_time - start_time
            
            # Should handle 1000 items in reasonable time
            assert pagination_time < 2.0, f"Pagination took {pagination_time:.3f}s for 1000 items"
            assert len(all_items) == 1000
            
            # Test items per second throughput
            throughput = len(all_items) / pagination_time
            assert throughput > 500, f"Throughput {throughput:.1f} items/sec too low"

    def test_search_performance(self, client):
        """Test search performance with various query sizes."""
        search_results = [
            {
                "id": i,
                "first_name": f"John{i}",
                "last_name": f"Doe{i}",
                "email": f"john{i}@example.com",
                "created_at": "2025-01-01T10:00:00Z",
                "updated_at": "2025-01-01T10:00:00Z",
                "addresses": [],
                "phone_numbers": [],
                "email_addresses": [],
                "web_addresses": []
            }
            for i in range(1, 51)  # 50 search results
        ]
        
        response_data = APIResponseMocker.paginated_response(
            items=search_results,
            total=50,
            page=1,
            per_page=50
        )
        
        with patch.object(client.constituents.client, '_get', return_value=response_data):
            # Test multiple search operations
            search_times = []
            
            for i in range(10):  # 10 search operations
                start_time = time.time()
                results = client.constituents.search([f"name=John{i}"])
                end_time = time.time()
                
                search_times.append(end_time - start_time)
                assert len(results['items']) == 50
            
            # Analyze search performance
            avg_search_time = statistics.mean(search_times)
            max_search_time = max(search_times)
            
            assert avg_search_time < 0.1, f"Average search time {avg_search_time:.3f}s too slow"
            assert max_search_time < 0.2, f"Maximum search time {max_search_time:.3f}s too slow"

    def test_date_parsing_performance(self):
        """Test date parsing performance with many dates."""
        from lgl_client.models.common import parse_date, parse_datetime
        
        # Generate date strings
        date_strings = [f"2025-{month:02d}-{day:02d}" for month in range(1, 13) for day in range(1, 29)]
        datetime_strings = [f"{date_str}T{hour:02d}:{minute:02d}:00Z" 
                          for date_str in date_strings[:50] 
                          for hour in range(0, 24, 6) 
                          for minute in range(0, 60, 15)]
        
        # Test date parsing performance
        start_time = time.time()
        parsed_dates = [parse_date(date_str) for date_str in date_strings]
        date_parse_time = time.time() - start_time
        
        # Test datetime parsing performance
        start_time = time.time()
        parsed_datetimes = [parse_datetime(dt_str) for dt_str in datetime_strings]
        datetime_parse_time = time.time() - start_time
        
        # Verify all dates were parsed
        assert all(date is not None for date in parsed_dates)
        assert all(dt is not None for dt in parsed_datetimes)
        
        # Performance assertions
        date_throughput = len(date_strings) / date_parse_time
        datetime_throughput = len(datetime_strings) / datetime_parse_time
        
        assert date_throughput > 1000, f"Date parsing throughput {date_throughput:.1f} dates/sec too slow"
        assert datetime_throughput > 500, f"Datetime parsing throughput {datetime_throughput:.1f} dt/sec too slow"

    def test_memory_usage_with_large_responses(self, client, large_dataset):
        """Test memory usage doesn't grow excessively with large responses."""
        import tracemalloc
        
        # Start memory tracing
        tracemalloc.start()
        
        # Process large dataset
        response_data = APIResponseMocker.paginated_response(
            items=large_dataset,
            total=len(large_dataset),
            page=1,
            per_page=len(large_dataset)
        )
        
        with patch.object(client.categories._client, '_get', return_value=response_data):
            # Take initial memory snapshot
            snapshot1 = tracemalloc.take_snapshot()
            
            # Process the large response
            all_items = client.categories.list(limit=len(large_dataset))
            
            # Take final memory snapshot
            snapshot2 = tracemalloc.take_snapshot()
            
            # Calculate memory difference
            top_stats = snapshot2.compare_to(snapshot1, 'lineno')
            total_memory_diff = sum(stat.size_diff for stat in top_stats)
            
            # Stop tracing
            tracemalloc.stop()
            
            # Verify processing completed
            assert len(all_items) == len(large_dataset)
            
            # Memory usage should be reasonable (less than 50MB for 1000 items)
            memory_mb = total_memory_diff / (1024 * 1024)
            assert memory_mb < 50, f"Memory usage {memory_mb:.1f}MB too high for {len(large_dataset)} items"

    def test_concurrent_operation_performance(self, client):
        """Test performance of concurrent-like operations."""
        # Simulate multiple rapid API calls
        response_data = APIResponseMocker.paginated_response(
            items=[{"id": 1, "name": "Test", "item_type": "Constituent"}],
            total=1,
            page=1,
            per_page=10
        )
        
        with patch.object(client.categories._client, '_get', return_value=response_data):
            start_time = time.time()
            
            # Perform multiple operations rapidly
            results = []
            for i in range(100):  # 100 rapid operations
                items = client.categories.list(limit=10)
                results.append(items)
            
            end_time = time.time()
            total_time = end_time - start_time
            
            # Verify all operations completed
            assert len(results) == 100
            assert all(len(result) == 1 for result in results)
            
            # Performance should be reasonable
            ops_per_second = 100 / total_time
            assert ops_per_second > 50, f"Operations per second {ops_per_second:.1f} too low"

    def test_parameter_validation_performance(self, client):
        """Test parameter validation performance with complex parameters."""
        # Generate complex parameter sets
        complex_params = [
            {
                f"param_{i}_{j}": f"value_{i}_{j}"
                for j in range(10)
            }
            for i in range(50)
        ]
        
        start_time = time.time()
        
        validated_params = []
        for params in complex_params:
            validated = client.categories._client._validate_api_params(params)
            validated_params.append(validated)
        
        end_time = time.time()
        validation_time = end_time - start_time
        
        # Verify all parameters were validated
        assert len(validated_params) == 50
        
        # Validation should be fast
        validation_throughput = (50 * 10) / validation_time  # 50 param sets * 10 params each
        assert validation_throughput > 1000, f"Validation throughput {validation_throughput:.1f} params/sec too slow"

    def test_model_serialization_performance(self, large_dataset):
        """Test model serialization performance."""
        from lgl_client.models.category import Category
        
        # Create models
        categories = [Category(**item) for item in large_dataset[:100]]
        
        # Test serialization performance
        start_time = time.time()
        
        serialized_data = []
        for category in categories:
            data = category.model_dump()
            serialized_data.append(data)
        
        end_time = time.time()
        serialization_time = end_time - start_time
        
        # Verify serialization
        assert len(serialized_data) == 100
        assert all(isinstance(data, dict) for data in serialized_data)
        
        # Performance check
        serialization_throughput = 100 / serialization_time
        assert serialization_throughput > 200, f"Serialization throughput {serialization_throughput:.1f} models/sec too slow"

    def test_exception_handling_performance(self, client):
        """Test that exception handling doesn't significantly impact performance."""
        from lgl_client.lgl_api.exceptions import LGLAPIError
        
        # Test creating many exceptions
        start_time = time.time()
        
        exceptions = []
        for i in range(100):
            try:
                raise LGLAPIError(f"Test error {i}", status_code=400, url="/test")
            except LGLAPIError as e:
                exceptions.append(e)
        
        end_time = time.time()
        exception_time = end_time - start_time
        
        # Verify exceptions were created
        assert len(exceptions) == 100
        
        # Exception handling should be efficient
        exception_throughput = 100 / exception_time
        assert exception_throughput > 500, f"Exception handling throughput {exception_throughput:.1f} exceptions/sec too slow"

    def test_debug_output_performance(self, debug_client=None):
        """Test that debug output doesn't significantly slow down operations."""
        if debug_client is None:
            from lgl_client.lgl_api.client import LGLClient
            debug_client = LGLClient(api_key="test_key", debug=True)
        
        response_data = APIResponseMocker.paginated_response(
            items=[{"id": 1, "name": "Test", "item_type": "Constituent"}],
            total=1,
            page=1,
            per_page=10
        )
        
        with patch.object(debug_client, '_client') as mock_httpx:
            mock_response = type('MockResponse', (), {
                'status_code': 200,
                'is_success': True,
                'json': lambda self: response_data,
                'raise_for_status': lambda self: None
            })()
            mock_httpx.get.return_value = mock_response
            mock_httpx.headers = {"Authorization": "Bearer test_key"}
            
            # Test with debug mode
            start_time = time.time()
            for i in range(20):  # Fewer iterations due to debug output
                debug_client._get("test", param=f"value_{i}")
            debug_time = time.time() - start_time
            
            # Debug mode should still be reasonably fast
            debug_throughput = 20 / debug_time
            assert debug_throughput > 10, f"Debug mode throughput {debug_throughput:.1f} ops/sec too slow"

    @pytest.mark.slow
    def test_large_scale_pagination(self, client):
        """Test pagination performance with very large datasets."""
        # Simulate a very large dataset (10,000 items)
        def mock_get_side_effect(*args, **kwargs):
            offset = kwargs.get('offset', 0)
            limit = kwargs.get('limit', 100)
            
            # Generate items for this page
            start_id = offset + 1
            end_id = min(offset + limit, 10000)
            items = [
                {"id": i, "name": f"Item {i}", "item_type": "Constituent"}
                for i in range(start_id, end_id + 1)
            ]
            
            return APIResponseMocker.paginated_response(
                items=items,
                total=10000,
                page=(offset // limit) + 1,
                per_page=limit
            )
        
        with patch.object(client.categories._client, '_get', side_effect=mock_get_side_effect):
            start_time = time.time()
            all_items = client.categories.fetch_all()
            end_time = time.time()
            
            pagination_time = end_time - start_time
            
            # Should handle 10,000 items efficiently
            assert len(all_items) == 10000
            assert pagination_time < 10.0, f"Large pagination took {pagination_time:.3f}s for 10,000 items"
            
            # Check throughput
            throughput = 10000 / pagination_time
            assert throughput > 1000, f"Large dataset throughput {throughput:.1f} items/sec too low"