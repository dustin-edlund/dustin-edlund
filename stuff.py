from sklearn import tree


X = [[180,80,44],[177,70,43],[160,60,38],[154,54,37],[166,63,40],[190,90,47],[175,64,39],[177,70,40],[159,55,37],[171,75,42]]

Y = ['m','f','f','f','m','m','m','f','m','f']
clf = tree.DecisionTreeClassifier()

clf = clf.fit(X,Y)

prediction = clf.predict([[205,45,188]])

print prediction
