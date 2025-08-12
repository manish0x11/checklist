from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, Name
from .forms import TaskForm, TaskStatusForm
from django.utils import timezone
from django.db.models.functions import TruncDate
from datetime import date

# Create your views here.
def task_list(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task-list')

            # Get today's date
    today = date.today()

    # Split tasks into today and previous
    today_tasks = Task.objects.select_related('user').filter(created_at__date=today).order_by('-created_at')
    previous_tasks = (
        Task.objects.select_related('user').exclude(created_at__date=today)
        .annotate(date=TruncDate('created_at'))
        .order_by('-date', '-created_at')
    )

    return render(request, 'main/task_list.html', {
        'today_tasks': today_tasks,
        'previous_tasks': previous_tasks,
        'usernames': Name.objects.all(),
        'form': TaskForm()
    })


def toggle_status(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        # If checkbox is ticked, "status" will be in POST
        task.status = 'status' in request.POST
        task.completed_at = timezone.now() if task.status else None
        task.save()
    return redirect('task-list')
