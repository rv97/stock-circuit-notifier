from multiprocessing import Process
from notifier import loop_companies

def proc_start(company_list):
    proc_to_start = Process(target=loop_companies, args=(company_list, ))
    proc_to_start.start()
    return proc_to_start

def proc_to_stop(proc):
    proc.terminate()
