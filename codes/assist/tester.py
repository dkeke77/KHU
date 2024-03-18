import time
from assist import rand_func

def tester_rand_rep(func,sample,rep):
    time_lst = []
   
    for i in range(rep):
        arr = rand_func.rand_num_list(sample)
        start_time = time.time()
        func(arr)
        end_time = time.time()
        time_lst.append(end_time-start_time)
   
    return "%.10f ms" % (sum(time_lst) / len(time_lst)*1000)

def tester_rand_rep_du(func,sample,rep):
    time_lst = []
   
    for i in range(rep):
        arr = rand_func.rand_num_list_du(sample,1,1000)
        start_time = time.time()
        func(arr)
        end_time = time.time()
        time_lst.append(end_time-start_time)
   
    return "%.4f ms" % (sum(time_lst) / len(time_lst)*1000)