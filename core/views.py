from django.shortcuts import get_object_or_404, render
from .models import Url, Click
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'core/index.html')

def req(request, unique_id):
    if len(unique_id) == 7:
        try:
            url = Url.objects.get(unique_id = unique_id)
        except Url.DoesNotExist:
            messages.error(request, 'Oops! Link does not exist.')
            return HttpResponseRedirect('/')
        else:
            click = Click(
                url=url,
                ip_address=request.META['REMOTE_ADDR']
            )
            click.save()
            if url.clicks is not None:
                url.clicks += 1
                url.save()
            else:
                url.clicks = 1
                url.save()
            if url.url.startswith(('https://', 'http://')):
                return HttpResponseRedirect(url.url)
            else:
                return HttpResponseRedirect(f'https://{url.url}')
    else:
        return HttpResponse(1)



@login_required(login_url='/accounts/signin')
def dashboard(request, username):
    if request.user.username == username:
        urls = Url.objects.filter(user = User.objects.get(username=username))
        context = {
            'urls': urls
        }
        return render(request, 'core/dashboard.html', context)
    else:
        messages.add_message(request, messages.ERROR, 'Oops! An error occured.')
        return HttpResponseRedirect('/')

@login_required(login_url='/accounts/signin')
def url_stats(request, username, unique_id):
    if request.user.username == username:
        user = get_object_or_404(User, username=username)
        url = get_object_or_404(Url, user=user, unique_id=unique_id)
        clicks_data = Click.objects.filter(
            url = Url.objects.get(
                user = User.objects.get(username=username),
                unique_id=unique_id
            )
        )

        context = {
            'clicks_data': clicks_data,
            'url': Url.objects.get(
                user = User.objects.get(username=username),
                unique_id=unique_id
            ).url
        }
        return render(request, 'core/url_stats.html', context)
    else:
        messages.add_message(request, messages.ERROR, 'Oops! An error occured.')
        return HttpResponseRedirect('/')













