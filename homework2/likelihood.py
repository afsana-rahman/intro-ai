import random

with open("likelihoodout.txt", 'w') as f:
    d_truec = 0
    notd_truec = 0

    b_truec = 0
    notb_truec = 0

    d_trueab = 0
    notd_trueab = 0

    #1000 samples
    for i in range (1000):
        w = 1
        b_1 = random.randint(1,100)
        c_1 = random.randint(1,100)
        d_1 = random.randint(1,100)

        # prob(d|c)
        b = b_1 <= 90
        d =  (b and d_1 <= 75) or (not b and d_1 <= 50)
        # weighting
        if b:
            w = 0.5
            # prob(b|c) -- same rules as earlier, because evidence vars are same
            b_truec += w
        else:
            w = 0
            notb_truec += w
        if d:
            d_truec += w
        else:
            notd_truec += w

        # prob(d|nota, b)
        w = 0.9
        b = True
        c = c_1 <= 50
        d = (c and d_1 <= 75) or (not c and d_1 <= 10)
        # weighting
        if d:
            d_trueab += w
        else:
            notd_trueab += w
        
    dc_sum = d_truec + notd_truec
    bc_sum = b_truec + notb_truec
    dab_sum = d_trueab + notd_trueab

    f.write("Total weight for P(d|c): " + str(dc_sum) + ", sample true: " + str(d_truec) + '\n' + "NORMALIZATION = " + str(float(d_truec)/float(dc_sum)) + '\n\n')
    f.write("Total weight for P(b|c): " + str(bc_sum) + ", sample true: " + str(b_truec) + '\n' + "NORMALIZATION = " + str(float(b_truec)/float(bc_sum))+ '\n\n')
    f.write("Total weight for P(d|nota, b): " + str(dab_sum) + ", sample true: " + str(d_trueab) + '\n' + "NORMALIZATION = " + str(float(d_trueab)/float(dab_sum))+ '\n\n')
        
        