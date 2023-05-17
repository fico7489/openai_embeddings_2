import openai, numpy as np
import json

def read_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        
    return data['data'][0]['embedding']

question_1 = read_json_file('question_1.json')
question_2 = read_json_file('question_2.json')
question_3 = read_json_file('question_3.json')
question_4 = read_json_file('question_4.json')

similarity_2 = np.dot(question_1, question_2)
similarity_3 = np.dot(question_1, question_3)
similarity_4 = np.dot(question_1, question_4)


print('similarity_2=' + str(similarity_2))
print('similarity_3=' + str(similarity_3))
print('similarity_4=' + str(similarity_4))
