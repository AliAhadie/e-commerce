from django.core.validators import RegexValidator
def validate_phone_number(value):
    validator = RegexValidator(
        regex=r'^\+989\d{9}$',
        message="Phone number must be entered in the format: '+989xxxxxxxxx'. Up to 13 characters allowed.",
    )
    validator(value)
