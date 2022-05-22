from channels.auth import AuthMiddlewareStack  # AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter  # add URLRouter
import ChatApp.routing

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': AuthMiddlewareStack(
        URLRouter(
            ChatApp.routing.websocket_urlpatterns
        )
    )
})
