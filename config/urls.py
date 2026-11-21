from django.contrib import admin
from django.urls import path, include

admin.site.site_header = 'QuickMart Admin'
admin.site.site_title = 'QuickMart'
admin.site.index_title = 'Store management'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', include('store.urls')),
]
