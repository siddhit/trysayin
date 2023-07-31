from django.shortcuts import render
from trysayin_project import settings


def index(request):
    # Define any initial context variables here if needed
    context = {}

    if request.method == 'POST':
        # Retrieve user input from the form
        name = request.POST.get('name', '') # name should match the name attribute of your input
        
        # Process the user input and generate the ARPAbet code and IPA format
        arpabet_code = convert_to_arpabet(name)
        ipa_format = convert_to_ipa(arpabet_code)

        # Add the converted data to the context to be diplayed in the template
        context['name'] = name
        context['arpabet_code'] = arpabet_code
        context['ipa_format'] = ipa_format

    # Render the index.html tempalte with the context
    return render(request, 'index.html')