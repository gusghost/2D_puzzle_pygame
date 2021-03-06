from stage_variable import *

def stage_select(stageNum):
    stage_list = [
        [
            # 0
            [s,n],
            [n,g]
        ],
        [
            [n,n,s],
            [n,n,p],
            [g,p,n]
        ],[
            [g,a,s],
            [h,f,p],
            [ar,p,au]
        ],[
            # 3
            [o,p,o,o,n,g],
            [p,n,p,n,n,n],
            [p,n,s,h,p,n],
            [n,n,n,n,n,p]
        ],[
            [o,ad,o,b,o],
            [o,ad,n,b,n],
            [o,ad,s,b,n],
            [g,ad,n,b,n]
        ],[
            [o,a,o,b,o,n,n,g],
            [o,a,n,b,n,n,a,n],
            [o,a,n,b,n,n,n,n],
            [o,a,n,b,n,n,n,n],
            [s,a,n,b,n,o,o,o]
        ],[
            # 6
            [n,s,n,n,n],
            [n,g,n,n,n],
            [n,n,n,n,n],
            [n,n,n,n,n],
            [n,n,n,n,n],
            [n,n,n,n,n],
            [n,n,n,n,n],
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
    marginW = (sc_width-(stageW*W))/2
    marginH = (sc_height-(stageH*H))/2
    margin = (marginW, marginH)

    return stage, margin

def chip_effect(type):

    # walk, dash, jump, drop, stop, turn
    # location = [Y, X]
    Zokusei= {
        au:("turn",[-1,0]),ad:("turn",[1,0]),al:("turn",[0,-1]),ar:("turn",[0,1])
        ,n:("walk",[0,0])
        ,h:("walk",[0,0])
        ,b:("jump",[0,0])
        ,f:("dash",[0,0])
        ,p:("drop",[0,0])
        ,s:("walk",[0,0]), g:("stop",[0,0]), o:("stop",[0,0])
        
    }

    return Zokusei[type]
