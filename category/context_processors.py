from .models import Category

def menu_links(request):
    # ESTE DICCIONARIO VA ESTAR GLOBAL, USAR UN NOMBRE UNICO
    links = Category.objects.all()
    # retornamos un diccinario
    return dict(links=links)