#### modified by ghz, 2019,10,26 16:58
def Read_OUTCAR():
    with open('OUTCAR','r') as outcar:
        outcar_content = outcar.readlines()
    kx = []; ky = []; kz = []
    k1 = []; k2 = []; k3 = []
    flag = 'N'
    for line in outcar_content[257:]:
        if 'k-points in units of 2pi/SCALE and weight:' in line:
            flag = 'Y'
            continue
        if 'k-points in reciprocal lattice and weights:' in line:
            flag = 'H'
            continue
        if 'position of ions in fractional coordinates' in line:
            flag = 'I'
        if flag == 'Y':
            if line == ' \n':
                continue
            kx.append(float(line.split()[0]))
            ky.append(float(line.split()[1]))
            kz.append(float(line.split()[2]))
        if flag == 'H':
            if line == ' \n':
                continue
            k1.append(float(line.split()[0]))
            k2.append(float(line.split()[1]))
            k3.append(float(line.split()[2]))
        if 'E-fermi' in line:
            E_fermi = float(line.split()[2])
            break
    return kx,ky,kz,k1,k2,k3,E_fermi

def Read_EIGENVAL():
    with open('EIGENVAL','r') as eig:
        eig_content = eig.readlines()
    system = eig_content[4].strip('\n').strip()[0]
    totalkpoint = eig_content[5].split()[1]
    totalband = eig_content[5].split()[2]
    return eig_content,system,totalband,totalkpoint
    
def SelectBand(eig_content,totalband,band):
    ek = []
    for i in range(6,len(eig_content)):
        if (i-7)%(int(totalband)+2) == band:
            ek.append(eig_content[i].split()[1])
    return ek

def Write_dat(kx,ky,kz,k1,k2,k3,Ek,band_index,kgrid1,E_fermi):
    Ek_len = len(Ek)
    with open('band_plane.dat','w') as f1:
        f1.write('#{0:>13} {1:>14} {2:>14} {3:>12} {4:>12} {5:>12}'.format('kx','ky','kz','k1','k2','k3'))
        for i in band_index:
            f1.write(' {:>14}'.format('E_'+ str(i)))
        f1.write('\n')
        for i in range(len(kx)):
            f1.write('{0:>14} {1:>14} {2:>14} {3:>12} {4:>12} {5:>12}'.format(kx[i],ky[i],kz[i],k1[i],k2[i],k3[i]))
            for each in range(Ek_len):
                f1.write(' {:>14}'.format(Ek[each][i]))
            f1.write('\n')
            if (i+1)%kgrid1 == 0:
                f1.write('\n')
    with open('band_plane.gnu','w') as f2:
        f2.write('set encoding iso_8859_1\n')
        f2.write('#set terminal  postscript enhanced color\n')
        f2.write("#set output 'bulkek_plane.eps'\n")
        f2.write('set terminal  png truecolor enhanced size 1920, 1680 font ",36"\n')
        f2.write("set output 'band_plane.png'\n")
        f2.write('set palette rgbformulae 33,13,10\n')
        f2.write('unset key\n')
        f2.write('set pm3d\n')
        f2.write('set origin 0.2, 0\n')
        f2.write('set size 0.8, 1\n')
        f2.write('set border lw 3\n')
        f2.write('#set xtics font ",24"\n')
        f2.write('#set ytics font ",24"\n')
        f2.write('set size ratio -1\n')
        f2.write('set xtics\n')
        f2.write('set ytics\n')
        f2.write('set zrange [:]\n')
        f2.write('set view 80,60\n')
        f2.write('set xlabel "k_1"\n')
        f2.write('set ylabel "k_2"\n')
        f2.write('set zlabel "Energy (eV)" rotate by 90\n')
        f2.write('unset colorbox\n')
        f2.write('set autoscale fix\n')
        f2.write('set pm3d interpolate 4,4\n')
        f2.write("splot 'band_plane.dat' u 1:2:($8-{}) w pm3d, \\\n".format(E_fermi))
        f2.write("      'band_plane.dat' u 1:2:($9-{}) w pm3d\n".format(E_fermi))
        

def main():
    kx,ky,kz,k1,k2,k3,E_fermi = Read_OUTCAR()
    eig_content,system,totalband,totalkpoint = Read_EIGENVAL()
    try:
        kgrid = eval(input('请输入二维 k 网格(例如:100,120):'))
        kgrid1 = kgrid[0]
    except:
        print('请正确输入网格!!!!')
        exit()
    print('该体系({0:})有 {1:}个k点,{2:}条能带.'.format(system,totalkpoint,totalband))

    band_range = eval(input('请输入绘制哪几条能带(例如:10,13): '))
    band_min = band_range[0]
    band_max = band_range[1]
    band_index = [i for i in range(band_min,band_max + 1)]
    Ek = [] ## total ek
    for band in range(band_min,band_max + 1):
        print('正在绘制第{}条能带'.format(band))
        ek = SelectBand(eig_content,totalband,band)
        Ek.append(ek)
    Write_dat(kx,ky,kz,k1,k2,k3,Ek,band_index,kgrid1,E_fermi)
if __name__ == '__main__':
    main()
