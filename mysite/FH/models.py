from django.db import models


class Story(models.Model):
    title = models.CharField(max_length=200)
    timeBegan = models.DateTimeField('story began')
    timeEnded = models.DateTimeField('story ended')


class Paragraph(models.Model):
    text = models.TextField()
    story = models.ForeignKey(Story)
    lastEdited = models.DateTimeField('last edited',auto_now=True)
    whenHappened = models.DateField('whenHappened')
    category = models.BigIntegerField()
    persons = models.ManyToManyField(Person)

class Category(models.Model):
    code = models.BigIntegerField()
    category = models.CharField('category_type',max_length=150)

class Person(models.Model):
    surname = models.CharField(max_length=255)
    givenNames = models.CharField(max_length=255)
    birthName = models.CharField(max_length=255)
    birthDate = models.DateField()
    deathDate = models.DateField()
    storyParagraphs = models.ManyToManyField(Paragraph)


