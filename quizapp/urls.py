from django.contrib import admin
from django.urls import path, include
import debug_toolbar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('quiz/', include('quiz.urls')),
    path('__debug__/', include(debug_toolbar.urls))
]
