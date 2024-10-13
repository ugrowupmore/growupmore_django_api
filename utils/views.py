# utils/views.py

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

class SoftDeleteViewSet(viewsets.ModelViewSet):
    """Base viewset to handle soft delete and restore functionality."""
    lookup_field = 'slug'  # Ensure the lookup is by slug instead of pk

    def get_queryset(self):
        """Override get_queryset to return the appropriate records, including soft-deleted ones if needed."""
        queryset = super().get_queryset()

        # Check if 'is_deleted' filter is present in the query params
        is_deleted = self.request.query_params.get('is_deleted', None)

        if is_deleted == 'true':
            # Include soft-deleted records
            return self.queryset.model.all_objects.filter(is_deleted=True)
        elif is_deleted == 'false':
            # Exclude soft-deleted records (default behavior)
            return self.queryset.model.objects.filter(is_deleted=False)

        # Return all non-deleted records by default
        return self.queryset.model.objects.all()

    def destroy(self, request, *args, **kwargs):
        """Override destroy method to perform a soft delete."""
        instance = self.get_object()
        instance.delete()  # Soft delete by setting is_deleted=True
        return Response({'message': 'Record soft deleted successfully'}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def restore(self, request, *args, **kwargs):
        """Custom action to restore a soft-deleted object."""
        # Use the appropriate lookup field (slug or pk)
        lookup_value = self.kwargs.get(self.lookup_field)

        # Include soft-deleted records
        instance = self.queryset.model.all_objects.filter(**{self.lookup_field: lookup_value}).first()

        if instance is None:
            return Response({'status': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

        if instance.is_deleted:
            instance.restore()
            return Response({'status': 'Restored successfully'}, status=status.HTTP_200_OK)

        return Response({'status': 'Not deleted'}, status=status.HTTP_400_BAD_REQUEST)
