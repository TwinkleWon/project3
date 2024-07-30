from django.shortcuts import render, get_object_or_404, redirect
from .models import Word
from .forms import WordForm
import random

def index(request):
    words = Word.objects.all()
    return render(request, 'language_learning/index.html', {'words': words})

def word_create(request):
    if request.method == "POST":
        form = WordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('language_learning:index')
    else:
        form = WordForm()
    return render(request, 'language_learning/word_form.html', {'form': form})

def word_update(request, word_id):
    word = get_object_or_404(Word, pk=word_id)
    if request.method == "POST":
        form = WordForm(request.POST, instance=word)
        if form.is_valid():
            form.save()
            return redirect('language_learning:word_detail', word_id=word.id)
    else:
        form = WordForm(instance=word)
    return render(request, 'language_learning/word_form.html', {'form': form})

def word_delete(request, word_id):
    word = get_object_or_404(Word, pk=word_id)
    if request.method == "POST":
        word.delete()
        return redirect('language_learning:index')
    return render(request, 'language_learning/word_confirm_delete.html', {'word': word})

def word_detail(request, word_id):
    word = get_object_or_404(Word, id=word_id)
    if request.method == "POST":
        pronunciation = request.POST.get('pronunciation')
        category = request.POST.get('category')
        word.pronunciation = pronunciation
        word.category = category
        word.save()
        return redirect('language_learning:word_detail', word_id=word.id)
    return render(request, 'language_learning/word_detail.html', {'word': word})

def edit_pronunciation(request, word_id):
    word = get_object_or_404(Word, pk=word_id)
    if request.method == "POST":
        form = WordForm(request.POST, instance=word)
        if form.is_valid():
            word = form.save(commit=False)
            word.pronunciation = form.cleaned_data['pronunciation']
            word.save()
            return redirect('language_learning:word_detail', word_id=word.id)
    else:
        form = WordForm(instance=word)
    return render(request, 'language_learning/edit_pronunciation.html', {'form': form, 'word': word})

def edit_category(request, word_id):
    word = get_object_or_404(Word, pk=word_id)
    if request.method == "POST":
        form = WordForm(request.POST, instance=word)
        if form.is_valid():
            word = form.save(commit=False)
            word.category = form.cleaned_data['category']
            word.save()
            return redirect('language_learning:word_detail', word_id=word.id)
    else:
        form = WordForm(instance=word)
    return render(request, 'language_learning/edit_category.html', {'form': form, 'word': word})

def quiz(request):
    words = Word.objects.all()
    if request.method == "POST":
        selected_word_id = int(request.POST.get("word_id"))
        selected_answer = request.POST.get("answer")
        selected_word = get_object_or_404(Word, id=selected_word_id)
        
        correct = selected_answer == selected_word.meaning
        return redirect('language_learning:quiz_result', word_id=selected_word_id, correct=str(correct).lower())

    if words:
        question_word = random.choice(words)
        options = list(Word.objects.exclude(id=question_word.id).values_list('meaning', flat=True))
        options = random.sample(options, min(3, len(options)))
        options.append(question_word.meaning)
        random.shuffle(options)
        
        return render(request, 'language_learning/quiz.html', {
            'question_word': question_word,
            'options': options
        })
    else:
        return render(request, 'language_learning/quiz.html', {
            'message': '등록된 단어가 없습니다. 단어를 추가해 주세요.'
        })

def quiz_result(request, word_id, correct):
    word = get_object_or_404(Word, id=word_id)
    correct = correct == 'true'
    return render(request, 'language_learning/quiz_result.html', {'word': word, 'correct': correct})
