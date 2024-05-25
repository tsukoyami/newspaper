
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Story
from .serializers import StorySerialiser
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from registereduser.decorator import login_required

@csrf_exempt
# @login_required
def story(request):
    return render(request, 'story/index.html')

@csrf_exempt
# @login_required
@api_view(['GET', 'POST'])
def story_list(request):
    if 'logged_in_user' not in request.session:
        return JsonResponse({'status': 'error', 'message': 'User not logged in'}, status=401)
    user_id = request.session['logged_in_user']
    if request.method == 'GET':
        stories = Story.objects.filter(created_by_id=user_id)
        serializer = StorySerialiser(stories, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        request.data['created_by'] = user_id  # Assign the logged-in user to the story
        serializer = StorySerialiser(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
# @login_required
@api_view(['GET', 'PUT', 'DELETE'])
def story_detail(request, pk):
    if 'logged_in_user' not in request.session:
        return JsonResponse({'status': 'error', 'message': 'User not logged in'}, status=401)

    user_id = request.session['logged_in_user']
    story = get_object_or_404(Story, pk=pk, created_by_id=user_id)

    if request.method == 'GET':
        serializer = StorySerialiser(story)
        return JsonResponse(serializer.data)
    
    elif request.method == 'PUT':
        serializer = StorySerialiser(story, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        story.delete()
        return JsonResponse({'message': 'Story deleted successfully'}, status=204)


@api_view(['GET'])
def search_story(request):
    query = request.GET.get('q', '')
    story = Story.objects.filter(title__icontains=query) | Story.objects.filter(url__icontains=query)
    story_list = list(story.values('id', 'created_by_id', 'source_id', 'title', 'tags', 'url', 'body_text', 'published_date'))
    return JsonResponse(story_list, safe=False)


@api_view(['GET'])
def filter_story_by_tag(request):
    tag = request.GET.get('tag', '')
    story = Story.objects.filter(tags__icontains=tag)
    story_list = list(story.values('id', 'created_by_id', 'source_id', 'title', 'tags', 'url', 'body_text', 'published_date'))
    return JsonResponse(story_list, safe=False)

