import requests
import json
import datetime
import xlwt
import openpyxl
import threading
import time
import datetime
import random
from concurrent.futures import ThreadPoolExecutor
import time


name_list=['fceshi00', 'fceshi01', 'fceshi02', 'fceshi03', 'fceshi04', 'fceshi05', 'fceshi06', 'fceshi07', 'fceshi08', 'fceshi09', 'fceshi010', 'fceshi011', 'fceshi012', 'fceshi013', 'fceshi014', 'fceshi015', 'fceshi016', 'fceshi017', 'fceshi018', 'fceshi019', 'fceshi020', 'fceshi021', 'fceshi022', 'fceshi023', 'fceshi024', 'fceshi025', 'fceshi026', 'fceshi027', 'fceshi028', 'fceshi029', 'fceshi030', 'fceshi031', 'fceshi032', 'fceshi033', 'fceshi034', 'fceshi035', 'fceshi036', 'fceshi037', 'fceshi038', 'fceshi039', 'fceshi040', 'fceshi041', 'fceshi042', 'fceshi043', 'fceshi044', 'fceshi045', 'fceshi046', 'fceshi047', 'fceshi048', 'fceshi049', 'fceshi050', 'fceshi051', 'fceshi052', 'fceshi053', 'fceshi054', 'fceshi055', 'fceshi056', 'fceshi057', 'fceshi058', 'fceshi059', 'fceshi060', 'fceshi061', 'fceshi062', 'fceshi063', 'fceshi064', 'fceshi065', 'fceshi066', 'fceshi067', 'fceshi068', 'fceshi069', 'fceshi070', 'fceshi071', 'fceshi072', 'fceshi073', 'fceshi074', 'fceshi075', 'fceshi076', 'fceshi077', 'fceshi078', 'fceshi079', 'fceshi080', 'fceshi081', 'fceshi082', 'fceshi083', 'fceshi084', 'fceshi085', 'fceshi086', 'fceshi087', 'fceshi088', 'fceshi089', 'fceshi090', 'fceshi091', 'fceshi092', 'fceshi093', 'fceshi094', 'fceshi095', 'fceshi096', 'fceshi097', 'fceshi098', 'fceshi099', 'fceshi0100', 'fceshi0101', 'fceshi0102', 'fceshi0103', 'fceshi0104', 'fceshi0105', 'fceshi0106', 'fceshi0107', 'fceshi0108', 'fceshi0109', 'fceshi0110', 'fceshi0111', 'fceshi0112', 'fceshi0113', 'fceshi0114', 'fceshi0115', 'fceshi0116', 'fceshi0117', 'fceshi0118', 'fceshi0119', 'fceshi0120', 'fceshi0121', 'fceshi0122', 'fceshi0123', 'fceshi0124', 'fceshi0125', 'fceshi0126', 'fceshi0127', 'fceshi0128', 'fceshi0129', 'fceshi0130', 'fceshi0131', 'fceshi0132', 'fceshi0133', 'fceshi0134', 'fceshi0135', 'fceshi0136', 'fceshi0137', 'fceshi0138', 'fceshi0139', 'fceshi0140', 'fceshi0141', 'fceshi0142', 'fceshi0143', 'fceshi0144', 'fceshi0145', 'fceshi0146', 'fceshi0147', 'fceshi0148', 'fceshi0149', 'fceshi0150', 'fceshi0151', 'fceshi0152', 'fceshi0153', 'fceshi0154', 'fceshi0155', 'fceshi0156', 'fceshi0157', 'fceshi0158', 'fceshi0159', 'fceshi0160', 'fceshi0161', 'fceshi0162', 'fceshi0163', 'fceshi0164', 'fceshi0165', 'fceshi0166', 'fceshi0167', 'fceshi0168', 'fceshi0169', 'fceshi0170', 'fceshi0171', 'fceshi0172', 'fceshi0173', 'fceshi0174', 'fceshi0175', 'fceshi0176', 'fceshi0177', 'fceshi0178', 'fceshi0179', 'fceshi0180', 'fceshi0181', 'fceshi0182', 'fceshi0183', 'fceshi0184', 'fceshi0185', 'fceshi0186', 'fceshi0187', 'fceshi0188', 'fceshi0189', 'fceshi0190', 'fceshi0191', 'fceshi0192', 'fceshi0193', 'fceshi0194', 'fceshi0195', 'fceshi0196', 'fceshi0197', 'fceshi0198', 'fceshi0199', 'fceshi0200', 'fceshi0201', 'fceshi0202', 'fceshi0203', 'fceshi0204', 'fceshi0205', 'fceshi0206', 'fceshi0207', 'fceshi0208', 'fceshi0209', 'fceshi0210', 'fceshi0211', 'fceshi0212', 'fceshi0213', 'fceshi0214', 'fceshi0215', 'fceshi0216', 'fceshi0217', 'fceshi0218', 'fceshi0219', 'fceshi0220', 'fceshi0221', 'fceshi0222', 'fceshi0223', 'fceshi0224', 'fceshi0225', 'fceshi0226', 'fceshi0227', 'fceshi0228', 'fceshi0229', 'fceshi0230', 'fceshi0231', 'fceshi0232', 'fceshi0233', 'fceshi0234', 'fceshi0235', 'fceshi0236', 'fceshi0237', 'fceshi0238', 'fceshi0239', 'fceshi0240', 'fceshi0241', 'fceshi0242', 'fceshi0243', 'fceshi0244', 'fceshi0245', 'fceshi0246', 'fceshi0247', 'fceshi0248', 'fceshi0249', 'fceshi0250', 'fceshi0251', 'fceshi0252', 'fceshi0253', 'fceshi0254', 'fceshi0255', 'fceshi0256', 'fceshi0257', 'fceshi0258', 'fceshi0259', 'fceshi0260', 'fceshi0261', 'fceshi0262', 'fceshi0263', 'fceshi0264', 'fceshi0265', 'fceshi0266', 'fceshi0267', 'fceshi0268', 'fceshi0269', 'fceshi0270', 'fceshi0271', 'fceshi0272', 'fceshi0273', 'fceshi0274', 'fceshi0275', 'fceshi0276', 'fceshi0277', 'fceshi0278', 'fceshi0279', 'fceshi0280', 'fceshi0281', 'fceshi0282', 'fceshi0283', 'fceshi0284', 'fceshi0285', 'fceshi0286', 'fceshi0287', 'fceshi0288', 'fceshi0289', 'fceshi0290', 'fceshi0291', 'fceshi0292', 'fceshi0293', 'fceshi0294', 'fceshi0295', 'fceshi0296', 'fceshi0297', 'fceshi0298', 'fceshi0299', 'fceshi0300', 'fceshi0301', 'fceshi0302', 'fceshi0303', 'fceshi0304', 'fceshi0305', 'fceshi0306', 'fceshi0307', 'fceshi0308', 'fceshi0309', 'fceshi0310', 'fceshi0311', 'fceshi0312', 'fceshi0313', 'fceshi0314', 'fceshi0315', 'fceshi0316', 'fceshi0317', 'fceshi0318', 'fceshi0319', 'fceshi0320', 'fceshi0321', 'fceshi0322', 'fceshi0323', 'fceshi0324', 'fceshi0325', 'fceshi0326', 'fceshi0327', 'fceshi0328', 'fceshi0329', 'fceshi0330', 'fceshi0331', 'fceshi0332', 'fceshi0333', 'fceshi0334', 'fceshi0335', 'fceshi0336', 'fceshi0337', 'fceshi0338', 'fceshi0339', 'fceshi0340', 'fceshi0341', 'fceshi0342', 'fceshi0343', 'fceshi0344', 'fceshi0345', 'fceshi0346', 'fceshi0347', 'fceshi0348', 'fceshi0349', 'fceshi0350', 'fceshi0351', 'fceshi0352', 'fceshi0353', 'fceshi0354', 'fceshi0355', 'fceshi0356', 'fceshi0357', 'fceshi0358', 'fceshi0359', 'fceshi0360', 'fceshi0361', 'fceshi0362', 'fceshi0363', 'fceshi0364', 'fceshi0365', 'fceshi0366', 'fceshi0367', 'fceshi0368', 'fceshi0369', 'fceshi0370', 'fceshi0371', 'fceshi0372', 'fceshi0373', 'fceshi0374', 'fceshi0375', 'fceshi0376', 'fceshi0377', 'fceshi0378', 'fceshi0379', 'fceshi0380', 'fceshi0381', 'fceshi0382', 'fceshi0383', 'fceshi0384', 'fceshi0385', 'fceshi0386', 'fceshi0387', 'fceshi0388', 'fceshi0389', 'fceshi0390', 'fceshi0391', 'fceshi0392', 'fceshi0393', 'fceshi0394', 'fceshi0395', 'fceshi0396', 'fceshi0397', 'fceshi0398', 'fceshi0399', 'fceshi0400', 'fceshi0401', 'fceshi0402', 'fceshi0403', 'fceshi0404', 'fceshi0405', 'fceshi0406', 'fceshi0407', 'fceshi0408', 'fceshi0409', 'fceshi0410', 'fceshi0411', 'fceshi0412', 'fceshi0413', 'fceshi0414', 'fceshi0415', 'fceshi0416', 'fceshi0417', 'fceshi0418', 'fceshi0419', 'fceshi0420', 'fceshi0421', 'fceshi0422', 'fceshi0423', 'fceshi0424', 'fceshi0425', 'fceshi0426', 'fceshi0427', 'fceshi0428', 'fceshi0429', 'fceshi0430', 'fceshi0431', 'fceshi0432', 'fceshi0433', 'fceshi0434', 'fceshi0435', 'fceshi0436', 'fceshi0437', 'fceshi0438', 'fceshi0439', 'fceshi0440', 'fceshi0441', 'fceshi0442', 'fceshi0443', 'fceshi0444', 'fceshi0445', 'fceshi0446', 'fceshi0447', 'fceshi0448', 'fceshi0449', 'fceshi0450', 'fceshi0451', 'fceshi0452', 'fceshi0453', 'fceshi0454', 'fceshi0455', 'fceshi0456', 'fceshi0457', 'fceshi0458', 'fceshi0459', 'fceshi0460', 'fceshi0461', 'fceshi0462', 'fceshi0463', 'fceshi0464', 'fceshi0465', 'fceshi0466', 'fceshi0467', 'fceshi0468', 'fceshi0469', 'fceshi0470', 'fceshi0471', 'fceshi0472', 'fceshi0473', 'fceshi0474', 'fceshi0475', 'fceshi0476', 'fceshi0477', 'fceshi0478', 'fceshi0479', 'fceshi0480', 'fceshi0481', 'fceshi0482', 'fceshi0483', 'fceshi0484', 'fceshi0485', 'fceshi0486', 'fceshi0487', 'fceshi0488', 'fceshi0489', 'fceshi0490', 'fceshi0491', 'fceshi0492', 'fceshi0493', 'fceshi0494', 'fceshi0495', 'fceshi0496', 'fceshi0497', 'fceshi0498', 'fceshi0499', 'fceshi0500', 'fceshi0501', 'fceshi0502', 'fceshi0503', 'fceshi0504', 'fceshi0505', 'fceshi0506', 'fceshi0507', 'fceshi0508', 'fceshi0509', 'fceshi0510', 'fceshi0511', 'fceshi0512', 'fceshi0513', 'fceshi0514', 'fceshi0515', 'fceshi0516', 'fceshi0517', 'fceshi0518', 'fceshi0519', 'fceshi0520', 'fceshi0521', 'fceshi0522', 'fceshi0523', 'fceshi0524', 'fceshi0525', 'fceshi0526', 'fceshi0527', 'fceshi0528', 'fceshi0529', 'fceshi0530', 'fceshi0531', 'fceshi0532', 'fceshi0533', 'fceshi0534', 'fceshi0535', 'fceshi0536', 'fceshi0537', 'fceshi0538', 'fceshi0539', 'fceshi0540', 'fceshi0541', 'fceshi0542', 'fceshi0543', 'fceshi0544', 'fceshi0545', 'fceshi0546', 'fceshi0547', 'fceshi0548', 'fceshi0549', 'fceshi0550', 'fceshi0551', 'fceshi0552', 'fceshi0553', 'fceshi0554', 'fceshi0555', 'fceshi0556', 'fceshi0557', 'fceshi0558', 'fceshi0559', 'fceshi0560', 'fceshi0561', 'fceshi0562', 'fceshi0563', 'fceshi0564', 'fceshi0565', 'fceshi0566', 'fceshi0567', 'fceshi01134', 'fceshi01135', 'fceshi0570', 'fceshi0571', 'fceshi0572', 'fceshi0573', 'fceshi0574', 'fceshi0575', 'fceshi0576', 'fceshi0577', 'fceshi0578', 'fceshi0579', 'fceshi0580', 'fceshi0581', 'fceshi0582', 'fceshi0583', 'fceshi0584', 'fceshi0585', 'fceshi0586', 'fceshi0587', 'fceshi0588', 'fceshi0589', 'fceshi0590', 'fceshi0591', 'fceshi0592', 'fceshi0593', 'fceshi0594', 'fceshi0595', 'fceshi0596', 'fceshi0597', 'fceshi0598', 'fceshi0599', 'fceshi0600', 'fceshi0601', 'fceshi0602', 'fceshi0603', 'fceshi0604', 'fceshi0605', 'fceshi0606', 'fceshi0607', 'fceshi0608', 'fceshi0609', 'fceshi0610', 'fceshi0611', 'fceshi0612', 'fceshi0613', 'fceshi0614', 'fceshi0615', 'fceshi0616', 'fceshi0617', 'fceshi0618', 'fceshi0619', 'fceshi0620', 'fceshi0621', 'fceshi0622', 'fceshi0623', 'fceshi0624', 'fceshi0625', 'fceshi0626', 'fceshi0627', 'fceshi0628', 'fceshi0629', 'fceshi0630', 'fceshi0631', 'fceshi0632', 'fceshi0633', 'fceshi0634', 'fceshi0635', 'fceshi0636', 'fceshi0637', 'fceshi0638', 'fceshi0639', 'fceshi0640', 'fceshi0641', 'fceshi0642', 'fceshi0643', 'fceshi0644', 'fceshi0645', 'fceshi0646', 'fceshi0647', 'fceshi0648', 'fceshi0649', 'fceshi0650', 'fceshi0651', 'fceshi0652', 'fceshi0653', 'fceshi0654', 'fceshi0655', 'fceshi0656', 'fceshi0657', 'fceshi0658', 'fceshi0659', 'fceshi0660', 'fceshi0661', 'fceshi0662', 'fceshi0663', 'fceshi0664', 'fceshi0665', 'fceshi0666', 'fceshi0667', 'fceshi0668', 'fceshi0669', 'fceshi0670', 'fceshi0671', 'fceshi0672', 'fceshi0673', 'fceshi0674', 'fceshi0675', 'fceshi0676', 'fceshi0677', 'fceshi0678', 'fceshi0679', 'fceshi0680', 'fceshi0681', 'fceshi0682', 'fceshi0683', 'fceshi0684', 'fceshi0685', 'fceshi0686', 'fceshi0687', 'fceshi0688', 'fceshi0689', 'fceshi0690', 'fceshi0691', 'fceshi0692', 'fceshi0693', 'fceshi0694', 'fceshi0695', 'fceshi0696', 'fceshi0697', 'fceshi0698', 'fceshi0699', 'fceshi0700', 'fceshi0701', 'fceshi0702', 'fceshi0703', 'fceshi0704', 'fceshi0705', 'fceshi0706', 'fceshi0707', 'fceshi0708', 'fceshi0709', 'fceshi0710', 'fceshi0711', 'fceshi0712', 'fceshi0713', 'fceshi0714', 'fceshi0715', 'fceshi0716', 'fceshi0717', 'fceshi0718', 'fceshi0719', 'fceshi0720', 'fceshi0721', 'fceshi0722', 'fceshi0723', 'fceshi0724', 'fceshi0725', 'fceshi0726', 'fceshi0727', 'fceshi0728', 'fceshi0729', 'fceshi0730', 'fceshi0731', 'fceshi0732', 'fceshi0733', 'fceshi0734', 'fceshi0735', 'fceshi0736', 'fceshi0737', 'fceshi0738', 'fceshi0739', 'fceshi0740', 'fceshi0741', 'fceshi0742', 'fceshi0743', 'fceshi0744', 'fceshi0745', 'fceshi0746', 'fceshi0747', 'fceshi0748', 'fceshi0749', 'fceshi0750', 'fceshi0751', 'fceshi0752', 'fceshi0753', 'fceshi0754', 'fceshi0755', 'fceshi0756', 'fceshi0757', 'fceshi0758', 'fceshi0759', 'fceshi0760', 'fceshi0761', 'fceshi0762', 'fceshi0763', 'fceshi0764', 'fceshi0765', 'fceshi0766', 'fceshi0767', 'fceshi0768', 'fceshi0769', 'fceshi0770', 'fceshi0771', 'fceshi0772', 'fceshi0773', 'fceshi0774', 'fceshi0775', 'fceshi0776', 'fceshi0777', 'fceshi0778', 'fceshi0779', 'fceshi0780', 'fceshi0781', 'fceshi0782', 'fceshi0783', 'fceshi0784', 'fceshi0785', 'fceshi0786']
# name_list=['ht01', 'ht02', 'ht03', 'ht04', 'ht05', 'ht06', 'ht07', 'ht08', 'ht09', 'ht010', 'ht011', 'ht012', 'ht013', 'ht014', 'ht015', 'ht016', 'ht017', 'ht018', 'ht019', 'ht020', 'ht021', 'ht022', 'ht023', 'ht024', 'ht025', 'ht026', 'ht027', 'ht028', 'ht029', 'ht030', 'ht031', 'ht032', 'ht033', 'ht034', 'ht035', 'ht036', 'ht037', 'ht038', 'ht039', 'ht040', 'ht041', 'ht042', 'ht043', 'ht044', 'ht045', 'ht046', 'ht047', 'ht048', 'ht049', 'ht050', 'ht051', 'ht052', 'ht053', 'ht054', 'ht055', 'ht056', 'ht057', 'ht058', 'ht059', 'ht060', 'ht061', 'ht062', 'ht063', 'ht064', 'ht065', 'ht066', 'ht067', 'ht068', 'ht069', 'ht070', 'ht071', 'ht072', 'ht073', 'ht074', 'ht075', 'ht076', 'ht077', 'ht078', 'ht079', 'ht080', 'ht081', 'ht082', 'ht083', 'ht084', 'ht085', 'ht086', 'ht087', 'ht088', 'ht089', 'ht090', 'ht091', 'ht092', 'ht093', 'ht094', 'ht095', 'ht096', 'ht097', 'ht098', 'ht099', 'ht0100', 'ht0101', 'ht0102', 'ht0103', 'ht0104', 'ht0105', 'ht0106', 'ht0107', 'ht0108', 'ht0109', 'ht0110', 'ht0111', 'ht0112', 'ht0113', 'ht0114', 'ht0115', 'ht0116', 'ht0117', 'ht0118', 'ht0119', 'ht0120', 'ht0121', 'ht0122', 'ht0123', 'ht0124', 'ht0125', 'ht0126', 'ht0127', 'ht0128', 'ht0129', 'ht0130', 'ht0131', 'ht0132', 'ht0133', 'ht0134', 'ht0135', 'ht0136', 'ht0137', 'ht0138', 'ht0139', 'ht0140', 'ht0141', 'ht0142', 'ht0143', 'ht0144', 'ht0145', 'ht0146', 'ht0147', 'ht0148', 'ht0149', 'ht0150', 'ht0151', 'ht0152', 'ht0153', 'ht0154', 'ht0155', 'ht0156', 'ht0157', 'ht0158', 'ht0159', 'ht0160', 'ht0161', 'ht0162', 'ht0163', 'ht0164', 'ht0165', 'ht0166', 'ht0167', 'ht0168', 'ht0169', 'ht0170', 'ht0171', 'ht0172', 'ht0173', 'ht0174', 'ht0175', 'ht0176', 'ht0177', 'ht0178', 'ht0179', 'ht0180', 'ht0181', 'ht0182', 'ht0183', 'ht0184', 'ht0185', 'ht0186', 'ht0187', 'ht0188', 'ht0189', 'ht0190', 'ht0191', 'ht0192', 'ht0193', 'ht0194', 'ht0195', 'ht0196', 'ht0197', 'ht0198', 'ht0199', 'ht0200', 'ht0201', 'ht0202', 'ht0203', 'ht0204', 'ht0205', 'ht0206', 'ht0207', 'ht0208', 'ht0209', 'ht0210', 'ht0211', 'ht0212', 'ht0213', 'ht0214', 'ht0215', 'ht0216', 'ht0217', 'ht0218', 'ht0219', 'ht0220', 'ht0221', 'ht0222', 'ht0223', 'ht0224', 'ht0225', 'ht0226', 'ht0227', 'ht0228', 'ht0229', 'ht0230', 'ht0231', 'ht0232', 'ht0233', 'ht0234', 'ht0235', 'ht0236', 'ht0237', 'ht0238', 'ht0239', 'ht0240', 'ht0241', 'ht0242', 'ht0243', 'ht0244', 'ht0245', 'ht0246', 'ht0247', 'ht0248', 'ht0249', 'ht0250', 'ht0251', 'ht0252', 'ht0253', 'ht0254', 'ht0255', 'ht0256', 'ht0257', 'ht0258', 'ht0259', 'ht0260', 'ht0261', 'ht0262', 'ht0263', 'ht0264', 'ht0265', 'ht0266', 'ht0267', 'ht0268', 'ht0269', 'ht0270', 'ht0271', 'ht0272', 'ht0273', 'ht0274', 'ht0275', 'ht0276', 'ht0277', 'ht0278', 'ht0279', 'ht0280', 'ht0281', 'ht0282']


