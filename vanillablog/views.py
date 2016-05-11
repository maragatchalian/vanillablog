from vanilla import ListView, CreateView, DetailView, DeleteView
from vanillablog.forms import PostForm
from django.utils import timezone
from django.core.urlresolvers import reverse_lazy
from django.template import RequestContext
from .models import List
from django.http import HttpResponseRedirect
from django.core.exceptions import ImproperlyConfigured

class ListView(ListView):
    model = List

class CreatePost(CreateView):
    model = List
    form_class = PostForm
    success_url = reverse_lazy('list')

    def form_valid(self, form):
        form = form.save(commit=False)
        form.author = self.request.user
        form.published_date = timezone.now()
        form.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self):
        return self.render_to_response(context)

class ViewPost(DetailView):
    model = List
    template_name = 'vanillablog/post_detail.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data()
        return self.render_to_response(context)

class DeletePost(DeleteView):
    model = List
    success_url = reverse_lazy('list')
    template_name_suffix = '_confirm_delete'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data()
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return HttpResponseRedirect(self.get_success_url())
