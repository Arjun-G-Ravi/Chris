import openai

f = open("C:\\Users\\Home\\Desktop\\Programs\\keyOpenAI.txt",'r')
key = f.read()
f.close()
openai.api_key = key
while True:
    prompt = input("Enter prompt: ")
    response = openai.Completion.create(model="text-davinci-003", prompt=prompt, temperature=0.7, max_tokens=30)
    print(response["choices"][0]["text"])
    # print(response["choices"][0])
    