import {
  obtenerCategorias,
  crearCategoria,
  obtenerProductos,
  eliminarProducto,
  generarUrlSubida,
  subirArchivoAS3,
  crearMedia,
  crearProducto,
} from "./api.js";

const EXT_A_CONTENT_TYPE = {
  png: "image/png",
  jpg: "image/jpeg",
  jpeg: "image/jpeg",
};
const TAMANO_MIN_BYTES = 5 * 1024;
const TAMANO_MAX_BYTES = 10 * 1024 * 1024;
const CARPETA_SUBIDA = "productos/";

const form = document.getElementById("form-producto");
const selectCategoria = document.getElementById("categoria");
const selectFiltroCategoria = document.getElementById("filtro-categoria");
const inputNuevaCategoria = document.getElementById("nueva-categoria-nombre");
const btnCrearCategoria = document.getElementById("btn-crear-categoria");
const inputImagen = document.getElementById("imagen");
const previewImagen = document.getElementById("preview-imagen");
const mensajeFormulario = document.getElementById("mensaje-formulario");
const mensajeLista = document.getElementById("mensaje-lista");
const listaProductos = document.getElementById("lista-productos");
const btnGuardar = document.getElementById("btn-guardar");
const btnRecargar = document.getElementById("btn-recargar");
const btnFiltrar = document.getElementById("btn-filtrar");
const inputFiltroNombre = document.getElementById("filtro-nombre");

let categorias = [];

function mostrarMensaje(elemento, texto, tipo) {
  elemento.textContent = texto;
  elemento.classList.remove("error", "exito");
  if (tipo) elemento.classList.add(tipo);
}

function pintarSelectsCategorias() {
  const opciones = categorias
    .map((c) => `<option value="${c.id}">${c.nombre}</option>`)
    .join("");

  selectCategoria.innerHTML =
    `<option value="" disabled selected>Selecciona una categoría</option>` + opciones;
  selectFiltroCategoria.innerHTML = `<option value="">Todas las categorías</option>` + opciones;
}

async function cargarCategorias() {
  categorias = await obtenerCategorias();
  pintarSelectsCategorias();
}

function nombreCategoria(id) {
  const categoria = categorias.find((c) => c.id === id);
  return categoria ? categoria.nombre : "Sin categoría";
}

function pintarProductos(productos) {
  if (!productos.length) {
    listaProductos.innerHTML = "";
    mostrarMensaje(mensajeLista, "No hay productos para mostrar.", "");
    return;
  }

  mostrarMensaje(mensajeLista, "", "");
  listaProductos.innerHTML = productos
    .map((producto) => {
      const imagen = producto.url
        ? `<img src="${producto.url}" alt="${producto.nombre}" />`
        : `<div class="sin-imagen">Sin imagen</div>`;

      const badgeClase = producto.disponible ? "badge" : "badge no-disponible";
      const badgeTexto = producto.disponible ? "Disponible" : "No disponible";

      return `
        <article class="producto-card" data-id="${producto.id}">
          ${imagen}
          <div class="info">
            <h3>${producto.nombre}</h3>
            <span>${nombreCategoria(producto.categoria)}</span>
            <span class="${badgeClase}">${badgeTexto}</span>
            <div class="acciones">
              <button type="button" class="btn-eliminar" data-id="${producto.id}">Eliminar</button>
            </div>
          </div>
        </article>`;
    })
    .join("");
}

async function cargarProductos(filtros = {}) {
  mostrarMensaje(mensajeLista, "Cargando productos...", "");
  try {
    const productos = await obtenerProductos(filtros);
    pintarProductos(productos);
  } catch (error) {
    mostrarMensaje(mensajeLista, error.message, "error");
  }
}

function validarArchivo(archivo) {
  const ext = archivo.name.split(".").pop().toLowerCase();
  const contentTypeEsperado = EXT_A_CONTENT_TYPE[ext];

  if (!contentTypeEsperado || contentTypeEsperado !== archivo.type) {
    throw new Error("La imagen debe ser PNG o JPG/JPEG.");
  }
  if (archivo.size < TAMANO_MIN_BYTES || archivo.size > TAMANO_MAX_BYTES) {
    throw new Error("La imagen debe pesar entre 5KB y 10MB.");
  }
  return { ext, contentType: contentTypeEsperado };
}

