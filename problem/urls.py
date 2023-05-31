from django.urls import path
from .views import (
    ProblemListView,
    ProblemDetailView,
    ProblemCreateView,
    ProblemEditView,
    ProblemDeleteView,
)

app_name = "problem"

urlpatterns = [
    path("", ProblemListView.as_view(), name="problems_list"),
    path("<int:pk>/", ProblemDetailView.as_view(), name="problem_detail"),
    path("<int:pk>/edit/", ProblemEditView.as_view(), name="problem_edit"),
    path("<int:pk>/delete/", ProblemDeleteView.as_view(), name="problem_delete"),
    path("create/", ProblemCreateView.as_view(), name="problem_create"),
]
