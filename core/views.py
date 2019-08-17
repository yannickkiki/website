from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "core/home.html"


class AboutView(TemplateView):
    template_name = "core/about.html"


class CareerView(TemplateView):
    template_name = "core/career.html"


class BlogView(TemplateView):
    template_name = "core/blog.html"
