from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class PaginacionEstandar(PageNumberPagination):
    # Este atributo modificará el tamaño de elementos que retornaremos por página
    page_size = 5
    # Este es el query_param que se usará para poder indicar la cantidad de elementos que se mostrarán, pero tiene que ser menor que el max_page_size por que si es mayor, usará el max_page_size y si no es proveído se usará el page_size
    page_size_query_param = "cantidad"
    # Es el límite que podemos retornar de elementos por página
    max_page_size = 10
    # Es el query param que se usará para poder seleccionar una página que queremos navegarñ
    page_query_param = "pagina"

    # Este mensaje se mostrará cuando ingresemos a una página que no es correcta
    invalid_page_message = "Página inválida"

    def get_paginated_response(self, data):
        # El parámetro data contendrá toda la información a paginar
        return Response(data={
            "content": data,
            "paginacion": {
                "total": self.page.paginator.count, # Total de elementos que hay en la búsqueda
                "pagina_actual": self.page.number, # La página en la que me encuentro
                "total_paginas": self.page.paginator.num_pages, # Total de página que puede naveagar
                "siguiente": self.get_next_link(), # la url de la página siguiente (si hay)
                "anterior": self.get_previous_link() # la url de la página anterior (si hay)
            }
        })