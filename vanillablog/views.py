from vanilla import ListView, CreateView, DetailView, DeleteView, UpdateView
from vanillablog.forms import PostForm
from django.utils import timezone
from django.core.urlresolvers import reverse_lazy
from django.template import RequestContext
from .models import List
from django.http import HttpResponseRedirect

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

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return HttpResponseRedirect(self.get_success_url())

class EditPost(UpdateView):
    model = List
    form_class = PostForm
    success_url = reverse_lazy('list')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form(data=request.POST, files=request.FILES, instance=self.object)
        if form.is_valid():
            return self.form_valid(form)
        return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        context = self.get_context_data(form=form)
        return self.render_to_response(context)