from django.db import models

class Varna(models.Model):
    varna_name = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.varna_name

class Source(models.Model):
    source_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.source_name

class Type(models.Model):
    type_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.type_name

class Word(models.Model):
    varna = models.ForeignKey(Varna, on_delete=models.CASCADE)
    source = models.ForeignKey(Source, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    root_word = models.CharField(max_length=100)
    details = models.JSONField()  # JSONB field for label, origin, example, synonyms, etc.

    def __str__(self):
        return self.root_word