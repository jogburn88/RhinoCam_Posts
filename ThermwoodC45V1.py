from post_ext import *

PostProcVersion = 2021.2
# Set base *.spm file to use; if a variable is removed, will be used default.spm
BaseSPMFileName = "ThermwoodC45-Ogburn.spm"
# Set output file ext., used if "File Extension from Post Processor" option is enabled
GENERAL_OutputFileExt = ".nc"

def OnStartProcessing(blockData: PostBlockData, globalData: PostGlobalData):
    return
    
def OnEndProcessing(blockData: PostBlockData, globalData: PostGlobalData):
    return

# operation types: 1 - Holes, 2 - Holes 4Axis, 3/4/5 - 3/4/5 Axis operation 
def OnMOpStart(blockData: PostBlockData, globalData: PostGlobalData, operationType: int): 
    return
    
def OnMOpEnd(blockData: PostBlockData, globalData: PostGlobalData):
    return
    
def OnComment(blockData: PostBlockData, globalData: PostGlobalData):
    return

# Setup types: 0 - Coordinate system change, 1 - Rotate Head, 2 - Rotate Table 
def OnSetupStart(blockData: PostBlockData, globalData: PostGlobalData, type: int, MOpCount: int):
    return

def OnSetup(blockData: PostBlockData, globalData: PostGlobalData):
    return

def OnSetupEnd(blockData: PostBlockData, globalData: PostGlobalData):
    return
 
# Collector types: 1 - MOpSet 2 - Fixture offset 3 - XY Instance Linear 4 - XY Instance Polar 5 - RotTable
def OnCollectorStart(blockData: PostBlockData, globalData: PostGlobalData, type: int, MOpCount: int):
    return
    
def OnCollectorEnd(blockData: PostBlockData, globalData: PostGlobalData):
    return
    
def OnWorkZero(blockData: PostBlockData, globalData: PostGlobalData):
    return
    
def OnToolChange(blockData: PostBlockData, globalData: PostGlobalData):
    return
    
def OnSpindleSpeed(blockData: PostBlockData, globalData: PostGlobalData):
    return
    
def OnFeedRate(blockData: PostBlockData, globalData: PostGlobalData):
    return
    
def OnToolCompensation(blockData: PostBlockData, globalData: PostGlobalData):
    return
    
def OnCoolant(blockData: PostBlockData, globalData: PostGlobalData):
    return
    
def OnRapidMotion(blockData: PostBlockData, globalData: PostGlobalData):
    return
    
def OnLinearMotion(blockData: PostBlockData, globalData: PostGlobalData):
    return
    
def OnCirclularMotion(blockData: PostBlockData, globalData: PostGlobalData):
    return
    
def OnSpiralMotion(blockData: PostBlockData, globalData: PostGlobalData):
    return
    
def OnHelicalMotion(blockData: PostBlockData, globalData: PostGlobalData):
    return
    
def On4AxisRapidMotion(blockData: PostBlockData, globalData: PostGlobalData):
    return
    
def On4AxLinearMotion(blockData: PostBlockData, globalData: PostGlobalData):
    return
    
def On5AxRapidMotion(blockData: PostBlockData, globalData: PostGlobalData):
    return
    
def On5AxLinearMotion(blockData: PostBlockData, globalData: PostGlobalData):
    return
    
def OnCycleStart(blockData: PostBlockData, globalData: PostGlobalData):
    return
    
def OnCyclePoint(blockData: PostBlockData, globalData: PostGlobalData):
    return
    
def OnCycleEnd(globalData: PostGlobalData):
    return
    
def OnDwell(blockData: PostBlockData, globalData: PostGlobalData):
    return
    
def OnRotateHead(blockData: PostBlockData, globalData: PostGlobalData):
    return
    
def OnRotateTable(blockData: PostBlockData, globalData: PostGlobalData):
    return
    
def OnMachineRewind(blockData: PostBlockData, globalData: PostGlobalData):
    return
    