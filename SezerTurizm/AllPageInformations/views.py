from django.views.generic import TemplateView

class HomeView(TemplateView):
    """Class-based view for the home page using TemplateView.
    
    Methods:
        get_context_data: Return context data for the home page.
    """

    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        """Return the context data for the home page.

        Returns:
            dict: Context data for the home page.
        """
        context = super().get_context_data(**kwargs)
        # You can add additional context data here, if needed.

        return context