i_list = []

toten_list = []
orderNo_list = []
# 赛事ID列表
INPLAY_matchid_list = []
TODAY_matchid_list = []
EARLY_matchid_list = []

INPLAY_num_list = []
TODAY_num_list = []
EARLY_num_list = []

sort_list_null = []
matchid_dict = {}
ttt_list = []

mixedNum_N_1_number_YYds_list_01 = []
mixedNum_N_1_number_YYds_list_02 = []
mixedNum_N_1_number_YYds_list_03 = []
# 最后打印列表
matchid_yyds = []
sprot_yyds = []
LAY_yyds = []
orderNo_yyds = []

all_mixedNum_list = []
all_mixedNum_N_list = []

# 下注字典
submit_dict = {}
submit_list = []
submit_yyds_list = []
list_a_b = []

mixedNum_list = []
mixedNum_N_list = []

# 下注相关列表
sub_list = []
outcomeId_lsit = []
odds_list = []
oddsType_list = []
orderNo_list = []
kkkk_lsit = []
sport_lsit = []
sport_lsit_null = []

sr_match_list = []
# 写入text
aa_list = []
bb_list = []
cc_list = []
dd_list = []
ee_list = []
yy_list = []
num_list = []
oddt_list = []
ods_list = []

count01 = 0
count = 3


