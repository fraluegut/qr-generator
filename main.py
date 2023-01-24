import qrcode
from dataclasses import dataclass

@dataclass
class QRCodeGenerator:
    """
    Initialize the QR code generator with the data and file name.

    Parameters:
    data (str): The data (text or url) to be encoded in the QR code.
    file_name (str): The name of the file where the QR code will be saved.
    """

    data: str
    file_name: str


    def create(self):
        """
        Create a QR code using the data and save it in the specified file.
        """
        # Create a QR code object with default parameters
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        # Add data to QR code object
        qr.add_data(self.data)
        # Make QR code
        qr.make(fit=True)
        # Create an image of the QR code
        img = qr.make_image(fill_color="black", back_color="white")
        # Save image to file
        img.save(self.file_name)

    @staticmethod
    def from_text(text: str, file_name: str) -> "QRCodeGenerator":
        return QRCodeGenerator(text, file_name)

# Example of usage
qr = QRCodeGenerator("https://www.example.com", "qr_code.png")
qr.create()
