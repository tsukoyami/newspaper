
from functools import wraps
from django.shortcuts import redirect
from django.urls import resolve

def login_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if 'logged_in_user' in request.session:
            return view_func(request, *args, **kwargs)
        else:
            resolved_view_name = resolve(request.path_info).url_name
            print("Resolved view name:", resolved_view_name)
            if resolved_view_name == 'signup':
                return view_func(request, *args, **kwargs)
            print("Redirecting to login page...")
            return redirect('login')
    return _wrapped_view