def get_toten_00():
    global toten, name
    # 账号的拼接
    name = "fceshi0" + str(0)
    # name="CCeshi0"+str(j)
    url = str(URL) + "/creditUser/creditUserLogIn"
    headers01 = {'content-type': 'application/json'}
    data = {
        "userName": name,
        "password": "991444c1f732105f81fa51df09c2619d",
        "loginUrl": "http://192.168.10.120:96"
    }
    response = requests.post(url=url, headers=headers01, json=data)
    # 返回结果json转化
    results = json.loads(response.text)
    # print(results)
    toten = results['data']['data']['accessCode']
    # toten_list.append(toten)
    # print(f"正在下注用户：fceshi0{j}")
    # print(f"toten:{toten}")
    return toten


# 请求登录接口，获取toten
def get_toten_01(name):
    global toten01
    # 账号的拼接
    # name = "fceshi0" + str(i)
    # name="CCeshi0"+str(j)
    url = str(URL) + "/creditUser/creditUserLogIn"
    headers01 = {'content-type': 'application/json'}
    data = {
        "userName": name,
        "password": "991444c1f732105f81fa51df09c2619d",
        "loginUrl": "http://192.168.10.120:96"
    }
    response = requests.post(url=url, headers=headers01, json=data)
    # 返回结果json转化
    results = json.loads(response.text)
    # print(results)
    toten01 = results['data']['data']['accessCode']
    toten_list.append(toten01)
    print(f"正在下注用户：{name},toten:{toten01}")
    time.sleep(1)
    # print(f"toten:{toten}")
    return toten01


