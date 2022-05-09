from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.shortcuts import render

from app.forms import UserForm
from . models import User

# get all user
def index(request):
    obj = User.objects.all()
    context = {}
    users = []

    for user in obj:
        users.append({
            'id' : user.id,
            'name' : user.Name,
            'email' : user.Email,
            'phone' : user.Phone,
            'ville' : user.City
            })
        context['len-users'] = len(obj)
        context["users"]=users
    return JsonResponse(context)


# create new user
def post(request):
    if request.method=="POST":
        form = UserForm(request.POST)
        if form.is_valid():
            name = request.POST.get("Name")
            form.save()
            print(request.POST.get('Name'))
            return HttpResponse(f"""OK, User "{name}" is Created !""")
        else:
            return HttpResponse("Form not valid. try again")
    else:
        form = UserForm
        return render(request, 'app/post.html', {'form':form})

# edit user
def edit(request, id):
    user = User.objects.get(id=id)
    if request.method=="POST":
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return HttpResponse("User is updated !")
        else:
            return HttpResponse("Form is invalid")


# get user by id
def show(request, id):
    json = {}
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        return HttpResponse("Cet utilisateur n'existe pas")
    else:
        json['id'] = user.id
        json['name'] = user.Name
        json['email'] = user.Email
        json['phone'] = user.Phone
        json['ville'] = user.City
        return JsonResponse(json)


# delete user
def remove(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return HttpResponse("User deleted !")