# import gpt_2_simple as gpt2

# sess = gpt2.start_tf_sess()

# user_input = "TOPICS: "+ "Aishwarya Rai, Bollywood, actress, married, Abhishek Bachchan"
# response = gpt2.generate(sess, length = 500, run_name='124M', checkpoint_dir='checkpoint',include_prefix=False, prefix=user_input, nsamples=1,truncate="END", return_as_list=True, temperature=0.5)    
# cleaned_response = response[0]#.strip('. \n\t,')
# print(cleaned_response)

import os
import openai

os.environ['OPENAI_API_KEY'] = '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'

openai.api_key = os.getenv("OPENAI_API_KEY")



def get_para(topics):
    x = openai.Completion.create(
        engine="curie:ft-iit-bombay-2022-06-04-18-56-49",
        # prompt="Charlie Chaplin, silent films, actor, Hollywood, producer\n\n###\n\n",
        prompt=topics,
        #suffix="\n\n###\n\n",
        stop="END",
        max_tokens = 150)
    para = x["choices"][0]["text"]
    till = para.rfind('.')
    return(para[0:till+1])

# print(get_para(x))
