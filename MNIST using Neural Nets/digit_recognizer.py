from ANN import *

data = pickle.load(open('train.p'))
inputs = []
targets = []

print 'Loaded the pickle'

for i in range(len(data[:2000])):
    out = data[i][0]
    inp = np.array([i/255. for i in data[i][1:].tolist()])
    inputs.append(inp)
    targets.append(out)

inputs = np.array(inputs)
targets = np.array(targets)

nn = NeuralNetwork(784,32,10)

print 'Training'
nn.train(inputs[:1600], targets[:1600], (inputs[1600:1800], targets[1600:1800]), 10, regularizer_type=None)
# nn.save('model.p')

c = 0

# nn = load('model.p')
print 'Predicting'
for i in xrange(len(inputs[1800:])-1):
    pred = nn.predict(inputs[1800+i])
    print 'Expected : ', targets[1800+i], 'Predicted : ', pred
    if targets[1800+i] == pred:
        c += 1

print 'Accuracy : ', c/200. * 100



