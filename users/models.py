from locale import currency
from django.db import models
from django.contrib.auth.models import AbstractUser
from regex import F

# Create your models here.
class User(AbstractUser):

    """Custom User Models"""

    GENDER_MALE = 'male'
    GENDER_FEMALE = 'female'

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female")
    )
    
    LANGUAGE_ENG = "english"
    LANGUAGE_KR = "korean"
    LANGUAGE_CHOIES = (
        (LANGUAGE_ENG, "English"),
        (LANGUAGE_KR, "Korean")
    )

    CURRENCY_USD = 'usd'
    CURRENCY_KRW = 'krw'
    CURRENCY_CHOIES = (
        (CURRENCY_USD, 'USD'),
        (CURRENCY_KRW, "KRW")
    )

    avatar = models.ImageField( blank=True)
    gender = models.CharField(choices = GENDER_CHOICES ,max_length=10)
    bio = models.TextField(blank=True)
    birthday = models.DateField(blank=True, null =True)
    language = models.CharField(choices=LANGUAGE_CHOIES, max_length=8, blank=True)
    currency = models.CharField(choices=CURRENCY_CHOIES, max_length=3, blank=True)
    superhost = models.BooleanField(default=False)

    