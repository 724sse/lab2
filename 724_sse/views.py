from django.views.generic.base import TemplateView
from .models import *
import re


def get_headers(model):
    return list(
        map(
            lambda x: re.sub('.*\.', '', str(x)),
            model._meta.fields
        )
    )


def get_content(model):
    return list(
        map(
            lambda x: [getattr(
                x,
                re.sub('.*\.', '', str(field))
            ) for field in model._meta.fields],
            model.objects.all()
        )
    )


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update(
            {
                'tables': [
                    {
                        'name': '724_sse.Ware',
                        'headers': get_headers(Ware),
                        'content': get_content(Ware)
                    },
                    {
                        'name': '724_sse.Supplier',
                        'headers': get_headers(Supplier),
                        'content': get_content(Supplier)
                    },
                    {
                        'name': '724_sse.Receiver',
                        'headers': get_headers(Receiver),
                        'content': get_content(Receiver)
                    },
                    {
                        'name': '724_sse.Supply',
                        'headers': get_headers(Supply),
                        'content': get_content(Supply)
                    },
                    {
                        'name': '724_sse.Shipment',
                        'headers': get_headers(Shipment),
                        'content': get_content(Shipment)
                    }
                ]
            }
        )
        return context
