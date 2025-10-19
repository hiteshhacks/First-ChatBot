import google.generativeai as genai
genai.configure(api_key="AIzaSyDCrWRQ6nZaBLqadtcncmSU88DslW7ZdzA")

for m in genai.list_models():
    print(m.name)
