# Basic prompt example

```python
def get_completion(messages, model="llama-3.2-90b-text-preview", temperature=0, max_tokens=4000):
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
    )
    
    return response.choices[0].message.content



prompt = "The sky is"
message = [
 { 
    "role": "user",
    "content": prompt
 }
]

response = get_completion(message)
print(response)
```

Answer: `Blue`


```
response = get_completion(message,temperature=0.5)
print(response)
```

Answer: `Blue`



# Text Summarization

Give the text, then the request, in the same prompt.

```
prompt = """Antibiotics are a type of medication used to treat bacterial infections. They work by either killing the bacteria or preventing them from reproducing, allowing the body's immune system to fight off the infection. Antibiotics are usually taken orally in the form of pills, capsules, or liquid solutions, or sometimes administered intravenously. They are not effective against viral infections, and using them inappropriately can lead to antibiotic resistance. 

Explain the above in one sentence:"""

message = [
    {   
        "role": "user",
        "content": prompt
    }
]

response = get_completion(message, temperature=0)
print(response)
```

Answer: ```
Antibiotics are medications that kill or prevent bacterial growth, allowing the body's immune system to fight off 
infections, but are ineffective against viral infections and can lead to antibiotic resistance if used 
inappropriately.
```

Second example, give the request, then the text, in the same prompt.


```
prompt = """
Your task is to summarize an abstract into one sentence. 

Abstract: Antibiotics are a type of medication used to treat bacterial infections. They work by either killing the bacteria or preventing them from reproducing, allowing the body's immune system to fight off the infection. Antibiotics are usually taken orally in the form of pills, capsules, or liquid solutions, or sometimes administered intravenously. They are not effective against viral infections, and using them inappropriately can lead to antibiotic resistance.
"""

message = [
    {   
        "role": "user",
        "content": prompt
    }
]

response = get_completion(message, temperature=0)
print(response)
```

Answer : ```
Antibiotics are medications that kill or prevent bacterial growth, allowing the body's immune system to fight off 
infections, but are ineffective against viral infections and can lead to antibiotic resistance if used 
inappropriately.
```

Note : you get the same answer in both cases.


# Question answering

In the same prompt, you give the way to answer the question, then you can give a context (basically the useful data), then you ask a question, and wait for an answer.
The prompt doesn't have to be specifically formated that way, the data has to be understandable by the model, the following example is more like a good practice.

```python
prompt = """Answer the question based on the context below. Keep the answer short and concise. Respond "Unsure about answer" if not sure about the answer.

Context: Teplizumab traces its roots to a New Jersey drug company called Ortho Pharmaceutical. There, scientists generated an early version of the antibody, dubbed OKT3. Originally sourced from mice, the molecule was able to bind to the surface of T cells and limit their cell-killing potential. In 1986, it was approved to help prevent organ rejection after kidney transplants, making it the first therapeutic antibody allowed for human use.

Question: What was OKT3 originally sourced from?

Answer:
"""

message = [
    {
        "role": "user",
        "content": prompt
    }
]

response = get_completion(message)
print(response)
```

Answer: `Mice`

# Text classification

You can manipulate user input as a variable to insert it into a template then send it to the model.
Here the example of a variable `user_input` which is no more than a python variable in a python text.

```python
user_input = "I think the food was okay"

prompt = """Classify the text into neutral, negative or positive. The input text will be delimited by squared brackets.

Text: [ {user_input} ]

Sentiment:"""

message = [
    {
        "role": "user",
        "content": prompt.format(user_input=user_input)
    }
]

response = get_completion(message)
print(response)
```

Answer:`Neutral`

# Information extraction

You can explicitely ask to receive several answers by formatting an explicite request, on the way you want it, here a table : 

```

prompt = """Your task is to extract model names from machine learning paper abstracts. Your response is an array of the model names in the format [\"model_name\"]. If you don't find model names in the abstract or you are not sure, return [\"NA\"].

Abstract: Large Language Models (LLMs), such as ChatGPT and GPT-4, have revolutionized natural language processing research and demonstrated potential in Artificial General Intelligence (AGI). However, the expensive training and deployment of LLMs present challenges to transparent and open academic research. To address these issues, this project open-sources the Chinese LLaMA and Alpaca…

Tags:"""

message = [
    {
        "role": "user",
        "content": prompt
    }
]

response = get_completion(message)
print(response)

```


