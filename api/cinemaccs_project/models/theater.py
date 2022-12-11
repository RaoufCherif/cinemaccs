from django.db import models

from cinemaccs_project.models import BrandLogo, DescriptionElement


class Theater(models.Model):

    class Meta:
        ordering = ['zipcode']

    company_name = models.CharField(max_length=100, null=True)
    name = models.CharField(max_length=300, null=True)
    internal_id = models.CharField(max_length=10, null=True)
    complex_slug = models.CharField(max_length=100, null=True)
    cinema_national_id = models.IntegerField(null=True)
    address_1 = models.CharField(max_length=300, null=True)
    address_2 = models.CharField(max_length=300, null=True)
    city = models.CharField(max_length=100, null=True)
    zipcode = models.IntegerField(null=True)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    parking_info = models.CharField(max_length=300, null=True)
    is_gift_store = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=1000, null=True)
    accessibility_description = models.CharField(max_length=1000, null=True)
    entry_description = models.CharField(max_length=1000, null=True)
    sanitary_description = models.CharField(max_length=1000, null=True)
    popcorn_description = models.CharField(max_length=1000, null=True)
    public_transport = models.CharField(max_length=300, null=True)
    currency_code = models.CharField(max_length=100, null=True)
    allow_print_at_home_bookings = models.CharField(max_length=10, null=True)
    allow_on_line_voucher_validation = models.CharField(max_length=10, null=True)
    display_sofa_seats = models.CharField(max_length=10, null=True)
    time_zone_id = models.CharField(max_length=100, null=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    modified_date = models.DateTimeField(auto_now=True, null=True)
    logo = models.ForeignKey(BrandLogo, related_name='theaters', null=True, on_delete=models.CASCADE)
    description_elements = models.ManyToManyField(DescriptionElement, null=True)
    # theater_picture_set
    # pictures

    # TODO: Add description rendering
    # TODO
    # # room_set
    # # rooms

    @property
    def full_name(self):
        return ' - '.join([self.company_name, self.name])

    @property
    def address(self):
        return self.address_1

    @property
    def description_elements_kwargs(self):
        # Suppose a prefetch
        return {
            e.id: e.text for e in self.description_elements
        }

    @property
    def accessibility_description(self):
        return
