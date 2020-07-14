from django.db import models

from projects.models import Project
from util.logging import get_logger

logger = get_logger(__name__)


class DataDogConfiguration(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="data_dog_config")
    base_url = models.URLField(blank=False, null=False)
    api_key = models.CharField(max_length=100, blank=False, null=False)
