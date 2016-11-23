lst = ['cylinder', 'cylinder', 'cylinder', 'cylinder', 'cylinder', 'cylinder', 'cylinder', 'cylinder', 'cone', 'cube', 'cylinder']

pred = max(set(lst), key=lst.count)

print pred
print '{:.2%}'.format(float(lst.count(pred)) / len(lst))