from django.shortcuts import render
from myapp.tasks import add
from celery.result import AsyncResult

# Create your views here.

def index_view(request):

    # add(10, 20)
    result = add.delay(10, 20)
    # result = add.apply_async(args=[10, 30])

    #result1 = add.apply_async(args=[10, 30])
    #print("Result 1:", result1)

    #result2 = add.apply_async(args=[50, 30])
    #print("Result 2:", result2)

    context = {
        "title": "Django Celery Redis",
        "result": result
    }

    return render(request, "myapp/index.html", context=context)

def check_result_view(request, task_id):
    result = AsyncResult(task_id)

    print("Ready:", result.ready())
    print("Successful:", result.successful())
    print("Failed:", result.failed())
    print("Get:", result.get())

    context = {
        "title": "Django Celery Redis",
        "result": result
    }

    return render(request, "myapp/result.html", context)
