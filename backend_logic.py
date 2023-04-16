import pandas as pd 
from chatterbot.utils import print_progress_bar
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
from os.path import exists
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

def train_csv( csv_file ): 
    # reading dataset 
    df = pd.read_csv( csv_file, sep=',' )

    for index, row in df.iterrows(): 
        conv = []
        for i in row: 
            if type(i) == str: 
                conv.append( i )
        
        conv_dataset.append( conv )

        if index == 1000: 
            break

@csrf_exempt
def get_response_from_bot( request, *args, **kwargs ):
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)

        # Get a response to an input statement
        res_string = chatbot.get_response(body_data['input_text'])
        response = JsonResponse( {'ans': str( res_string ) } )

        return response

# flag to check if db exists so training is done only once
db_exists = exists('db.sqlite3')

# dataset which stores all the data
conv_dataset = [] 

# training for casual data and artimas data 
# train_csv( 'casual_data_windows.csv' )
train_csv( 'artimas_data.csv' )

# creating instance of chatbot 
chatbot = ChatBot( 
    'Artibot',
    logic_adapters=[
        {
            'import_path': 'custom_logic_adapter.CustomLogicAdapter'
        },
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': "I am sorry, I don't get it",
            'maximum_similarity_threshold': 0.70
        },
        'chatterbot.logic.MathematicalEvaluation',      
    ]
)

if not db_exists:
    trainer = ListTrainer( chatbot, show_training_progress=False  )

    # training using the reddit dataset
    dataset_len = len( conv_dataset )

    print("Total Size : ", dataset_len, "records " )

    for k, conversation in enumerate( conv_dataset ): 
        print_progress_bar('training progress', k, dataset_len-1 )
        trainer.train( conversation )    

    print()
