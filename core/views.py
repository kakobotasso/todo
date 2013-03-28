from models import todo
from django.shortcuts import render_to_response

def index(request):
	items = todo.objects.all()
	return render_to_response('index.html', {'items': items})
