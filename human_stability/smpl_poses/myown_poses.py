from smpl_webuser.serialization import load_model, save_model
import numpy as np

## Load SMPL model (here we load the female model)
## Make sure path is correct
m = load_model( r'/home/byy/smpl/smpl/models/basicmodel_m_lbs_10_207_0_v1.1.0.pkl' )

## Assign poses as standard poses
m.pose[:] = np.random.rand(m.pose.size) * .00

# start with "mabu" pose
pose = np.zeros((24, 3))
pose[0] = np.array([0.0, 0.0, 0.0])  # Gupen

# Hips
pose[1] = np.array([-1.5, 1, 0])  # Zuokuan
pose[2] = np.array([-1.5, -1, 0])  # Youhuan

# Knees
pose[4] = np.array([0.0, -0.00, 0.0])  # Left
pose[5] = np.array([0.0, 0.00, -0.0])  # Right

# Ankels
pose[7] = np.array([0.0, -0.8, 0.0])  # Left
pose[8] = np.array([0.0, 0.8, 0.0])  # Right

# Torse
pose[3] = np.array([0.0, 0.0, 0.0])  # waist
pose[6] = np.array([0.25, 0.0, 0.0])  # breast

# arms
# left arm
pose[16] = np.array([0.0, -1.50, 0.0])  # left shoulder
pose[18] = np.array([0.0, 0.0, 0])  # left elbow
pose[20] = np.array([0.0, 0.0, 0.0])  # left waist

# right hand
pose[17] = np.array([0.0, 1.50, 0.0])  # right shoulder
pose[19] = np.array([0.0, 0.0, 0])  # right elbow
pose[23] = np.array([0.0, 0.0, 0])  # right hand

# neck
pose[12] = np.array([0.0, 0.0, 0])  # head rotation

pose_mod = np.reshape(pose, 72)
m.pose[:] = pose_mod

# use standard physiques
m.betas[:] = np.random.rand(m.betas.size) * .03

## Write to an .obj file
outmesh_path = './lean_male_10.obj'
with open( outmesh_path, 'w') as fp:
    for v in m.r:
        fp.write( 'v %f %f %f\n' % ( v[0], v[1], v[2]) )

    for f in m.f+1: # Faces are 1-based, not 0-based in obj files
        fp.write( 'f %d %d %d\n' %  (f[0], f[1], f[2]) )

# m1 = save_model(m, r'./mabu_male_pose.pkl' )

## Print message
print '..Output mesh saved to: ', outmesh_path 
