import random

with open("rejsampout.txt", 'w') as f:
    d_truec = 0
    notd_truec = 0

    b_truec = 0
    notb_truec = 0

    d_trueab = 0
    notd_trueab = 0

    #1000 samples
    for i in range (1000000):

        b_1 = random.randint(1,100)
        c_1 = random.randint(1,100)
        d_1 = random.randint(1,100)

        b = b_1 <= 90
        c = b and c_1 <= 50
        d = (c and d_1 <= 75) or (not c and d_1 <= 10) if b else (c and d_1 <= 50) or (not c and d_1 <= 20)

        # prob(d|c) and prob(b|c)
        if c:
            if d:
                d_truec += 1
            else:
                notd_truec += 1

            if b:
                b_truec += 1
            else:
                notb_truec += 1

        # prob(d|nota, b)
        if b:
            if d:
                d_trueab += 1
            else:
                notd_trueab += 1

    # normalize
    dc_sum = d_truec + notd_truec
    bc_sum = b_truec + notb_truec
    dab_sum = d_trueab + notd_trueab

    f.write("Samples passed for P(d|c): " + str(dc_sum) + ", samples true: " + str(d_truec) + '\n' + "NORMALIZATION = " + str(float(d_truec)/float(dc_sum)) + '\n\n')
    f.write("Samples passed for P(b|c): " + str(bc_sum) + ", samples true: " + str(b_truec) + '\n' + "NORMALIZATION = " + str(float(b_truec)/float(bc_sum))+ '\n\n')
    f.write("Samples passed for P(d|nota, b): " + str(dab_sum) + ", samples true: " + str(d_trueab) + '\n' + "NORMALIZATION = " + str(float(d_trueab)/float(dab_sum))+ '\n\n')