def get_balance(toten01):
    global balance
    url = str(URL) + "/creditUser/getUserAmount"
    headers01 = {
        'content-type': 'application/json',
        'lang': 'ZH',
        'accessCode': toten01
    }
    date = {}
    response = requests.get(url=url, headers=headers01, params=date)
    # 返回结果json转化
    results = json.loads(response.text)
    # print(results)
    balance = results['data']['balance']
    winLoseAmount = results['data']['winLoseAmount']
    print(str(name) + "   " + "余额：" + str(balance) + "  输赢：" + str(winLoseAmount) + "\n")
    # 写入订单详情
    path02 = "C:\\test\\balance-01.txt"
    f = open(path02, 'a')
    f.write(
        str(name) + "   " + "余额：" + str(balance) + "  输赢：" + str(winLoseAmount) + "\n"
    )
    # print(f"已完成{number}")
    return balance


# 获取赛事信息
def get_today_odds(nub, oddsType):
    global odds, ods, yy, matchId
    # if count01 % 3 > 0:
    #     # count01-=3
    #     nub = random.randint(2, 3)
    #     print("count01%3取值：" + str(count01 % 3))
    #     print("取模随机取值：" + str(nub))
    # else:
    #     nub = 3
    #     # nub = random.randint(1, 3)
    #     print("随机早盘取值：" + str(nub))
    if oddsType == 1:
        oddsType_name = "欧洲盘"
    else:
        oddsType_name = "香港盘"
    if nub == 1:
        ods = "滚球盘"
        yy = "INPLAY"
    if nub == 2:
        ods = "今日盘"
        yy = "TODAY"
    if nub == 3:
        ods = "早盘"
        yy = "EARLY"
    print(f"下注盘：{str(ods)},赔率类型：{oddsType_name}，正在遍历赛事,预计需求10~15秒")
    # print(f"正在遍历赛事,预计需求10秒")
    ods_list.append(ods)
    url = str(URL) + "/creditMatchPC/matchList"
    headers01 = {
        'content-type': 'application/json',
        'lang': 'ZH',
        'accessCode': toten
    }
    if nub == 1 or nub == 2:
        data = {
            "sort": 2,
            "periodId": yy,
            "highlight": False,
            "marketGroupId": marketGroupId,
            "sportCategoryId": sport,
            "oddsType": oddsType,
            "tournamentIds": [],
            "matchIds": [],
            "page": 1,
            "limit": 500,
        }
    if nub == 3:
        data = {
            "sort": 2,
            "periodId": yy,
            "highlight": False,
            "marketGroupId": "100",
            "sportCategoryId": sport,
            "oddsType": oddsType,
            "tournamentIds": [],
            "matchIds": [],
            "page": 1,
            "limit": 1000,
            "dateOffset": -1}
    '''
    response = requests.post(url=url, headers=headers01, json=data)
    # 返回结果json转化
    results = json.loads(response.text)
    # print(results)
    odds = results['data']['data']
    oddt_list.append(odds)
    '''
    # test_01=results['data']['data'][0]['matchList'][0]['matchId']
    # print(test_01)
    # 遍历取出对应的赛事matchid
    '''
    nub==1 代表:滚球盘
    nub==2 代表:今日盘
    nub==3 代表:早盘
    '''
    if nub == 1:
        if len(INPLAY_matchid_list) == 0:
            response = requests.post(url=url, headers=headers01, json=data)
            # 返回结果json转化
            results = json.loads(response.text)
            # print(results)
            odds = results['data']['data']
            oddt_list.append(odds)
            for i in odds:
                matchlist = i['matchList']
                for matchinfo in matchlist:
                    INPLAY_matchid_list.append(matchinfo['matchId'])
                    INPLAY_num_list.append(matchinfo['totalMarketAmount'])
            print("共计赛事：" + str(len(INPLAY_matchid_list)))

        else:
            print("共计赛事：" + str(len(INPLAY_matchid_list)))

    if nub == 2:
        if len(TODAY_matchid_list) == 0:
            response = requests.post(url=url, headers=headers01, json=data)
            # 返回结果json转化
            results = json.loads(response.text)
            # print(results)
            odds = results['data']['data']
            oddt_list.append(odds)
            for i in odds:
                matchlist = i['matchList']
                for matchinfo in matchlist:
                    TODAY_matchid_list.append(matchinfo['matchId'])
                    TODAY_num_list.append(matchinfo['totalMarketAmount'])
            print("共计赛事：" + str(len(TODAY_matchid_list)))
        else:
            print("共计赛事：" + str(len(TODAY_matchid_list)))
    if nub == 3:
        if len(EARLY_matchid_list) == 0:
            response = requests.post(url=url, headers=headers01, json=data)
            # 返回结果json转化
            results = json.loads(response.text)
            # print(results)
            odds = results['data']['data']
            # print(odds)
            # print(odds)
            oddt_list.append(odds)
            for i in odds:
                matchlist = i['matchList']
                # 获取球类所有的赛事ID和其所有玩法的盘口数量
                for matchinfo in matchlist:
                    EARLY_matchid_list.append(matchinfo['matchId'])
                    EARLY_num_list.append(matchinfo['totalMarketAmount'])
            print("共计赛事：" + str(len(EARLY_matchid_list)))
        else:
            print("共计赛事：" + str(len(EARLY_matchid_list)))
    if len(INPLAY_matchid_list) > 0:
        matchId = INPLAY_matchid_list
        sort_list_null.append(yyds)
    if len(TODAY_matchid_list) > 0:
        matchId = TODAY_matchid_list
        sort_list_null.append(yyds)
    if len(EARLY_matchid_list) > 0:
        matchId = EARLY_matchid_list
        sort_list_null.append(yyds)

    # matchid_yyds.append(matchId)
    # LAY_yyds.append(yy)
    # print(f"赛事列表赛事ID打印:{matchId}")


