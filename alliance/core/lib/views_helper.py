from django.shortcuts import _get_queryset
from django.core.exceptions import MultipleObjectsReturned


def get_object_or_none(klass, **kwargs):
    """
    This function safely returns an object without throwing exceptions for
    DoesNotExist or MultipleObjectsReturned. It is should be used in the view.
    """
    queryset = _get_queryset(klass)
    try:
        return queryset.get(**kwargs)
    except (queryset.model.DoesNotExist, MultipleObjectsReturned):
        return None
