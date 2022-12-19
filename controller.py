from User_Interface import user_choice
from  process import data_processor
from work_file import *

data = 'processing_model.csv'

t = user_choice()
user_list = data_processor(read_file(data), t)

if t == 6:
    write_file_2(user_list, mod='w')
else:
    write_file_1(user_list, mod='w')