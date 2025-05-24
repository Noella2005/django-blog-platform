from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def comment_list(request):
    return HttpResponse("List of comments")

def add_comment(request):
    return HttpResponse("Add a new comment")

def edit_comment(request, pk):
    return HttpResponse(f"Edit comment {pk}")

def delete_comment(request, pk):
    return HttpResponse(f"Delete comment {pk}")