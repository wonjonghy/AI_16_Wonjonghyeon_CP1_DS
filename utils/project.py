import re
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from transformers import pipeline
from pykospacing import Spacing

class Summary():

    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("wjh203/project-cp1")
        self.model = AutoModelForSeq2SeqLM.from_pretrained("wjh203/project-cp1")
        self.remove_lst = ['[\u2e80-\u2eff\u31c0-\u31ef\u3200-\u32ff\u3400-\u4dbf\u4e00-\u9fbf\uf900-\ufaff]', '(http(s)?:\/\/)([a-z0-9\w]+\.*)+[a-z0-9]{2,4}', '[a-z]+[.][a-z]+[.][a-z]+[.][a-z]', '[\u25b4\u2015]', '[⊙·■#▲▶…☎ㆍ「」─｢｣『』․ \n]', '[a-z]+[.][a-z]+[.][a-z]+[/][a-z]+', '\d+[-]\d+[-]\d+', '\(\)', '\( \)', '\]', '\(  \)']
    
    def open_txt(self, txt_file):
        file = open(txt_file, "r")
        test_txt=file.read()
        return test_txt

    def preprocess(self, test_txt):
        for i in self.remove_lst:
            test_txt=re.sub(i, '', test_txt)

        spacing = Spacing()
        result = spacing(test_txt)
        
        return result

    def inference(self, test_txt):
        
        gen_kwargs={'length_penalty': 0.8, 'num_beams':8, 'max_length':128}
                
        pipe = pipeline('summarization', model = self.model, tokenizer = self.tokenizer)
        
        return pipe(test_txt, **gen_kwargs)[0]['summary_text']