import datetime

print('Welcome to toll plaza...')
lmv_tot = 0
lmv_pvt = 0
lmv_pub = 0
hmv_tot = 0
count = 0

while(True):


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
    veh_num = input('Enter your vehicle number: ')

    count = count +1



    veh_tot = lmv_tot + hmv_tot


    print('Total number of LMVs: ', lmv_tot)
    print('     Total number of Public LMVs: ', lmv_pub)
    print('     Total number of Private LMVs: ', lmv_pvt)
    print('Total number of HMVs: ', hmv_tot)
    print('Total number of Vehicles: ', veh_tot)
    print('Vehicle Number:', veh_num.upper())


    while(count >= 5):

        now  = datetime.datetime.now()

        f = open('toll_plaza.txt', 'a')
        (f.write('---------------------- \n'))
        f.close

        f = open('toll_plaza.txt', 'a')
        (f.write(now.strftime("%d-%m-%y | %H:%M:%S \n")))
        f.close

        # def func1():
        f = open('toll_plaza.txt', 'a')
        f.write('Total number of LMVs:')
        (f.write(str(lmv_tot))) and (f.write(str(' \n')))
        f.close


        f = open('toll_plaza.txt', 'a')
        f.write('-----Total number of private LMVs:')
        (f.write(str(lmv_pvt))) and (f.write(str(' \n')))
        f.close


        f = open('toll_plaza.txt', 'a')
        f.write('-----Total number of public LMVs:')
        (f.write(str(lmv_pub))) and (f.write(str(' \n')))
        f.close


        f = open('toll_plaza.txt', 'a')
        f.write('Total number of HMVs:')
        (f.write(str(hmv_tot))) and (f.write(str(' \n')))
        f.close

        f = open('toll_plaza.txt', 'a')
        f.write('Total number of Vehicles:')
        (f.write(str(veh_tot))) and (f.write(str(' \n')))
        f.close


        f = open('toll_plaza.txt', 'a')
        f.write('Vehicle Number:')
        (f.write(str(veh_num.upper()))) and (f.write(str(' \n')))
        f.close

        break
    continue