from .models import Response

#This function returns a dictionary that is used as the context for views.py to output the data
# from my survey. This would be better implemented as model form methods, but I have not seen an 
# example of Django model forms methods used on the internet. 

def createResultSContextDictionary(WorkDict, TOTAL_RESPONSES):

    # Need to find a way to prevent divide by 0
    # Option 1, implement logic.
    # Option 2, generate a bunch of objects so there's never 0 instances of 1 response. 

    #Q1A, Q1B, Q1C, Q1D, Q2A, Q2B, Q3A, Q3B, Q3C, Q3D, Q4A, Q4B, Q4C, Q4D, Q5A, Q5B, Q5C  = 0
    Q1A = Response.objects.filter(Question1 = 'Yes').count()
    Q1B = Response.objects.filter(Question1 = 'No').count()
    Q1C = Response.objects.filter(Question1 = 'Maybe').count()
    Q1D = Response.objects.filter(Question1 = 'idk').count()
    Q2A = Response.objects.filter(Question2 = 'Yes').count()
    Q2B = Response.objects.filter(Question2 = 'No').count()
    Q3A = Response.objects.filter(Question3 = 'Please God').count()
    Q3B = Response.objects.filter(Question3 = 'Panspermia').count()
    Q3C = Response.objects.filter(Question3 = 'Persist').count()
    Q3D = Response.objects.filter(Question3 = 'Idealism').count()
    Q4A = Response.objects.filter(Question4 = 'Physiological').count()
    Q4B = Response.objects.filter(Question4 = 'Safety').count()
    Q4C = Response.objects.filter(Question4 = 'Education conditional').count()
    Q4D = Response.objects.filter(Question4 = 'Education unconditional').count()
    Q5A = Response.objects.filter(Question5 = 'Humans').count()
    Q5B = Response.objects.filter(Question5 = 'Alien Intervention').count()
    Q5C = Response.objects.filter(Question5 = 'Divine Intervention').count()
    
    Q1A = Percentage(Q1A, TOTAL_RESPONSES)
    Q1B = Percentage(Q1B, TOTAL_RESPONSES)
    Q1C = Percentage(Q1C, TOTAL_RESPONSES)
    Q1D = Percentage(Q1D, TOTAL_RESPONSES)
    Q2A = Percentage(Q2A, TOTAL_RESPONSES)
    Q2B = Percentage(Q2B, TOTAL_RESPONSES)
    Q3A = Percentage(Q3A, TOTAL_RESPONSES)
    Q3B = Percentage(Q3B, TOTAL_RESPONSES)
    Q3C = Percentage(Q3C, TOTAL_RESPONSES)
    Q3D = Percentage(Q3D, TOTAL_RESPONSES)
    Q4A = Percentage(Q4A, TOTAL_RESPONSES)
    Q4B = Percentage(Q4B, TOTAL_RESPONSES)
    Q4C = Percentage(Q4C, TOTAL_RESPONSES)
    Q4D = Percentage(Q4D, TOTAL_RESPONSES)
    Q5A = Percentage(Q5A, TOTAL_RESPONSES)
    Q5B = Percentage(Q5B, TOTAL_RESPONSES)
    Q5C = Percentage(Q5C, TOTAL_RESPONSES)


    WorkDict = {                                                         
                                                                              
        'Q1_A': Q1A,
        'Q1_B': Q1B,
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


# We need to calculate votes as a percentage users. If the vote count is 0 for a given response,
# then just return 0 to prevent a divide by 0 error when calculating the percentage. 
def Percentage(count, total_responses):
    if count == 0:                       # Prevent divide by 0 error.
        return 0
    proportion = count / total_responses # Calculate percentage
    percent = proportion * 100
    percent = int(percent) # Return percentage as a whole number, for now.
    return percent

