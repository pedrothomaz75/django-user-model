from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),

]

admin.site.site_header = 'Adm de Pedro'
admin.site.site_title = 'Adm de Pedro'
admin.site.index_title = 'Gerenciamento de post'