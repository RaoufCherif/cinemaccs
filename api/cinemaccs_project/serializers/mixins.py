class ExtraFieldMixin:
    def get_field_names(self, declared_fields, info):
        expanded_fields = super().get_field_names(declared_fields, info)

        if getattr(self.Meta, "extra_fields", False):
            return expanded_fields + self.Meta.extra_fields
        else:
            return expanded_fields
