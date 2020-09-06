from django.shortcuts import render
from gestion_diccionario.models import Entradas
from django.utils.datastructures import MultiValueDictKeyError

# Create your views here.

############################
# Pagina inicial
############################
def inicio(request):

    return render(request, "inicio.html")

############################
# Buscar palabras
############################

def busqueda(request):

    pal=request.GET["palabra"]
    pal=pal.lower()
    definiciones=Entradas.objects.filter(palabra=pal)

    if definiciones:

        return render(request, "busqueda.html",{"palabra":pal, "definiciones":definiciones})

    else:
        return render(request, "busqueda.html",{"palabra":"La palabra %s no existe o no esta registrada" % (pal)})



############################
# Añadir palabras
############################

def anadirPalabra(request):

    return render(request, "templates_anadir_palabra/anadirPalabra.html")

def success_anadida(request):

    #Se comprueba que se haya seleccionado una de las opciones
    try:
        tipo_pal=request.POST["tipo_palabra"]
    except MultiValueDictKeyError:
        return render(request, "templates_anadir_palabra/fallo_anadida.html",{"mensaje":"Error no has seleccionado el tipo de palabra"})
    definicion=request.POST["definicion"]


    #Se comprueba si existe una entrada exactamente igual
    pal=request.POST["palabra"]
    pal=pal.lower()
    definiciones = Entradas.objects.filter(palabra=pal)
    existe = False
    for defi in definiciones:
        if defi.tipo_palabra == tipo_pal and defi.definiciones == definicion:
            existe = True

    if existe:
        return render(request, "templates_anadir_palabra/fallo_anadida.html",{"mensaje":"Error ya existe esa entrada"})
    else:
        #Se comprueba que los campos no esten vacios
        if pal and definicion:
            nueva_entrada=Entradas(palabra=pal,tipo_palabra=tipo_pal,definiciones=definicion)
            nueva_entrada.save()
            return render(request, "templates_anadir_palabra/success_anadida.html")
        else:
            return render(request, "templates_anadir_palabra/fallo_anadida.html",{"mensaje":"Error no has escrito la palabra o la definición"})

        

############################
# Eliminar palabras
############################

def eliminarPalabra(request):

    return render(request, "templates_eliminar_palabra/eliminarPalabra.html")

def success_eliminada(request):

    pal=request.POST["palabra"]
    pal=pal.lower()
    #Se busca si la palabra escrita existe y si existe no elimina ninguna y sale mensaje de error
    definiciones = Entradas.objects.filter(palabra=pal)

    if definiciones:
        definiciones.delete()
        return render(request, "templates_eliminar_palabra/success_eliminada.html")

    else:
        return render(request, "busqueda.html",{"palabra":"La palabra %s no existe o no esta registrada" % (pal)})



############################
# Editar palabras
############################

def editar_def_paso1(request):

    return render(request, "templates_editar_palabra/editar_def_paso1.html")


def editar_def_paso2(request):

    pal=request.GET["palabra"]
    pal=pal.lower()

    #Se busca si la palabra escrita existe si existe muestra sus definiciones sino sale mensaje de error
    definiciones = Entradas.objects.filter(palabra=pal)
    if definiciones:
        return render(request, "templates_editar_palabra/editar_def_paso2.html",{"palabra":pal,"definiciones":definiciones})
    else:
        return render(request, "busqueda.html",{"palabra":"La palabra %s no existe o no esta registrada" % (pal)})

def success_editada(request):

    #Se comprueba que se haya seleccionado una de las opciones
    try:
        id=request.POST["defi"]
    except MultiValueDictKeyError:
        return render(request, "busqueda.html",{"palabra":"No has seleccionado ninguna definición"})
    
    entrada = Entradas.objects.get(id=id)
    definicion_nueva=request.POST["mensaje"]

    #Si se he escrito una definición se cambia la nueva por la anterior 
    #sino se ha escrito nada unicamente se elimina la definición seleccionada
    
    if definicion_nueva:
        entrada.definiciones=definicion_nueva
        entrada.save()
        return render(request, "templates_editar_palabra/success_editada.html",{"mensaje":"editada"})
    else:
        entrada.delete()
        return render(request, "templates_editar_palabra/success_editada.html",{"mensaje":"eliminada"})
    