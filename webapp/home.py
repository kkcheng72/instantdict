import justpy as jp
from webapp import layout
from webapp import page


class Home(page.Page):
    path = "/"

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)
        lay = layout.DefaultLayout(a=wp)
        container = jp.QPageContainer(a=lay)
        div = jp.Div(a=container, classes="bg-gray-200 h-screen")
        jp.Div(a=div, text="This is the Home page.", classes="text-4xl m-2")
        jp.Div(a=div, text="""
        In literary theory, a text is any object that can be "read",
        whether this object is a work of literature, a street sign,
        an arrangement of buildings on a city block, or styles of clothing.
        It is a coherent set of signs that transmits some kind of informative
        message.
        """, classes="text-lg")
        return wp


jp.Route(Home.path, Home.serve)
