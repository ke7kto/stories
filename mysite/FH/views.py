from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import Story, Paragraph, Person

def index(request):
    story_list = Story.objects.order_by('-pub_date')
    template = loader.get_template('FH/index.html')
    person_list = Person.objects.order_by('surname')
    context = {'story_list': story_list,
            'person_list': person_list}
    return render(request, 'FH/index.html')

def story(request, question_id):
    story = get_object_or_404(Story, pk=question_id)
    return render(request, 'FH/story.html', {'story': story})
