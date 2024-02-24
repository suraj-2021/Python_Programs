from django.shortcuts import redirect  # Import the redirect function

def form_page(request):
    form = TimFerrissForm()
    if request.method == 'POST':
        form = TimFerrissForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('home')  # Return the redirect response
    else:
        print("ERROR FORM IS INVALID")
    return render(request, 'forms.html', {'form': form})
