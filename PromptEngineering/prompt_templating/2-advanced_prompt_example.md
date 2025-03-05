# Advanced prompting techniques

Reference : https://aiengineering.academy/PromptEngineering/prompt_engineering

Please refer to the `1-basic_prompt_example.md` file to see the detail of the function `get_completion`, it's basically requesting a AI model and getting back the answer.

## Few-shot prompts

In this technique, the idea is to sent a few examples of question-answers to the model, directly in the prompt, before to concatenate the desired question :

```
prompt = """The odd numbers in this group add up to an even number: 4, 8, 9, 15, 12, 2, 1.
A: The answer is False.

The odd numbers in this group add up to an even number: 17,  10, 19, 4, 8, 12, 24.
A: The answer is True.

The odd numbers in this group add up to an even number: 16,  11, 14, 4, 8, 13, 24.
A: The answer is True.

The odd numbers in this group add up to an even number: 17,  9, 10, 12, 13, 4, 2.
A: The answer is False.

The odd numbers in this group add up to an even number: 15, 32, 5, 13, 82, 7, 1. 
A:"""

messages = [
    {
        "role": "user",
        "content": prompt
    }
]

response = get_completion(messages)
print(response)
```

Answer:

```
Let's add up the odd numbers in the group: 15 + 5 + 13 + 7 + 1 = 41. Since 41 is an odd number, the statement is 
False.

So, the correct answer is:

A: The answer is False.
```

## Chain-of-Throught (CoT) Prompting

In this technique, the context will be to explain that you want the IA to follow a defined logical path, which might not be the most straightforward.
In this specific example, we explain how we represente a list of number and the mistaken one that we want to detect. Consequently the IA will follow our way of doing it.

```
prompt = """The odd numbers in this group add up to an even number: 4, 8, 9, 15, 12, 2, 1.
A: Adding all the odd numbers (9, 15, 1) gives 25. The answer is False.

The odd numbers in this group add up to an even number: 15, 32, 5, 13, 82, 7, 1. 
A:"""

messages = [
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
Let's add up the odd numbers: 15, 5, 13, 7, 1 = 41. The answer is False.
```


# Zero shot chain-of-though (Zero Shot CoT)

In this technique, you just admit that the model is smart enough to propose you the best way to display the result according to your request.
In the example we ask the AI to expose its way of thinking step by step.

```
prompt = """I went to the market and bought 10 apples. I gave 2 apples to the neighbor and 2 to the repairman. I then went and bought 5 more apples and ate 1. How many apples did I remain with?

Let's think step by step."""

messages = [
    {
        "role": "user",
        "content": prompt
    }
]

response = get_completion(messages)
print(response)
```

Answer: 
```
Let's break it down step by step:

1. You started with 10 apples.
2. You gave 2 apples to the neighbor, so you have 10 - 2 = 8 apples left.
3. You gave 2 apples to the repairman, so you have 8 - 2 = 6 apples left.
4. You bought 5 more apples, so you now have 6 + 5 = 11 apples.
5. You ate 1 apple, so you have 11 - 1 = 10 apples left.

So, you remain with 10 apples.
```
