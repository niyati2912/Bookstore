from django.http import JsonResponse
from .models import Book, Order
from django.views.decorators.csrf import csrf_exempt
import json

def book_list(request):
    books = Book.objects.all().values()
    return JsonResponse(list(books), safe=False)

@csrf_exempt
def place_order(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        book_id = data.get('book_id')
        quantity = data.get('quantity', 1)

        try:
            book = Book.objects.get(id=book_id)
            if book.stock >= quantity:
                book.stock -= quantity
                book.save()
                order = Order.objects.create(book=book, quantity=quantity)
                return JsonResponse({'message': 'Order placed successfully!', 'order_id': order.id})
            else:
                return JsonResponse({'error': 'Not enough stock!'}, status=400)
        except Book.DoesNotExist:
            return JsonResponse({'error': 'Book not found!'}, status=404)

    return JsonResponse({'error': 'Invalid request method!'}, status=405)
