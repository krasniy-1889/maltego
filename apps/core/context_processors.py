from django.http import HttpRequest


def url_name(request: HttpRequest):
    return {"url_name": request.resolver_match.url_name}  # type: ignore
