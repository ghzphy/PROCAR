##### modified by ghz, 2019,10,27,17:00
# Extracting the bands we wanted from PROCAR file, and generate PROCAR_band files
def filter_PROCAR_band(band_number):
    with open('PROCAR','r',encoding = 'utf-8') as procar:
        procar_content = procar.readlines()
        
    filtered_band_filepath = 'PROCAR_band{}'.format(band_number)
    with open(filtered_band_filepath,'w') as procar_filtered_band:
        flag = 'N'
        for line in procar_content:
            if 'band{0: 6}'.format(band_number+1) in line:
                flag = 'N'
                continue
            if 'band{0: 6}'.format(band_number) in line:
                flag = 'Y'
            if flag == 'Y':
                if 'band{0: 6}'.format(band_number) in line:
                    procar_filtered_band.write(line)
                if 'tot' in line:
                    procar_filtered_band.write(line)

# Extracting spin from PROCAR_band file
def ExtractSpin(band_number):
    with open('PROCAR_band{}'.format(band_number),'r') as procar_filtered_band:
        filtered_band_content = procar_filtered_band.readlines()

    s_x = [];s_y = [];s_z = []
    for i in range(len(filtered_band_content)):
        if i%6 == 3:
            sx = filtered_band_content[i].strip('\n').split(' ')[-1]
            s_x.append(float(sx))
        if i%6 == 4:
            sy = filtered_band_content[i].strip('\n').split(' ')[-1]
            s_y.append(float(sy))
        if i%6 == 5:
            sz = filtered_band_content[i].strip('\n').split(' ')[-1]
            s_z.append(float(sz))
    return s_x,s_y,s_z

# Extracting energy from PROCAR_band file
def ExtractEnergy(band_number):
    with open('PROCAR_band{}'.format(band_number),'r') as procar_filtered_band:
        filtered_band_content = procar_filtered_band.readlines()
        
    ek = []
    for line in filtered_band_content:
        if 'band' in line:
            ek.append(float(line.split()[4]))
    return ek

# Extracting k points from OUTCAR file，and generate kpoints file
def Read_OUTCAR():
    with open('OUTCAR','r') as outcar:
        outcar_content = outcar.readlines()
    kx = []; ky = []; kz = []
    flag = 'N'
    for line in outcar_content[257:]:
        if 'k-points in units of 2pi/SCALE and weight:' in line:
            flag = 'Y'
            continue
        if 'k-points in reciprocal lattice and weights:' in line:
            flag = 'N'
            continue
        if flag == 'Y':
            if line == ' \n':
                continue
            kx.append(float(line.split()[0]))
            ky.append(float(line.split()[1]))
            kz.append(float(line.split()[2]))
        if 'E-fermi' in line:
            E_fermi = float(line.split()[2])
            break
    return kx,ky,kz,E_fermi

# Writing kx,ky,E,sx,sy,sz to spin file
def Write_dat(kx,ky,kz,Ek,S_x,S_y,S_z,E_fermi,band_index,kgrid1):
    with open('spintexture.dat','w') as f1:
        f1.write('# The coordinates of kx,ky,E,sx,sy,sz \n')
        f1.write('#{0:>15}{1:>15}{2:>15}'.format('kx','ky','kz'))
        for i in band_index:
            f1.write('{0:>15} {1:>7} {2:>7} {3:>7}'.format('E_'+ str(i),'Sx','Sy','Sz'))
        f1.write('\n')
        for i in range(len(kx)):
            f1.write('{0:>15} {1:>15} {2:>15}'.format(kx[i],ky[i],kz[i]))
            for each in range(len(Ek)):
                f1.write(' {0:>15} {1:>7} {2:>7} {3:>7}'.format(Ek[each][i],S_x[each][i],S_y[each][i],S_z[each][i]))
            f1.write('\n')
            if (i+1)%kgrid1 == 0:
                f1.write('\n')

def main():
    kx,ky,kz,E_fermi = Read_OUTCAR()
    try:
        kgrid = eval(input('请输入二维 k 网格(例如:100,120):'))
        kgrid1 = kgrid[0]
    except:
        print('请正确输入网格!!!!')
        exit()
    band_range = eval(input('请输入绘制哪几条能带(例如:10,13): '))
    band_min = band_range[0]
    band_max = band_range[1]
    band_index = [i for i in range(band_min,band_max + 1)]
    Ek = [] ## total ek
    S_x = []; S_y = []; S_z = [] ## total spin
    for band in range(band_min,band_max + 1):
        print('正在处理第{}条能带'.format(band))
        filter_PROCAR_band(band)
        ek = ExtractEnergy(band)
        s_x,s_y,s_z = ExtractSpin(band)
        Ek.append(ek)
        S_x.append(s_x)
        S_y.append(s_y)
        S_z.append(s_z)
    Write_dat(kx,ky,kz,Ek,S_x,S_y,S_z,E_fermi,band_index,kgrid1)

if __name__ == '__main__':
    main()
