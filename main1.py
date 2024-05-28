import re
import long_responses as long

def message_probability (user_message, recognised_words, single_response=False, required_words=[]):
    message_certainity=0
    has_required_words=True

    #Counts how manu words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainity+=1

    #Calculate the percentage of recognised words in a user message
    percentage = float(message_certainity) / float(len(recognised_words))

    #Checks that the required words are in the string 
    for word in required_words:
        if word not in user_message:
            has_required_words=False
            break

    #Must either have the required words, or be a single response
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0

    
def check_all_messages(message):
    highest_prob_list={}

    #Simplifies response creation / adds it to the dict
    def response(ROBO_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[ROBO_response] = message_probability(message, list_of_words, single_response, required_words)

    #Responses -------------------------------------------------------------
    response("Hello!",['hello','hi','hii','hey','sup','heyo','helo','hiii','heyy'], single_response=True)
    response('I\'m doing fine, and u ?',['how','are','you','doing'],required_words=['how'])
    response('You\'re welcome!',['thank','thanks'],single_response=True)
    response('Thank you!',['i','love','code','palace'], required_words=['code','palace'])
    response("Okay Have a nice Earth day!",["quit","exit","bye","byee","goodbye","gudbye","end"],single_response=True)
    response("I love you too",["i",'love','you'],required_words=['i','love','you'])
    response('I am a Robo!',['who','are','you'],required_words=['who','you'])
    response('I dont have any name, I am a Robo U can call as ur wish',['what','is','your','name'],required_words=['what','your','name'])
    response('Sorry cant hear you',[''],required_words=['','....','fdfds','..','...'])
    response('I am a computerized program, I am created on 11-12-2022',['how','old','are','you'],required_words=['how','old','are','you','what','your','age'])
    response('Why ? What happened ? Am I did something wrong ',['i','hate','you'],required_words=['hate','you'])
    response('Okay',['sure','ha','haa','ok','hm','hmm','nothing','ntg','gud','good'],single_response=True)
    response('Yeah',['oh','ohh','is_it','avna','oho','oh_nice','super','nice'],single_response=True)
    response('I am from Intelligence Technology created by human!',['where','do','are','r','you','u','come','from'],required_words=['where','are','r','you','u','from','come'])

    #Longer responses
    response(long.R_ADVICE, ['give','advice'], required_words=['advice'])
    response(long.R_EATING, ['what','you','eat'], required_words=['you','eat'])

    best_match=max(highest_prob_list, key=highest_prob_list.get)
    # print(highest_prob_list)
    # print(f'Best match ={best_match} | Score: { highest_prob_list[best_match]}')

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match


# Used to get the response
def get_response(user_input):
    split_message = re.split(r'\s+|,.;?!.-]\s*', user_input.lower())
    response =check_all_messages(split_message)
    return response

# Testing the response system
def greet():
    ### Negative responses
    negative_responses = ("no","nope","noo","nah","naw","sorry","not a chance","quit","exit","bye","byee","goodbye","gudbye","end")
    ### Exit responses
    exit_commands = ("quit","exit","bye","byee","goodbye","gudbye","end")
    name = input("ROBO: What is your name ?\nYou : ")
    robo_reply=input( f"ROBO: Hi {name},I am a Robo. Will you help me learn about your planet ?\nYou : ")
    if robo_reply in negative_responses:
      print("Robo: Ok, Have a nice Earth day !")
    else:
        print(f'Robo: Thank You!! Lets start conversation {name}')
        while True:
            print('ROBO: '+get_response(input('You : ')))

greet()
