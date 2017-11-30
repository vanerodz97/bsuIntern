import textwrap
"""Imports the textwrap method"""

from django.http import HttpResponse
from django.views.generic import View


class HomePageView(View):
    """Class that represents visuals of the hello world app."""

    def dispatch(request, *args, **kwargs):
        """Return the visual representation of greetings."""
        response_text = textwrap.dedent('''\
            <html>
            <head>
                <title>Hello Everyone</title>
            </head>
            <body>
                <h1>Greetings</h1>
                <p>Hello, world!</p>
            </body>
            </html>
        ''')
        return HttpResponse(response_text)
