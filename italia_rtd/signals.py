import logging

from django.dispatch import receiver

from readthedocs.doc_builder.signals import finalize_sphinx_context_data
from readthedocs.restapi.client import api as apiv2

log = logging.getLogger(__name__)


@receiver(finalize_sphinx_context_data)
def add_sphinx_context_data(sender, **kwargs):
    data = kwargs.get('data')
    build_env = kwargs.get('build_env')
    subprojects = (apiv2.project(build_env.project.pk)
                   .subprojects()
                   .get()['subprojects'])
    data['subprojects'] = subprojects
