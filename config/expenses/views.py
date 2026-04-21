from django.shortcuts import render,redirect
from .models import Expense,Category
# Create your views here.


def expense_list(request):
    expenses = Expense.objects.all()
    return render(request, 'expenses/list.html', {'expenses': expenses})



def add_expense(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        description = request.POST.get('description')
        amount = request.POST.get('amount')
        date = request.POST.get('date')
        category_id = request.POST.get('category')

        category = Category.objects.get(id=category_id)

        Expense.objects.create(
            description=description,
            amount=amount,
            date=date,
            category=category
        )
        return redirect('expense_list')

    return render(request, 'expenses/add.html', {'categories': categories})


from django.shortcuts import get_object_or_404

def delete_expense(request, id):
    expense = get_object_or_404(Expense, id=id)
    expense.delete()
    return redirect('expense_list')


def edit_expense(request, id):
    expense = get_object_or_404(Expense, id=id)

    if request.method == 'POST':
        expense.description = request.POST.get('description')
        expense.amount = request.POST.get('amount')
        expense.date = request.POST.get('date')
        expense.category = request.POST.get('category')
        expense.save()

        return redirect('expense_list')

    return render(request, 'expenses/edit.html', {'expense': expense})

from django.db.models import Sum

def monthly_summary(request):
    month = request.GET.get('month')  # from URL

    expenses = Expense.objects.all()

    if month:
        expenses = expenses.filter(date__month=month)

    total = expenses.aggregate(Sum('amount'))['amount__sum']

    return render(request, 'expenses/summary.html', {
        'total': total,
        'month': month
    })