# 根据赛事ID，遍历每一场赛事的盘口
def get_odds(g):
    global isLive, num_outcomeId, aa, bb, cc, dd, ee, matchId, count01
    url = str(URL) + "/creditMatchPC/totalMarketList?"
    headers01 = {
        'content-type': 'application/json',
        'lang': 'ZH',
        'accessCode': toten
    }

    data = {
        "matchId": matchId[g],
        "oddsType": oddsType,
        "sportCategoryId": "sr:sport"
    }
    # "matchId": matchId,
    response = requests.get(url=url, headers=headers01, params=data)
    # 返回结果json转化
    results = json.loads(response.text)
    # print(results)
    isLive = results['data']['isLive']
    # print(isLive)
    # outcomeId=results['data']['marketList'][0]['outcomeList'][0][0]['outcomeId']
    # print(outcomeId)
    num_outcomeId = len(results['data']['marketList'])
    # print(num_outcomeId)
    # print(matchId[g])
    # print("下注盘口:" + str(num_outcomeId) + "个")
    if num_outcomeId == 0:
        print(
            "-----------------------------------------------------------" + ods + "无法下注，请重新选择-----------------------------------------------------------")
    # 判断盘口ID，是否为0，为0重新取
    if num_outcomeId == 0:
        count01 = count01 + 1
        get_today_odds()
        get_odds()
    else:
        # 赛事里取出本场比赛的所有盘口ID,方便下注
        # k = random.randint(0, len(results['data']['marketList']))
        k_list = []
        id_list=['16','18','1','66','68','60','223','225','219','188','314','186','256','258','251',]
        for k in range(0, len(results['data']['marketList'])):
            # print((results['data']['marketList'][k]['outcomeList'][0]))
            if results['data']['marketList'][k]['id'] in id_list:
                k_list.append((results['data']['marketList'][k]['outcomeList'][0]))
            else:
                pass
        matchid_dict[matchId[g]] = k_list
        mixedNum_N_1_number_YYds_list_01.append(len(k_list))
        aa_list.append(results['data']['awayTeamName'])
        bb_list.append(results['data']['homeTeamName'])

        # print(matchid_dict)
        # print(matchid_dict[matchId[g]])
        # matchid_dict.clear()
    time.sleep(1)
    return outcomeId_lsit, odds_list, oddsType_list, isLive, num_outcomeId, matchId


