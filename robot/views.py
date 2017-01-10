from django.shortcuts import render, get_object_or_404
from .models import Robot
from orders.forms import OrderForm


def robot_list(request):
    robot = Robot.objects.all()
    return render(request, "robot/robot_list.html", {"robot": robot})


def robot_detail (request, robot_id):
    robot = get_object_or_404(Robot, id=robot_id)
    form = OrderForm(request.POST or None, initial={
        "robot": robot
    })

    if request.method == "POST":
        if form.is_valid():
            form.save()

    return render(request, "robot/robot_detail.html", {
        "robot": robot,
        "form": form
    })