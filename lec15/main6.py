def worker( arg2=1,arg3=1,arg4=1,arg5=1,arg6=1,arg7=1,arg8=1,arg9=1):
    def true_worker(arg1):
        for i in range(1, 100000000):
            pass 
        print('Some results', arg1)
        return "Done" + str(arg1)
    return true_worker

func = worker(10,10 ,"LINUX", "MSK", 20,30 ,'UTF-8', 10)

func(2)
func(3)
func(4)


