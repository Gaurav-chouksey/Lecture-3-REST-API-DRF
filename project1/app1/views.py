from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(http_method_names=['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def first_api(request):
    if request.method == "POST":
        incoming_data = request.data                    # incoming_data is variable here
        incoming_data["address"] = "shivaji nagar"      # just for inserting data inside dictionary / JSON data
        print(type(incoming_data))                      # for getting the type of data we are getting 
        if incoming_data:
            return Response(data=incoming_data)
        return Response(data={'detail': 'POST method is used to create a new resource'})
    if request.method == "PUT":
        if incoming_data:
            return Response(data=incoming_data)
        return Response(data={'detail': 'PUT Method is used to update fully data on the server'})
    if request.method == "PATCH":
        if incoming_data:
            return Response(data=incoming_data)
        return Response(data={'detail': 'PATCH method is used to partially update a resource'})
    if request.method == "DELETE":
        if incoming_data:
            return Response(data=incoming_data)
#        incoming_data = request.data        # incoming_data is variable here
#        print(incoming_data)
        return Response(data={'detail': 'DELETE method is used to delete a resource from the server'})
    return Response(data={'detail':'GET method is used to retrieve the data from resource'})     