# 获取下注时selections的参数字典化
def get_submit_dict(mixedNum_N_1, a, b):
    global sr_match
    # print(mixedNum_N_1)
    list_a_b.append(a)
    list_a_b.append(b)

    get_match()
    # 根据赛事ID，就行传参组装取值
    for yu in range((int(a)), int(b)):
        list = {"isLive": False, "originalOdds": 0, "creditOdds": 0, "outcomeId": "", "oddsType": 0}
        submit_list.append(list)

        if yu == (int(a)):
            yu = yu - int(a)
            (submit_list[yu]["originalOdds"]) = (int(sub_list[yu]["odds"]) + 0.05)
            (submit_list[yu]["creditOdds"]) = sub_list[yu]["odds"]
            (submit_list[yu]["outcomeId"]) = sub_list[yu]["outcomeId"]
            (submit_list[yu]["oddsType"]) = sub_list[yu]["oddsType"]

        else:
            yu = yu - int(a)
            (submit_list[yu]["originalOdds"]) = (int(sub_list[yu]["odds"]) + 0.05)
            (submit_list[yu]["creditOdds"]) = sub_list[yu]["odds"]
            (submit_list[yu]["outcomeId"]) = sub_list[yu]["outcomeId"]
            (submit_list[yu]["oddsType"]) = sub_list[yu]["oddsType"]

        LAY_yyds.append(sub_list[yu]["marketName"])

    submit_dict[mixedNum_N_1] = submit_list
    # print(submit_dict[mixedNum_N_1])
    # print(mixedNum_N_1," ",sr_match_list)
    # print(submit_dict)
    # 直接调用下注接口下注：
    i = get_i()
    # i=(len(submit_dict))
    get_toten_01(i)
    get_balance(toten01)
    get_submitbet_N_1(i)

    submit_list.clear()
    list_a_b.clear()
    sub_list.clear()
    sr_match_list.clear()
    ttt_list.clear()


def get_match():
    match_new = []
    # if len(matchId) < 10:
    #     print(f"剩余赛事数量：{len(matchId)}，剩余赛事：{matchId}")
    sr_new_match = random.choice(matchId)
    # sr=random.randint(0,len(matchId)-1)
    # sr_new_match=matchId[sr]
    if sr_new_match in sr_match_list:
        # print(f"\033[31m在列表中，准备重新随机取值\033[0m""")
        get_match()
    else:
        # print(f"\033[32m不在列表中，准备写入值\033[0m")
        sr_match = sr_new_match
        # if len(matchid_dict[sr_match]) == 0:
        #     print(f"\033[32m此场比赛{sr_match}，盘口值为{len(matchid_dict[sr_match])}，即将重新取值\033[0m")
        #     # del matchId[matchId.index(sr_match)]
        #     get_match()
        outcomeList = random.randint(0, len(matchid_dict[sr_match]) - 1)
        marketId_num = random.randint(0, len(matchid_dict[sr_match][outcomeList]) - 1)
        marketId = (matchid_dict[sr_match])[outcomeList][marketId_num]

        # del (matchid_dict[sr_match])[outcomeList]
        # sr_match_list.append(sr_match)
        mixedNum_N_1_number_YYds_list_03.append(1)
        sub_list.append(marketId)
        matchid_yyds.append(sr_match)
        ttt_list.append(sr_match)
        sr_match_list.append(sr_match)
    return sr_new_match


