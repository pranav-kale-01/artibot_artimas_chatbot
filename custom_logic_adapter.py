from chatterbot.logic import LogicAdapter 
from chatterbot.logic import BestMatch
from chatterbot.conversation import Statement
from datetime import datetime
from mail_client import send_mail
from backend_logic import process_weather_information
from translate_logic import translate_text_logic
from google_search_logic import google_search

class CustomLogicAdapter(LogicAdapter): 
    email_flow = [ "Sure thing! Enter your mail-id so that the reciever knows who you are!. To exit the process at any time type 'cancel'", "Please Enter email address of the reciever", "Please tell me the subject of your mail", "Please Enter the body of the mail", "Enter confirm to send mail or cancel to cancel the process" ]
    email_details = []

    def __init__(self, chatbot, **kwargs):
        self.chatbot = chatbot

        super().__init__(chatbot, **kwargs)

    def can_process(self, statement):
        return True

    def process(self, input_statement, additional_response_selection_parameters):
        import random
        
        if( input_statement.text.lower().startswith('cancel') ): 
            CustomLogicAdapter.email_details = [] 

        elif (input_statement.text.lower().startswith('hey artibot') and ("google" in input_statement.text.lower() and "search" in input_statement.text.lower()) ): 
            result = google_search( input_statement.text )
            return Statement( result )
        
        elif (input_statement.text.lower().startswith('hey artibot') and ("translate" in input_statement.text.lower() and "to" in input_statement.text.lower()) ): 
            result = translate_text_logic( input_statement.text )
            print("result :", result )
            return Statement( result )

        elif (input_statement.text.lower().startswith('hey artibot') and ("get" in input_statement.text.lower() and "weather" in input_statement.text.lower()) ): 
            # calling the get weather function
            weather_info = process_weather_information( input_statement.text );            
            return Statement(weather_info)

        elif (input_statement.text.lower().startswith('hey artibot') and ("send" in input_statement.text.lower() and "mail" in input_statement.text.lower()) or 'index' in additional_response_selection_parameters ): 
            # checking if this is the final step
            if( 'index' in additional_response_selection_parameters and additional_response_selection_parameters['index'] == 5 ): 
                # checking if used entered to confirm or cancel 
                if input_statement.text.lower().startswith('confirm'): 
                    send_mail( CustomLogicAdapter.email_details )
                else: 
                    CustomLogicAdapter.email_details = []

                return Statement("Sending Email")
            else: 
                CustomLogicAdapter.email_details.append( input_statement.text )
                return Statement( CustomLogicAdapter.email_flow[ additional_response_selection_parameters['index'] if 'index' in additional_response_selection_parameters else 0 ] )
        
        elif input_statement.text.lower().startswith('hey artibot'):
            cur_time = datetime.now() 

            current_hour = int( cur_time.strftime("%H") )

            if( current_hour > 4 and current_hour < 12 ): 
                return Statement("Good morning! Currently it  is : " + cur_time.strftime("%Y-%m-%d %H:%M:%S") )
            elif ( current_hour > 12 and current_hour < 14 ): 
                return Statement("Good Afternnon! Currently it is : " + cur_time.strftime("%Y-%m-%d %H:%M:%S") )
            else :
                return Statement("Good evening! Currently it is : " + cur_time.strftime("%Y-%m-%d %H:%M:%S") )
            
        else:
            # Randomly select a confidence between 0 and 1
            confidence = random.uniform(0, 1)

            # For this example, we will just return the input as output
            selected_statement = BestMatch( self.chatbot ).process( input_statement )
            selected_statement.confidence = confidence

            return selected_statement

