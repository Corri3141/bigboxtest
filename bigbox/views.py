from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Box, Activity
from django.views.generic import ListView, DetailView
from django.shortcuts import redirect


class BoxListView(View):
    def get(self, request,  *args, **kwargs):
        slug = self.request.GET.get("slug")
        if slug:
            return redirect("box-detail", slug=slug)
        context = {'object_list': Box.objects.all()}
        return render(request, "bigbox/box_list.html", context)

class BoxDetailView(DetailView):
    model = Box

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        box = context["object"]
        activities = box.activities.all()[:5]
        context["activities"] = activities
        return context

class ActivityListView(ListView):
    model = Activity
    paginate_by = 20

    def get_queryset(self):
        box = get_object_or_404(Box, pk=self.kwargs["box_pk"])
        return super().get_queryset().filter(box=box)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        box = get_object_or_404(Box, pk=self.kwargs["box_pk"])
        context['box'] = box
        return context

class ActivityDetailView(DetailView):

    def get_object(self, queryset=None):
            activity = get_object_or_404(Activity, pk=self.kwargs["pk"])
            return activity

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["box"] = get_object_or_404(Box, pk=self.kwargs["box_pk"])
        return context    
