from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views
from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(
    title="Django Recipe API",
    description="REST API to manage cooking recipes",
    version="0.1",
)

urlpatterns = [
    path("", TemplateView.as_view(template_name="swagger-ui.html"), name="swagger-ui"),
    path("schema", schema_view, name="schema_url"),
    # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_URL, admin.site.urls),
    # User management
    path("users/", include("django_recipe.users.urls", namespace="users")),
    path("accounts/", include("allauth.urls")),
    # cooking_recipes API
    path(
        "cooking/", include("django_recipe.cooking_recipes.urls", namespace="cooking")
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
