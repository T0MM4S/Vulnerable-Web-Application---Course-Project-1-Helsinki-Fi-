from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.db import connection
from .models import Event, Registration
from .forms import RegistrationForm

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'events/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
    return render(request, 'events/login.html')

@login_required
def index(request):
    events = Event.objects.all()
    return render(request, 'events/index.html', {'events': events})

@login_required
def register_for_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # FLAW 5: A03:2021 - Injection (SQL Injection)
            # Using raw SQL with unsanitized user input
            comments = request.POST.get('comments', '')
            cursor = connection.cursor()
            query = f"INSERT INTO events_registration (event_id, user_id, comments, registered_at) VALUES ({event_id}, {request.user.id}, '{comments}', datetime('now'))"
            cursor.execute(query)
            
            # FIX 5: Use Django ORM or parameterized queries
            # registration = Registration(
            #     event=event,
            #     user=request.user,
            #     comments=form.cleaned_data['comments']
            # )
            # registration.save()
            # Source: https://docs.djangoproject.com/en/4.2/topics/security/#sql-injection-protection
            
            return redirect('participants', event_id=event_id)
    else:
        form = RegistrationForm()
    
    return render(request, 'events/register_event.html', {'event': event, 'form': form})

@login_required
def participants(request, event_id):
    # FLAW 3: A01:2021 - Broken Access Control
    # No authorization check - any logged-in user can view any event's participants
    # and potentially access sensitive information
    event = get_object_or_404(Event, pk=event_id)
    
    # FIX 3 (Part 2): Implement proper access control
    # Only allow event creator or registered participants to view the list
    # if request.user != event.created_by and not Registration.objects.filter(event=event, user=request.user).exists():
    #     return render(request, 'events/error.html', {
    #         'message': 'You do not have permission to view this participant list.'
    #     })
    # Source: https://owasp.org/Top10/A01_2021-Broken_Access_Control/
    
    # FLAW 4: A03:2021 - Injection (SQL Injection in search)
    search_query = request.GET.get('search', '')
    if search_query:
        cursor = connection.cursor()
        query = f"SELECT * FROM events_registration WHERE event_id = {event_id} AND comments LIKE '%{search_query}%'"
        cursor.execute(query)
        # This is vulnerable to SQL injection
        registrations = Registration.objects.filter(event=event)
    else:
        registrations = Registration.objects.filter(event=event)
    
    # FIX 4 (Alternative): Use ORM with proper filtering
    # if search_query:
    #     registrations = Registration.objects.filter(
    #         event=event,
    #         comments__icontains=search_query
    #     )
    # else:
    #     registrations = Registration.objects.filter(event=event)
    # Source: https://docs.djangoproject.com/en/4.2/topics/security/#sql-injection-protection
    
    return render(request, 'events/participants.html', {
        'event': event,
        'registrations': registrations
    })
