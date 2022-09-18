
from sklearn import tree
clf = tree.DecisionTreeClassifier()
x = [[190, 100, 40], [189, 99, 42], [180, 90, 44], [179, 98, 45], [160, 50, 32], [169, 59, 31], [150, 70, 34], [155, 66, 32]]

y = [ 'hombre', 'hombre', 'hombre', 'hombre', 'mujer', 'mujer','mujer', 'mujer']

clf = clf.fit(x,y)
dato1 = [190, 99, 39]
prediction = clf.predict([dato1])
print(prediction)
if prediction == 'hombre':
  print('Estas caracteristicas son de un hombre')
else: 
  print('Estas caracteristicas son de una mujer')