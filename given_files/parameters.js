class Parameters {
    constructor(itemWeights, itemValues, maxWeightCapacity) {
        this.itemWeights = itemWeights;
        this.itemValues = itemValues;
        this.maxWeightCapacity = maxWeightCapacity;
    }

    static easy() {
        const easyMaxWeight = 20000;
        const weights = [7250, 421, 7195, 2104, 5077, 1537, 2229, 5653, 474, 6881];
        const values = [9818, 4040, 5412, 2789, 8080, 793, 886, 4294, 2366, 2929];
        return new Parameters(weights, values, easyMaxWeight);
    }

    static medium() {
        const mediumMaxWeight = 60000;
        const weights = [1076, 8879, 9401, 8948, 3814, 9599, 2434, 82, 9719, 8063, 1642, 1511, 762, 3922, 2796, 4171, 4415, 9487, 9384, 5033, 4140, 9538, 8043, 8222, 6179, 3026, 8485, 3837, 9122, 6612, 7953, 1255, 6352, 5573, 9763, 8144, 3789, 1500, 4907, 8322, 5261, 956, 9273, 7175, 4259, 3005, 6271, 8327, 4180, 3829, 7747, 3423, 8277, 1257, 1578, 9370, 937, 9802, 1832, 662, 2088, 6896, 98, 707, 8469, 278, 7490, 1881, 651, 5344, 7936, 9575, 2433, 2899, 6497, 861, 6492, 6430, 6229, 7139, 3616, 8259, 5724, 8218, 5223, 764, 4249, 1759, 5644, 4466, 6599, 9539, 6186, 3424, 4542, 5720, 5574, 3262, 7813, 8139];
        const values = [3795, 3219, 874, 6627, 4056, 4262, 3650, 5191, 834, 9215, 6761, 6800, 9360, 4531, 6514, 2582, 4773, 1147, 2130, 4173, 4102, 3111, 9397, 2971, 7412, 2310, 7752, 3665, 3151, 8552, 3576, 1575, 3276, 3552, 4152, 5242, 7999, 7484, 8407, 1121, 5725, 2244, 483, 69, 3126, 9929, 3332, 3621, 250, 7518, 2237, 8479, 9347, 3563, 5264, 320, 8147, 7084, 9811, 1404, 8445, 5080, 2298, 6876, 9995, 3510, 7907, 4446, 7102, 1658, 5266, 1399, 9226, 7114, 5415, 4137, 3306, 4481, 6857, 7745, 2262, 1581, 5154, 4981, 5849, 5250, 2656, 7086, 2065, 3933, 2347, 3695, 2226, 4151, 4750, 4732, 9210, 6934, 1727, 4638];
        return new Parameters(weights, values, mediumMaxWeight);
    }

    static hard() {
        const hardMaxWeight = 120000;
        const weights = [8429, 6601, 7272, 7832, 1204, 2396, 8460, 6927, 825, 3899, 9029, 9752, 4801, 1455, 2364, 2970, 2414, 3417, 4958, 4811, 5281, 3107, 1975, 7455, 4438, 4125, 8597, 2122, 4366, 9417, 9197, 6781, 1542, 6517, 508, 265, 4638, 608, 1158, 2898, 6974, 3762, 326, 2131, 5659, 4635, 8395, 6861, 2116, 7164, 2341, 2183, 4090, 9917, 5117, 5816, 2862, 7043, 7838, 8294, 4600, 7648, 3565, 2170, 4833, 206, 7392, 9475, 2946, 5121, 5225, 2796, 629, 760, 601, 3168, 4953, 9258, 6675, 7414, 48, 8856, 1457, 8012, 2456, 3847, 4797, 677, 6253, 4038, 1669, 3417, 9940, 6920, 2268, 1745, 7822, 3001, 1338, 4401, 2098, 5053, 6716, 5921, 8163, 7759, 7790, 6808, 9439, 9294, 4773, 5874, 8948, 1927, 6404, 6536, 498, 2428, 7265, 2929, 9009, 6555, 2949, 9877, 1154, 1721, 825, 2904, 3152, 3771, 9210, 2044, 6958, 2700, 237, 2483, 2494, 6473, 1631, 5307, 1307, 7431, 6020, 246, 3326, 9723, 2258, 295, 8877, 6896, 3928, 2627, 4450, 7361, 5295, 69, 1814, 9392, 7955, 6379, 9912, 8505, 3856, 7865, 3028, 3125, 2025, 8669, 9361, 2121, 7070, 1838, 4310, 5640, 8126, 8727, 9354, 2056, 2366, 7437, 9226, 2166, 8411, 2360, 9079, 1615, 1615, 5211, 4281, 6891, 6399, 8104, 8124, 1634, 1566, 652, 7359, 4041, 2794, 8328, 8055, 4460, 3243, 4378, 639, 8133, 9614, 6590, 19, 2006, 4294, 1605, 687, 8843, 7648, 6161, 6769, 1004, 6192, 7169, 7491, 1685, 682, 4405, 2790, 7822, 5419, 884, 7618, 7670, 7413, 3204, 6499, 8158, 6332, 2102, 3464, 7941, 3941, 5639, 1699, 2279, 6714, 4463, 9533, 1230, 3726, 7954, 4650, 6192, 646, 2703, 9896, 1891, 7431, 7747, 2368, 6618, 300, 6799, 9758, 980, 7719, 2941, 680, 8992, 1606, 1574, 3661, 5896, 4713, 2201, 5268, 1013, 4053, 315, 6510, 9548, 7678, 7753, 6883, 4387, 802, 4254, 1612, 5153, 7715, 8814, 4443, 8828, 4803, 1184, 1741, 6183, 821, 2338, 898, 7731, 1346, 6589, 8926, 7918, 9660, 3798, 8880, 9560, 7413, 8557, 6061, 658, 5898, 881, 3120, 1940, 7355, 1224, 6024, 673, 5310, 6640, 3818, 8747, 5208, 4850, 1857, 4445, 5154, 4021, 1771, 333, 7307, 4574, 5042, 9136, 2535, 9343, 1156, 3071, 1890, 106, 2162, 7667, 5765, 6074, 5159, 6557, 1912, 6208, 5185, 1450, 8743, 2418, 7769, 8651, 7969, 7081, 8817, 7726, 2574, 7155, 6362, 7116, 6542, 1917, 5059, 651, 4174, 9745, 7450, 1821, 1362, 7708, 9158, 9866, 1296, 308, 8233, 8918, 4835, 1524, 7537, 1779, 1915, 3809, 6017, 6308, 8031, 8938, 2023, 3667, 8412, 4626, 3551, 6922, 8528, 5241, 2426, 2876, 8035, 6442, 7879, 3534, 3939, 4574, 1647, 2675, 4190, 2546, 2481, 3373, 87, 8288, 2795, 915, 9765, 1018, 9271, 3982, 4619, 4046, 1223, 4684, 5021, 490, 7707, 7217, 7798, 6445, 1585, 1614, 7730, 1150, 5739, 5941, 9622, 4768, 20, 8237, 1791, 9327, 9098, 1832, 7408, 5630, 5802, 2080, 8417, 2654, 5592, 9409, 1852, 8481, 5326, 5618, 8072, 855, 1091, 6794, 6272, 4443, 2863, 2106, 3310, 6580, 4502, 863, 227, 8432, 8198, 9695, 7153, 9649, 5766, 6467, 2428, 5677, 1217, 7526, 8968, 5246, 6723, 194, 4846, 760, 5224, 2826, 6227, 576, 4246, 3092, 8949, 6663, 8326, 319, 7404, 2933, 828, 6300, 3803, 8485, 4958, 7976, 9179, 4408, 4970, 6653, 9505, 7887, 122, 4883, 4371, 7392, 8390, 5466, 1272, 4498, 7021, 1027, 9284, 8608, 9844, 8823, 1706, 7383, 7164, 5458, 8406, 1687, 7742, 9605, 8717, 3634, 5110, 845, 6721, 1186, 8746, 1699, 5675, 4783, 3347, 3858, 987, 8565, 7923, 2503, 5051, 1270, 2845, 6617, 8777, 4749, 8869, 7665, 7527, 2728, 9440, 6846, 9597, 9395, 228, 6867, 4797, 6785, 425, 1326, 1824, 9633, 6919, 587, 5909, 8477, 3484, 2106, 8592, 8258, 9631, 5482, 7237, 6437, 6571, 9626, 5575, 7734, 3489, 8719, 5299, 590, 8567, 2150, 8488, 2567, 3088, 1723, 939, 6746, 4131, 4350, 4802, 7860, 7165, 190, 9513, 4014, 9056, 206, 5041, 2579, 9327, 2739, 5099, 7129, 6824, 9547, 6086, 6044, 2387, 9664, 8794, 3191, 3076, 679, 5411, 806, 6396, 9905, 4331, 3177, 1947, 3457, 8229, 7756, 2488, 6921, 4158, 6209, 7356, 3812, 9558, 7909, 2508, 8714, 5452, 9330, 9578, 6135, 2392, 579, 7853, 9755, 6106, 6211, 4793, 2164, 3530, 5367, 3727, 5638, 3883, 7518, 1169, 5699, 8995, 5037, 3655, 8373, 7791, 2118, 4152, 7382, 1785, 5566, 5452, 769, 5834, 9609, 9160, 6793, 2684, 1502, 2412, 7571, 4350, 3772, 8799, 7825, 7099, 6107, 643, 9746, 5447, 7979, 8536, 4504, 4399, 4485, 6101, 4492, 2381, 5230, 3507, 5576, 5422, 8535, 2544, 7092, 5517, 7312, 9512, 6768, 2208, 5858, 7078, 5781, 6791, 8302, 6632, 4445, 6768, 5470, 9280, 2893, 5543, 3627, 8523, 5629, 8582, 6007, 1794, 6186, 3958, 210, 2246, 6964, 4908, 1020, 2844, 4045, 4516, 7643, 8369, 6435, 3993, 1494, 1354, 5874, 7537, 2030, 4692, 8177, 9955, 7108, 8387, 9699, 7701, 8555, 5228, 6673, 810, 8973, 6816, 1248, 879, 2673, 1429, 2014, 5514, 2738, 1330, 8509, 5662, 2794, 9769, 9121, 4350, 3474, 5564, 9107, 6415, 7210, 1145, 8552, 9226, 7437, 8455, 4166, 155, 3086, 5883, 3396, 1686, 2274, 6773, 8055, 2038, 8207, 3310, 8274, 2463, 2426, 2182, 6481, 7094, 708, 2265, 7656, 3288, 9640, 6225, 4039, 2650, 2633, 7284, 1444, 2014, 9984, 7961, 2867, 5152, 6686, 2990, 4434, 8232, 4468, 5508, 6575, 2376, 7239, 4029, 7175, 3734, 5705, 7549, 8115, 7115, 9247, 8213, 9619, 1462, 7332, 2238, 7344, 7472, 409, 8734, 6105, 7486, 1732, 8226, 8450, 6082, 5016, 2391, 8715, 4903, 9891, 5407, 8551, 5514, 8384, 9893, 9134, 9856, 5032, 4550, 1567, 5177, 7512, 5397, 1500, 6529, 9876, 8384, 8148, 5230, 1544, 9913, 2101, 7333, 5960, 105, 4244, 1619, 4156, 4242, 9213, 1414, 5790, 7168, 8254, 8558, 5523, 5668, 3014, 6249, 9371, 2561, 1824, 619, 2726, 2309, 1483, 4842, 3677, 9636, 1285, 8579, 7113, 298, 5586, 4594, 5817, 1093, 2838, 2180, 4936, 4290, 3500, 4297, 2977, 8716, 2249, 2403, 5670, 888, 7570, 9781, 178, 6672, 2533, 6352, 7571, 1326, 3759, 6781, 1888, 9851, 5342, 2025, 9951, 1667, 8444, 9794, 6455, 5220, 2544, 1939, 950, 2278, 9363, 7315, 408, 9624, 2117, 1519, 7398, 1605, 5486, 3288, 6052, 9626, 6127, 3333, 6389, 5133, 5079, 8967, 2499, 800, 5089, 245, 2610, 1995, 4363, 6950, 7085, 3094, 7878, 5524, 9135, 3934, 5002, 1135, 6689, 1026, 1046, 2247, 9893, 5252, 2672, 5592, 3928, 5938, 7096, 9685, 3391, 1845, 6382, 684, 8942];
        const values = [3272, 8281, 1424, 216, 6387, 9394, 5945, 757, 6781, 4609, 7190, 4739, 6499, 9271, 3950, 8661, 9288, 4179, 8366, 804, 9365, 5246, 4126, 5138, 4490, 2913, 418, 9589, 477, 2311, 6163, 6642, 1644, 6399, 8092, 7272, 3399, 9812, 3911, 9340, 1384, 8382, 6889, 4109, 2378, 1615, 7682, 3885, 9048, 636, 9946, 614, 2390, 9576, 4179, 5510, 4204, 5771, 9724, 5196, 9204, 4229, 5881, 6413, 9069, 4987, 3091, 3998, 8576, 6524, 1041, 6916, 3304, 3423, 8200, 5576, 9127, 9898, 8342, 4411, 126, 3456, 1630, 6002, 5657, 4973, 3067, 5749, 2316, 9719, 1476, 4674, 2088, 4679, 8883, 648, 1797, 5274, 9174, 4786, 6841, 4318, 2950, 6379, 9363, 4640, 4022, 880, 3014, 9856, 1345, 3097, 4530, 6976, 9598, 5249, 1488, 9049, 5867, 9987, 9928, 3709, 4112, 6173, 4695, 6230, 503, 1000, 9303, 7339, 8802, 7388, 5775, 7243, 9558, 5872, 1817, 5969, 6814, 2804, 2113, 3216, 1002, 3826, 5396, 8540, 740, 9215, 2407, 4609, 9909, 8194, 3108, 5873, 9268, 7160, 5359, 5485, 9322, 5346, 7479, 4184, 4826, 231, 135, 5656, 2831, 2099, 2182, 7153, 7857, 2604, 5829, 2192, 1445, 4432, 7076, 3160, 6075, 64, 3586, 3313, 9621, 4972, 8246, 1048, 8906, 2391, 1459, 669, 4765, 7613, 4174, 3050, 5185, 6162, 1467, 320, 8258, 6107, 4315, 175, 5147, 6245, 3744, 4987, 551, 8995, 8868, 3417, 4747, 4256, 6718, 7710, 4716, 3495, 2766, 9841, 1891, 8118, 606, 6961, 4452, 6361, 9527, 7449, 2709, 3049, 8030, 9209, 7807, 2174, 7235, 559, 787, 2510, 990, 332, 1529, 495, 1839, 8155, 6682, 1041, 3659, 6774, 682, 8446, 5615, 9327, 6586, 2303, 9443, 4546, 1648, 3283, 5704, 3724, 8776, 6467, 4203, 4175, 8996, 1221, 2388, 1163, 3913, 7661, 9678, 9227, 6347, 6106, 3864, 9058, 2571, 9062, 6568, 3387, 561, 9705, 9449, 1771, 9449, 3660, 1278, 232, 5783, 3284, 8261, 3918, 6600, 3726, 389, 6119, 9405, 4312, 1067, 8349, 7417, 4683, 1994, 9106, 3795, 6621, 2360, 6398, 1066, 570, 3143, 6553, 6030, 6555, 129, 462, 1164, 8550, 5941, 6983, 1476, 458, 795, 3787, 484, 9705, 4881, 2158, 296, 2679, 1740, 297, 5654, 783, 488, 1003, 2673, 5368, 6133, 2954, 964, 199, 5995, 5679, 5719, 8759, 4061, 4475, 6476, 5271, 4136, 7026, 4791, 8288, 708, 436, 455, 2710, 7217, 9373, 3082, 5256, 4059, 767, 4238, 5034, 8873, 9367, 3412, 907, 765, 7319, 9747, 1291, 524, 2276, 5704, 8916, 8993, 4473, 9666, 4982, 8599, 2785, 4411, 9834, 5646, 759, 947, 2896, 1100, 8261, 6626, 5171, 4648, 8547, 7603, 1198, 6365, 640, 4447, 4371, 8405, 6388, 7703, 5068, 69, 166, 32, 52, 647, 8576, 2303, 4441, 4839, 7909, 1260, 5847, 4580, 6257, 5907, 94, 7512, 539, 8198, 5600, 5977, 5006, 2080, 2123, 7944, 9783, 9565, 5421, 8686, 7951, 7543, 6258, 9715, 8123, 2124, 2261, 4230, 4273, 8523, 947, 9769, 1485, 9468, 9861, 2272, 3013, 9016, 31, 1749, 7596, 612, 8861, 9480, 8532, 3220, 432, 9491, 6046, 9357, 341, 3170, 5909, 2053, 9332, 7606, 1144, 1109, 1098, 2963, 3309, 4066, 5812, 3926, 6190, 3799, 7103, 3924, 1219, 8968, 8316, 6029, 8925, 9145, 6943, 1950, 3367, 4031, 6543, 6908, 7237, 3866, 8412, 2502, 8891, 6686, 8007, 3091, 9069, 5574, 9725, 9437, 7169, 1594, 9541, 3758, 5307, 2455, 6596, 3383, 5745, 8023, 7151, 8326, 6446, 2642, 9365, 7016, 8339, 2805, 5914, 1368, 2824, 845, 8674, 205, 2078, 7213, 7626, 1742, 1225, 7242, 1159, 1961, 4270, 8333, 3886, 1961, 1768, 707, 3443, 6966, 433, 8352, 6042, 4893, 964, 9143, 6291, 1646, 9216, 7634, 3567, 3675, 3275, 2886, 8517, 1505, 82, 2542, 7910, 1104, 6926, 1708, 8147, 6532, 5769, 5038, 9691, 6437, 9314, 4354, 6407, 1577, 5750, 8641, 4335, 7954, 2267, 4690, 2392, 7524, 8591, 3392, 1153, 1528, 8335, 8585, 3573, 6866, 3857, 7855, 5788, 749, 6573, 1102, 961, 1157, 1148, 7439, 3014, 1928, 3931, 679, 7141, 2783, 1484, 6005, 6614, 2293, 7180, 7298, 4120, 4080, 9638, 2478, 142, 8758, 9281, 8275, 7402, 1942, 3709, 1145, 5478, 7432, 9935, 6055, 2930, 9672, 9857, 8057, 9173, 4331, 67, 3813, 4928, 4962, 5356, 7685, 8042, 260, 6444, 6928, 7287, 7386, 3450, 4022, 2653, 6159, 8701, 9691, 4966, 7296, 8960, 6620, 4253, 5653, 9232, 2676, 8762, 2174, 2614, 951, 4919, 2309, 2875, 4365, 8064, 9470, 8599, 493, 8985, 4470, 7408, 7762, 4078, 7210, 7506, 1099, 1060, 709, 9129, 2268, 3394, 7535, 9217, 350, 2406, 9461, 6872, 7821, 5414, 6315, 8269, 3677, 980, 2302, 4705, 589, 3338, 7548, 7743, 4583, 7201, 6907, 4057, 4542, 6951, 780, 4636, 1007, 1903, 1091, 5448, 2969, 6503, 2822, 780, 6241, 7815, 8124, 569, 1686, 8761, 9101, 5774, 8201, 4391, 5619, 6542, 3319, 3776, 5159, 974, 2363, 9624, 9925, 2399, 429, 7375, 8724, 8064, 1637, 6781, 9426, 7538, 1770, 7646, 2498, 9252, 1091, 7535, 6459, 9218, 8752, 7069, 2691, 3262, 3140, 1721, 911, 7865, 2119, 4070, 9406, 1597, 869, 4810, 8663, 8268, 5593, 6455, 1689, 6500, 9091, 9644, 3789, 418, 6576, 1482, 5481, 1514, 3880, 4050, 7036, 9653, 7359, 7343, 1710, 7935, 3316, 5991, 2126, 8039, 2638, 8661, 9087, 2116, 2942, 7968, 197, 563, 377, 6444, 1143, 2034, 9629, 1452, 1931, 291, 4763, 4524, 5152, 6703, 5003, 1484, 6536, 2455, 5609, 4804, 6078, 2849, 8395, 4793, 6956, 9982, 5439, 9038, 4736, 2963, 9233, 1751, 1882, 787, 7302, 7418, 3776, 6693, 2282, 7062, 1773, 1657, 6594, 1022, 5359, 7200, 833, 2483, 4816, 8519, 9399, 9518, 401, 9416, 7837, 9590, 940, 6170, 9831, 9609, 6476, 8490, 1570, 952, 2612, 1372, 3083, 1191, 731, 6641, 5784, 5425, 8341, 3940, 6160, 6180, 355, 654, 6486, 2843, 938, 1281, 9467, 9050, 9200, 2131, 4948, 2535, 6206, 1100, 5722, 4904, 8172, 6536, 6739, 8605, 5609, 2947, 3204, 2665, 5217, 3930, 5059, 1212, 3160, 477, 7785, 6577, 349, 7805, 3212, 1731, 5690, 4223, 3299, 8168, 7187, 6941, 3664, 7599, 3099, 6193, 159, 617, 948, 4717, 8830, 1425, 2542, 4476, 3364, 2502, 9912, 1258, 7173, 7902, 6228, 4596, 4210, 1412, 347, 7108, 8612, 8698, 9192, 4694, 3678, 4184, 9542, 5332, 868, 4463, 4459, 6523, 5521, 3463, 9548, 7996, 7282, 4487, 4617, 8268, 8403, 4200, 3721, 215, 948, 1432, 9733, 6478, 9491, 6635, 1407, 330, 2652, 3078, 9530, 3369, 5272, 4311, 758, 7235, 1083, 7433, 3196, 7462, 674, 2270, 508, 3196, 4521, 4517, 5788, 9118, 6446, 5137];
        return new Parameters(weights, values, hardMaxWeight);
    }
}

console.log(Parameters.easy().itemWeights)