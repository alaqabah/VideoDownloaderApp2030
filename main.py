from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from pytube import YouTube

class DownloadLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)

        self.url_input = TextInput(hint_text='أدخل رابط الفيديو هنا', multiline=False)
        self.add_widget(self.url_input)

        self.download_button = Button(text='تحميل الفيديو', size_hint=(1, 0.2))
        self.download_button.bind(on_press=self.download_video)
        self.add_widget(self.download_button)

    def download_video(self, instance):
        url = self.url_input.text
        if url:
            try:
                yt = YouTube(url)
                stream = yt.streams.get_highest_resolution()
                stream.download()
                self.url_input.text = 'تم التحميل بنجاح!'
            except Exception as e:
                self.url_input.text = f'حدث خطأ: {str(e)}'

class VideoDownloaderApp2030(App):
    def build(self):
        return DownloadLayout()

if __name__ == '__main__':
    VideoDownloaderApp().run()


