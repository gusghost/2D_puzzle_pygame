n = "N" 
f = "F"
b = "B"
a = "A"

au = "AU"
al = "AL"
ar = "AR"
ad = "AD"

c = "C"
p = "P"
h = "H"
o = "O"
s = "S"
g = "G"


def stage_select(stageNum):
    stage_list = [
        [
            [n,n,s],
            [n,n,p],
            [g,p,n]
        ],[
            [g,a,s],
            [h,f,p],
            [n,p,n]
        ],[
            [o,p,o,o,n,g],
            [p,n,p,n,n,n],
            [p,n,h,h,p,n],
            [s,n,n,n,n,p]
        ],[
            [o,a,o,b,o],
            [o,a,n,b,n],
            [o,a,n,b,n],
            [g,a,n,b,n]
        ],[
            [o,a,o,b,o,n,n,n],
            [o,a,n,b,n,n,a,n],
            [o,a,n,b,n,n,n,n],
            [g,a,n,b,n,n,n,n],
            [g,a,n,b,n,o,o,o]
        ]
    ]
    stage = stage_list[stageNum]
    return stage