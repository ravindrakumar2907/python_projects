from logging import Logger
from turtle import title
from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.
from django.http import HttpResponse
from django.http import HttpRequest
from django.template import loader

from books.models import Books
from books.serializers import BooksSerializer

@api_view(['GET'])
def hc(request):
    return HttpResponse('Server is running fine')

def showIndex(request):
    return render(request, "index.html", {'name': 'ravi'} )

#API's information by default get method
@api_view(['POST'])
def addBook(request):
    book_data = JSONParser().parse(request)
    book_serializer = BooksSerializer(data=book_data)
    if book_serializer.is_valid():
        add_response = {"status": "success"}
        book_serializer.save()
        return JsonResponse(book_serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(book_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def updateBook(request):
    title = ""
    if request.query_params:
        title = request.query_params.get('title')
    else:
        return JsonResponse({'message': 'invalid request check title params'})
    print("title value is " + str(title))
    #Logger.debug("title value is " + str(title), exc_info=1)
    if title:
        try:
            book_data1 = Books.objects.filter(title=title)
        except Books.DoesNotExist:
            return JsonResponse({'message': 'The book does not exist'}, status=status.HTTP_404_NOT_FOUND)
    else:
        return JsonResponse({'message': 'invalid request check title params'})
    
    book_data = JSONParser().parse(request)
    book_serializer = BooksSerializer(book_data1, data=book_data)
    if book_serializer.is_valid():
        update_response = {"status": "success", "data":book_serializer.data}
        book_serializer.save()#update
        return JsonResponse(update_response)
    return JsonResponse(book_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deleteBook(request):
    title = ""
    if request.query_params:
        title = request.query_params.get('title')
    else:
        return JsonResponse({'message': 'invalid request check title params'})
    print("title value is " + str(title))
    #Logger.debug("title value is " + str(title), exc_info=1)
    if title:
        try:
            book_data1 = Books.objects.filter(title=title)
        except Books.DoesNotExist:
            return JsonResponse({'message': 'The book does not exist'}, status=status.HTTP_404_NOT_FOUND)
    else:
        return JsonResponse({'message': 'invalid request check title params'})
    if book_data1:
        book_data1.delete()
        return JsonResponse({'message': 'Book was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def getAllBooks(request):
    books = Books.objects.all()
    if books:
        book_serializer = BooksSerializer(books, many=True)
        return JsonResponse(book_serializer.data, safe=False)
    else:
        return JsonResponse({'message': 'NO Data'})
    
@api_view(['GET'])
def getBook(request):
    title = ""
    if request.query_params:
        title = request.query_params.get('title')
    else:
        return JsonResponse({'message': 'invalid request check name params'})
    print("title value is " + str(title))
    #Logger.debug("title value is " + str(title), exc_info=1)
    #queryset = Model.objects.filter(location__distance_lte=(location, D(m=distance))).distance(location).order_by('distance')
    if title:
        try:
            book_data1 = Books.objects.filter(title=title)
            #book_data1 = Books.objects.filter(title=title).first()
            #book_data1 = Books.objects.get(title=title)
        except Exception as e:#except Books.DoesNotExist:
            return JsonResponse({'message': 'The book does not exist' + str(e)}, status=status.HTTP_404_NOT_FOUND)
    else:
        return JsonResponse({'message': 'invalid request check title params'})
    
    if book_data1:
        book_serializer = BooksSerializer(book_data1, many=True)
        return JsonResponse(book_serializer.data, safe=False)
    else:
        return JsonResponse({'message': 'No Data ' + "title: "+ str(title) + " "+ str(book_data1)})