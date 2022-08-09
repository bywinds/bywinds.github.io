
class Meta:
    def __init__(self):
        self.width = 640
        self.height = 480
        self.fps = 60
        self.model = 1
        self.pointCloud = True
        self.view = True
        self.insertKeyframe = False
        self.data = []
        self.dataLen = 0
        self.index = 0
        self.func = None
        self.cap = None
        self.cancel = False
        self.rotationMatrix = None
        self.scaleRatio = [1, 1, 1]
        self.origin = []
        self.landmark = []
        self.dazLandmark = []
        self.stable = []
        self.boneMatix = []
        self.length = []
        self.angle = []
        self.parameter = []
        self.reference = {}
        self.history = []
        self.drive = False

cmeta = {'name': None, 'meta': None}


facePointNumber = 69
posePointNumber = 29
handPointNumber = 21
scaleUnit = 1
dazName = 'Genesis8_1Female'

faceBonePointMap = {}
faceBonePointMap[0] = 'LipUpperMiddle'
faceBonePointMap[1] = 'Nose'
faceBonePointMap[5] = ''
faceBonePointMap[6] = ''
faceBonePointMap[9] = 'CenterBrow'
faceBonePointMap[16] = 'LipLowerMiddle'
faceBonePointMap[31] = 'rSquintOuter'
faceBonePointMap[33] = 'rEyelidOuter'
faceBonePointMap[50] = 'rCheekUpper'
faceBonePointMap[57] = 'rLipCorner'
faceBonePointMap[70] = 'rBrowOuter'
faceBonePointMap[73] = 'rLipUpperInner'
faceBonePointMap[92] = 'rLipNasolabialCrease'
faceBonePointMap[105] = 'rBrowMid'
faceBonePointMap[107] = 'rBrowInner'
faceBonePointMap[138] = 'rJawClench'
faceBonePointMap[145] = 'rEyelidLower'
faceBonePointMap[146] = 'rLipLowerOuter'
faceBonePointMap[153] = 'rEyelidLowerInner'
faceBonePointMap[155] = 'rEyelidInner'
faceBonePointMap[157] = 'rEyelidUpperInner'
faceBonePointMap[159] = 'rEyelidUpper'
faceBonePointMap[161] = 'rEyelidUpperOuter'
faceBonePointMap[163] = 'rEyelidLowerOuter'
faceBonePointMap[167] = 'rLipBelowNose'
faceBonePointMap[168] = 'MidNoseBridge'
faceBonePointMap[180] = 'rLipLowerInner'
faceBonePointMap[185] = 'rLipUpperOuter'
faceBonePointMap[195] = ''
faceBonePointMap[197] = ''
faceBonePointMap[199] = 'Chin'
faceBonePointMap[200] = 'LipBelow'
faceBonePointMap[203] = 'rNasolabialMiddle'
faceBonePointMap[211] = 'rNasolabialLower'
faceBonePointMap[212] = 'rNasolabialMouthCorner'
faceBonePointMap[214] = 'rCheekLower'
faceBonePointMap[217] = 'rNasolabialUpper'
faceBonePointMap[220] = 'rNostril'
faceBonePointMap[231] = 'rSquintInner'
faceBonePointMap[261] = 'lSquintOuter'
faceBonePointMap[263] = 'lEyelidOuter'
faceBonePointMap[280] = 'lCheekUpper'
faceBonePointMap[287] = 'lLipCorner'
faceBonePointMap[300] = 'lBrowOuter'
faceBonePointMap[303] = 'lLipUpperInner'
faceBonePointMap[322] = 'lLipNasolabialCrease'
faceBonePointMap[334] = 'lBrowMid'
faceBonePointMap[336] = 'lBrowInner'
faceBonePointMap[367] = 'lJawClench'
faceBonePointMap[374] = 'lEyelidLower'
faceBonePointMap[375] = 'lLipLowerOuter'
faceBonePointMap[380] = 'lEyelidLowerInner'
faceBonePointMap[382] = 'lEyelidInner'
faceBonePointMap[384] = 'lEyelidUpperInner'
faceBonePointMap[386] = 'lEyelidUpper'
faceBonePointMap[388] = 'lEyelidUpperOuter'
faceBonePointMap[390] = 'lEyelidLowerOuter'
faceBonePointMap[393] = 'lLipBelowNose'
faceBonePointMap[404] = 'lLipLowerInner'
faceBonePointMap[409] = 'lLipUpperOuter'
faceBonePointMap[423] = 'lNasolabialMiddle'
faceBonePointMap[431] = 'lNasolabialLower'
faceBonePointMap[432] = 'lNasolabialMouthCorner'
faceBonePointMap[434] = 'lCheekLower'
faceBonePointMap[437] = 'lNasolabialUpper'
faceBonePointMap[440] = 'lNostril'
faceBonePointMap[451] = 'lSquintInner'
faceBonePointMap[468] = 'rEye'
faceBonePointMap[473] = 'lEye'
faceBonePointExclude = [5, 6, 195, 197]
faceBoneIndexExclude = []
faceBoneIndexMap = {}
facePointIndexMap = {}
faceIndexPointMap = {}
faceBoneIndexTemp = -1
for bonePoint in sorted(faceBonePointMap):
    faceBoneIndexTemp += 1
    facePointIndexMap[bonePoint] = faceBoneIndexTemp
    faceIndexPointMap[faceBoneIndexTemp] = bonePoint
    if bonePoint in faceBonePointExclude:
        faceBoneIndexExclude.append(faceBoneIndexTemp)
        faceBoneIndexMap[faceBoneIndexTemp] = False
    else:
        faceBoneIndexMap[faceBoneIndexTemp] = faceBonePointMap[bonePoint]

