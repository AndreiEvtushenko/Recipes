from django.utils import timezone


def year(request):
    """
    Creates a variable with the current year.
    Returns a dictionary with the current year.
    """
    request = timezone.now()
    return {
        'year': request.year,
    }
