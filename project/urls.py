
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('authenticate', include('person_portfolio.urls')),
    path('', include('mpesa.urls'))

    
]
