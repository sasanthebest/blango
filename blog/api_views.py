import json
from http import HTTPStatus
from blog.serializers import PostSerializer
from django.http import JsonResponse, HttpResponse, HttpResponseNotAllowed
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from blog.models import Post



@csrf_exempt
def post_list(request):
    if request.method == "GET":
        posts = Post.objects.all()
        serializer=PostSerializer(posts,many=True)
        return JsonResponse(serializer.data)
    elif request.method == "POST":
        serializer=PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        post=serializer.save()
        return HttpResponse(
            status=HTTPStatus.CREATED,
            headers={"Location": reverse("api_post_detail", args=(post.pk,))},
        )

    return HttpResponseNotAllowed(["GET", "POST"])


@csrf_exempt
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == "GET":
        serializer=PostSerializer(post)
        return JsonResponse(serializer.data)
    elif request.method == "PUT":
        serializer=PostSerializer(instance=post,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return HttpResponse(status=HTTPStatus.OK)
        return HttpResponse(status=HTTPStatus.NO_CONTENT)
    elif request.method == "DELETE":
        post.delete()
        return HttpResponse(status=HTTPStatus.NO_CONTENT)

    return HttpResponseNotAllowed(["GET", "PUT", "DELETE"])