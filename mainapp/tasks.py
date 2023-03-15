from django.shortcuts import render
from django.http import HttpResponse

from celery import shared_task


@shared_task(bind = True)
def test_func(request): 
    
    for i in range(10):
        print(i)
    
    return 'Done'
