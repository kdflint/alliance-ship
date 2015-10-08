from django.shortcuts import _get_queryset
from django.core.exceptions import MultipleObjectsReturned
from django.db.models.Model import DoesNotExist


def get_object_or_none(klass, **kwargs):
    """
    This function safely returns an object without throwing exceptions for
    DoesNotExist or MultipleObjectsReturned. It is should be used in the view.
    """
    try:
        return _get_queryset(klass).get(**kwargs)
    except (DoesNotExist, MultipleObjectsReturned):
        return None
