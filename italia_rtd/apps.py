from django.apps import AppConfig


class ItaliaConfig(AppConfig):
    name = 'italia_rtd'
    verbose_name = 'Italia'

    def ready(self):
        from italia_rtd.signals import add_sphinx_context_data  # NOQA
