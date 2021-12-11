from .models import Response

def createResultSContextDictionary(WorkDict, TOTAL_RESPONSES):

    WorkDict = {                                                         
                                                                                # This is the dictionary 
        'Q1_A': (Response.objects.filter(Question1 = 'Yes').count() / TOTAL_RESPONSES) * 100, # for all my context objects
        'Q1_B': (Response.objects.filter(Question1 = 'No').count()/ TOTAL_RESPONSES) * 100,                  # for the Responces to the 
        'Q1_C': (Response.objects.filter(Question1 = 'Maybe').count()/ TOTAL_RESPONSES) * 100,           # the questionaire. This would 
        'Q1_D': (Response.objects.filter(Question1 = 'idk').count() / TOTAL_RESPONSES) * 100,             # be better implemented as 
        'Q2_A': (Response.objects.filter(Question2 = 'Yes').count() / TOTAL_RESPONSES) * 100,             # Model Methods, but I have not
        'Q2_B': (Response.objects.filter(Question2 = 'No').count() / TOTAL_RESPONSES) * 100,              # seen an example of how model
        'Q3_A': (Response.objects.filter(Question3 = 'Please God').count() / TOTAL_RESPONSES) * 100,      # methods are handeled in the 
        'Q3_B': (Response.objects.filter(Question3 = 'Panspermia').count() / TOTAL_RESPONSES) * 100,      # views.py 
        'Q3_C': (Response.objects.filter(Question3 = 'Persist').count() / TOTAL_RESPONSES) * 100,
        'Q3_D': (Response.objects.filter(Question3 = 'Idealism').count() / TOTAL_RESPONSES) * 100,
        'Q4_A': (Response.objects.filter(Question4 = '1').count() / TOTAL_RESPONSES) * 100,
        'Q4_B': (Response.objects.filter(Question4 = '2').count() / TOTAL_RESPONSES) * 100,
        'Q4_C': (Response.objects.filter(Question4 = '3').count() / TOTAL_RESPONSES) * 100,
        'Q4_D': (Response.objects.filter(Question4 = 'none').count() / TOTAL_RESPONSES) * 100,
        'Q5_A': (Response.objects.filter(Question5 = 'Humans').count() / TOTAL_RESPONSES) * 100,
        'Q5_B': (Response.objects.filter(Question5 = 'Alien Intervention').count() / TOTAL_RESPONSES) * 100,
        'Q5_C': (Response.objects.filter(Question5 = 'Divine Intervention').count() / TOTAL_RESPONSES) * 100
    }

    return WorkDict