async function subirImagenYCrearMedia(archivo) {
  const { ext, contentType } = validarArchivo(archivo);
  const nombreSinExtension = archivo.name.replace(/\.[^.]+$/, "") || "foto";

  const datosSubida = await generarUrlSubida({
    fileName: nombreSinExtension,
    ext,
    contentType,
    size: archivo.size,
    folder: CARPETA_SUBIDA,
  });

  await subirArchivoAS3(datosSubida.url, archivo, contentType);

  const media = await crearMedia({
    nombre: datosSubida.nombre,
    ext: datosSubida.ext,
    ruta: datosSubida.ruta,
    mimeType: datosSubida.mimeType,
  });

  return media.id;
}

inputImagen.addEventListener("change", () => {
  const archivo = inputImagen.files[0];
  if (!archivo) {
    previewImagen.hidden = true;
    return;
  }
  previewImagen.src = URL.createObjectURL(archivo);
  previewImagen.hidden = false;
});

btnCrearCategoria.addEventListener("click", async () => {
  const nombre = inputNuevaCategoria.value.trim();
  if (!nombre) {
    mostrarMensaje(mensajeFormulario, "Escribe un nombre de categoría.", "error");
    return;
  }

  try {
    btnCrearCategoria.disabled = true;
    const categoria = await crearCategoria(nombre);
    await cargarCategorias();
    selectCategoria.value = categoria.id;
    inputNuevaCategoria.value = "";
    mostrarMensaje(mensajeFormulario, `Categoría "${categoria.nombre}" creada.`, "exito");
  } catch (error) {
    mostrarMensaje(mensajeFormulario, error.message, "error");
  } finally {
    btnCrearCategoria.disabled = false;
  }
});

form.addEventListener("submit", async (evento) => {
  evento.preventDefault();
  mostrarMensaje(mensajeFormulario, "", "");

  const nombre = document.getElementById("nombre").value.trim();
  const categoria = selectCategoria.value;
  const disponible = document.getElementById("disponible").checked;
  const archivo = inputImagen.files[0];

  if (!categoria) {
    mostrarMensaje(mensajeFormulario, "Selecciona una categoría.", "error");
    return;
  }

  btnGuardar.disabled = true;
  try {
    let mediaId = null;

    if (archivo) {
      mostrarMensaje(mensajeFormulario, "Subiendo imagen...", "");
      mediaId = await subirImagenYCrearMedia(archivo);
    }

    mostrarMensaje(mensajeFormulario, "Creando producto...", "");
    await crearProducto({ nombre, disponible, categoria, media: mediaId });

    mostrarMensaje(mensajeFormulario, "Producto creado exitosamente.", "exito");
    form.reset();
    previewImagen.hidden = true;
    await cargarProductos();
  } catch (error) {
    mostrarMensaje(mensajeFormulario, error.message, "error");
  } finally {
    btnGuardar.disabled = false;
  }
});

listaProductos.addEventListener("click", async (evento) => {
  const boton = evento.target.closest(".btn-eliminar");
  if (!boton) return;

  const id = boton.dataset.id;
  if (!confirm("¿Eliminar este producto?")) return;

  boton.disabled = true;
  try {
    await eliminarProducto(id);
    await cargarProductos();
  } catch (error) {
    mostrarMensaje(mensajeLista, error.message, "error");
    boton.disabled = false;
  }
});

btnRecargar.addEventListener("click", () => cargarProductos());

btnFiltrar.addEventListener("click", () => {
  cargarProductos({
    nombre: inputFiltroNombre.value.trim(),
    categoria: selectFiltroCategoria.value,
  });
});

(async function iniciar() {
  try {
    await cargarCategorias();
  } catch (error) {
    mostrarMensaje(mensajeFormulario, `No se pudieron cargar categorías: ${error.message}`, "error");
  }
  await cargarProductos();
})();
