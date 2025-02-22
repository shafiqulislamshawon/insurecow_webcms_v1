from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

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
