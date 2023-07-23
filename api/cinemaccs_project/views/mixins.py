from rest_framework.response import Response
from rest_framework import status


class DefaultCustomMixin:

    def get_serializer_class(self):
        return self.custom_serializer.get(
            self.action, self.default_serializer
        )


class BatchCreateMixin:
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(
            data=request.data,
            many=isinstance(request.data, list)
        )
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
            headers=headers
        )
