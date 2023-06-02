import openai
import pyttsx3

openai.api_key = "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"

def llm(prompt) :
    res = openai.Completion.create(engine = "text-davinci-003",max_tokens = 256,temperature = 0.7,prompt = prompt)
    return res.choices[0].text


def findString(a) :
    f1s = a.index("1. ")
    f1e = a.index(":")
    first = a[f1s+3 : f1e] # gives 1st heading
    # print(first)
    a = a[f1e + 1 :]

    f2s = a.index("2. ")

    firstDes = a[:f2s-2] # gives 1st description
    # print(firstDes)

    f2e = a.index(":")
    second = a[f2s+3 : f2e] # gives 2nd heading
    # print(second)
    a = a[f2e + 1 :]

    f3s = a.index("3. ")

    secondDes = a[:f3s-2] # gives 2nd description
    # print(secondDes)

    f3e = a.index(":")
    third = a[f3s+3 : f3e] # gives 3rd heading
    a = a[f3e+1:] # gives 3rd description
    # print(a)
    # print(third)


    return [first,firstDes,second,secondDes,third,a]


ans = findString(a)

prompt="INPUT={focus}\nOUTPUT={description} \n ![IMG] (https://image.pollinations.ai/prompt/{description})\n{description} ={focusDetailed),%20(adjective1},%20(adjective2},%20(visualStyle1},%20(visualStyle2),%20(visual Style3),%20{artistReference}\nINPUT={0}\nOUTPUT={1}\nINPUT={2}\nOUTPUT={3}\nINPUT={4}\nOUTPUT={5}".format(ans[0],ans[1],ans[2],ans[3],ans[4],ans[5])
ans = llm(prompt)
print(ans)