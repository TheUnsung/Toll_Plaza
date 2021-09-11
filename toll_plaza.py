
print('Welcome to toll plaza...')
lmv_tot = 0
lmv_pvt = 0
lmv_pub = 0
hmv_tot = 0


vehicle = input("Enter your vehicle type (HMV/LMV): ")
if vehicle == 'LMV' or vehicle == 'Lmv' or vehicle == 'lmv':
    lmv_tot = lmv_tot +1
    vehicle_type = input("Select your vehicle type(Public/Private): ")
    if vehicle_type == 'PUBLIC' or vehicle_type == 'Public' or vehicle_type == 'public':
        lmv_pub = lmv_pub +1
    elif vehicle_type == 'PRIVATE' or  vehicle_type == 'private' or  vehicle_type == 'Private':
        lmv_pvt = lmv_pvt +1
elif vehicle == 'HMV' or vehicle == 'Hmv' or vehicle == 'hmv':
    hmv_tot = hmv_tot +1

veh_tot = lmv_tot + hmv_tot


print('Total number of LMVs: ', lmv_tot)
print('     Total number of Public LMVs: ', lmv_pub)
print('     Total number of Private LMVs: ', lmv_pvt)
print('Total number of HMVs: ', hmv_tot)
print('Total number of Vehicles: ', veh_tot)



