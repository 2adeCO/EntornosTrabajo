import xml.etree.ElementTree as ET
from .models import Categoria, ObjetoColeccionable, Usuario
from django.core.files import File
from django.conf import settings
import os

def cargar_objetos_desde_xml():
    tree = ET.parse(os.path.join(settings.BASE_DIR, 'coleccionables.xml'))
    root = tree.getroot()

    for item in root.findall('objeto'):
        nombre = item.find('nombre').text
        descripcion = item.find('descripcion').text
        imagen = item.find('imagen').text
        precio = item.find('precio').text
        categoria_nombre = item.find('categoria').text
        tipo_oferta = item.find('tipo_oferta').text
        usuario_id = int(item.find('usuario_id').text)

        categoria, _ = Categoria.objects.get_or_create(nombre=categoria_nombre)
        usuario = Usuario.objects.get(id=usuario_id)

        ruta_imagen = os.path.join(settings.BASE_DIR, 'media', 'imagenes', imagen)

        with open(ruta_imagen, 'rb') as f:
            imagen_file = File(f)
            ObjetoColeccionable.objects.create(
                nombre=nombre,
                descripcion=descripcion,
                imagen=imagen_file,
                precio=precio,
                categoria=categoria,
                ofertado_por=usuario,
                tipo_oferta=tipo_oferta,
            )
