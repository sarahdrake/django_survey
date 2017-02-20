from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    if 'submission' not in request.session:
        request.session['submission'] = 0
    return render(request, 'first_app/index.html')

def process(request):
    if request.method == "POST":
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['comment'] = request.POST['comment']
        request.session['submission'] += 1
        return redirect('/result')
    else:
        return redirect('/')
def result(request):
    return render(request, 'first_app/result.html')
