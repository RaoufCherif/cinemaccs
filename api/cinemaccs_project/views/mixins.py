class DefaultCustomMixin:

    def get_serializer_class(self):
        return self.custom_serializer.get(
            self.action, self.default_serializer
        )
