from django.shortcuts import render,redirect
from .models import Student
from .form import StudentForm
from django.http import JsonResponse
from django.http import HttpResponseRedirect

def home(request):
    form =StudentForm()
    data =Student.objects.all()
    return render(request, 'polls/loginform.html', {'form': form, 'data':data})

# from django.http import JsonResponse

def Login(request):
    if request.method == "POST":
        fm = StudentForm(request.POST)
        if fm.is_valid():
            name = request.POST['name']
            email = request.POST['email']
            password = request.POST['password']
            usr = Student(name=name, email=email, password=password)
            usr.save()
            stu = Student.objects.values()
            stusent_data = list(stu)
            return JsonResponse({'status': 'Save', 'stusent_data': stusent_data})
        else:
            return JsonResponse({'status': 'Invalid Form'})
    else:
        return JsonResponse({'status': 'Invalid Request'})

    #     fm = StudentForm()
    #     data = Student.objects.all()
    # return render(request, 'polls/loginform.html', {'form': fm, 'data':data})
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from polls.models import Student

def update(request, id):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        form = Student.objects.get(pk=id)
        form.name = name
        form.email = email
        form.password = password
        form.save()
        return JsonResponse({'status': 'Save',}, status=200)
    else:
        form = Student.objects.get(pk=id)
    return render(request, 'polls/loginform_Update.html', {'form': form})



def Delete(request,id):
   data=Student.objects.get(pk=id).delete()
   context = {
       'data': data
       }
   return  redirect('/students/',context)


# from django.shortcuts import redirect

# def Delete(request, id):
#     context = {}  # Define context variable with an empty dictionary
#     if request.method == 'POST':
#         id = request.POST.get('item')
#         data = Student.objects.get(pk=id)
#         data.delete()
#         context = {'data': data}  # Update context inside the if block
#         return JsonResponse({'status': 1})
#     return redirect('/students/', context)  # Pass context as a keyword argument

   

   





















# from django.shortcuts import render,redirect
# from .models import Student
# from django.http import HttpResponse, HttpResponseRedirect
# from .form import StudentForm
# from django.contrib import messages
# from django.contrib.auth.models import User
# from django.urls import reverse_lazy, reverse
# from django.http import JsonResponse
# # from django.contrib.auth import create_user
# # Create your views here.

# def home(request):
#     return render(request,'polls/base.html')


# def student_list_view(request):
#     students = Student.objects.all()  # Fetching all student records from the database
#     context = {'object_list': students}
#     return render(request, 'polls/table.html', context)
# def post(request):
#     if request.method == "POST":
#         name=request.POST['name']
#         email=request.POST['email']
#         password=request.POST['password']
#         Confirm=request.POST['Confirm']
#         city=request.POST['countries']
#         if(password != Confirm):
#             messages.error(request,'Password do not match')
#             return JsonResponse({
#                     'success':False,
#                     'messages': "Password do not match",
#                 })
#         else:  
#             messages.success(request,name+' Created successfully') 
#             member=Student(
#                 name=name,
#                 email=email,
#                 password=password,
#                 Confirm=Confirm,
#                 # gender=gender,
#                 city=city,
#         )
#             member.save()
#         return JsonResponse({
#                 'success':True,
#                 'messages': "User Created successfully",
#             })
#     return render(request,'polls/loginform.html')

# def Student_Login_form_Update(request, id):
#    mem=Student.objects.get(id=id)
#    return render (request, 'polls/loginform_Update.html',{'mem':mem})
# def Student_Login_form_form(request,id):
#     name=request.POST['name']
#     email=request.POST['email']
#     password=request.POST['password']
#     Confirm=request.POST['Confirm']
#     # gender=request.POST['gender']
#     city=request.POST['countries']
#     if(password != Confirm):
#         messages.error(request,'Password do not match')
#         return JsonResponse({
#                 'success':False,
#                 'messages': "Password do not match",
#                 })
#     else:  
#             # user = User.objects.create_user(password=password)
#         messages.success(request,name+' Update Created successfully')
#         member=Student.objects.get(id=id)
#         member.name=name
#         member.email=email
#         member.password=password
#         member.Confirm=Confirm

#         member.city=city
#         member.save()





# def Delete(request,id):
#    print(id)
#    object_list=Student.objects.get(pk=id).delete()
#    context = {
#        'object_list': object_list
#        }
#    return  redirect('/students',context)






