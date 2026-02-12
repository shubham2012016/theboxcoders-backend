from django.db import models

class CompanyContact(models.Model):
    phone_number = models.CharField(max_length=20)
    whatsapp_number = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return f"Phone Number: {self.phone_number}, Whatsapp Number: {self.whatsapp_number}"
    
class SocialHandle(models.Model):
    linkedin = models.URLField()
    twitter = models.URLField()
    youtube = models.URLField()
    reddit = models.URLField()
    facebook = models.URLField()
    instagram = models.URLField()

class ConsultationForm(models.Model):
    PROJECT_CHOICES = [
        ('web', 'Web Development'),
        ('python', 'Python Automation'),
        ('ai', 'AI Integration'),
        ('social', 'Social Media Automation'),
        ('tally', 'Tally Automation'),
        ('undecided', 'Undecided'),
    ]

    BUDGET_CHOICES = [
        ('<10k', 'Less than 10,000'),
        ('25-50k', '25,000 - 50,000'),
        ('50-80k', '50,000 - 80,000'),
        ('80-130k', '80,000 - 1,30,000'),
        ('130k+', '1,30,000+'),
        ('deciding', 'Still deciding'),
    ]

    TIMELINE_CHOICES = [
        ('asap', 'ASAP'),
        ('1-3', '1-3 months'),
        ('3-6', '3-6 months'),
        ('6+', '6+ months'),
        ('exploring', 'Just exploring'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)

    company_name = models.CharField(max_length=150, blank=True)
    website_url = models.URLField(blank=True)

    project_types = models.JSONField(blank=True, null=True)
    budget = models.CharField(max_length=20, choices=BUDGET_CHOICES, blank=True)
    timeline = models.CharField(max_length=20, choices=TIMELINE_CHOICES, blank=True)

    project_details = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"

# models.py

class ContactInquiry(models.Model):
    INTEREST_CHOICES = [
        ("web_development", "Web Development"),
        ("python_scripts", "Python Scripts"),
        ("ai_integration", "AI Integration"),
        ("instagram_automation", "Instagram Automation"),
        ("facebook_automation", "Facebook Automation"),
        ("whatsapp_automation", "WhatsApp Automation"),
        ("tally_automation", "Tally Automation"),
        ("custom_software", "Custom Software"),
        ("other", "Other"),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    interest = models.CharField(max_length=50, choices=INTEREST_CHOICES)
    message = models.TextField()

    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} – {self.interest}"



class WebProjectInquiry(models.Model):

    SERVICE_CHOICES = [
        ("website-development", "Website Development"),
        ("e-commerce-development", "E-commerce Development"),
        ("custom-web-app", "Custom Web App"),
        ("authentication-systems", "Authentication Systems"),
        ("automation/bots", "Automation / Bots"),
        ("crm-development", "CRM Development"),
        ("mobile-app", "Mobile App"),
        ("ai/ml-integration", "AI / ML Integration"),
        ("api-development", "API Development"),
        ("other", "Other"),
    ]

    # Core fields (direct form mapping)
    full_name = models.CharField(max_length=150)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, blank=True)

    service_type = models.CharField(
        max_length=50,
        choices=SERVICE_CHOICES
    )

    project_requirements = models.TextField()

    # Hidden SEO / attribution fields
    service_page = models.CharField(
        max_length=150
    )
    source_city = models.CharField(
        max_length=100
    )

    # Metadata (backend only)
    created_at = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(blank=True)

    def __str__(self):
        return f"{self.full_name} | {self.get_service_type_display()}"


class PythonProjectInquiry(models.Model):

    SERVICE_CHOICES = [
        ("automation", "Automation Script"),
        ("scraping", "Web Scraping Script"),
        ("api", "API Integration Script"),
        ("data", "Data Processing Script"),
        ("ai", "AI / ML Script"),
        ("other", "Other"),
    ]

    # Core form fields
    full_name = models.CharField(max_length=150)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, blank=True)

    service_type = models.CharField(
        max_length=30,
        choices=SERVICE_CHOICES
    )

    project_requirements = models.TextField()

    # Hidden SEO / attribution fields
    service_page = models.CharField(
        max_length=150,
        default="Python Automation Services Delhi"
    )
    source_city = models.CharField(
        max_length=100,
        default="Delhi"
    )

    # Backend metadata
    created_at = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(blank=True)

    def __str__(self):
        return f"{self.full_name} | {self.get_service_type_display()}"



