def isomorphic(s,t):
    if len(s) != len(t):
        return False

    mapping_s_t = {}
    mapping_t_s = {}
