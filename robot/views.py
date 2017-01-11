from django.shortcuts import render, get_object_or_404
from .models import Robot
from orders.forms import OrderForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .forms import RobotFilterForm


def robot_list(request):
    robot = Robot.objects.all()
    form =RobotFilterForm(request.GET)
    if form.is_valid():
        if form.cleaned_data["min_price"]:
            robot = robot.filter(price__gte=form.cleaned_data["min_price"])

        if form.cleaned_data["max_price"]:
            robot = robot.filter(price__lte=form.cleaned_data["max_price"])

        if form.cleaned_data["ordering"]:
            robot = robot.order_by(form.cleaned_data["ordering"])


    return render(request, "robot/robot_list.html", {"robot": robot, "form": form})


def robot_detail (request, robot_id):
    robot = get_object_or_404(Robot, id=robot_id)
    form = OrderForm(request.POST or None, initial={
        "robot": robot
    })

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("{}?sended=True".format(reverse("robot", kwargs={"robot_id": robot.id})))

    return render(request, "robot/robot_detail.html", {
        "robot": robot,
        "form": form,
        "sended": request.GET.get("sended", False)
    })