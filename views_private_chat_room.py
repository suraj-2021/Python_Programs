from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404

@login_required
def private_chat(request, username1, username2):
    # Ensure both users exist
    user1 = get_object_or_404(User, username=username1)
    user2 = get_object_or_404(User, username=username2)

   
    room_name = get_room_name(username1, username2)

   
    messages = Message.objects.filter(room_name=room_name)

    # Render the chat room with the room name

    return render(request, 'chat/room.html', {
        'room_name': room_name,
        'messages': messages,
        'other_user': user2 if request.user == user1 else user1,
    })
