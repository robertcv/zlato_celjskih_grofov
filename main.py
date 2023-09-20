import json

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.network.urlrequest import UrlRequest

URL = "https://www.nalozbenozlato.com/si/api/get_gold_price"


class ZlatoCeljskihGrofovApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        self.label = Label(text='Data will be displayed here')
        self.layout.add_widget(self.label)
        return self.layout

    def on_start(self):
        # Make an HTTP GET request to the API
        UrlRequest(URL, on_success=self.on_success, on_error=self.on_error)

    def on_success(self, urlrequest, result):
        # Handle the API response here
        data = json.loads(result)
        self.label.text = f"""
        {data['datum']}
        zlato: {data['zlato']}
        srebro: {data['srebro']}
        """

    def on_error(self, urlrequest, error):
        # Handle any errors that occur during the API request
        self.label.text = f"Error: {error}"


if __name__ == '__main__':
    ZlatoCeljskihGrofovApp().run()
