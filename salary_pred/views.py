from django.shortcuts import render, redirect
from .model import find_pred
# Create your views here.
def find(request):
    if request.method == 'POST':
        name = request.POST['name']
        gender = request.POST['gender']
        age = request.POST['age']
        salary = request.POST['es_salary']
        cap_gender = gender.capitalize()
        num_cap_gender = 0
        if cap_gender == 'Male':
            nu_cap_gender = 1
        res = find_pred(num_cap_gender, age, salary)
        result = ''
        if res == 0:
            result = 'No... {} Can\'t Buy the car'.format(name)
        else:
            result = 'Yes...{} will Can buy the car'.format(name)
        return render(request, 'result.html', {'res':result})
    return render(request, 'index.html')
