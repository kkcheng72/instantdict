import justpy as jp
from webapp.about import About_page
from webapp.dictionary import Dictionary
from webapp.home import Home

jp.Route(Home.path, Home.serve)
jp.Route(About_page.path, About_page.serve)
jp.Route(Dictionary.path, Dictionary.serve)

jp.justpy(port=8001)
