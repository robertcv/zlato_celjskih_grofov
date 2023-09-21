import json

from bs4 import BeautifulSoup
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.network.urlrequest import UrlRequest

URL = "https://www.nalozbenozlato.com/si/api/get_gold_price"


def parse_table(table_html: str) -> list:
    data = []

    soup = BeautifulSoup(table_html, features="html.parser")
    for table in soup.find_all('table'):
        table_body = table.find('tbody')
        for row in table_body.find_all('tr'):
            gold_brand, size, _, price = row.find_all('td')

            # extract
            gold_brand = gold_brand.find('p', attrs={'class': 'gold'}).string
            for s, p in zip(size.find_all('p'), price.find_all('p')):
                data.append(
                    (
                        gold_brand + " " + s.string.strip(),
                        float(p.string.strip().replace(".", "").replace(" €", "").replace(",", "."))
                    )
                )

    return data


class ZlatoCeljskihGrofovApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', spacing=10)

        self.label = Label(text='Data will be displayed here', font_size=20,  size_hint=(1, .9))
        self.layout.add_widget(self.label)

        self.refresh_btn = Button(text='Refresh', font_size=14,  size_hint=(1, .1), on_press=self.refresh_data)
        self.layout.add_widget(self.refresh_btn)
        return self.layout

    def refresh_data(self, instance):
        # Make an HTTP GET request to the API
        UrlRequest(URL, on_success=self.on_success, on_error=self.on_error)

    def on_start(self):
        self.refresh_data(None)

    def on_success(self, urlrequest, result):
        # Handle the API response here
        data = json.loads(result)
        tab = '\n'.join(map(str, parse_table(data['cenik'])))
        self.label.text = f"""
        {data['datum']}
        {tab}
        """

    def on_error(self, urlrequest, error):
        # Handle any errors that occur during the API request
        self.label.text = f"Error: {error}"


if __name__ == '__main__':
    ZlatoCeljskihGrofovApp().run()
