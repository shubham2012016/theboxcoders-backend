from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from .models import *


def get_client_ip(request):
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        return x_forwarded_for.split(",")[0]
    return request.META.get("REMOTE_ADDR")

def thank_you(request):
    contact = CompanyContact.objects.all()
    social = SocialHandle.objects.all()
    context = {
        'social': social,
        'contacts':contact
    }
    return render(request, 'thank-you-page.html', context)

def index(request):
    contact = CompanyContact.objects.all()
    social = SocialHandle.objects.all()
    context = {
        'social': social,
        'contacts':contact
    }
    return render(request, 'main.html',context)


def about(request):
    contact = CompanyContact.objects.all()
    social = SocialHandle.objects.all()
    context = {
        'social': social,
        'contacts':contact
    }
    return render(request, 'about.html', context)


@require_http_methods(["GET", "POST"])
def contact(request):
    contacts = CompanyContact.objects.all()
    social = SocialHandle.objects.all()

    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        phone = request.POST.get("phone", "").strip()
        interest = request.POST.get("interest")
        message = request.POST.get("message", "").strip()

        # HARD validation (no fake safety)
        if not all([name, email, phone, interest, message]):
            messages.error(request, "All fields are required.")
            return redirect("contact")

        if interest not in dict(ContactInquiry.INTEREST_CHOICES):
            interest = "other"

        ContactInquiry.objects.create(
            name=name,
            email=email,
            phone=phone,
            interest=interest,
            message=message,
            ip_address=get_client_ip(request),
            user_agent=request.META.get("HTTP_USER_AGENT", ""),
        )

        messages.success(
            request,
            "Thanks for reaching out. Our team will contact you shortly."
        )

        return redirect("thank_you")

    context = {
        "contacts": contacts,
        "social": social,
    }
    return render(request, "contact.html", context)


@require_http_methods(["GET", "POST"])
def web_devlopment(request):
    contact = CompanyContact.objects.all()
    social = SocialHandle.objects.all()

    if request.method == "POST":
        service_type = request.POST.get("service_type", "your selected service")

        WebProjectInquiry.objects.create(
            full_name=request.POST.get("full_name"),
            email=request.POST.get("email"),
            phone_number=request.POST.get("phone_number", ""),
            service_type=service_type,
            project_requirements=request.POST.get("project_requirements"),
            service_page=request.POST.get("service_page"),
            source_city=request.POST.get("source_city"),
            ip_address=get_client_ip(request),
            user_agent=request.META.get("HTTP_USER_AGENT", ""),
        )

        # ✅ Dynamic success message
        messages.success(
            request,
            f"Your request for {service_type.replace('-', ' ').title()} has been submitted. Our team will reach you soon."
        )

        return redirect("thank_you")

    context = {
        "social": social,
        "contacts": contact,
    }
    return render(request, "web-development-page.html", context)

@require_http_methods(["GET", "POST"])
def python_service(request):
    # Context data (GET only usage, but harmless on POST)
    contact = CompanyContact.objects.all()
    social = SocialHandle.objects.all()

    if request.method == "POST":
        # ---- Required fields validation ----
        full_name = request.POST.get("full_name", "").strip()
        email = request.POST.get("email", "").strip()
        project_requirements = request.POST.get("project_requirements", "").strip()

        if not full_name or not email or not project_requirements:
            messages.error(
                request,
                "Invalid submission. Please fill in all required fields."
            )
            return redirect(request.path)

        # ---- Service type validation ----
        service_type = request.POST.get("service_type", "other")
        valid_services = dict(PythonProjectInquiry.SERVICE_CHOICES)

        if service_type not in valid_services:
            service_type = "other"

        # ---- Create inquiry ----
        PythonProjectInquiry.objects.create(
            full_name=full_name,
            email=email,
            phone_number=request.POST.get("phone_number", "").strip(),
            service_type=service_type,
            project_requirements=project_requirements,
            service_page=request.POST.get(
                "service_page",
                "Python Automation Services Delhi"
            ),
            source_city=request.POST.get("source_city", "Delhi"),
            ip_address=get_client_ip(request),
            user_agent=request.META.get("HTTP_USER_AGENT", ""),
        )

        # ---- Success message ----
        messages.success(
            request,
            f"Your request for Python {valid_services[service_type]} has been submitted. "
            "Our team will reach you soon."
        )

        # PRG pattern (prevents duplicate submissions)
        return redirect("thank_you")

    # ---- GET request ----
    return render(
        request,
        "python-service-page.html",
        {
            "social": social,
            "contacts": contact,
        },
    )

@require_http_methods(["GET", "POST"])
def ai_intergration_services(request): 
    contact = CompanyContact.objects.all()
    social = SocialHandle.objects.all()

    if request.method == "POST":
        service_type = request.POST.get("service_type")

        # Validate service type against model choices
        valid_services = dict(AIProjectInquiry.SERVICE_CHOICES)
        if service_type not in valid_services:
            service_type = "custom"

        AIProjectInquiry.objects.create(
            full_name=request.POST.get("full_name"),
            email=request.POST.get("email"),
            phone_number=request.POST.get("phone_number", ""),
            service_type=service_type,
            project_requirements=request.POST.get("project_requirements"),
            service_page=request.POST.get("service_page"),
            source_city=request.POST.get("source_city"),
            ip_address=get_client_ip(request),
            user_agent=request.META.get("HTTP_USER_AGENT", ""),
        )

        # Clear, service-specific success message
        messages.success(
            request,
            f"Your request for {valid_services[service_type]} has been submitted. Our AI team will contact you shortly."
        )

        return redirect("thank_you")

    return render(
        request,
        "ai-integration-page.html",
        {
            "social": social,
            "contacts": contact,
        },
    )

