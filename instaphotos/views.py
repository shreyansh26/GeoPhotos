from django.shortcuts import render
import requests
from .forms import PostForm

# Create your views here.
def image_list(request):
    form = PostForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            location = form.cleaned_data['location']
            map_url = 'https://maps.googleapis.com/maps/api/geocode/json'
            payload = {'address': location}
            r = requests.get(map_url, params=payload)
            jsonval = r.json()
            #print(jsonval)
            lat = jsonval['results'][0]['geometry']['location']['lat']
            lng = jsonval['results'][0]['geometry']['location']['lng']
            #print(lat, lng)
            payload = {'lat': lat, 'lng': lng, 'access_token': 'ACCESS_TOKEN'}
            insta_url = 'https://api.instagram.com/v1/media/search'
            r2 = requests.get(insta_url, params=payload)
            jsonval2 = r2.json()
            # First two images for testing
            url_list = ['https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcST7YDjHjnP5DURcPrZpcFPO6BI6I4kOiqTvNeCy4NRYFbA--5J',
            'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTf4ZJbn77pAKbRtt9oSbaNONm-LXB4a6TLnZzGiURXflEA5dHwfg']
            for i in jsonval2['data']:
                url_list.append(i['images']['low_resolution']['url'])
            print(url_list)
        else:
            form = PostForm()
    return render(request, 'instaphotos/base.html', {'form': form, 'url_list': url_list})