class AIProjectInquiry(models.Model):

    SERVICE_CHOICES = [
        ("chatbot", "Chatbot Integration"),
        ("llm", "LLM Integration"),
        ("automation", "AI Automation"),
        ("search", "Semantic Search / RAG"),
        ("document", "Document AI"),
        ("custom", "Custom / Advanced AI"),
    ]

    # Core form fields
    full_name = models.CharField(max_length=150)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, blank=True)

    service_type = models.CharField(
        max_length=30,
        choices=SERVICE_CHOICES
    )

    project_requirements = models.TextField()

    # SEO / attribution fields
    service_page = models.CharField(max_length=200)
    source_city = models.CharField(max_length=100)

    # Backend metadata
    created_at = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(blank=True)

    def __str__(self):
        return f"{self.full_name} | {self.get_service_type_display()}"


class InstagramAutomationInquiry(models.Model):
    SERVICE_CHOICES = [
        ("automation", "Automation Bot"),
        ("scheduling", "Content Scheduling"),
        ("hashtags", "Hashtag System"),
        ("analytics", "Analytics Dashboard"),
        ("lead-gen", "Lead Generation"),
        ("influencer", "Influencer Tool"),
    ]

    full_name = models.CharField(max_length=150)
    email = models.EmailField()
    instagram_username = models.CharField(max_length=100, blank=True)

    service_type = models.CharField(
        max_length=30,
        choices=SERVICE_CHOICES
    )

    project_requirements = models.TextField()

    service_page = models.CharField(max_length=200)
    source_city = models.CharField(max_length=100)

    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Instagram Automation Inquiry"
        verbose_name_plural = "Instagram Automation Inquiries"

    def __str__(self):
        return f"{self.full_name} - {self.get_service_type_display()}"
    

class FacebookAutomationInquiry(models.Model):
    SERVICE_CHOICES = (
        ("messenger", "Messenger Bot"),
        ("comment", "Comment Automation"),
        ("lead", "Lead Form Automation"),
        ("crm", "CRM Integration"),
        ("ai", "AI Messaging Funnel"),
        ("full", "Full Automation Suite"),
    )

    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    facebook_page_name = models.CharField(max_length=150, blank=True)
    service_type = models.CharField(
        max_length=20, choices=SERVICE_CHOICES
    )
    project_requirements = models.TextField()

    service_page = models.CharField(max_length=200)
    source_city = models.CharField(max_length=100)

    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} – Facebook {self.get_service_type_display()}"
    

class WhatsAppAutomationInquiry(models.Model):

    SERVICE_CHOICES = (
        ("custom", "Custom WhatsApp Automation"),
        ("Starter", "Starter"),
        ("Business", "Business"),
        ("Enterprise", "Enterprise"),
    )

    full_name = models.CharField(max_length=120)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, blank=True)

    service_type = models.CharField(
        max_length=20,
        choices=SERVICE_CHOICES
    )

    project_requirements = models.TextField()

    service_page = models.CharField(max_length=255)
    source_city = models.CharField(max_length=100)

    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} | WhatsApp Automation"


class TallyAutomationInquiry(models.Model):

    SERVICE_CHOICES = [
        ("custom", "Custom Tally Automation"),
        ("Basic", "Basic"),
        ("Professional", "Professional"),
        ("Enterprise", "Enterprise"),
    ]

    full_name = models.CharField(max_length=150)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, blank=True)

    service_type = models.CharField(
        max_length=20,
        choices=SERVICE_CHOICES,
        default="custom"
    )

    project_requirements = models.TextField()

    service_page = models.CharField(max_length=200)
    source_city = models.CharField(max_length=100)

    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.get_service_type_display()}"


