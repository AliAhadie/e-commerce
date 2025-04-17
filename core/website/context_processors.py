from .forms import NewsLetterForm

def newsletter_form(request):
    return {'newsletter_form': NewsLetterForm()}