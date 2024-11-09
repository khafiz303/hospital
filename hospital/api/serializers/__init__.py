# __init__.py в директории serializers
from .doctor import (
    DoctorListSerializer,
    DoctorRetrieveSerializer,
    DoctorCreateSerializer,
    DoctorUpdateSerializer,

)

from .service import (
    ServiceListSerializer,
    ServiceRetrieveSerializer,
    ServiceCreateSerializer,
    ServiceUpdateSerializer,
)

from .visit import (
    VisitListSerializer,
    VisitRetrieveSerializer,
    VisitCreateSerializer,
    VisitUpdateSerializer,
VisitRatingSerializer
)

from .patient import (
    PatientListSerializer,
PatientRetrieveSerializer,
PatientCreateSerializer,
PatientUpdateSerializer
)
