#Magician
dType.SetInfraredSensor(api, 1 ,2, 1)
STEP_PER_CRICLE = 360.0 / 1.8 * 10.0 * 16.0
MM_PER_CRICLE = 3.1415926535898 * 36.0
vel = float((-10)) * STEP_PER_CRICLE / MM_PER_CRICLE
dType.SetEMotorEx(api, 0, 1, int(vel), 1)
dType.SetEndEffectorParamsEx(api, 59.7, 0, 0, 1)
dType.SetEndEffectorGripperEx(api, 1, 0)
dType.dSleep(1000)
current_pose = dType.GetPose(api)
dType.SetPTPCmdEx(api, 2, 251.88,  133.29,  (-15.87), current_pose[3], 1)
dType.dSleep(1000)
for count in range(100000000000):
  if (dType.GetInfraredSensor(api, 2)[0]) == 1:
     dType.dSleep(400)
     STEP_PER_CRICLE = 360.0 / 1.8 * 10.0 * 16.0
     MM_PER_CRICLE = 3.1415926535898 * 36.0
     vel = float(0) * STEP_PER_CRICLE / MM_PER_CRICLE
     dType.SetEMotorEx(api, 0, 0, int(vel), 1)
     current_pose = dType.GetPose(api)
     dType.SetPTPCmdEx(api, 2, 251.88,  133.29,  (-15.87), current_pose[3], 1)
     dType.dSleep(1000)
     current_pose = dType.GetPose(api)
     dType.SetPTPCmdEx(api, 2, 251.88,  133.29,  (-42.87), current_pose[3], 1)
     dType.dSleep(1000)
     dType.SetEndEffectorGripperEx(api, 1, 1)
     dType.dSleep(2000)
     with open('F:\Dissertation\class_number.txt', 'r') as file: 
         v = int(file.read())
     if v == 0:
       current_pose = dType.GetPose(api)
       dType.SetPTPCmdEx(api, 2, 251.88,  133.29,  (-15.87), current_pose[3], 1)
       current_pose = dType.GetPose(api)
       dType.SetPTPCmdEx(api, 2, 219.17,  46.29,  28, current_pose[3], 1)
       current_pose = dType.GetPose(api)
       dType.SetPTPCmdEx(api, 2, 125,  42,  (-15), current_pose[3], 1)
       dType.dSleep(1000)
       dType.SetEndEffectorGripperEx(api, 1, 0)
       current_pose = dType.GetPose(api)
       dType.SetPTPCmdEx(api, 2, 219.17,  46.29,  28, current_pose[3], 1)
       current_pose = dType.GetPose(api)
       dType.SetPTPCmdEx(api, 2, 251.88,  133.29,  (-15.87), current_pose[3], 1)
     elif v == 1:
       current_pose = dType.GetPose(api)
       dType.SetPTPCmdEx(api, 2, 251.88,  133.29,  (-15.87), current_pose[3], 1)
       current_pose = dType.GetPose(api)
       dType.SetPTPCmdEx(api, 2, 219.17,  46.29,  28, current_pose[3], 1)
       current_pose = dType.GetPose(api)
       dType.SetPTPCmdEx(api, 2, 125,  42,  (-15), current_pose[3], 1)
       current_pose = dType.GetPose(api)
       dType.SetPTPCmdEx(api, 2, 114.4,  6.2,  (-15), current_pose[3], 1)
       dType.dSleep(1000)
       dType.SetEndEffectorGripperEx(api, 1, 0)
       current_pose = dType.GetPose(api)
       dType.SetPTPCmdEx(api, 2, 125,  42,  (-15), current_pose[3], 1)
       current_pose = dType.GetPose(api)
       dType.SetPTPCmdEx(api, 2, 219.17,  46.29,  28, current_pose[3], 1)
       current_pose = dType.GetPose(api)
       dType.SetPTPCmdEx(api, 2, 251.88,  133.29,  (-15.87), current_pose[3], 1)
     elif v == 2:
       current_pose = dType.GetPose(api)
       dType.SetPTPCmdEx(api, 2, 251.88,  133.29,  (-15.87), current_pose[3], 1)
       current_pose = dType.GetPose(api)
       dType.SetPTPCmdEx(api, 2, 219.17,  46.29,  28, current_pose[3], 1)
       current_pose = dType.GetPose(api)
       dType.SetPTPCmdEx(api, 2, 125,  42,  (-15), current_pose[3], 1)
       current_pose = dType.GetPose(api)
       dType.SetPTPCmdEx(api, 2, 114.4,  (-26),  (-15), current_pose[3], 1)
       dType.dSleep(1000)
       dType.SetEndEffectorGripperEx(api, 1, 0)
       current_pose = dType.GetPose(api)
       dType.SetPTPCmdEx(api, 2, 125,  42,  (-15), current_pose[3], 1)
       current_pose = dType.GetPose(api)
       dType.SetPTPCmdEx(api, 2, 219.17,  46.29,  28, current_pose[3], 1)
       current_pose = dType.GetPose(api)
       dType.SetPTPCmdEx(api, 2, 251.88,  133.29,  (-15.87), current_pose[3], 1)
     elif v == 3:
       current_pose = dType.GetPose(api)
       dType.SetPTPCmdEx(api, 2, 251.88,  133.29,  (-15.87), current_pose[3], 1)
       current_pose = dType.GetPose(api)
       dType.SetPTPCmdEx(api, 2, 219.17,  46.29,  28, current_pose[3], 1)
       current_pose = dType.GetPose(api)
       dType.SetPTPCmdEx(api, 2, 125,  42,  (-15), current_pose[3], 1)
       current_pose = dType.GetPose(api)
       dType.SetPTPCmdEx(api, 2, 114.4,  (-56),  (-15), current_pose[3], 1)
       dType.dSleep(1000)
       dType.SetEndEffectorGripperEx(api, 1, 0)
       current_pose = dType.GetPose(api)
       dType.SetPTPCmdEx(api, 2, 125,  42,  (-15), current_pose[3], 1)
       current_pose = dType.GetPose(api)
       dType.SetPTPCmdEx(api, 2, 219.17,  46.29,  28, current_pose[3], 1)
       current_pose = dType.GetPose(api)
       dType.SetPTPCmdEx(api, 2, 251.88,  133.29,  (-15.87), current_pose[3], 1)
     elif v == 4:
       STEP_PER_CRICLE = 360.0 / 1.8 * 10.0 * 16.0
       MM_PER_CRICLE = 3.1415926535898 * 36.0
       vel = float((-10)) * STEP_PER_CRICLE / MM_PER_CRICLE
       dType.SetEMotorEx(api, 0, 1, int(vel), 1)
     with open('F:\Dissertation\class_number.txt', 'w') as file: 
         file.write("4")
     current_pose = dType.GetPose(api)
     dType.SetPTPCmdEx(api, 2, 251.88,  133.29,  (-15.87), current_pose[3], 1)
     STEP_PER_CRICLE = 360.0 / 1.8 * 10.0 * 16.0
     MM_PER_CRICLE = 3.1415926535898 * 36.0
     vel = float((-10)) * STEP_PER_CRICLE / MM_PER_CRICLE
     dType.SetEMotorEx(api, 0, 1, int(vel), 1)
     dType.SetEndEffectorGripperEx(api, 1, 0)




