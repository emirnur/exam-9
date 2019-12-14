# from django.shortcuts import render
# from django.views.generic import ListView
#
# from webapp.models import Photo
#
#
# class IndexView(ListView):
#     model = Photo
#     template_name = 'index.html'
#
#     def get_queryset(self):
#         return Product.objects.filter(in_order=True)
#
#
# class ProductView(StatsMixin, DetailView):
#     model = Product
#     template_name = 'product/detail.html'
#
#
# class ProductCreateView(PermissionRequiredMixin, StatsMixin, CreateView):
#     model = Product
#     template_name = 'product/create.html'
#     fields = ('name', 'category', 'price', 'photo', 'in_order')
#     permission_required = 'webapp.add_product', 'webapp.can_have_piece_of_pizza'
#     permission_denied_message = '403 Доступ запрещён!'
#
#     def get_success_url(self):
#         return reverse('webapp:product_detail', kwargs={'pk': self.object.pk})
#
#
# class ProductUpdateView(LoginRequiredMixin, StatsMixin, UpdateView):
#     model = Product
#     template_name = 'product/update.html'
#     fields = ('name', 'category', 'price', 'photo', 'in_order')
#     context_object_name = 'product'
#
#     def get_success_url(self):
#         return reverse('webapp:product_detail', kwargs={'pk': self.object.pk})
#
#
# class ProductDeleteView(LoginRequiredMixin, StatsMixin, DeleteView):
#     model = Product
#     template_name = 'product/delete.html'
#     success_url = reverse_lazy('webapp:index')
#     context_object_name = 'product'
#
#     def delete(self, request, *args, **kwargs):
#         product = self.object = self.get_object()
#         product.in_order = False
#         product.save()
#         return HttpResponseRedirect(self.get_success_url())
