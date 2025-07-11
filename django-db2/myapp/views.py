# myapp/views.py
from django.shortcuts import render
from .models import Person


def person_query(request):
    # 데이터 추가 (INSERT INTO myapp_person)
    # Person.objects.create(
    #     first_name='lee',
    #     last_name='min'
    # )
    # Person.objects.create(
    #     first_name='kim',
    #     last_name='Gayeong'
    # )
    # Person.objects.create(
    #     first_name='ma',
    #     last_name='shiro'
    # )

    if request.method == 'POST':
        # POST 요청일 때만 insert
        Person.objects.create(
            first_name='lee',
            last_name='min'
        )
    
    all_persons = Person.objects.all()
    lee_persons = Person.objects.filter(first_name='lee')
    names_only = Person.objects.values('first_name', 'last_name')
    
    context = {
        'all_persons': all_persons,
        'lee_persons': lee_persons,
        'names_only': names_only,
    }
    
    return render(request, 'myapp/person_list.html', context)