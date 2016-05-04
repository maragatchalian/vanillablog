from vanilla import ListView, TemplateView, CreateView
from vanillablog.forms import PostForm
from django.utils import timezone
from django.core.urlresolvers import reverse_lazy
from django.template import RequestContext
from .models import List


from django.http import HttpResponseRedirect
class PostView(TemplateView):
    template_name = 'list'

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