from django.urls import path, include
from django.views.generic import RedirectView
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('chaining/', include('smart_selects.urls')),

    path('', RedirectView.as_view(pattern_name='apllicant_changelist'), name='home'),
    path('lead/', include('Leads.urls')),

]
