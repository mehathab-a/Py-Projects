# Mini-Project: Sorting via Renaming files

os.chdir('/home/mehathab/Desktop/Files for Python/Files Renamed')
fsplit = ''
renamed = ''
for dpath, dname, fname in os.walk('/home/mehathab/Desktop/Files for Python/Files'):
    print("File Name:", fname)
    for i in range(0, 10):
        fsplit = os.path.splitext(fname[i])
        fsname = str(fsplit[0])
        fsname1 = fsname.split('-')
        fsname1[-1] = fsname1[-1].split('#')
        fext = fsplit[1]
        if int(fsname1[-1][1]) < 10:
            fsname1[-1][1] = '0' + fsname1[-1][1]
        renamed = str(fsname1[-1][1] + ' - ' + fsname1[0] + fext)
        print(renamed)
        os.rename(fname[i], renamed)
