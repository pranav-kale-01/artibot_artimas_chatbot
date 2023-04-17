from googletrans import Translator

def find_str(s, char):
    index = 0

    if char in s:
        c = char[0]
        for ch in s:
            if ch == c:
                if s[index:index+len(char)] == char:
                    return index

            index += 1

    return -1

def translate_text_logic( input_text ): 
    start_ind = find_str(input_text, 'translate ') 
    end_ind = find_str(input_text, 'to ')
    
    translate_text = input_text[start_ind+len('translate'):end_ind]
    translate_language = input_text.split("to",1)[1]

    # finding the language to convert into
    if 'marathi' in translate_language: 
        translate_language = "mr"
    elif 'hindi' in translate_language: 
        translate_language = "hi"

    
    print( translate_text )
    print( translate_language )

    translator = Translator(service_urls=['translate.googleapis.com']) 
    output = translator.translate( translate_text, dest=translate_language )
    return output.text