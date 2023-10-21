from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class BaseActionHandler(APIView):
    object = None
    model_class = None
    permissions = {}
    permission_classes = []
    action = None

    def initial(self, request, *args, **kwargs):
        self.action = kwargs.get('action', None)
        return super().initial(request, *args, **kwargs)

    def put(self, request, **kwargs):
        return self.handle(**kwargs)

    def handle(self, **kwargs):
        handler = getattr(self, 'action_{}'.format(self.action), None)
        if not handler:
            return Response("Bad action", status=status.HTTP_400_BAD_REQUEST)

        kwargs.pop('action', None)
        pk = kwargs.pop('pk', None)
        if pk and self.model_class:
            self.object = get_object_or_404(self.model_class, pk=pk)
            self.check_object_permissions(self.request, self.object)
        result = handler(**kwargs)
        if not isinstance(result, Response):
            if result is not None:
                result = Response(status=202, data=result)
            else:
                result = Response(status=202)
        return result
