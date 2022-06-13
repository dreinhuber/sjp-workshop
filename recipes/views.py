from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView


from recipes.forms import RecipeForm
from recipes.models import Recipe


class RecipeCreateView(CreateView):
    model = Recipe
    template_name = 'recipes/new.html'
    fields = ["name", "author", "description", "image"]

    def get_success_url(self):
        return reverse('recipe_detail', args=[self.object.pk])

# def create_recipe(request):
#     if request.method == "POST" and RecipeForm:
#         form = RecipeForm(request.POST)
#         if form.is_valid():
#             recipe = form.save()
#             return redirect("recipe_detail", pk=recipe.pk)
#     elif RecipeForm:
#         form = RecipeForm()
#     else:
#         form = None
#     context = {
#         "form": form,
#     }
#     return render(request, "recipes/new.html", context)


class RecipeUpdateView(UpdateView):
    model = Recipe
    template_name = 'recipes/edit.html'
    fields = ["name", "description", "image"]

def change_recipe(request, pk):
    if Recipe and RecipeForm:
        instance = Recipe.objects.get(pk=pk)
        if request.method == "POST":
            form = RecipeForm(request.POST, instance=instance)
            if form.is_valid():
                form.save()
                return redirect("recipe_detail", pk=pk)
        else:
            form = RecipeForm(instance=instance)
    else:
        form = None
    context = {
        "form": form,
    }
    return render(request, "recipes/edit.html", context)


# def show_recipes(request):
#     context = {
#         "recipes": Recipe.objects.all() if Recipe else [],
#     }
#     return render(request, "recipes/list.html", context)

class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipes/list.html'


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipes/detail.html'


# def show_recipe(request, pk):
#     context = {
#         "recipe": Recipe.objects.get(pk=pk) if Recipe else None,
#     }
#     return render(request, "recipes/detail.html", context)
