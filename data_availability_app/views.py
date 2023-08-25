
# Create your views here.

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Count, Q
from .models import DataPoint
import json

@csrf_exempt
def get_data_points(request):
	total_valid_data_points = DataPoint.objects.exclude(Q(value=None) | Q(value=9999) | Q(value__isnull=True)).count()
	max_data_points = DataPoint.objects.count()
	data_availability = "{:.2f}".format((total_valid_data_points / max_data_points) * 100) if max_data_points > 0 else 0
	response_data = {
		"total_valid_data_points": total_valid_data_points,
		"max_data_points": max_data_points,
		"data_availability": data_availability
	}
	return JsonResponse(response_data)

@csrf_exempt
def post_data_point(request):
    
	if request.method == 'POST':
		try:
			request_data = request.body
			request_data_str = request_data.decode('utf-8')
			data = json.loads(request_data_str)

			value = data.get('value')
			if value is not None:
				try:
					data_point = DataPoint.objects.create(value=float(value))
					data_point.save()
					return JsonResponse({"message": "Data point created successfully"})
				except ValueError:
					return JsonResponse({"message": "Invalid value provided"})
			else:
				return JsonResponse({'error': 'Invalid data point value.'}, status=400)
		except json.JSONDecodeError:
			return JsonResponse({'error': 'Invalid JSON data.'}, status=400)
	return JsonResponse({'error': 'Only POST requests are allowed.'}, status=405)

