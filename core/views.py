import json
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from .models import ContactUs, Gallery, FAQ
from django.core.exceptions import ValidationError
import re

@api_view(['GET'])
def ping(request):
    return Response({'message': 'pong'})
from django.http import JsonResponse
from .models import Logo, Slider, MenuItem


def logo_view(request):
    try:
        # Get the active logo
        logo = Logo.objects.filter(is_active=True).order_by('-created_at').first()

        if not logo:
            return JsonResponse({
                "status": "error",
                "message": "No active logo found",
                "data": None
            }, status=404)

        response_data = {
            "status": "success",
            "message": "Logo retrieved successfully",
            "data": {
                "id": logo.id,
                "name": logo.name,
                "image_url": request.build_absolute_uri(logo.image.url) if logo.image else None,
                "created_at": logo.created_at,
                "updated_at": logo.updated_at
            }
        }
        return JsonResponse(response_data, status=200)

    except Exception as e:
        return JsonResponse({
            "status": "error",
            "message": "An error occurred while retrieving the logo",
            "error": str(e),
            "data": None
        }, status=500)


def slider_list_view(request):
    try:
        # Get all sliders
        sliders = Slider.objects.filter(is_active=True).order_by('-id')

        if not sliders.exists():
            return JsonResponse({
                "status": "error",
                "message": "No sliders found",
                "data": []
            }, status=404)

        slider_data = []
        for slider in sliders:
            slider_data.append({
                "id": slider.id,
                "title": slider.title,
                "image_url": request.build_absolute_uri(slider.image.url) if slider.image else None,
                "created_at": slider.created_at,
                "updated_at": slider.updated_at
            })

        return JsonResponse({
            "status": "success",
            "message": "Sliders retrieved successfully",
            "data": slider_data
        }, status=200)

    except Exception as e:
        return JsonResponse({
            "status": "error",
            "message": "An error occurred while retrieving sliders",
            "error": str(e),
            "data": None
        }, status=500)


def menu_view(request):
    try:
        # Fetch all top-level menu items (those without a parent)
        menu_items = MenuItem.objects.filter(parent__isnull=True,is_active=True ).order_by('id')

        if not menu_items:
            return JsonResponse({
                "status": "error",
                "message": "No menu items found",
                "data": None
            }, status=404)

        # Prepare the menu data manually
        menu_data = []
        for item in menu_items:
            # Fetch the sub-menu items
            sub_menu_items = MenuItem.objects.filter(parent=item,is_active=True).order_by('id')
            sub_menu_data = []

            for sub_item in sub_menu_items:
                sub_menu_data.append({
                    "title": sub_item.title,
                    "link": sub_item.link
                })

            # Add the current menu item to the menu data list
            menu_data.append({
                "title": item.title,
                "link": item.link,
                "sub_menu": sub_menu_data
            })

        response_data = {
            "status": "success",
            "message": "Menu retrieved successfully",
            "data": menu_data
        }

        return JsonResponse(response_data, status=200)

    except Exception as e:
        return JsonResponse({
            "status": "error",
            "message": "An error occurred while retrieving the menu",
            "error": str(e),
            "data": None
        }, status=500)



@csrf_exempt  # Allow POST requests without CSRF token for simplicity in this example.
def contact_us_view(request):
    if request.method == 'POST':
        try:
            # Get the data from the request body (assuming it's in JSON format)
            data = json.loads(request.body)

            # Validate required fields
            name = data.get('name')
            email = data.get('email')
            phone = data.get('phone')
            description = data.get('description')

            if not name or not email or not phone or not description:
                return JsonResponse({
                    "status": "error",
                    "message": "All fields are required"
                }, status=400)

            # Validate email format
            if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                return JsonResponse({
                    "status": "error",
                    "message": "Invalid email format"
                }, status=400)

            # Validate phone format (simple validation for the sake of this example)
            if not re.match(r"^\+?\d{10,15}$", phone):
                return JsonResponse({
                    "status": "error",
                    "message": "Invalid phone number format"
                }, status=400)

            # Create the ContactUs entry
            contact = ContactUs.objects.create(
                name=name,
                email=email,
                phone=phone,
                description=description
            )

            response_data = {
                "status": "success",
                "message": "Your message has been submitted successfully",
                "data": {
                    "id": contact.id,
                    "name": contact.name,
                    "email": contact.email,
                    "phone": contact.phone,
                    "description": contact.description,
                    "created_at": contact.created_at
                }
            }
            return JsonResponse(response_data, status=201)

        except ValidationError as e:
            return JsonResponse({
                "status": "error",
                "message": str(e)
            }, status=400)

        except Exception as e:
            return JsonResponse({
                "status": "error",
                "message": "An error occurred while submitting the message",
                "error": str(e)
            }, status=500)

    else:
        return JsonResponse({
            "status": "error",
            "message": "Only POST method is allowed"
        }, status=405)



def get_gallery(request):
    try:
        gallery_items = Gallery.objects.all()
        gallery_data = []

        for item in gallery_items:
            gallery_data.append({
                "id": item.id,
                "title": item.title,
                "image_url": request.build_absolute_uri(item.image.url),
                "description": item.description,
                "created_at": item.created_at,
                "updated_at": item.updated_at
            })

        return JsonResponse({
            "status": "success",
            "message": "Gallery retrieved successfully",
            "data": gallery_data
        }, status=200)

    except Exception as e:
        return JsonResponse({
            "status": "error",
            "message": "An error occurred while retrieving the gallery",
            "error": str(e),
        }, status=500)

def get_gallery_item(request, gallery_id):
    try:
        gallery_item = Gallery.objects.get(id=gallery_id)

        response_data = {
            "id": gallery_item.id,
            "title": gallery_item.title,
            "image_url": request.build_absolute_uri(gallery_item.image.url),
            "description": gallery_item.description,
            "created_at": gallery_item.created_at,
            "updated_at": gallery_item.updated_at
        }

        return JsonResponse({
            "status": "success",
            "message": "Gallery item retrieved successfully",
            "data": response_data
        }, status=200)

    except Gallery.DoesNotExist:
        return JsonResponse({
            "status": "error",
            "message": "Gallery item not found",
        }, status=404)

    except Exception as e:
        return JsonResponse({
            "status": "error",
            "message": "An error occurred while retrieving the gallery item",
            "error": str(e),
        }, status=500)



def get_faqs(request):
    try:
        faqs = FAQ.objects.all()
        faq_data = []

        for faq in faqs:
            faq_data.append({
                "question": faq.question,
                "answer": faq.answer,
                "created_at": faq.created_at,
                "updated_at": faq.updated_at
            })

        return JsonResponse({
            "status": "success",
            "message": "FAQs retrieved successfully",
            "data": faq_data
        }, status=200)

    except Exception as e:
        return JsonResponse({
            "status": "error",
            "message": "An error occurred while retrieving the FAQs",
            "error": str(e),
        }, status=500)
