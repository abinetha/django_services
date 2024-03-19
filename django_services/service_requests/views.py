from django.shortcuts import render, redirect
from .forms import ServiceRequestForm
from .models import ServiceRequest

def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('track_request', request_id=form.instance.pk)
    else:
        form = ServiceRequestForm()
    return render(request, 'service_requests/submit_request.html', {'form': form})

def track_request(request, request_id):
    service_request = ServiceRequest.objects.get(pk=request_id)
    return render(request, 'service_requests/track_request.html', {'service_request': service_request})
