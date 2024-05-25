
from django.http import JsonResponse
from .models import Source
from .serializers import SourceSerialiser
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.core.management import call_command
from django.utils.decorators import method_decorator
from registereduser.decorator import login_required

@csrf_exempt
# @login_required
def source(request):
    return render(request, 'source/index.html')

@csrf_exempt
# @login_required
@api_view(['GET', 'POST'])
def source_list(request):
    if 'logged_in_user' not in request.session:
        return JsonResponse({'status': 'error', 'message': 'User not logged in'}, status=401)
    user_id = request.session['logged_in_user']
    if request.method == 'GET':
        sources = Source.objects.filter(source_user_id=user_id)
        serializer = SourceSerialiser(sources, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        request.data['source_user'] = user_id  # Assign the logged-in user to the source
        serializer = SourceSerialiser(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    

@csrf_exempt
# @login_required
@api_view(['GET', 'PUT', 'DELETE'])
def source_detail(request, pk):
    if 'logged_in_user' not in request.session:
        return JsonResponse({'status': 'error', 'message': 'User not logged in'}, status=401)

    user_id = request.session['logged_in_user']
    source = get_object_or_404(Source, pk=pk, source_user_id=user_id)

    if request.method == 'GET':
        serializer = SourceSerialiser(source)
        return JsonResponse(serializer.data)
    
    elif request.method == 'PUT':
        serializer = SourceSerialiser(source, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        source.delete()
        return JsonResponse({'message': 'Source deleted successfully'}, status=204)
    
    

@method_decorator(csrf_exempt, name='dispatch')
class FetchStoriesView(View):

    def post(self, request, source_id):
        try:
            call_command('fetch_stories', source_id)
            return JsonResponse({'status': 'success'}, status=200)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)


@api_view(['GET'])
def search_sources(request):
    query = request.GET.get('q', '')
    sources = Source.objects.filter(source_name__icontains=query) | Source.objects.filter(source_url__icontains=query)
    source_list = list(sources.values('id', 'source_user_id', 'source_name', 'source_url', 'story_count', 'tags'))
    return JsonResponse(source_list, safe=False)


@api_view(['GET'])
def filter_sources_by_tag(request):
    tag = request.GET.get('tag', '')
    sources = Source.objects.filter(tags__icontains=tag)
    source_list = list(sources.values('id', 'source_user_id', 'source_name', 'source_url', 'story_count', 'tags'))
    return JsonResponse(source_list, safe=False)


 


# @csrf_exempt
# @api_view(['GET', 'POST'])
# def source(request):
#     if request.method == 'GET':
#         sources = Source.objects.all()
#         serializer = SourceSerialiser(sources, many=True)
#         return JsonResponse(serializer.data, safe=False)
    
#     elif request.method == 'POST':
#         serializer = SourceSerialiser(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)

