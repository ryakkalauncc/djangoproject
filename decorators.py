
path, resolved_login_url,redirect_field_name)
return _wrapped_view
return decorator
def login_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME,):
    """"
    Decorator for views that checks that the user is logged in, redirecting
    to the log-in page if necessary.
    """
    actual_decorator = user_passes_test(
        lambda u: u.is_authenticated,
        login_url=reverse_lazy('login'),
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator

def permission_required(perm, login_url=None, redirect_field_name=REDIRECT_FIELD_NAME):
    actual_decorator = user_passes_test(
        lambda u: u.has_perm(perm),
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    return actual_decorator