@login_required
def send_message(request, recipient_id):
    recipient = get_object_or_404(User, id=recipient_id)
    
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.recipient = recipient
            message.save()
            return redirect(reverse('accountability_app:inbox'))
    else:
        form = MessageForm()
        
    return render(request, 'accountability_app/send_message.html', {'form': form, 'recipient': recipient})
