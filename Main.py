import sample
import learn
import kNN

size = int(input("size\n"))
sample1 = sample.willing(size)
sta = learn.learn(sample1, size)
test = sample.willing(size)
error = kNN.cal(sta, test)
print(error)
