def queensAttack(n, k, r_q, c_q, obstacles):
    nr = n - r_q
    s = r_q - 1
    e = n - c_q
    w = c_q - 1
    
    ne = min(nr, e)
    nw = min(nr, w)
    sw = min(s, w)
    se = min(s, e)
    
    ne_o = sorted([x for x in obstacles if x[0] > r_q and x[1] > c_q])
    nw_o = sorted([x for x in obstacles if x[0] > r_q and x[1] < c_q])
    se_o = sorted([x for x in obstacles if x[0] < r_q and x[1] > c_q], reverse=True)
    sw_o = sorted([x for x in obstacles if x[0] < r_q and x[1] < c_q], reverse=True)
    
    if ne_o:
        dist = ne_o[0][0] - r_q
        ne = min(ne, dist - 1)
    
    if nw_o:
        dist = nw_o[0][0] - r_q
        nw = min(nw, dist - 1)
    
    if se_o:
        dist = r_q - se_o[0][0]
        se = min(se, dist - 1)
    
    if sw_o:
        dist = r_q - sw_o[0][0]
        sw = min(sw, dist - 1)
    
    return nr + s + e + w + ne + nw + sw + se
