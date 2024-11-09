from datetime import datetime

from .models import Visit


def get_upcoming_visits_count():
    # return Visit.objects.filter(
    #     schedule__timestamp_start__gte = datetime.date.now()
    # ).count()

    return Visit.objects.filter(
        visit_date_time__gte=datetime.now()
    ).count()




# для полусчени другого поля не визит а скудл и они не свчзаны никак вроде