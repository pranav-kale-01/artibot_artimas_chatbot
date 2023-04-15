from chatterbot.logic import LogicAdapter 
from chatterbot.logic import BestMatch
from chatterbot.conversation import Statement
from datetime import datetime

class CustomLogicAdapter(LogicAdapter): 
    def __init__(self, chatbot, **kwargs):
        self.chatbot = chatbot

        super().__init__(chatbot, **kwargs)

    def can_process(self, statement):
        if statement.text.startswith('Hey Artibot'):
            return True
        else:
            return True

    def process(self, input_statement, additional_response_selection_parameters):
        import random

        if input_statement.text.lower().startswith('hey artibot'):
            cur_time = datetime.now() 

            current_hour = int( cur_time.strftime("%H") )

            if( current_hour < 12 ): 
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

