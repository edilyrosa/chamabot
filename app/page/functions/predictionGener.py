
from sklearn import tree
clf = tree.DecisionTreeClassifier()
x = [[1,2,2,1], [1,1,1,1], [11, 11, 11, 11], [11, 12,11,11], [11,12,12,11], [11,11,11,11], [1, 1, 1, 1], [1, 2,1,1]]

y = [ 'ingenieria', 'ingenieria', 'ingenieria','ingenieria', 'abogado', 'abogado', 'abogado','abogado', ]

clf = clf.fit(x,y)
dato1 = [11,11,11,1]
prediction = clf.predict([dato1])
print(prediction)
if prediction == 'Ingeniero':
  print('Estas caracteristicas son de un Ingeniero')
else: 
  print('Estas caracteristicas son de un Abogado')