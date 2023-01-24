# QR Code Generator

Este script es una herramienta para generar códigos QR a partir de una URL o un texto. Utiliza la biblioteca qrcode y una estructura de datos dataclass para crear una clase QRCodeGenerator que permite generar códigos QR de manera sencilla.

## Uso
Para utilizar el script, se debe crear una instancia de la clase __QRCodeGenerator__ con la data y el nombre del archivo donde se guardará el código QR. Una vez creada la instancia, se puede llamar al método create() para generar el código QR.

```
from qr_code_generator import QRCodeGenerator

qr = QRCodeGenerator("https://www.example.com", "qr_code.png")
qr.create()
```

Además, se incluye un método estático from_text() que permite crear una instancia de la clase con un texto y un nombre de archivo especificados.

```
qr = QRCodeGenerator.from_text("https://www.example.com", "qr_code.png")
qr.create()
```

## Requisitos
- Python 3
- qrcode (se puede instalar mediante pip: pip install qrcode)
## Notas
- El código QR se guarda en el formato PNG, pero se puede cambiar a otro formato de imagen soportado si es necesario.
- La biblioteca qrcode permite cambiar otras opciones en el código QR como el tamaño, el borde, la versión, etc. Puedes consultar la documentación de la biblioteca para obtener más información.

## Licencia
Este script se distribuye bajo la licencia MIT.