from .models import Response

#This function returns a dictionary that is used as the context for views.py to output the data
# from my survey. This would be better implemented as model form methods, but I have not seen an 
# example of Django model forms methods used on the internet. 

def createResultSContextDictionary(WorkDict, TOTAL_RESPONSES):

    try:
        return int((Response.objects.filter(Question1 = 'Yes').count()))
    except ZeroDivisionError:
        return 1

    WorkDict = {                                                         
                                                                              
        'Q1_A': int((Response.objects.filter(Question1 = 'Yes').count() / TOTAL_RESPONSES) * 100),
        'Q1_B': int((Response.objects.filter(Question1 = 'No').count()/ TOTAL_RESPONSES) * 100),
        'Q1_C': int((Response.objects.filter(Question1 = 'Maybe').count()/ TOTAL_RESPONSES) * 100),
        'Q1_D': int((Response.objects.filter(Question1 = 'idk').count() / TOTAL_RESPONSES) * 100),
        'Q2_A': int((Response.objects.filter(Question2 = 'Yes').count() / TOTAL_RESPONSES) * 100),
        'Q2_B': int((Response.objects.filter(Question2 = 'No').count() / TOTAL_RESPONSES) * 100),
        'Q3_A': int((Response.objects.filter(Question3 = 'Please God').count() / TOTAL_RESPONSES) * 100),
        'Q3_B': int((Response.objects.filter(Question3 = 'Panspermia').count() / TOTAL_RESPONSES) * 100),
        'Q3_C': int((Response.objects.filter(Question3 = 'Persist').count() / TOTAL_RESPONSES) * 100),
        'Q3_D': int((Response.objects.filter(Question3 = 'Idealism').count() / TOTAL_RESPONSES) * 100),
        'Q4_A': int((Response.objects.filter(Question4 = 'Physiological').count() / TOTAL_RESPONSES) * 100),
        'Q4_B': int((Response.objects.filter(Question4 = 'Safety').count() / TOTAL_RESPONSES) * 100),
        'Q4_C': int((Response.objects.filter(Question4 = 'Education conditional').count() / TOTAL_RESPONSES) * 100),
        'Q4_D': int((Response.objects.filter(Question4 = 'Education unconditional').count() / TOTAL_RESPONSES) * 100),
        'Q5_A': int((Response.objects.filter(Question5 = 'Humans').count() / TOTAL_RESPONSES) * 100),
        'Q5_B': int((Response.objects.filter(Question5 = 'Alien Intervention').count() / TOTAL_RESPONSES) * 100),
        'Q5_C': int((Response.objects.filter(Question5 = 'Divine Intervention').count() / TOTAL_RESPONSES) * 100)
    }

    return WorkDict