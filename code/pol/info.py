normal_days = 450
outlier_days = 14


work_outlier_agents = {}
work_outlier_agents['YELLOW'] = [
    66, 809, 976, 4, 84, 268, 858, 416, 307, 956]  # 31
work_outlier_agents['ORANGE'] = [83, 478, 1,
                                 244, 379, 161, 147, 353, 517, 364]  # 32
work_outlier_agents['RED'] = [546, 644, 347,
                              62, 551, 992, 554, 949, 900, 57]  # 33

social_outlier_agents = {}
social_outlier_agents['YELLOW'] = [
    66, 809, 976, 4, 84, 268, 858, 416, 307, 956]
social_outlier_agents['ORANGE'] = [
    83, 478, 1, 244, 379, 161, 147, 353, 517, 364]
social_outlier_agents['RED'] = [546, 644, 347, 62, 551, 992, 554, 949, 900, 57]

hunger_outlier_agents = {}
hunger_outlier_agents['RED'] = [144, 345, 989, 14, 361, 153, 305, 774, 535, 646, 622, 860,
                                680, 39, 336, 430, 885, 185, 232, 62, 18, 152, 692, 878, 461, 206, 5, 508, 219, 896]
hunger_outlier_agents['ORANGE'] = [895, 697, 491, 143, 235, 412, 927, 913, 271, 282, 275, 711,
                                   957, 332, 914, 485, 863, 598, 985, 276, 805, 764, 556, 159, 377, 993, 604, 164, 288, 433]
hunger_outlier_agents['YELLOW'] = [351, 331, 871, 739, 347, 821, 63, 986, 951, 947, 769, 761,
                                   548, 886, 643, 50, 467, 228, 798, 753, 511, 8, 385, 400, 836, 930, 766, 872, 435, 787]


combined_work_outlier_agents = {}
combined_work_outlier_agents['RED'] = [1381, 1708,
                                       2787, 2477, 1813, 2410, 2725, 2752, 2332, 2637]
combined_work_outlier_agents['ORANGE'] = [
    827, 964, 26, 1036, 1643, 2380, 561, 1895, 1701, 1940]
combined_work_outlier_agents['YELLOW'] = [
    1013, 1249, 677, 1022, 2667, 193, 1892, 2712, 1547, 2627]

combined_social_outlier_agents = {}
combined_social_outlier_agents['RED'] = [
    2170, 507, 2139, 2701, 748, 902, 396, 2273, 780, 1585]
combined_social_outlier_agents['ORANGE'] = [
    2234, 156, 795, 2454, 1745, 226, 1744, 2720, 2100, 2512]
combined_social_outlier_agents['YELLOW'] = [
    2863, 430, 2217, 216, 738, 2223, 962, 947, 2608, 2614]


combined_hunger_outlier_agents = {}
combined_hunger_outlier_agents["RED"] = [2114, 809, 2000, 1028, 84, 1882, 1440, 1331, 956, 1107, 13, 2144,
                                         12, 692, 2796, 979, 2541, 1966, 81, 2167, 2746, 1818, 1659, 1871, 1524, 185, 1188, 2643, 1206, 2880]
combined_hunger_outlier_agents['ORANGE'] = [1731, 844, 2303, 2102, 1590, 1466, 2258, 2770, 2903, 2257, 1502,
                                            2049, 353, 2565, 1388, 1570, 2692, 347, 551, 554, 1906, 211, 1877, 1881, 1796, 810, 462, 1005, 1441, 2432]
combined_hunger_outlier_agents['YELLOW'] = [352, 1705, 518, 470, 422, 384, 1884, 2230, 1228, 1419, 1815,
                                            826, 1722, 2394, 14, 1621, 266, 1197, 1580, 50, 1924, 57, 1546, 1450, 2427, 225, 450, 1153, 1230, 539]
combined_outlier_agents = {}
combined_outlier_agents['WORK'] = combined_work_outlier_agents
combined_outlier_agents['SOCIAL'] = combined_social_outlier_agents
combined_outlier_agents['HUNGER'] = combined_hunger_outlier_agents
