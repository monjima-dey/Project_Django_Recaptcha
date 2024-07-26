from django.urls import path
from .views import contact

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('contact/', contact, name='contact')
]
