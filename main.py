import io
import qrcode
from kivy.app import App
from kivy.core.image import Image as CoreImage
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class QRLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", padding=20, spacing=10, **kwargs)

        self.add_widget(Label(
            text="Вставь свою ссылку:",
            font_size="18sp",
            size_hint_y=None,
            height=40,
        ))

        self.entry = TextInput(
            multiline=False,
            font_size="16sp",
            size_hint_y=None,
            height=50,
        )
        self.entry.bind(on_text_validate=self.show_qr)  # Enter тоже работает
        self.add_widget(self.entry)

        self.add_widget(Button(
            text="Сделать QR",
            font_size="16sp",
            size_hint_y=None,
            height=50,
            on_release=self.show_qr,
        ))

        self.qr_image = Image(allow_stretch=True, keep_ratio=True)
        self.add_widget(self.qr_image)

    def show_qr(self, *args):
        link = self.entry.text.strip()
        if not link:
            return

        img = qrcode.make(link).convert("RGB")
        buf = io.BytesIO()
        img.save(buf, format="PNG")
        buf.seek(0)

        self.qr_image.texture = CoreImage(buf, ext="png").texture


class QRApp(App):
    title = "QR-генератор"

    def build(self):
        return QRLayout()


if __name__ == "__main__":
    QRApp().run()