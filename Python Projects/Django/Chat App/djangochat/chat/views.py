from django.shortcuts import render, redirect
from chat.models import Room, Message
from django.http import HttpResponse, JsonResponse

# Create your views here.
def home(request):
    return render(request, "home.html")

def room(request, room):
    username = request.GET.get("username")
    room_details = Room.objects.get(name=room)
    return render(request, "room.html", {
        "username": username,
        "room": room,
        "room_details": room_details
    })

def checkview(request):
    room = request.POST["room_name"]
    username = request.POST["username"]

    if Room.objects.filter(name=room).exists():
        return redirect("/"+room+"/?username="+username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect("/"+room+"/?username="+username)

def send(request):
    username = request.POST["username"]
    room_id = request.POST["room_id"]
    message = request.POST["message"]

    new_message = Message.objects.create(user=username, room=room_id, value=message)
    new_message.save()
    return HttpResponse("Message sent successfully")

def getMessages(request, room):
    room_details = Room.objects.get(name=room)

    messages = Message.objects.filter(room__icontains=room_details.id)
    return JsonResponse({"messages": list(messages.values())})