faceEyeAreaPoints = [384,386,388,390,374,380,473,157,159,161,163,145,153,468]
faceCommonLargePoints = [9, 451,261,231,31, 280,423,50,203]
faceCommonSmallPoints = [336,334,300,107,105,70, 382,263,155,33]
faceNosePoints = [1,220,217,168,437,440]
faceLipsPoints = [287,432,57,212]
faceLipUpperPoints = [322,393,167,92,0,303,409,185,73]
faceLipLowerPoints = [16,180,146,375,404]
faceJawPoints = [200,431,199,211,434,367,214,138]
print('facePointIndexMap: ', facePointIndexMap)


poseBonePointMap = {}
poseBonePointMap[0] = 'Nose'
poseBonePointMap[1] = 'lEyelidInner'
poseBonePointMap[3] = 'lEyelidOuter'
poseBonePointMap[4] = 'rEyelidInner'
poseBonePointMap[6] = 'rEyelidOuter'
poseBonePointMap[9] = 'lLipCorner'
poseBonePointMap[10] = 'rLipCorner'
poseBonePointMap[11] = 'lShldrBend'
poseBonePointMap[12] = 'rShldrBend'
poseBonePointMap[13] = 'lForearmBend'
poseBonePointMap[14] = 'rForearmBend'
poseBonePointMap[15] = 'lHand'
poseBonePointMap[16] = 'rHand'
poseBonePointMap[17] = 'lPinky1'
poseBonePointMap[18] = 'rPinky1'
poseBonePointMap[19] = 'lIndex1'
poseBonePointMap[20] = 'rIndex1'
poseBonePointMap[21] = 'lThumb1'
poseBonePointMap[22] = 'rThumb1'
poseBonePointMap[23] = 'lThighBend'
poseBonePointMap[24] = 'rThighBend'
poseBonePointMap[25] = 'lShin'
poseBonePointMap[26] = 'rShin'
poseBonePointMap[27] = 'lFoot'
poseBonePointMap[28] = 'rFoot'
poseBonePointMap[29] = ''
poseBonePointMap[30] = ''
poseBonePointMap[31] = 'lToe'
poseBonePointMap[32] = 'rToe'
poseBonePointExclude = [29, 30]
poseBoneIndexExclude = []
poseBoneIndexMap = {}
posePointIndexMap = {}
poseIndexPointMap = {}
poseBoneIndexTemp = -1
for bonePoint in sorted(poseBonePointMap):
    poseBoneIndexTemp += 1
    posePointIndexMap[bonePoint] = poseBoneIndexTemp
    poseIndexPointMap[poseBoneIndexTemp] = bonePoint
    if bonePoint in poseBonePointExclude:
        poseBoneIndexExclude.append(poseBoneIndexTemp)
        poseBoneIndexMap[poseBoneIndexTemp] = False
    else:
        poseBoneIndexMap[poseBoneIndexTemp] = poseBonePointMap[bonePoint]
