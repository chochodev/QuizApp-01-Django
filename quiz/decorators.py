from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.models import Group


def allowed_users(allowed_roles):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            if request.user.groups.all():
                group = request.user.groups.all()[0].name
            else:
                group = None

            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            return HttpResponse('You are not authorised!')
        return wrapper_func
    return decorator





# class AllowedRoles:
#     def __init__(self, roles):
#         self.roles = roles

#     def __call__(self, view_class):
#         class wrapper(view_class):
#             def dispatch(self, request, *args, **kwargs):
#                 user_roles = request.user.groups.all()

#                 if any(role in self.roles for role in user_roles):
#                     return super().dispatch(request, *args, **kwargs)
#                 return HttpResponse('You are not authorised')

#         return wrapper
