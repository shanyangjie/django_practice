from typing import Any
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name="index.html"

    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt["username"]='yae'
        return ctxt

class AboutView(TemplateView):
    template_name="about.html"

    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt["num_service"]=123456789
        ctxt["skills"]=[
            # "pyhotn",
            # "C++",
            # "C",
            # "Ruby",
        ]

        return ctxt