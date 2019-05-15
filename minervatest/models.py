from django.db import models


class This(models.Model):
    name = models.CharField(max_length=255, null=False)

    def get_this(self):
        return self.name


class That(models.Model):
    name = models.CharField(max_length=255, null=False)

    def get_that(self):
        return self.name