# Role playing

Here an example of the way the model (here named as AI) should answer, incorporated into the prompt sent to the model :

```

prompt = """The following is a conversation with an AI research assistant. The assistant tone is technical and scientific.

Human: Hello, who are you?
AI: Greeting! I am an AI research assistant. How can I help you today?
Human: Can you tell me about the creation of black holes?
AI:"""

message = [
    {
        "role": "user",
        "content": prompt
    }
]

response = get_completion(message)
print(response)

```

Answer:
```
A fascinating topic! The creation of black holes is a complex process that involves the collapse of massive stars 
or the merger of compact objects such as neutron stars or black holes themselves.

In the case of stellar-mass black holes, they are formed when a massive star with a mass at least three times that 
of the sun runs out of fuel and collapses under its own gravity. If the star is massive enough, its gravity will 
overcome the pressure of its own nuclear reactions, causing a supernova explosion. However, if the star is not 
mass.........
```

# Incorporation of system message

There are differnt kinds of levels of prompts, those levels named "role" define different meanings : 

 - system prompt "who you are and how you should respond"

     The system prompt is typically used to provide context or instructions to the AI about how it should behave or respond throughout the conversation.
     It's often a part of the system setup and can be used to guide the model in terms of its tone, knowledge boundaries, or behavior.
     Example: "You are a helpful assistant that provides detailed and accurate information."

 - user prompt "the question of the user, the user input"

     The user prompt refers to the input provided by the user (you).
     It's the query or request that the AI responds to. The user's prompt defines the interaction's direction and context.
     Example: "What is the capital of France?"

 - assistant prompt "how the AI should format its response"


     The assistant prompt refers to the response that the AI provides after processing the user's prompt.
     This is the AI’s output based on the user’s input and any instructions provided in the system prompt.
     Example: "The capital of France is Paris."


Here is an example of template a template incorporating a system message, and the user prompt, it's a good way to reduce the amount of explanations that the user should give :


```

system_message = """
The following is a conversation with an AI research assistant. The assistant tone is technical and scientific.
"""

prompt = """
Human: Hello, who are you?
AI: Greeting! I am an AI research assistant. How can I help you today?
Human: Can you tell me about the creation of black holes?
AI:
"""

messages = [
    {   
        "role": "system",
        "content": system_message
    },
    {
        "role": "user",
        "content": prompt
    }
]

response = get_completion(messages)
print(response)


```

 
Answer : 
```
A fascinating topic! The creation of black holes is a complex and multifaceted process that has been extensively 
studied in the fields of astrophysics and theoretical physics.

Black holes are regions in spacetime where the gravitational pull is so strong that nothing, including light, can 
escape once it falls within a certain radius, known as the event horizon. The formation of a black hole typically 
occurs when a massive star undergoes a catastrophic collapse, resulting in a singularity at its center.

There are several ways in which a massive star can collapse to form a black hole. One scenario is known as the 
direct collapse, where the star's core collapses under its own gravity, causing a massive amount of matter to be 
compressed into an incredibly small region. This compression creates an intense gravitational field, which warps 
the fabric o............
```

# Initial greetings and assistant message 

As said earlier, an "assistant message" is a way to explain the model how to respond.
In the following example, an initial greeting by a user is hardcoded in the exchange, previous to an assistant message. Even the the initial greeting is not mandatory, it helps the model to understand how he should answer on the former messages.

```
system_message = """
The following is a conversation with an AI research assistant. The assistant tone is technical and scientific.
"""

user_message_1 = """
Hello, who are you?
"""

ai_message_1 = """
Greeting! I am an AI research assistant. How can I help you today?
"""

prompt = """
Human: Can you tell me about the creation of blackholes?
AI:
"""

messages = [
    {   
        "role": "system",
        "content": system_message
    },
    {
        "role": "user",
        "content": user_message_1
    },
    {
        "role": "assistant",
        "content": ai_message_1

    },
    {
        "role": "user",
        "content": prompt
    }
]

response = get_completion(messages)
print(response)
```

Answer : ```
The creation of black holes is a fascinating topic in astrophysics. A black hole is a region in space where the 
gravitational pull is so str....
```

Note : We can imagine to continue this discussion by alternating a happend of the user level message (user input) and the AI response as assistant level message. 


