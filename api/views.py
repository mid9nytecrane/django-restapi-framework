from django.shortcuts import render, get_object_or_404
# from django.http import JsonResponse
from students.models import Student
from rest_framework.response import Response 
from rest_framework import status 
from rest_framework.decorators import api_view
from .serializers import StudentSerializers,EmployeeSerializers
from rest_framework.views import APIView
from django.http import Http404
from employees.models import Employee
from rest_framework import mixins,generics, viewsets 

@api_view(["GET", "POST"])
def studentsView(request):
    # students = Student.objects.all()
    # print(type(students))
    # # students_list = list(students.values())
    # students_list = [student for student in students.values()]
    # print(students_list)
    # return JsonResponse(students_list, safe=False)

    if request.method == "GET":
        """Get all data from Student table"""
        students = Student.objects.all()
        serializers = StudentSerializers(students, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        serializers = StudentSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        print(serializers.errors)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(["GET", "PUT", "DELETE"])
def studentDetailView(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializers = StudentSerializers(student)
        return Response(serializers.data,status=status.HTTP_200_OK)
    
    if request.method == 'PUT':
        serializers = StudentSerializers(student, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


# class Employees(APIView):
#     def get(self, request):
#         employees = Employee.objects.all()
#         serializer = EmployeeSerializers(employees, many=True)
#         print(f"serializer content: {serializer}")
#         print(f"serializer data content: {serializer.data}")
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def post(self, request):
#         # employees = Employee.objects.all()
#         serializer = EmployeeSerializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


# class EmployeesDetail(APIView):
#     def get_object(self,pk):
#         try:
#             return Employee.objects.get(pk=pk)
#         except Employee.DoesNotExist:
#             raise Http404 
        
#     def get(self, request, pk):
#         employee = self.get_object(pk)
#         serializer = EmployeeSerializers(employee)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def put(self, request, pk):
#         employee = self.get_object(pk)
#         serializer = EmployeeSerializers(employee, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

#     def delete(self, request, pk):
#         employee = self.get_object(pk=pk)
#         employee.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    



"""

# Mixins
class Employees(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers

    def get(self, request):
        return self.list(request)
    
    def post(self,request):
        return self.create(request)


# mixins
class EmployeesDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers 

    def get(self, request, pk):
        return self.retrieve(request, pk)
    
    def put(self, request, pk):
        return self.update(request, pk)
    
    def delete(self, request, pk):
        return self.destroy(request, pk)

    
"""


"""

class Employees(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers


class EmployeesDetail(generics.RetrieveAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers 
    lookup_field = "pk"
"""


"""
# using ViewSet
class EmployeeViewset(viewsets.ViewSet):
    def list(self, request):
        queryset = Employee.objects.all()
        serialiezers = EmployeeSerializers(queryset, many=True)
        return Response(serialiezers.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        serializers = EmployeeSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors)
    
    def retrieve(self, request, pk=None):
        employee = get_object_or_404(Employee, pk=pk)
        serializer = EmployeeSerializers(employee)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def update(self, request, pk=None):
        employee = get_object_or_404(Employee, pk=pk)
        serializer = EmployeeSerializers(employee,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk=None):
        employee = get_object_or_404(Employee, pk=pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
"""


class EmployeeViewset(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers