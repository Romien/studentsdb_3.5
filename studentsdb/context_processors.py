#from .settings import PORTAL_URL


def students_proc(request):
    base_url = "{0}://{1}".format(request.scheme,
                                     request.get_host())
    return {'PORTAL_URL': base_url}
