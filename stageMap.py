from stage_valiable import *
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

def stage_gene(stage_No, sc_width, sc_height,scale =100):

    W = scale
    H = scale
    stage = stage_select(stage_No)
    stageW = len(stage[0])
    stageH = len(stage)
    marginX = (sc_width-(stageW*W))/2
    marginH = (sc_height-(stageH*H))/2
    margin = (marginX, marginH)

    return stage, margin