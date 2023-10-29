import ray 
ray.init() 
@ray.remote 
def var8 ( var6 ) : 
    return var6 * var6 

var7 =[ var8 .remote( i ) for i in range( 2 ) ] 
print( ray.get( var7 ) ) 