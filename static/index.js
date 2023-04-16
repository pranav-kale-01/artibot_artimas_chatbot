const arbody = document.querySelector(".ar-body");
const userinput = document.querySelector("#user-input");
const arsend = document.querySelector(".send");

// send.addEventListener("click", () => decodeusermessage());
arsend.addEventListener("click", () => decodeusermessage());

// when press enter then message should sent
userinput.addEventListener("keyup", (event) => {
    // checking the keycode = 13 because this is the code for enter key
    if(event.keyCode === 13){
        decodeusermessage();
    }
});

const decodeusermessage = () => {
    const text_input = userinput.value;
    rendermessage(text_input);
    userinput.value = "";
    // clearing the message after one is sent
    setTimeout(() => {
        decodebotsmessage(text_input);
    }, 600);
    if(arbody.scrollHeight > 0){
        arbody.scrollTop = arbody.scrollHeight;
    }
};

// Here users message is rendered (converted from text to text-node then text-node is appended to div element then div element is appeded to ar-body)
const rendermessage = (txt) => {
    let message_arrived = document.createElement("div");
    let text_node = document.createTextNode(txt);
    message_arrived.classList.add("message-by-user");
    // This adds the given CSS class to div element -> message_arrived
    message_arrived.append(text_node);
    arbody.append(message_arrived);
};

const decodebotsmessage = async (txt) => {
    const res = await getbotresponse(txt);
    let bots_message = document.createElement("div");
    let text_node = document.createTextNode(res);
    bots_message.classList.add("message-by-bot");
    bots_message.append(text_node);
    arbody.append(bots_message);
}

const getbotresponse = async (txt) =>  {
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");

    var raw = JSON.stringify({
    "input_text": txt
    });

    var requestOptions = {
        method: 'POST',
        headers: myHeaders,
        body: raw,
    };

    

    response = await fetch("http://127.0.0.1:8080/artibot/", requestOptions)
    result = ""

    if (response.ok) {
        await response.json().then( json => {
            result = json['ans'];
      });
    }

    console.log( result );
    return result;
};