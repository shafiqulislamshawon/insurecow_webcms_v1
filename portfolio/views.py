from django.http import JsonResponse
from .models import Category, Portfolio
from django.shortcuts import get_object_or_404


# View for getting a list of all categories
def category_view(request):
    try:
        # Get all categories
        categories = Category.objects.all().order_by('-id')

        if not categories:
            return JsonResponse({
                "status": "error",
                "message": "No categories found",
                "data": None
            }, status=404)

        # Prepare the list of categories
        category_list = []
        for category in categories:
            category_list.append({
                "id": category.id,
                "name": category.name,
                "description": category.description
            })

        response_data = {
            "status": "success",
            "message": "Categories retrieved successfully",
            "data": category_list
        }
        return JsonResponse(response_data, status=200)

    except Exception as e:
        return JsonResponse({
            "status": "error",
            "message": "An error occurred while retrieving categories",
            "error": str(e),
            "data": None
        }, status=500)


# View for getting active portfolios by category
def category_portfolio_view(request, category_id):
    try:
        # Get the category by category_id (UUID)
        category = get_object_or_404(Category, id=category_id)

        # Get all active portfolios for the given category
        portfolios = Portfolio.objects.filter(category=category, is_active=True).order_by('-created_at')

        if not portfolios:
            return JsonResponse({
                "status": "error",
                "message": "No active portfolios found for this category",
                "data": None
            }, status=404)

        # Prepare the list of portfolios for the category
        portfolio_list = []
        for portfolio in portfolios:
            portfolio_list.append({
                "id": portfolio.id,
                "name": portfolio.name,
                "location": portfolio.location,
                "investment_value": str(portfolio.investment_value),
                "currency": portfolio.currency,
                "investment_period": portfolio.investment_period,
                "expected_return_min": str(portfolio.expected_return_min),
                "expected_return_max": str(portfolio.expected_return_max),
                "total_return_min": str(portfolio.total_return_min),
                "total_return_max": str(portfolio.total_return_max),
                "image_url": request.build_absolute_uri(portfolio.image.url) if portfolio.image else None,
                "description": portfolio.description,
                "extra_data": portfolio.extra_data,
                "created_at": portfolio.created_at,
                "updated_at": portfolio.updated_at
            })

        response_data = {
            "status": "success",
            "message": "Portfolios retrieved successfully",
            "data": portfolio_list
        }
        return JsonResponse(response_data, status=200)

    except Exception as e:
        return JsonResponse({
            "status": "error",
            "message": "An error occurred while retrieving portfolios by category",
            "error": str(e),
            "data": None
        }, status=500)


# View for getting active portfolios by category
def portfolio_view(request):
    try:
        # Get the category using the category_id (UUID)

        # Get all active portfolios for the given category
        portfolios = Portfolio.objects.filter(is_active=True).order_by('-created_at')

        if not portfolios:
            return JsonResponse({
                "status": "error",
                "message": "No active portfolios found",
                "data": None
            }, status=404)

        # Prepare the list of portfolios to be returned
        portfolio_list = []
        for portfolio in portfolios:
            portfolio_list.append({
                "id": portfolio.id,
                "name": portfolio.name,
                "location": portfolio.location,
                "investment_value": str(portfolio.investment_value),
                "currency": portfolio.currency,
                "investment_period": portfolio.investment_period,
                "expected_return_min": str(portfolio.expected_return_min),
                "expected_return_max": str(portfolio.expected_return_max),
                "total_return_min": str(portfolio.total_return_min),
                "total_return_max": str(portfolio.total_return_max),
                "image_url": request.build_absolute_uri(portfolio.image.url) if portfolio.image else None,
                "description": portfolio.description,
                "extra_data": portfolio.extra_data,
                "created_at": portfolio.created_at,
                "updated_at": portfolio.updated_at
            })

        response_data = {
            "status": "success",
            "message": "Portfolios retrieved successfully",
            "data": portfolio_list
        }
        return JsonResponse(response_data, status=200)

    except Exception as e:
        return JsonResponse({
            "status": "error",
            "message": "An error occurred while retrieving portfolios",
            "error": str(e),
            "data": None
        }, status=500)


# View for getting details of a specific portfolio
def portfolio_details_view(request, portfolio_id):
    try:
        # Get the portfolio using the portfolio_id (UUID)
        portfolio = get_object_or_404(Portfolio, id=portfolio_id)

        response_data = {
            "status": "success",
            "message": "Portfolio details retrieved successfully",
            "data": {
                "id": portfolio.id,
                "name": portfolio.name,
                "location": portfolio.location,
                "investment_value": str(portfolio.investment_value),
                "currency": portfolio.currency,
                "investment_period": portfolio.investment_period,
                "expected_return_min": str(portfolio.expected_return_min),
                "expected_return_max": str(portfolio.expected_return_max),
                "total_return_min": str(portfolio.total_return_min),
                "total_return_max": str(portfolio.total_return_max),
                "image_url": request.build_absolute_uri(portfolio.image.url) if portfolio.image else None,
                "description": portfolio.description,
                "extra_data": portfolio.extra_data,
                "is_active": portfolio.is_active,
                "created_at": portfolio.created_at,
                "updated_at": portfolio.updated_at,
                "category": {
                    "id": portfolio.category.id,
                    "name": portfolio.category.name
                }
            }
        }
        return JsonResponse(response_data, status=200)

    except Exception as e:
        return JsonResponse({
            "status": "error",
            "message": "An error occurred while retrieving portfolio details",
            "error": str(e),
            "data": None
        }, status=500)
