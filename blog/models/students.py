from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Student(models.Model):
    GENDER_CHOICE = {
        "MN": 'Erkak',
        'WN': 'Ayol',
        'OT': 'Boshqa'
    }
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, null=True)
    birthday = models.DateField(null=True)
    phone = models.CharField(max_length=12)
    payed = models.BooleanField(default=False)
    gender = models.CharField(max_length=2, choices=GENDER_CHOICE, default='MN')
    image = models.ImageField(upload_to='student/', null=True, blank=True)
    total_points = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    passed_points = models.IntegerField(default=60, validators=[MinValueValidator(0), MaxValueValidator(100)])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"({self.id} {self.first_name!r} ball={self.total_points!r})"

    @property
    def fullname(self):
        return f"{self.first_name} {self.last_name}"
