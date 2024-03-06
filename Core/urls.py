
from django.contrib import admin
from django.urls import path, include
# from django.conf import settings
# from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
# from App_Survey import views
# app_name = 'App_Survey'
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',include("App_Survey.urls")),
    path('surveys/', include('djf_surveys.urls'))
    # path('survey/<int:survey_id>/', views.survey_form, name='survey_form'),
]

# urlpatterns += staticfiles_urlpatterns()
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

