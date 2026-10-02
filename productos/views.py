# productos/views.py
from django.http import HttpRequest, HttpResponse


def bienvenida(request: HttpRequest) -> HttpResponse:
    """Devuelve la pagina principal del sistema de inventario.

    Args:
        request: Objeto HttpRequest generado por Django.
    Returns:
        HttpResponse con HTML de bienvenida.
    """
    html = (
        "<h1>Sistema de Inventario</h1>"
        "<p>Semana 1 — Modulo II — Tecnico en Programacion</p>"
        "<p>Django 4.2 activo. Sprint 0 en curso.</p>"
    )
    return HttpResponse(html)