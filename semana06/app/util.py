from math import ceil

def paginationInfo(total, pagina, porPagina):
    # Es la encargada de indicar cuántos elementos por página contendrá el resultado
    itemPorPagina = porPagina if total >= porPagina else total
    # Esta propiedad me indicará cuántas páginas en total puede el usuario navegar y esto se calcula en base al total entre los elementos por página redondeado
    # el método 'ceil' sirve para redondear el número flotante al siguiente número entero sin importar si es: 3.1 > 4, 3.99 > 4
    totalPaginas = ceil(total / itemPorPagina) if itemPorPagina > 0 else None
    paginaPrevia = pagina - 1 if pagina > 1 and pagina <= totalPaginas else None
    paginaSiguiente = pagina + 1 if totalPaginas > 1 and pagina < totalPaginas else None

    return {
        'porPagina': itemPorPagina,
        'total': total,
        'pagina': pagina,
        'paginaPrevia': paginaPrevia,
        'paginaSiguiente': paginaSiguiente,
        'totalPaginas': totalPaginas
    }