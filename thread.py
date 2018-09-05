import threading, time
import crawler

#存放线程的数组，相当于线程池
threads = []
for i in range(1, 26):
    t = threading.Thread(target=loop, name=str(i))
    threads.append(t)

start = time.clock()
for j in threads:
    j.start()
for k in threads:
    k.join()


print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
end = time.clock()
print(end-start)