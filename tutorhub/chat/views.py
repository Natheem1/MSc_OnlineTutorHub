from django.shortcuts import render, redirect 
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django .db .models import Q
from .models import Room, Topic, ChatMessage
from .forms import RoomForm, TopicForm
from userprofile .models import StudentProfile

#All Chat Rooms 
def AllChatRooms(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    rooms = Room.objects.filter(
         Q(topic__name__icontains=q) | 
         Q(name__icontains=q) |
         Q(description__icontains=q)
         )
    
    topics = Topic.objects.all()[0:5]
    room_count = rooms.count()
    room_messages = ChatMessage.objects.filter(Q(room__topic__name__icontains=q))

    context = {'rooms': rooms, 'topics': topics, 
                'room_count': room_count, 'room_messages': room_messages}
    return render(request, 'chat/rooms.html', context)


# Student Chat Profile
def StudentChatUser(request, pk):
    user = StudentProfile.objects.get(id=pk)
    rooms = user.room_set.all()
    room_messages = user.chatmessage_set.all()  # Use the correct related name
    topics = Topic.objects.all()
    total_rooms = Room.objects.count()


    context = {'user': user, 'rooms': rooms, 'room_messages': room_messages,
                'topics': topics, 'total_rooms': total_rooms}
    return render(request, 'chat/chat-profile.html',context )




# Rooms
def room(request, pk):
    room = Room.objects.get(id=pk)
    room_messages = room.chatmessage_set.all().order_by('-created')
    participants = room.participants.all()

    if request.method == 'POST':
       message = ChatMessage.objects.create(
          user=request.user.studentprofile,
          room=room,
          body=request.POST.get('body')
        )
       room.participants.add(request.user.studentprofile)
       return redirect ('room', pk=room.id)

    context = {'room': room, 'room_messages': room_messages, 
               'participants': participants}
    return render(request, 'chat/room.html', context)

#Create Topic
@login_required(login_url='login')
def createTopic(request):
    form = TopicForm()

    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form .is_valid():
            form.save()
            messages.success(request, 'New Topic Created Successfully')
            return redirect('create-room')

    context = {'form': form}
    return render( request, 'chat/topic_form.html', context)


#Create Room 
@login_required(login_url='login')
def createRoom(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            topic = form.cleaned_data['topic'] 
            room = form.save(commit=False)
            room.host = request.user.studentprofile
            room.save()
            messages.success(request, 'Room Created Successfully')
            return redirect('all-rooms')
    else:
        form = RoomForm()
    
    topics = Topic.objects.all()
    context = {'form': form, 'topics': topics}
    return render(request, 'chat/room_form.html', context)





@login_required(login_url='login')
def updateRoom(request, pk):
     room = Room.objects.get(id=pk)
     form = RoomForm(instance=room)
     topics = Topic.objects.all()

     if request.method == 'POST':
         topic_name = request.POST.get('topic')
         topic, created = Topic.objects.get_or_create(name=topic_name)
         room.name = request.POST.get('name')
         room.topic = topic
         room.description = request.POST.get('description')
         room.save()
         return redirect('all-rooms')

     context = {'form': form, 'topics': topics, 'room': room}
     return render(request, 'chat/room_form.html', context)




@login_required(login_url='login')
def deleteRoom(request, pk):
     room = Room.objects.get(id=pk)

     if request.user.studentprofile != room.host:
          messages.error(request, 'Unauthorized Access')
          return redirect('signup')
     
     if request.method == 'POST':
          room.delete()
          return redirect('all-rooms')
     return render(request, 'chat/delete-room.html', {'obj': room})



@login_required(login_url='login')
def deleteMessage(request, pk):
     try:
          messages = int(pk)
          messages = ChatMessage.objects.get(id=pk)

          if request.user.studentprofile != messages.user:
               messages.error(request, 'Unauthorized Access')
               return redirect('signup')
     
          if request.method == 'POST':
               messages.delete()
               return redirect('all-rooms')
          return render(request, 'chat/delete-room.html', {'obj': messages})
     except ChatMessage.DoesNotExist:
        messages.error(request, 'Message not Found')
        return redirect('signup')
     except ValueError:
        messages.error(request, 'Invalid Message ID')
        return request('signup')
     

def topicsPage(request):
     q = request.GET.get('q') if request.GET.get('q') != None else ''
     topics = Topic.objects.filter(name__icontains=q)
     return render(request, 'chat/topics.html', {'topics': topics})

def activityPage(request):
     room_messages = ChatMessage.objects.all()
     return render(request, 'chat/activity.html', {'room_messages': room_messages})