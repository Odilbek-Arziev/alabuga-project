from django.db import models


class BaseModel(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False, null=True)
    updated_at = models.DateTimeField(auto_now=True, editable=False, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        abstract = True
        ordering = ('id',)


class Monarch(BaseModel):
    reign_started = models.DateField()
    country = models.CharField(max_length=255)

    class Meta:
        db_table = 'estates_monarchs'
        app_label = 'estates'


class Senior(BaseModel):
    king = models.ForeignKey(Monarch, on_delete=models.CASCADE)

    class Meta:
        db_table = 'estates_seniors'
        app_label = 'estates'


KNIGHT = 'Knight'
LANDLORD = 'Landlord'
MERCHANT = 'Merchant'

STATUS_TYPES = [
    (KNIGHT, 'Рыцарь'),
    (LANDLORD, 'Землевладелец'),
    (MERCHANT, 'Купец'),
]


class Dweller(BaseModel):
    social_status = models.CharField(max_length=255, choices=STATUS_TYPES)
    salary_per_month = models.IntegerField()
    obeys_to = models.ForeignKey(Senior, on_delete=models.CASCADE)

    class Meta:
        db_table = 'estates_dwellers'
        app_label = 'estates'


class Peasant(BaseModel):
    owner = models.ForeignKey(Dweller, on_delete=models.CASCADE)

    class Meta:
        db_table = 'estates_peasants'
        app_label = 'estates'
