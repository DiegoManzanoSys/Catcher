import requests

base_url = "http://localhost:8080/"

def print_response(resp):
    print(f"✅ {resp.request.method} {resp.request.url} -> {resp.status_code}")
    if resp.request.body:
        print("📦 Cuerpo enviado:")
        if isinstance(resp.request.body, bytes):
            print(resp.request.body.decode("utf-8", errors="ignore"))
        else:
            print(resp.request.body)
    if resp.request.headers.get("Cookie"):
        print(f"🍪 Cookies enviadas: {resp.request.headers.get('Cookie')}")
    print("-" * 60)

def main():
    print("🚀 Iniciando pruebas HTTP...")

    # 1. GET básico
    print("📘 [GET] Solicitud simple sin parámetros")
    r = requests.get(base_url)
    print_response(r)

    # 2. GET con parámetros (simula login por URL)
    print("🔐 [GET] Enviando usuario y contraseña por URL (user=admin, password=123456)")
    r = requests.get(base_url, params={"user": "admin", "password": "123456"})
    print_response(r)

    # 3. POST con formulario (simula login por formulario)
    print("📝 [POST] Formulario con datos sensibles: usuario=diego, clave=supersecreta123")
    form_data = {
        "usuario": "diego",
        "clave": "supersecreta123",
        "token": "abc123xyz"
    }
    r = requests.post(base_url, data=form_data)
    print_response(r)

    # 4. POST JSON (envía datos sensibles)
    print("📦 [POST] Enviando JSON con datos sensibles: email y contraseña")
    json_data = {
        "email": "diego@example.com",
        "password": "contraseña123",
        "remember": True
    }
    r = requests.post(base_url, json=json_data)
    print_response(r)

    # 5. Envío de cookies simuladas
    print("🍪 [GET] Solicitud con cookies: sessionid y csrftoken")
    cookies = {
        "sessionid": "xyz-987",
        "csrftoken": "token123abc"
    }
    r = requests.get(base_url + "perfil", cookies=cookies)
    print_response(r)

    # 6. Cabeceras personalizadas
    print("⚙️ [GET] Cabeceras personalizadas con API key y debug")
    headers = {
        "X-Api-Key": "ABCDEF123456",
        "X-Debug-Mode": "true",
        "User-Agent": "SnifferTest/1.0"
    }
    r = requests.get(base_url, headers=headers)
    print_response(r)

    # 7. PUT con formulario
    print("✏️ [PUT] Actualización de datos: nombre y email")
    r = requests.put(base_url + "usuario/actualizar", data={"nombre": "Diego", "email": "nuevo@correo.com"})
    print_response(r)

    # 8. DELETE con query string
    print("❌ [DELETE] Eliminando cuenta con id=123")
    r = requests.delete(base_url + "cuenta/eliminar?id=123")
    print_response(r)

    # 9. HEAD (solo cabeceras)
    print("📭 [HEAD] Solicitud solo para obtener cabeceras")
    r = requests.head(base_url)
    print(f"✅ HEAD -> {r.status_code}")
    print("-" * 60)

    # 10. POST con texto plano
    print("🧾 [POST] Texto plano con información oculta")
    r = requests.post(base_url, data="Este es un cuerpo de texto plano con 💀 secretos internos 💀")
    print_response(r)

    print("✅ Todas las solicitudes fueron enviadas correctamente.")

if __name__ == "__main__":
    main()
