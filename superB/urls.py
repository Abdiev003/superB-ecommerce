from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    path('jet/dashboard/', include('jet.dashboard.urls',
         'jet-dashboard')),  # Django JET dashboard URLS
    path('admin/', admin.site.urls),
    path('', include('core.urls', namespace='core')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('', include('product.urls', namespace='product')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = "helpers.views.handle_not_found"
