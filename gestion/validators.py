
from django.forms import ValidationError
import re


class letras_solo:

    
    def __call__(self, value):
        if not re.match(r'[a-zA-Z0-9]+$', value):
			
            raise ValidationError("debe ser solo letras")
        return value






