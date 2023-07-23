from django.db import models

from cinemaccs_project.models import Brand, DescriptionElement


class Theater(models.Model):
    class Meta:
        ordering = ["zipcode"]

    brand = models.ForeignKey(
        Brand, related_name='theaters', null=True, on_delete=models.CASCADE
    )

    internal_id = models.CharField(max_length=10, null=True)
    name = models.CharField(max_length=300, null=True)
    complex_slug = models.CharField(max_length=100, null=True)
    cinema_national_id = models.IntegerField(null=True)
    address_1 = models.CharField(max_length=300, null=True)
    address_2 = models.CharField(max_length=300, null=True)
    city = models.CharField(max_length=100, null=True)
    zipcode = models.IntegerField(null=True)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    parking_info = models.CharField(max_length=300, null=True)
    is_gift_store = models.BooleanField(null=True)
    public_transport = models.CharField(max_length=300, null=True)
    currency_code = models.CharField(max_length=100, null=True)
    allow_print_at_home_bookings = models.BooleanField(null=True)
    allow_on_line_voucher_validation = models.BooleanField(null=True)
    display_sofa_seats = models.BooleanField(null=True)
    time_zone_id = models.CharField(max_length=100, null=True)

    accessibility_description = models.CharField(max_length=1000, null=True)
    entry_description = models.CharField(max_length=1000, null=True)
    sanitary_description = models.CharField(max_length=1000, null=True)
    popcorn_description = models.CharField(max_length=1000, null=True)
    description = models.CharField(max_length=1000, null=True)
    description_elements = models.ManyToManyField(
        DescriptionElement, blank=True
    )

    created_date = models.DateTimeField(auto_now_add=True, null=True)
    modified_date = models.DateTimeField(auto_now=True, null=True)

    # theater_picture_set
    # pictures

    # room_set
    # rooms

    @property
    def full_name(self):
        return " - ".join([
            self.company_name if self.company_name is not None else "",
            self.name if self.name is not None else "",
        ])

    @property
    def address(self):
        return self.address_1

    @property
    def description_elements_kwargs(self):
        # Suppose a prefetch
        return {e.id: e.text for e in self.description_elements.all()}

    @property
    def accessibility_description(self):
        return (
            self.description if self.description else ''
            + '\n'
            + ' '.join(
                [v for _, v in self.description_elements_kwargs.items()]
            )
        )
