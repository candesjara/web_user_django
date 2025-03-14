from playwright.sync_api import sync_playwright

def test_crear_registro():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Cambia a True para ocultar el navegador
        page = browser.new_page()

        # Reemplaza con la URL de tu app Django
        page.goto("http://127.0.0.1:8000/crud/nuevo/")

        # Llenar el formulario
        page.fill('input[name="nombre"]', "Juan Pérez")
        page.fill('input[name="direccion"]', "Calle 123")
        page.fill('input[name="telefono"]', "123456789")
        page.fill('input[name="correo"]', "juanperez@gmail.com")
        page.select_option('select[name="genero"]', "M")
        page.fill('input[name="edad"]', "30")

        # Enviar formulario
        page.click('button[type="submit"]')
        page.wait_for_timeout(2000)  # Espera 2 segundos
        print(page.content())  # Imprimir el HTML de la página después de enviar el formulario

       

        assert page.text_content("body").find("Juan Pérez") != -1

        browser.close()