@require_http_methods(["GET", "POST"])
def instagram_automation(request):
    contact = CompanyContact.objects.all()
    social = SocialHandle.objects.all()

    if request.method == "POST":
        service_type = request.POST.get("service_type")

        # Safety fallback (never trust frontend)
        valid_services = dict(InstagramAutomationInquiry.SERVICE_CHOICES)
        if service_type not in valid_services:
            service_type = "automation"

        InstagramAutomationInquiry.objects.create(
            full_name=request.POST.get("full_name"),
            email=request.POST.get("email"),
            instagram_username=request.POST.get("instagram_username", ""),
            service_type=service_type,
            project_requirements=request.POST.get("project_requirements"),
            service_page=request.POST.get("service_page"),
            source_city=request.POST.get("source_city"),
            ip_address=get_client_ip(request),
            user_agent=request.META.get("HTTP_USER_AGENT", ""),
        )

        messages.success(
            request,
            f"Your request for Instagram {valid_services[service_type]} has been submitted. Our team will contact you shortly."
        )

        return redirect("thank_you")

    return render(
        request,
        "instagram-automation-page.html",
        {
            "contacts": contact,
            "social": social,
        },
    )

@require_http_methods(["GET", "POST"])
def facebook_automation(request):
    contact = CompanyContact.objects.all()
    social = SocialHandle.objects.all()

    if request.method == "POST":
        service_type = request.POST.get("service_type")

        if service_type not in dict(FacebookAutomationInquiry.SERVICE_CHOICES):
            service_type = "full"

        FacebookAutomationInquiry.objects.create(
            full_name=request.POST.get("full_name"),
            email=request.POST.get("email"),
            facebook_page_name=request.POST.get(
                "facebook_page_name", ""
            ),
            service_type=service_type,
            project_requirements=request.POST.get("project_requirements"),
            service_page=request.POST.get("service_page"),
            source_city=request.POST.get("source_city"),
            ip_address=get_client_ip(request),
            user_agent=request.META.get("HTTP_USER_AGENT", ""),
        )

        messages.success(
            request,
            f"Your request for Facebook {dict(FacebookAutomationInquiry.SERVICE_CHOICES)[service_type]} has been submitted. Our team will contact you shortly."
        )

        return redirect("thank_you")

    return render(
        request,
        "facebook-automation.html",
        {
            "contacts": contact,
            "social": social,
        },
    )

@require_http_methods(["GET", "POST"])
def whatsapp_automation(request):
    if request.method == "POST":

        service_type = request.POST.get("service_type")

        if service_type not in dict(WhatsAppAutomationInquiry.SERVICE_CHOICES):
            service_type = "custom"

        WhatsAppAutomationInquiry.objects.create(
            full_name=request.POST.get("full_name"),
            email=request.POST.get("email"),
            phone_number=request.POST.get("phone_number", ""),
            service_type=service_type,
            project_requirements=request.POST.get("project_requirements"),
            service_page=request.POST.get("service_page"),
            source_city=request.POST.get("source_city"),
            ip_address=get_client_ip(request),
            user_agent=request.META.get("HTTP_USER_AGENT", ""),
        )

        messages.success(
            request,
            "Your WhatsApp automation inquiry has been submitted. Our team will contact you shortly."
        )

        return redirect("thank_you")

    return render(request, "whatsapp-automation.html")

@require_http_methods(["GET", "POST"])
def tally_automation(request):
    if request.method == "POST":

        service_type = request.POST.get("service_type", "custom")

        if service_type not in dict(TallyAutomationInquiry.SERVICE_CHOICES):
            service_type = "custom"

        TallyAutomationInquiry.objects.create(
            full_name=request.POST.get("full_name"),
            email=request.POST.get("email"),
            phone_number=request.POST.get("phone_number", ""),
            service_type=service_type,
            project_requirements=request.POST.get("project_requirements"),
            service_page=request.POST.get("service_page"),
            source_city=request.POST.get("source_city"),
            ip_address=get_client_ip(request),
            user_agent=request.META.get("HTTP_USER_AGENT", ""),
        )

        messages.success(
            request,
            "Your Tally automation inquiry has been submitted. Our team will contact you shortly."
        )

        return redirect("thank_you")

    return render(request, "tally-automation-page.html")


def book_consultation(request):
    if request.method == "POST":

        # Detect source
        source = "desktop"
        if "business-email-mobile" in request.POST:
            source = "mobile"
        elif "business-email-tablet" in request.POST:
            source = "tablet"

        # Normalize common fields
        name = request.POST.get("name") or request.POST.get("name-mobile") or request.POST.get("name-tablet")
        email = (
            request.POST.get("email") or
            request.POST.get("business-email-mobile") or
            request.POST.get("business-email-tablet")
        )

        phone = request.POST.get("phone_number") or request.POST.get("phone-number")

        # Project types
        project_types = request.POST.getlist("project_types[]")

        ConsultationForm.objects.create(
            name=name,
            email=email,
            phone_number=phone,
            company_name=request.POST.get("company_name"),
            website_url=request.POST.get("website_url"),
            project_types=project_types,
            budget=request.POST.get("budget"),
            timeline=request.POST.get("timeline"),
            project_details=request.POST.get("project_details")
        )

        return render(request, "book-consultation-thankyou.html", {"source": source})