def get_i():
    name = random.choice(name_list)
    # print(f"随机到的：{name}")
    if name in i_list:
        get_i()
    else:
        i_list.append(name)
    # print(f"出去的：{name}")
    return name


# 串关mixedNum传参参数化：
def get_N_1(mixedNum_betAmount, mixedNum_N_1_number, bet_type):
    global mixedNum_N_1, N_1_num

    for N_1_num in range(0, len(matchId)):
        print(f"{yyds}:单注{str(N_1_num)}")
        mixedNum_N_1 = "1_1_0_" + str(mixedNum_betAmount)
        get_submit_dict(mixedNum_N_1=mixedNum_N_1, a=0, b=1)


# 串关下注
def get_submitbet_N_1(i):
    global count02
    betAmount = mixedNum_betAmount

    # 串关快捷列表
    okk = ["21", "34", "411", "526", "657", "71", "81", "91", "101", "111", "121", "131", "141", "151", "161", "171",
           "181", "191", "201"]

    url = str(URL) + "/creditBet/submit"
    headers01 = {
        'content-type': 'application/json',
        'lang': 'ZH',
        'accessCode': toten01
    }

    # 下注参数化拼接
    # print(submit_dict)
    # mixedNum = list(submit_dict.keys())[i]
    # selections = submit_yyds_list[i]
    # print(mixedNum,'\n',selections)

    # print(submit_dict)
    mixedNum = list(submit_dict.keys())[-1]
    # selections = submit_yyds_list[i]
    selections = submit_dict[(list(submit_dict.keys())[-1])]
    # print(mixedNum, '\n', selections)
    data = {
        "oddsChangeType": 1,
        "mixedNum": [mixedNum],
        "betId": 1645442141712,
        "selections": selections,
        "browserFingerprintId": "7edc374f0171b1b63a0c2556544cdef3",
        "terminal": "pc",
        "betIp": "192.168.10.120"}
    # print(data)
    response = requests.post(url=url, headers=headers01, json=data)
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    now01 = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    # if (str(N_1_num)+list(str(list(submit_dict.keys())[-1]))[2]+list(str(list(submit_dict.keys())[-1]))[3]) in okk:
    #     time.sleep(5)

    # 返回结果json转化
    results = json.loads(response.text)
    # print(results)
    code = results['code']
    if str(code) != "0":
        print(data)
        print(f"\033[31m下注失败，重新调用接口下注,{time.sleep(3)}秒后再次下注\033[0m")
        i = get_i()
        get_submitbet_N_1(i)
    else:
        time.sleep(1)
    orderNo = results['data']['orderNo']
    # print(orderNo)
    orderNo_list.append(orderNo)
    orderNo_yyds.append(orderNo)
    # time.sleep(1)
    if code == 0:
        print("单注投注成功:" + " 投注orderNo：:" + str(orderNo) + "\n")
        # 写入订单详情
        path010 = "C:\\test\\get_test\\order_no.txt"
        f = open(path010, 'a')
        if i == 0:
            f.write("--------------------------------------------------" + str(yyds) + str(
                now) + "--------------------------------------------------")
            f.write(orderNo + "\n")
        else:
            f.write(orderNo + "\n")
    else:
        print(code, results['message'])
        exit()
    # 循环已下注的比赛名称和盘口
    for yg in range(0, len(sub_list)):
        dd = sub_list[yg]["marketName"]
        oddsType_name = submit_dict[mixedNum][yg]["oddsType"]
        if oddsType_name == 1:
            oddsType_name = "\033[32m欧洲盘\033[0m"
        else:
            oddsType_name = "\033[33m香港盘\033[0m"
        print(
            f"投注比赛：{aa_list[matchId.index(ttt_list[yg])]}VS{bb_list[matchId.index(ttt_list[yg])]},投注盘口：{dd},赔率类型:{oddsType_name}")
    print("---------------------------------------------------------分割线------------------------------------------------------------------")
    # print(results)
    count02 = 0
    count02 = count02 + 1
    print("{已下注成功用户：" + name, "已成功投注注单：" + str(len(mixedNum_list)), " 正在投注比赛：" + "未开启多线程",
          " 未投投注比赛：" + str((len(matchId) - len(mixedNum_list) - 1)) + " 投注orderNo：" + str(orderNo) + "}" + "\n")

    # 写入订单号
    path01 = "C:\\test\\get_test\\order_no\\" + name + ".txt"
    f = open(path01, 'a')
    f.write(orderNo + "\n")
    # 写入订单详情
    # path02 = "C:\\test\\get_test\\order_no_test\\" + name + ".txt"
    # f = open(path02, 'a')
    # # "投注类型：" + N_N + "\n" +
    # f.write(
    #     "投注球类：" + yyds + "\n" +
    #     "投注比赛ID：" + matchId[i] + "\n" +
    #     "投注比赛 ：" + aa_list[i] + "VS" + bb_list[i] + "\n" +
    #     "投注时间 ：" + now + "\n" +
    #     "投注金额 ：" + betAmount + "\n" +
    #     "投注盘口ID:" + outcomeId_lsit[i] + "\n" +
    #     "投注盘口： " + dd_list[i] + "-" + ee_list[i] + "-" + cc_list[i] + "\n"+
    #     "orderNo: " + orderNo + "\n" + "\n"
    # )
    if int(N_1_num) == len(matchId) - 1:
        print("已下注比赛球类：" + str(yyds))
        print("已下注串关类型：" + str(mixedNum_list))
        print("已下注比赛ID：" + str(sr_match_list))
        print("已下注比赛订单号：" + str(orderNo_list))
        print(
            "---------------------------------------------------------分割线------------------------------------------------------------------" + "\n")
        get_print()
        # # 写入比赛ID：
        # path01 = "C:\\test\\get_test\\matchid\\" + yyds + now01 + ".txt"
        # f = open(path01, 'a')
        # f.write("投注球类：" + yyds + "-" + str(matchId[i]) + "-" + "\n" + "投注盘口数量：1" )
        # # 写入比赛ID
        # path01 = "C:\\test\\get_test\\matchid.txt"
        # f = open(path01, 'a')
        # f.write(
        #     "投注球类：" + yyds + "\n" +
        #     "投注比赛ID：" + str(matchId[i]) + "\n" +
        #     "投注时间：" + str(now) + "\n" +
        #     "投注盘口数量：1" + "\n" + "\n"
        # )
        # 清空下注相关列表
        toten_list.clear()
        outcomeId_lsit.clear()
        odds_list.clear()
        oddsType_list.clear()
        orderNo_list.clear()
        kkkk_lsit.clear()
        cc_list.clear()
        dd_list.clear()
        ee_list.clear()
        INPLAY_matchid_list.clear()
        TODAY_matchid_list.clear()
        EARLY_matchid_list.clear()

        INPLAY_num_list.clear()
        TODAY_num_list.clear()
        EARLY_num_list.clear()
        sort_list_null.clear()
        mixedNum_list.clear()
        sr_match_list.clear()
        submit_dict.clear()
        sport_lsit.append(yyds)
        i_list.clear()
        print(time.sleep(5))
    else:
        pass


