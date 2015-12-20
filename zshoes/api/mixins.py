from django.http import Http404

from rest_framework.response import Response
from rest_framework import status


class CustomListRendererMixin(object):
    def get(self, format=None, *args, **kwargs):
        error_response = {
            "error_msg": "",
            "error_code": "",
            "success": False,
        }
        try:
            objects = self.get_queryset()
        except Http404, e:
            error_response['error_msg'] = e.message
            error_response['error_code'] = status.HTTP_404_NOT_FOUND
            return Response(
                error_response, status=error_response['error_code'])
        except ValueError, e:
            error_response['error_msg'] = e.message
            error_response['error_code'] = status.HTTP_400_BAD_REQUEST
            return Response(
                error_response, status=error_response['error_code'])

        serializer = self.serializer_class(objects, many=True)
        model = objects.model
        response = {
            str(model._meta.verbose_name_plural): serializer.data,
            'total_elements': objects.count(),
            'success': True,
        }
        return Response(response, status=status.HTTP_200_OK)
