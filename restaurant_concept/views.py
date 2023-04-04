from django.shortcuts import render


def handler404(request, exception):  # 404 error handler
    return render(request, '404.html', status=404)
