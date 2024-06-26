# app/middleware.py

from django.shortcuts import redirect
from django.urls import resolve

class RoleBasedAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.forbidden_urls = {
            'T': ['/curator/', '/methodist/', '/admin/'],
            'C': ['/tutor/', '/methodist/', '/admin/'],
            'M': ['/tutor/', '/curator/', '/admin/'],
            'A': []
        }

    def __call__(self, request):
        if request.session is not None:
            user_role = request.session.setdefault('user_roles', [])
            
            if user_role:
                current_url = request.path
                forbidden_urls_for_role = self.forbidden_urls.get(user_role[0], [])

                # if any(current_url.startswith(url) for url in forbidden_urls_for_role):
                #     return redirect('forbidden')

        response = self.get_response(request)
        return response
