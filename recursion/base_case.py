def mult(a, b): 
    if b == 1:
        return a
    else:
        return a + mult(a, b-1) ## creamos un scope tenemos control
    
print(mult(10, 5)) ## 50

## si fuera factorial
## fact(n) return n*fact(n-1)
## iteraciones: facto_iter(n) return ()


