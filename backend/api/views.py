# from django.http import JsonResponse, HttpResponse
from products.models import Product
from django.forms.models import model_to_dict
import json
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import ProductSerializer


@api_view(["POST"])
def api_home(request, *args, **kwargs):
    
    '''
    Django rest framework API VIEW
    '''
    
    # if request.method != "POST":
    #     return Response({"message": "get method is not allowed"}, status=405)
    
    instance = Product.objects.all().order_by("?").first()
    
    data = {}
    
    if instance:
        data = ProductSerializer(instance).data
    # if instance:
    #     data = model_to_dict(instance, fields=['id', "title","price", "sale_price"])
        
    return Response(data)
    
    




# def api_home(request , *args, **kwargs):
    
    
#     model_data = Product.objects.all().order_by("?").first()
#     data ={}
#     if model_data:
        
#         data = model_to_dict(model_data, fields =['id','title'])
        
        
#     return HttpResponse(data, headers= {"content-type": "application/json"})
#         # data['id'] =model_data.id
#         # data['title'] = model_data.title
#         # data['content'] = model_data.content
#         # data['price'] = model_data.price
#         # serializtion--->
#         # model instance(model_data)
#         # turn a python dict
#         # return json
    
#     # -----> Study purpose
#     # # request -> HttpRequest -> Django
#     # # print(dir(request))
#     # # request.body
#     # # print(request.GET) # this always gives the url query parameters
#     # body= request.body #byte string of JSON Data
#     # # print(body)
    
#     # data ={}
#     # try:
#     #     data = json.loads(body) # string of JSON data -> python dict
        
#     # except:
#     #     pass
#     # data['params'] =dict(request.GET)
#     # data['headers']= dict(request.headers)
#     # # print(request.headers)
#     # data['content_type'] = request.content_type
    
#     # print(data)
#     return JsonResponse(data)