from .models import Response

#This function returns a dictionary that is used as the context for views.py to output the data
# from my survey. This would be better implemented as model form methods, but I have not seen an 
# example of Django model forms methods used on the internet. 

def createResultSContextDictionary(WorkDict, TOTAL_RESPONSES):

    # Need to find a way to prevent divide by 0
    # Option 1, implement logic.
    # Option 2, generate a bunch of objects so there's never 0 instances of 1 response. 

    Q1Yes = 0
    Q1Yes = Response.objects.filter(Question1 = 'Yes').count()
    Q1Yes = Percentage(Q1Yes, TOTAL_RESPONSES)

    WorkDict = {                                                         
                                                                              
        'Q1_A': Q1Yes,
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


# We need to calculate votes as a percentage users. If the vote count is 0 for a given response,
# then just return 0 to prevent a divide by 0 error when calculating the percentage. 
def Percentage(count, total_responses):
    if count == 0:                       # Prevent divide by 0 error.
        return 0
    proportion = count / total_responses # Calculate percentage
    percent = proportion * 100
    percent = int(percent) # Return percentage as a whole number, for now.
    return percent

