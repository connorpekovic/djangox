from .models import Response

# This function returns a dictionary that is used as the context for views.py 
# to output the data from my survey. I wish I know how to implement this as a
# model method, but I have not seen doc on that. 
def createContextDictionary():

    TOTAL_RESPONSES = Response.objects.all().count() #Total number of votes.

    thisdict = {} #Create an empty dictionary to pass into django template as context.

    Q1A = 0
    Q1B = 0 
    Q1C = 0
    Q1D = 0

    Q1A = Response.objects.filter(Question1 = 'not legitimate').count()
    Q1B = Response.objects.filter(Question1 = 'legitimate earthly').count()
    Q1C = Response.objects.filter(Question1 = 'legitimate earthly few extraterrestrial').count()
    Q1D = Response.objects.filter(Question1 = 'legitimate extraterrestrial').count()
    
    #The function Percentage parm1=Total votes per choice parm2=Total # of responces
    Q1A = Percentage(Q1A, TOTAL_RESPONSES)
    Q1B = Percentage(Q1B, TOTAL_RESPONSES)
    Q1C = Percentage(Q1C, TOTAL_RESPONSES)
    Q1D = Percentage(Q1D, TOTAL_RESPONSES)


    WorkDict = {                                                         
                                                                              
        'Q1_A': Q1A,
        'Q1_B': Q1B,
        'Q1_C': Q1C,
        'Q1_D': Q1D,
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

