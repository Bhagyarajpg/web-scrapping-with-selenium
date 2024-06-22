# myapp/views.py
from django.http import JsonResponse
from django.views.decorators.http import require_GET
from .models import Entity
from .utils import extract_entities, clean_data

@require_GET
def save_entity(request):
    url = request.GET.get('url')
    #raw_data = extract_entities(url)
    #cleaned_data = clean_data(raw_data)
    cleaned_data = extract_entities(url)

    entity = Entity(
        url=url,
        artist_name=cleaned_data['artist_name'],
        program_name=cleaned_data['program_name'],
        artist_role=cleaned_data['artist_role'],
        date=cleaned_data['date'],
        time=cleaned_data['time'],
        auditorium=cleaned_data['auditorium']
    )
    entity.save()

    return JsonResponse({'status': 'success', 'entity_id': entity.id})

@require_GET
def get_entity(request):
    url = request.GET.get('url')
    entities = Entity.objects.filter(url=url)
    data = list(entities.values())
    return JsonResponse({'entities': data})

