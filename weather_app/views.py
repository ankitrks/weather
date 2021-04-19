# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import requests
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def index(request):
	return render(request, 'index.html', {})

@csrf_exempt
def ajax_weather_data(request):
	data = {'status' : 'success'}
	try:
		c_lat = request.GET.get('lat')
		c_long = request.GET.get('long')
		# url = 'https://api.met.no/weatherapi/locationforecast/2.0/compact?lat=' + c_lat + '&lon=' + c_long
		
		# using hard-coded url as most of the location are returning 403s
		url = 'https://api.met.no/weatherapi/locationforecast/2.0/compact?lat=51.5&lon=-0.25'
		response = requests.get(url).json()
		data['w_data'] = response
	except Exception as e:
		# Send sample response bbecause of the API limitations...
		data = {'status' : 'fail', 'message' : 'Could not find the location'}
	return JsonResponse(data) 