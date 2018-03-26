import sys
import os
import pdb
import collections

try:
  first_arg = sys.argv[1]
  second_arg = sys.argv[2]
  third_arg = sys.argv[3]
  #pdb.set_trace()
  check=second_arg
  if (float(check))>1:
  	print("alpha can not be greater than 1")
  	sys.exit()
  else:
	  d = {}
	  out = {} 
	  def main_program (data=first_arg):
	    with open(data, 'r') as f:
	      for line in f:
	        (key, val) = line.strip().split('\t') 
	        if val in d:
	          d[val].append(key)
	        else:
	          d[val] = [key]
	        if key not in d:
	          d[key] = []

	        if key in out:
	          out[key]=out[key]+1
	        else:
	          out[key]=1
	        if val not in out:
	          out[val]=0
	    pagerank(d, float(second_arg), float(third_arg))

	  def pagerank(graph, alpha, betha):
	  	if alpha==0 and betha ==0:
	  		#pdb.set_trace()
	  		#print (graph)
	  		sgraph=collections.OrderedDict(sorted(graph.items()))
	  		for key, value in sgraph.items():
	  			print (str(key)+"\t"+str(len(value)))
	  		print("when alpha is 1 and betha 0, pagerank equals to number of in-degree edges in directed graph ")
	  	else:
		    epsilon=1.0e-8
		    pre_prank={}
		    deference=1
		    new_prank={}
		    #count=0
		    for k in d:
		        pre_prank[k]=1
		        new_prank[k]=1
		    while deference>epsilon:
		      #pdb.set_trace()
		      #count+=1
		      deference=0
		      for vertex, invertexs in d.items():
		        sumi=0
		        for invertex in invertexs:
		          if out[invertex]==0: outdegree=1
		          else: outdegree=out[invertex]
		          sumi=sumi + pre_prank[invertex] / outdegree
		        new_prank[vertex] = alpha * sumi + betha
		        deference= deference+abs(new_prank[vertex]-pre_prank[vertex])
		        #deference = sum(abs(new_prank[v] - pre_prank[v]) for v in new_prank.keys())
		        pre_prank[vertex]=new_prank[vertex]
		    for key, value in pre_prank.items():
		    	print (str(key)+"\t"+str(value)) 
 

  if __name__ == '__main__':
     main_program()

except Exception as e:
  print ("please give an input, alpha and betha ")
  sys.stdout.flush()
