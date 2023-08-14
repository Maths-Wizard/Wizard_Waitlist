# Validation Utils
from typing import Dict


def clean_data(data):
    """ cleans up the request data """
    clean = {
        'email': data.get('email'),
    }

    return clean