print('posePointIndexMap: ', posePointIndexMap)


leftHandBonePointMap = {}
leftHandBonePointMap[0] = 'lHand'
leftHandBonePointMap[1] = 'lThumb1'
leftHandBonePointMap[2] = 'lThumb2'
leftHandBonePointMap[3] = 'lThumb3'
leftHandBonePointMap[4] = ''
leftHandBonePointMap[5] = 'lIndex1'
leftHandBonePointMap[6] = 'lIndex2'
leftHandBonePointMap[7] = 'lIndex3'
leftHandBonePointMap[8] = ''
leftHandBonePointMap[9] = 'lMid1'
leftHandBonePointMap[10] = 'lMid2'
leftHandBonePointMap[11] = 'lMid3'
leftHandBonePointMap[12] = ''
leftHandBonePointMap[13] = 'lRing1'
leftHandBonePointMap[14] = 'lRing2'
leftHandBonePointMap[15] = 'lRing3'
leftHandBonePointMap[16] = ''
leftHandBonePointMap[17] = 'lPinky1'
leftHandBonePointMap[18] = 'lPinky2'
leftHandBonePointMap[19] = 'lPinky3'
leftHandBonePointMap[20] = ''
leftHandBonePointExclude = [4, 8, 12, 16, 20]
leftHandBoneIndexExclude = []
leftHandBoneIndexMap = {}
leftHandPointIndexMap = {}
leftHandIndexPointMap = {}
leftHandBoneIndexTemp = -1
for bonePoint in sorted(leftHandBonePointMap):
    leftHandBoneIndexTemp += 1
    leftHandPointIndexMap[bonePoint] = leftHandBoneIndexTemp
    leftHandIndexPointMap[leftHandBoneIndexTemp] = bonePoint
    if bonePoint in leftHandBonePointExclude:
        leftHandBoneIndexExclude.append(leftHandBoneIndexTemp)
        leftHandBoneIndexMap[leftHandBoneIndexTemp] = False
    else:
        leftHandBoneIndexMap[leftHandBoneIndexTemp] = leftHandBonePointMap[bonePoint]
rightHandBonePointMap = {}
rightHandBonePointMap[0] = 'rHand'
rightHandBonePointMap[1] = 'rThumb1'
rightHandBonePointMap[2] = 'rThumb2'
rightHandBonePointMap[3] = 'rThumb3'
rightHandBonePointMap[4] = ''
rightHandBonePointMap[5] = 'rIndex1'
rightHandBonePointMap[6] = 'rIndex2'
rightHandBonePointMap[7] = 'rIndex3'
rightHandBonePointMap[8] = ''
rightHandBonePointMap[9] = 'rMid1'
rightHandBonePointMap[10] = 'rMid2'
rightHandBonePointMap[11] = 'rMid3'
rightHandBonePointMap[12] = ''
rightHandBonePointMap[13] = 'rRing1'
rightHandBonePointMap[14] = 'rRing2'
rightHandBonePointMap[15] = 'rRing3'
rightHandBonePointMap[16] = ''
rightHandBonePointMap[17] = 'rPinky1'
rightHandBonePointMap[18] = 'rPinky2'
rightHandBonePointMap[19] = 'rPinky3'
rightHandBonePointMap[20] = ''
rightHandBonePointExclude = [4, 8, 12, 16, 20]
rightHandBoneIndexExclude = []
rightHandBoneIndexMap = {}
rightHandPointIndexMap = {}
rightHandIndexPointMap = {}
rightHandBoneIndexTemp = -1
for bonePoint in sorted(rightHandBonePointMap):
    rightHandBoneIndexTemp += 1
    rightHandPointIndexMap[bonePoint] = rightHandBoneIndexTemp
    leftHandIndexPointMap[leftHandBoneIndexTemp] = bonePoint
    if bonePoint in rightHandBonePointExclude:
        rightHandBoneIndexExclude.append(rightHandBoneIndexTemp)
        rightHandBoneIndexMap[rightHandBoneIndexTemp] = False
    else:
        rightHandBoneIndexMap[rightHandBoneIndexTemp] = rightHandBonePointMap[bonePoint]
handBonePointMap = leftHandBonePointMap
handBoneIndexMap = leftHandBoneIndexMap
handPointIndexMap = leftHandPointIndexMap
print('handPointIndexMap: ', handPointIndexMap)
