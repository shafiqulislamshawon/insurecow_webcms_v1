import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import *


@csrf_exempt
def insurance_types_view(request):
    try:
        insurance_types = InsuranceType.objects.all().order_by('-id')
        if not insurance_types:
            return JsonResponse({
                "status": "error",
                "message": "No insurance types found",
                "data": None
            }, status=404)

        data = [{"id": it.id, "name": it.name} for it in insurance_types]
        return JsonResponse({
            "status": "success",
            "message": "Insurance types retrieved successfully",
            "data": data
        }, status=200)
    except Exception as e:
        return JsonResponse({
            "status": "error",
            "message": "An error occurred while retrieving insurance types",
            "error": str(e),
            "data": None
        }, status=500)


@csrf_exempt
def dynamic_form_view(request, insurance_type_id):
    try:
        insurance_type = InsuranceType.objects.get(id=insurance_type_id)
        form_fields = insurance_type.form_fields.all()

        data = [{
            "id": field.id,
            "label": field.label,
            "field_type": field.field_type,
            "required": field.required,
            "choices": field.choices.split(',') if field.choices else []
        } for field in form_fields]

        return JsonResponse({
            "status": "success",
            "message": "Dynamic form retrieved successfully",
            "data": data
        }, status=200)
    except InsuranceType.DoesNotExist:
        return JsonResponse({
            "status": "error",
            "message": "Insurance type not found"
        }, status=404)
    except Exception as e:
        return JsonResponse({
            "status": "error",
            "message": "An error occurred while retrieving the dynamic form",
            "error": str(e)
        }, status=500)


@csrf_exempt
def form_submission_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            name = data.get('name')
            phone = data.get('phone')
            email = data.get('email')
            insurance_type_id = data.get('insurance_type_id')
            responses = data.get('responses', [])

            if not all([name, phone, insurance_type_id]):
                return JsonResponse({
                    "status": "error",
                    "message": "Missing required fields"
                }, status=400)

            insurance_type = InsuranceType.objects.get(id=insurance_type_id)
            submission = UserSubmission.objects.create(
                name=name, phone=phone, email=email, insurance_type=insurance_type
            )

            for response in responses:
                field_id = response.get('field_id')
                value = response.get('value')
                field = DynamicFormField.objects.get(id=field_id)
                DynamicFormResponse.objects.create(submission=submission, field=field, value=value)

            return JsonResponse({
                "status": "success",
                "message": "Form submitted successfully",
                "submission_id": submission.id
            }, status=201)
        except Exception as e:
            return JsonResponse({
                "status": "error",
                "message": "An error occurred while submitting the form",
                "error": str(e)
            }, status=500)

    return JsonResponse({"status": "error", "message": "Invalid request method"}, status=405)

