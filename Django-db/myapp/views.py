from django.shortcuts import render

# Create your views here.
# myapp/views.py
from django.shortcuts import render
from .models import Person

def person_query(request):
    # 데이터 조회 (SELECT * FROM myapp_person)
    all_persons = Person.objects.all()
    
    # 데이터 추가 (INSERT INTO myapp_person)
    Person.objects.create(
        first_name='lee',
        last_name='min'
    )
    
    # 필터링 예시 (WHERE 조건)
    lee_persons = Person.objects.filter(first_name='lee')
    
    # 특정 필드만 조회
    names_only = Person.objects.values('first_name', 'last_name')
    
    context = {
        'all_persons': all_persons,
        'lee_persons': lee_persons,
        'names_only': names_only,
    }
    
    return render(request, 'myapp/person_list.html', context)