from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.models import Group
from django.contrib.auth.mixins import AccessMixin

# class AllowedUsersMixin(AccessMixin):
#     def dispatch(self, request, *args, **kwargs):

#         return super().dispatch(request, *args, **kwargs)
