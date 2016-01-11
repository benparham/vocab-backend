from rest_framework.routers import Route, DynamicDetailRoute, SimpleRouter

class NoListRouter(SimpleRouter):
    routes = [
        Route(
            url=r'^{prefix}{trailing_slash}$',
            mapping={
                'post': 'create',
                'get': 'retrieve',
                'delete': 'destroy',
                'put': 'update',
                'patch': 'partial_update'
            },
            name='{basename}-detail',
            initkwargs={'suffix': 'Instance'}
        ),
        DynamicDetailRoute(
            url=r'^{prefix}/{methodnamehyphen}{trailing_slash}$',
            name='{basename}-{methodnamehyphen}',
            initkwargs={}
        )
    ]
