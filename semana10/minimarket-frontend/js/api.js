// URL base del backend Django (minimarket). Ajusta si corre en otro host/puerto.
export const API_BASE_URL = "http://127.0.0.1:8000";

async function manejarRespuesta(respuesta) {
  const data = await respuesta.json().catch(() => ({}));
  if (!respuesta.ok) {
    const detalle = data.content ? ` ${JSON.stringify(data.content)}` : "";
    throw new Error((data.message || "Error en la petición") + detalle);
  }
  return data;
}

export async function obtenerCategorias() {
  const res = await fetch(`${API_BASE_URL}/categorias`);
  const data = await manejarRespuesta(res);
  return data.content;
}

export async function crearCategoria(nombre) {
  const res = await fetch(`${API_BASE_URL}/categorias`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ nombre }),
  });
  const data = await manejarRespuesta(res);
  return data.content;
}

export async function obtenerProductos({ categoria, nombre } = {}) {
  const params = new URLSearchParams();
  if (categoria) params.append("categoria", categoria);
  if (nombre) params.append("nombre", nombre);
  const query = params.toString();
  const res = await fetch(`${API_BASE_URL}/productos${query ? `?${query}` : ""}`);
  const data = await manejarRespuesta(res);
  return data.content;
}

export async function eliminarProducto(id) {
  const res = await fetch(`${API_BASE_URL}/producto/${id}`, { method: "DELETE" });
  if (!res.ok && res.status !== 204) {
    const data = await res.json().catch(() => ({}));
    throw new Error(data.message || "No se pudo eliminar el producto");
  }
}

export async function generarUrlSubida({ fileName, ext, contentType, size, folder }) {
  const res = await fetch(`${API_BASE_URL}/generar-url`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ fileName, ext, contentType, size, folder }),
  });
  const data = await manejarRespuesta(res);
  return data.content;
}

export async function subirArchivoAS3(url, archivo, contentType) {
  const res = await fetch(url, {
    method: "PUT",
    headers: { "Content-Type": contentType },
    body: archivo,
  });
  if (!res.ok) {
    throw new Error("No se pudo subir la imagen al almacenamiento (S3)");
  }
}

export async function crearMedia({ nombre, ext, ruta, mimeType }) {
  const res = await fetch(`${API_BASE_URL}/media`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ nombre, ext, ruta, mimeType }),
  });
  const data = await manejarRespuesta(res);
  return data.content;
}

export async function crearProducto({ nombre, disponible, categoria, media }) {
  const payload = { nombre, disponible, categoria };
  if (media) payload.media = media;

  const res = await fetch(`${API_BASE_URL}/productos`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  });
  const data = await manejarRespuesta(res);
  return data.content;
}