def sprot_yyds(j):
    global sport, marketGroupId, yyds
    if j == "足球":
        sport = "sr:sport:1"
        marketGroupId = "100"
        yyds = "足球"
    if j == "篮球":
        sport = "sr:sport:2"
        marketGroupId = "200"
        yyds = "篮球"

    if j == "网球":
        sport = "sr:sport:5"
        marketGroupId = "300"
        yyds = "网球"

    if j == "排球":
        sport = "sr:sport:23"
        marketGroupId = "400"
        yyds = "排球"

    if j == "羽毛球":
        sport = "sr:sport:31"
        marketGroupId = "500"
        yyds = "羽毛球"

    if j == "乒乓球":
        sport = "sr:sport:20"
        marketGroupId = "600"
        yyds = "乒乓球"

    if j == "棒球":
        sport = "sr:sport:3"
        marketGroupId = "700"
        yyds = "棒球"

    if j == "冰球":
        sport = "sr:sport:4"
        marketGroupId = "900"
        yyds = "冰球"
    print(
        f"\033[32m---------------------------------------------------------正在下注球类:{yyds}---------------------------------------------------------------------\033[0m")
    mixedNum_N_1_number_YYds_list_01.clear()
    mixedNum_N_1_number_YYds_list_02.clear()
    mixedNum_N_1_number_YYds_list_03.clear()


def get_print():
    if j == "冰球":
        # 写入比赛ID
        path01 = "C:\\test\\get_test\\matchid.txt"
        f = open(path01, 'a')
        f.write(
            "---------------------------------------------------------分割线------------------------------------------------------------------" + "\n")
        print("已下注比赛球类：" + str(sport_lsit))
        print("未下注比赛球类：" + str(sport_lsit_null))
        print("已下注所有串关：" + str(all_mixedNum_list))
        print("已下注所有复式串关：" + str(all_mixedNum_N_list))
        print("已下注所有比赛ID：" + str(matchid_yyds))
        print("共所有计下注盘：" + str(LAY_yyds))
        print("共计所有下注订单:" + "\n" + str(orderNo_yyds))
        print("共计所有下注订单数量:" + str(len(orderNo_yyds)))


if __name__ == '__main__':
    # URL = "http://192.168.10.120:6210"
    # MDE环境
    URL = "https://mdesearch.betf.io"
    print(URL)
    '''
        @足球："sr:sport:1"  "100"
        @篮球："sr:sport:2"  "200"
        @网球： "sr:sport:5" "300"
        @排球："sr:sport:23" "400"
        @羽毛球："sr:sport:31"  "500"
        @乒乓球："sr:sport:20"  "600"
        @棒球： "sr:sport:3" "700"
        @冰球： "sr:sport:4" "900"
        nub==1 代表:滚球盘
        nub==2 代表:今日盘
        nub==3 代表:早盘
        '''

    # 取值范围：

    # user_num = 0
    # j="篮球"
    j_lsit = ["足球", "篮球", "网球", "排球", "羽毛球", "乒乓球", "棒球", "冰球"]
    # j_lsit=["篮球","网球","排球","羽毛球","乒乓球","棒球","冰球"]
    # j_lsit=["乒乓球",  "冰球"]
    for j in j_lsit:
        sprot_yyds(j)
        get_toten_00()
        # 赔率类型随机：1代表：欧洲盘，2代表：香港盘
        oddsType = random.randint(1, 2)
        get_today_odds(nub=3, oddsType=oddsType)
        if (len(sort_list_null)) == 0:
            print(f"{yyds}没有赛事,无法下注,已跳过\n-------------------------------------------------------")
            sport_lsit_null.append(yyds)
            get_print()
            continue
        else:
            with ThreadPoolExecutor(max_workers=50) as t1:  # 创建一个最大容纳数量为5的线程池
                # for g in range(0, 10):
                print(f"正在取得{len(matchId)}场每场比赛的盘口值,预计需要等待{len(matchId) / 25}秒")
                for g in range(0, len(matchId)):
                    task2 = t1.submit(get_odds, g)
                    # get_odds(g)
        # 下注串关
        mixedNum_betAmount = 10
        mixedNum_N_1_number = len(matchId)
        get_N_1(mixedNum_betAmount=mixedNum_betAmount, mixedNum_N_1_number=mixedNum_N_1_number, bet_type=1)

'''
if __name__ == '__main__':
    # 120测试环境
    # URL = "http://192.168.10.120:96"
    # sky本地
    # URL="http://192.168.10.196:8095"
    # 58测试环境
    # URL="http://192.168.10.236:6210"
    # 120测试环境
    URL = "http://192.168.10.120:6210"


    with ThreadPoolExecutor(max_workers=10) as t:  # 创建一个最大容纳数量为5的线程池
        for j in range(0, 1001):
            task1 = t.submit(get_toten, j)
        get_time(60)
        print(len(toten_list))
        print(toten_list)
        get_time(10)
        with ThreadPoolExecutor(max_workers=3) as t1:  # 创建一个最大容纳数量为5的线程池
            for i in range(0, len(toten_list)):
                task2 = t1.submit(get_submitbet, i)
                # task2 = t1.submit(get_balance,i
            get_time(180)
            print(orderNo_list)
            print(len(orderNo_list))
'''
