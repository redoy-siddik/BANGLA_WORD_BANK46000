from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Word
from .forms import WordForm

def word_list(request):
    query = request.GET.get('q', '')
    if query:
        words = Word.objects.filter(
            Q(root_word__icontains=query) |
            Q(varna__varna_name__icontains=query) |
            Q(source__source_name__icontains=query) |
            Q(type__type_name__icontains=query) |
            Q(details__label__icontains=query) |
            Q(details__origin__icontains=query) |
            Q(details__example__icontains=query)
        ).distinct()
    else:
        words = Word.objects.all()
    return render(request, 'vocabulary/word_list.html', {'words': words})

def add_word(request):
    if request.method == 'POST':
        form = WordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('word_list')
    else:
        form = WordForm()
    return render(request, 'vocabulary/add_word.html', {'form': form})

def update_word(request, word_id):
    word = get_object_or_404(Word, id=word_id)
    if request.method == 'POST':
        form = WordForm(request.POST, instance=word)
        if form.is_valid():
            form.save()
            return redirect('word_list')
    else:
        form = WordForm(instance=word)
    return render(request, 'vocabulary/update_word.html', {'form': form, 'word': word})

def delete_word(request, word_id):
    word = get_object_or_404(Word, id=word_id)
    if request.method == 'POST':
        word.delete()
        return redirect('word_list')
    return render(request, 'vocabulary/delete_word.html', {'word': word})