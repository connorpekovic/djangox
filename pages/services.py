from .models import Response

def RestAPI_ReturnContextDictionary():
    contextDictionary = {}
    return contextDictionary

# This function returns a python dictionary object will serve as  the context dictionary for views.py 
# The dictrionary contain percentages of the vote total each choice received. 
def createContextDictionary():


    # Initialize the variables that we will  the dictionary
    Q1A = 0
    Q1B = 0 
    Q1C = 0
    Q1D = 0

    # If there's 0 objects, querysets will abend the server, which is bad.
    # Try a query. If it fails (aka raises an EXCEPTion), return the dictionary to the caller.
    try:
        #Handel condition there is no 'Response' objects.
        isThere = Response.objects.all().count()
    except:
        # If the try block raises an error.
        # Load the context dictionary with defaults.
        ContextDictionary = {
            'Q1_A': Q1A,
            'Q1_B': Q1B,
            'Q1_C': Q1C,
            'Q1_D': Q1D,
        }
        return ContextDictionary



    # Start the Django query set's that load the variables with vote counts.
    Q1A = Response.objects.filter(Question1 = 'not legitimate').count()
    Q1B = Response.objects.filter(Question1 = 'legitimate earthly').count()
    Q1C = Response.objects.filter(Question1 = 'legitimate earthly few extraterrestrial').count()
    Q1D = Response.objects.filter(Question1 = 'legitimate extraterrestrial').count()
    
    # Take the percentage of those vote counts vs the total number of responces. 
    # The function Percentage is defined below.
    TOTAL_RESPONSES = Response.objects.all().count() #Total number of votes.
    Q1A = Percentage(Q1A, TOTAL_RESPONSES)
    Q1B = Percentage(Q1B, TOTAL_RESPONSES)
    Q1C = Percentage(Q1C, TOTAL_RESPONSES)
    Q1D = Percentage(Q1D, TOTAL_RESPONSES)

    # Load the context dictionary with percentages
    ContextDictionary = {

        'Q1_A': Q1A,
        'Q1_B': Q1B,
        'Q1_C': Q1C,
        'Q1_D': Q1D,
    }

    return ContextDictionary


# We need to calculate votes as a percentage users. If the vote count is 0 for a given response,
# then just return 0 to prevent a divide by 0 error when calculating the percentage.
#  parm1=Total votes per choice parm2=Total # of responces 
def Percentage(count, total_responses):
    if count == 0:                       # Prevent divide by 0 error.
        return 0
    proportion = count / total_responses # Calculate percentage
    percent = proportion * 100
    percent = int(percent) # Return percentage as a whole number, for now.
    return percent

