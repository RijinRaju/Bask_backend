"""

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os
import django
django.setup()
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application
import  Students.routing
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'broto_backend.settings')
django_asgi_app = get_asgi_application()



application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": AllowedHostsOriginValidator(
        AuthMiddlewareStack(URLRouter(Students.routing.websocket_urlpatterns))
    ),
})
 