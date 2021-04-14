# Exercise from lecture 9

def f(L):
    '''Assume L is a list of at least 3 floats.
    Return a copy of L, changed as follows.
    Each element is the average of itself and the
    two adjacent elements. But the first and last
    are unchanged.'''
    m = list(L)
    for i in range(1, len(L)-1):
        m[i] = (L[i-1] + L[i] + L[i+1])/3
    return m

def test_f():
    M0 = [2.0, 1.2, 3.96]
    M1 = M0 + M0 
    N0 = f(M0)
    assert M0 == [2.0, 1.2, 3.96] # check that M0 is unchanged
    N1 = f(M1)
    assert N1[0]==M1[0] and N1[len(N1)-1]==M1[len(N1)-1] # first and last

test_f()
print(f([2.0, 1.2,1.2,1.2,1.2, 3.96]))