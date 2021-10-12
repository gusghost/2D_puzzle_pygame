from stage_variable import *

def stage_select(stageNum):
    stage_list = [
        [
            [s,n],
            [n,g]
        ],
        [
            [ar,n,s],
            [n,n,p],
            [g,p,n]
        ],[
            [g,ad,s],
            [h,f,p],
            [n,p,n]
        ],[
            [o,p,o,o,n,g],
            [p,n,p,n,n,n],
            [p,n,h,h,p,n],
            [s,n,n,n,n,p]
        ],[
            [o,ad,o,b,o],
            [o,ad,n,b,n],
            [o,ad,n,b,n],
            [g,ad,n,b,n]
        ],[
            [o,ad,o,b,o,n,n,g],
            [o,ad,n,b,n,n,ad,n],
            [o,ad,n,b,n,n,n,n],
            [o,ad,n,b,n,n,n,n],
            [s,ad,n,b,n,o,o,o]
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

def chip_effect(type):

    # walk, dash, jump, drop, stop, turn

    Zokusei= {
        au:("turn",[0,-1]),ad:("turn",[0,1]),al:("turn",[1,0]),ar:("turn",[-1,0])
        ,n:("walk",[0,0])
        ,h:("walk",[0,0])
        ,b:("jump",[0,0])
        ,f:("dash",[0,0])
        ,p:("drop",[0,0])
        ,s:("walk",[0,0]), g:("stop",[0,0])
        
    }

    return Zokusei[type]