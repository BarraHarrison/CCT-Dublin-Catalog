from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# view for books
class BookView(APIView):
    def get(self, request):
        return Response({"hello": "django"})

    # def post(self, request):
    #     pass

book_view = BookView.as_view()