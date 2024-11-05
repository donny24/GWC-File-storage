
def read_GWC(filepath, ref_roughness=0.00, ref_height=150):
    # Reference roughness lengths [m]
    ref_roughness_lenghts = [0.00, 0.03, 0.10, 0.40, 1.50]

    # Reference heights above ground level [m]
    ref_roughness_heights = [10, 50, 100, 150, 200]

    f_index = 0
    ak_index = 0
    ref_r_l_cmp = abs(ref_roughness - ref_roughness_lenghts[0])
    ref_r_h_cmp = abs(ref_height - ref_roughness_heights[0])
    for i in range(1, len(ref_roughness_heights)):
        if (abs(ref_roughness_lenghts[i] - ref_roughness) < ref_r_l_cmp):
            ref_r_l_cmp = abs(ref_roughness_lenghts[i] - ref_roughness)
            f_index = i

        if (abs(ref_roughness_heights[i] - ref_height) < ref_r_h_cmp):
            ref_r_h_cmp = abs(ref_roughness_heights[i] - ref_height)
            ak_index = i


    f_line_val = [4, 15, 26, 37, 48]
    f_line_i = f_line_val[f_index]
    a_line_i = f_line_i + 1
    k_line_i = f_line_i + 2

    ak_add_on = [0, 2, 4, 6, 8]
    a_line_i = a_line_i + ak_add_on[ak_index]
    k_line_i = k_line_i + ak_add_on[ak_index]
    
    


    # open the sample file used 
    file = open(filepath)   
    # read the content of the file opened 
    content = file.readlines() 
    

    f = []
    a = []
    k = []

    f_tokens = content[f_line_i].split()
    a_tokens = content[a_line_i].split()
    k_tokens = content[k_line_i].split()

    for j in range(len(f_tokens)):
        f.append(round(float(f_tokens[j])/100, 4))
        a.append(float(a_tokens[j]))
        k.append(float(k_tokens[j]))

    print(f'f = {f}')
    print(f'a = {a}')
    print(f'k = {k}')


# HERE IS WHERE YOU CHANGE PARAMETERS TO GET THE PARAMETERS FOR SITES:
# f:	Frequencies of occurrence for reference roughness     
# a:    Weibull A-parameter
# k:    Weibull k-parameter
while(True):
    print("--PROVIDE--")
    filepath = str(input("Filepath: "))
    f = float(input("Roughness Lenght: "))
    h = float(input("Hub height: "))
    read_GWC("US/"+filepath, f, h)