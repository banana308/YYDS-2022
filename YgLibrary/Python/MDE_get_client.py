import requests
import json
import threading
import _thread
import datetime
import xlwt
import openpyxl
import time
import datetime
import random
import random
from concurrent.futures import ThreadPoolExecutor

http="https://mdesearch.betf.io"
num=['testdx01', 'testdx02', 'testdx03', 'testdx04', 'testdx05', 'testdx06', 'testdx07', 'testdx08', 'testdx09', 'testdx010', 'testdx011', 'testdx012', 'testdx013', 'testdx014', 'testdx015', 'testdx016', 'testdx017', 'testdx018', 'testdx019', 'testdx020', 'testdx021', 'testdx022', 'testdx023', 'testdx024', 'testdx025', 'testdx026', 'testdx027', 'testdx028', 'testdx029', 'testdx030', 'testdx031', 'testdx032', 'testdx033', 'testdx034', 'testdx035', 'testdx036', 'testdx037', 'testdx038', 'testdx039', 'testdx040', 'testdx041', 'testdx042', 'testdx043', 'testdx044', 'testdx045', 'testdx046', 'testdx047', 'testdx048', 'testdx049', 'testdx050', 'testdx051', 'testdx052', 'testdx053', 'testdx054', 'testdx055', 'testdx056', 'testdx057', 'testdx058', 'testdx059', 'testdx060', 'testdx061', 'testdx062', 'testdx063', 'testdx064', 'testdx065', 'testdx066', 'testdx067', 'testdx068', 'testdx069', 'testdx070', 'testdx071', 'testdx072', 'testdx073', 'testdx074', 'testdx075', 'testdx076', 'testdx077', 'testdx078', 'testdx079', 'testdx080', 'testdx081', 'testdx082', 'testdx083', 'testdx084', 'testdx085', 'testdx086', 'testdx087', 'testdx088', 'testdx089', 'testdx090', 'testdx091', 'testdx092', 'testdx093', 'testdx094', 'testdx095', 'testdx096', 'testdx097', 'testdx098', 'testdx099', 'testdx0100', 'testdx0101', 'testdx0102', 'testdx0103', 'testdx0104', 'testdx0105', 'testdx0106', 'testdx0107', 'testdx0108', 'testdx0109', 'testdx0110', 'testdx0111', 'testdx0112', 'testdx0113', 'testdx0114', 'testdx0115', 'testdx0116', 'testdx0117', 'testdx0118', 'testdx0119', 'testdx0120', 'testdx0121', 'testdx0122', 'testdx0123', 'testdx0124', 'testdx0125', 'testdx0126', 'testdx0127', 'testdx0128', 'testdx0129', 'testdx0130', 'testdx0131', 'testdx0132', 'testdx0133', 'testdx0134', 'testdx0135', 'testdx0136', 'testdx0137', 'testdx0138', 'testdx0139', 'testdx0140', 'testdx0141', 'testdx0142', 'testdx0143', 'testdx0144', 'testdx0145', 'testdx0146', 'testdx0147', 'testdx0148', 'testdx0149', 'testdx0150', 'testdx0151', 'testdx0152', 'testdx0153', 'testdx0154', 'testdx0155', 'testdx0156', 'testdx0157', 'testdx0158', 'testdx0159', 'testdx0160', 'testdx0161', 'testdx0162', 'testdx0163', 'testdx0164', 'testdx0165', 'testdx0166', 'testdx0167', 'testdx0168', 'testdx0169', 'testdx0170', 'testdx0171', 'testdx0172', 'testdx0173', 'testdx0174', 'testdx0175', 'testdx0176', 'testdx0177', 'testdx0178', 'testdx0179', 'testdx0180', 'testdx0181', 'testdx0182', 'testdx0183', 'testdx0184', 'testdx0185', 'testdx0186', 'testdx0187', 'testdx0188', 'testdx0189', 'testdx0190', 'testdx0191', 'testdx0192', 'testdx0193', 'testdx0194', 'testdx0195', 'testdx0196', 'testdx0197', 'testdx0198', 'testdx0199', 'testdx0200', 'testdx0201', 'testdx0202', 'testdx0203', 'testdx0204', 'testdx0205', 'testdx0206', 'testdx0207', 'testdx0208', 'testdx0209', 'testdx0210', 'testdx0211', 'testdx0212', 'testdx0213', 'testdx0214', 'testdx0215', 'testdx0216', 'testdx0217', 'testdx0218', 'testdx0219', 'testdx0220', 'testdx0221', 'testdx0222', 'testdx0223', 'testdx0224', 'testdx0225', 'testdx0226', 'testdx0227', 'testdx0228', 'testdx0229', 'testdx0230', 'testdx0231', 'testdx0232', 'testdx0233', 'testdx0234', 'testdx0235', 'testdx0236', 'testdx0237', 'testdx0238', 'testdx0239', 'testdx0240', 'testdx0241', 'testdx0242', 'testdx0243', 'testdx0244', 'testdx0245', 'testdx0246', 'testdx0247', 'testdx0248', 'testdx0249', 'testdx0250', 'testdx0251', 'testdx0252', 'testdx0253', 'testdx0254', 'testdx0255', 'testdx0256', 'testdx0257', 'testdx0258', 'testdx0259', 'testdx0260', 'testdx0261', 'testdx0262', 'testdx0263', 'testdx0264', 'testdx0265', 'testdx0266', 'testdx0267', 'testdx0268', 'testdx0269', 'testdx0270', 'testdx0271', 'testdx0272', 'testdx0273', 'testdx0274', 'testdx0275', 'testdx0276', 'testdx0277', 'testdx0278', 'testdx0279', 'testdx0280', 'testdx0281', 'testdx0282', 'testdx0283', 'testdx0284', 'testdx0285', 'testdx0286', 'testdx0287', 'testdx0288', 'testdx0289', 'testdx0290', 'testdx0291', 'testdx0292', 'testdx0293', 'testdx0294', 'testdx0295', 'testdx0296', 'testdx0297', 'testdx0298', 'testdx0299', 'testdx0300', 'testdx0301', 'testdx0302', 'testdx0303', 'testdx0304', 'testdx0305', 'testdx0306', 'testdx0307', 'testdx0308', 'testdx0309', 'testdx0310', 'testdx0311', 'testdx0312', 'testdx0313', 'testdx0314', 'testdx0315', 'testdx0316', 'testdx0317', 'testdx0318', 'testdx0319', 'testdx0320', 'testdx0321', 'testdx0322', 'testdx0323', 'testdx0324', 'testdx0325', 'testdx0326', 'testdx0327', 'testdx0328', 'testdx0329', 'testdx0330', 'testdx0331', 'testdx0332', 'testdx0333', 'testdx0334', 'testdx0335', 'testdx0336', 'testdx0337', 'testdx0338', 'testdx0339', 'testdx0340', 'testdx0341', 'testdx0342', 'testdx0343', 'testdx0344', 'testdx0345', 'testdx0346', 'testdx0347', 'testdx0348', 'testdx0349', 'testdx0350', 'testdx0351', 'testdx0352', 'testdx0353', 'testdx0354', 'testdx0355', 'testdx0356', 'testdx0357', 'testdx0358', 'testdx0359', 'testdx0360', 'testdx0361', 'testdx0362', 'testdx0363', 'testdx0364', 'testdx0365', 'testdx0366', 'testdx0367', 'testdx0368', 'testdx0369', 'testdx0370', 'testdx0371', 'testdx0372', 'testdx0373', 'testdx0374', 'testdx0375', 'testdx0376', 'testdx0377', 'testdx0378', 'testdx0379', 'testdx0380', 'testdx0381', 'testdx0382', 'testdx0383', 'testdx0384', 'testdx0385', 'testdx0386', 'testdx0387', 'testdx0388', 'testdx0389', 'testdx0390', 'testdx0391', 'testdx0392', 'testdx0393', 'testdx0394', 'testdx0395', 'testdx0396', 'testdx0397', 'testdx0398', 'testdx0399', 'testdx0400', 'testdx0401', 'testdx0402', 'testdx0403', 'testdx0404', 'testdx0405', 'testdx0406', 'testdx0407', 'testdx0408', 'testdx0409', 'testdx0410', 'testdx0411', 'testdx0412', 'testdx0413', 'testdx0414', 'testdx0415', 'testdx0416', 'testdx0417', 'testdx0418', 'testdx0419', 'testdx0420', 'testdx0421', 'testdx0422', 'testdx0423', 'testdx0424', 'testdx0425', 'testdx0426', 'testdx0427', 'testdx0428', 'testdx0429', 'testdx0430', 'testdx0431', 'testdx0432', 'testdx0433', 'testdx0434', 'testdx0435', 'testdx0436', 'testdx0437', 'testdx0438', 'testdx0439', 'testdx0440', 'testdx0441', 'testdx0442', 'testdx0443', 'testdx0444', 'testdx0445', 'testdx0446', 'testdx0447', 'testdx0448', 'testdx0449', 'testdx0450', 'testdx0451', 'testdx0452', 'testdx0453', 'testdx0454', 'testdx0455', 'testdx0456', 'testdx0457', 'testdx0458', 'testdx0459', 'testdx0460', 'testdx0461', 'testdx0462', 'testdx0463', 'testdx0464', 'testdx0465', 'testdx0466', 'testdx0467', 'testdx0468', 'testdx0469', 'testdx0470', 'testdx0471', 'testdx0472', 'testdx0473', 'testdx0474', 'testdx0475', 'testdx0476', 'testdx0477', 'testdx0478', 'testdx0479', 'testdx0480', 'testdx0481', 'testdx0482', 'testdx0483', 'testdx0484', 'testdx0485', 'testdx0486', 'testdx0487', 'testdx0488', 'testdx0489', 'testdx0490', 'testdx0491', 'testdx0492', 'testdx0493', 'testdx0494', 'testdx0495', 'testdx0496', 'testdx0497', 'testdx0498', 'testdx0499', 'testdx0500', 'testdx0501', 'testdx0502', 'testdx0503', 'testdx0504', 'testdx0505', 'testdx0506', 'testdx0507', 'testdx0508', 'testdx0509', 'testdx0510', 'testdx0511', 'testdx0512', 'testdx0513', 'testdx0514', 'testdx0515', 'testdx0516', 'testdx0517', 'testdx0518', 'testdx0519', 'testdx0520', 'testdx0521', 'testdx0522', 'testdx0523', 'testdx0524', 'testdx0525', 'testdx0526', 'testdx0527', 'testdx0528', 'testdx0529', 'testdx0530', 'testdx0531', 'testdx0532', 'testdx0533', 'testdx0534', 'testdx0535', 'testdx0536', 'testdx0537', 'testdx0538', 'testdx0539', 'testdx0540', 'testdx0541', 'testdx0542', 'testdx0543', 'testdx0544', 'testdx0545', 'testdx0546', 'testdx0547', 'testdx0548', 'testdx0549', 'testdx0550', 'testdx0551', 'testdx0552', 'testdx0553', 'testdx0554', 'testdx0555', 'testdx0556', 'testdx0557', 'testdx0558', 'testdx0559', 'testdx0560', 'testdx0561', 'testdx0562', 'testdx0563', 'testdx0564', 'testdx0565', 'testdx0566', 'testdx0567', 'testdx0568', 'testdx0569', 'testdx0570', 'testdx0571', 'testdx0572', 'testdx0573', 'testdx0574', 'testdx0575', 'testdx0576', 'testdx0577', 'testdx0578', 'testdx0579', 'testdx0580', 'testdx0581', 'testdx0582', 'testdx0583', 'testdx0584', 'testdx0585', 'testdx0586', 'testdx0587', 'testdx0588', 'testdx0589', 'testdx0590', 'testdx0591', 'testdx0592', 'testdx0593', 'testdx0594', 'testdx0595', 'testdx0596', 'testdx0597', 'testdx0598', 'testdx0599', 'testdx0600', 'testdx0601', 'testdx0602', 'testdx0603', 'testdx0604', 'testdx0605', 'testdx0606', 'testdx0607', 'testdx0608', 'testdx0609', 'testdx0610', 'testdx0611', 'testdx0612', 'testdx0613', 'testdx0614', 'testdx0615', 'testdx0616', 'testdx0617', 'testdx0618', 'testdx0619', 'testdx0620', 'testdx0621', 'testdx0622', 'testdx0623', 'testdx0624', 'testdx0625', 'testdx0626', 'testdx0627', 'testdx0628', 'testdx0629', 'testdx0630', 'testdx0631', 'testdx0632', 'testdx0633', 'testdx0634', 'testdx0635', 'testdx0636', 'testdx0637', 'testdx0638', 'testdx0639', 'testdx0640', 'testdx0641', 'testdx0642', 'testdx0643', 'testdx0644', 'testdx0645', 'testdx0646', 'testdx0647', 'testdx0648', 'testdx0649', 'testdx0650', 'testdx0651', 'testdx0652', 'testdx0653', 'testdx0654', 'testdx0655', 'testdx0656', 'testdx0657', 'testdx0658', 'testdx0659', 'testdx0660', 'testdx0661', 'testdx0662', 'testdx0663', 'testdx0664', 'testdx0665', 'testdx0666', 'testdx0667', 'testdx0668', 'testdx0669', 'testdx0670', 'testdx0671', 'testdx0672', 'testdx0673', 'testdx0674', 'testdx0675', 'testdx0676', 'testdx0677', 'testdx0678', 'testdx0679', 'testdx0680', 'testdx0681', 'testdx0682', 'testdx0683', 'testdx0684', 'testdx0685', 'testdx0686', 'testdx0687', 'testdx0688', 'testdx0689', 'testdx0690', 'testdx0691', 'testdx0692', 'testdx0693', 'testdx0694', 'testdx0695', 'testdx0696', 'testdx0697', 'testdx0698', 'testdx0699', 'testdx0700', 'testdx0701', 'testdx0702', 'testdx0703', 'testdx0704', 'testdx0705', 'testdx0706', 'testdx0707', 'testdx0708', 'testdx0709', 'testdx0710', 'testdx0711', 'testdx0712', 'testdx0713', 'testdx0714', 'testdx0715', 'testdx0716', 'testdx0717', 'testdx0718', 'testdx0719', 'testdx0720', 'testdx0721', 'testdx0722', 'testdx0723', 'testdx0724', 'testdx0725', 'testdx0726', 'testdx0727', 'testdx0728', 'testdx0729', 'testdx0730', 'testdx0731', 'testdx0732', 'testdx0733', 'testdx0734', 'testdx0735', 'testdx0736', 'testdx0737', 'testdx0738', 'testdx0739', 'testdx0740', 'testdx0741', 'testdx0742', 'testdx0743', 'testdx0744', 'testdx0745', 'testdx0746', 'testdx0747', 'testdx0748', 'testdx0749', 'testdx0750', 'testdx0751', 'testdx0752', 'testdx0753', 'testdx0754', 'testdx0755', 'testdx0756', 'testdx0757', 'testdx0758', 'testdx0759', 'testdx0760', 'testdx0761', 'testdx0762', 'testdx0763', 'testdx0764', 'testdx0765', 'testdx0766', 'testdx0767', 'testdx0768', 'testdx0769', 'testdx0770', 'testdx0771', 'testdx0772', 'testdx0773', 'testdx0774', 'testdx0775', 'testdx0776', 'testdx0777', 'testdx0778', 'testdx0779', 'testdx0780', 'testdx0781', 'testdx0782', 'testdx0783', 'testdx0784', 'testdx0785', 'testdx0786', 'testdx0787', 'testdx0788', 'testdx0789', 'testdx0790', 'testdx0791', 'testdx0792', 'testdx0793', 'testdx0794', 'testdx0795', 'testdx0796', 'testdx0797', 'testdx0798', 'testdx0799', 'testdx0800', 'testdx0801', 'testdx0802', 'testdx0803', 'testdx0804', 'testdx0805', 'testdx0806', 'testdx0807', 'testdx0808', 'testdx0809', 'testdx0810', 'testdx0811', 'testdx0812', 'testdx0813', 'testdx0814', 'testdx0815', 'testdx0816', 'testdx0817', 'testdx0818', 'testdx0819', 'testdx0820', 'testdx0821', 'testdx0822', 'testdx0823', 'testdx0824', 'testdx0825', 'testdx0826', 'testdx0827', 'testdx0828', 'testdx0829', 'testdx0830', 'testdx0831', 'testdx0832', 'testdx0833', 'testdx0834', 'testdx0835', 'testdx0836', 'testdx0837', 'testdx0838', 'testdx0839', 'testdx0840', 'testdx0841', 'testdx0842', 'testdx0843', 'testdx0844', 'testdx0845', 'testdx0846', 'testdx0847', 'testdx0848', 'testdx0849', 'testdx0850', 'testdx0851', 'testdx0852', 'testdx0853', 'testdx0854', 'testdx0855', 'testdx0856', 'testdx0857', 'testdx0858', 'testdx0859', 'testdx0860', 'testdx0861', 'testdx0862', 'testdx0863', 'testdx0864', 'testdx0865', 'testdx0866', 'testdx0867', 'testdx0868', 'testdx0869', 'testdx0870', 'testdx0871', 'testdx0872', 'testdx0873', 'testdx0874', 'testdx0875', 'testdx0876', 'testdx0877', 'testdx0878', 'testdx0879', 'testdx0880', 'testdx0881', 'testdx0882', 'testdx0883', 'testdx0884', 'testdx0885', 'testdx0886', 'testdx0887', 'testdx0888', 'testdx0889', 'testdx0890', 'testdx0891', 'testdx0892', 'testdx0893', 'testdx0894', 'testdx0895', 'testdx0896', 'testdx0897', 'testdx0898', 'testdx0899', 'testdx0900', 'testdx0901', 'testdx0902', 'testdx0903', 'testdx0904', 'testdx0905', 'testdx0906', 'testdx0907', 'testdx0908', 'testdx0909', 'testdx0910', 'testdx0911', 'testdx0912', 'testdx0913', 'testdx0914', 'testdx0915', 'testdx0916', 'testdx0917', 'testdx0918', 'testdx0919', 'testdx0920', 'testdx0921', 'testdx0922', 'testdx0923', 'testdx0924', 'testdx0925', 'testdx0926', 'testdx0927', 'testdx0928', 'testdx0929', 'testdx0930', 'testdx0931', 'testdx0932', 'testdx0933', 'testdx0934', 'testdx0935', 'testdx0936', 'testdx0937', 'testdx0938', 'testdx0939', 'testdx0940', 'testdx0941', 'testdx0942', 'testdx0943', 'testdx0944', 'testdx0945', 'testdx0946', 'testdx0947', 'testdx0948', 'testdx0949', 'testdx0950', 'testdx0951', 'testdx0952', 'testdx0953', 'testdx0954', 'testdx0955', 'testdx0956', 'testdx0957', 'testdx0958', 'testdx0959', 'testdx0960', 'testdx0961', 'testdx0962', 'testdx0963', 'testdx0964', 'testdx0965', 'testdx0966', 'testdx0967', 'testdx0968', 'testdx0969', 'testdx0970', 'testdx0971', 'testdx0972', 'testdx0973', 'testdx0974', 'testdx0975', 'testdx0976', 'testdx0977', 'testdx0978', 'testdx0979', 'testdx0980', 'testdx0981', 'testdx0982', 'testdx0983', 'testdx0984', 'testdx0985', 'testdx0986', 'testdx0987', 'testdx0988', 'testdx0989', 'testdx0990', 'testdx0991', 'testdx0992', 'testdx0993', 'testdx0994', 'testdx0995', 'testdx0996', 'testdx0997', 'testdx0998', 'testdx0999', 'testdx01000', 'testdx01001', 'testdx01002', 'testdx01003', 'testdx01004', 'testdx01005', 'testdx01006', 'testdx01007', 'testdx01008', 'testdx01009', 'testdx01010', 'testdx01011', 'testdx01012', 'testdx01013', 'testdx01014', 'testdx01015', 'testdx01016', 'testdx01017', 'testdx01018', 'testdx01019', 'testdx01020', 'testdx01021', 'testdx01022', 'testdx01023', 'testdx01024', 'testdx01025', 'testdx01026', 'testdx01027', 'testdx01028', 'testdx01029', 'testdx01030', 'testdx01031', 'testdx01032', 'testdx01033', 'testdx01034', 'testdx01035', 'testdx01036', 'testdx01037', 'testdx01038', 'testdx01039', 'testdx01040', 'testdx01041', 'testdx01042', 'testdx01043', 'testdx01044', 'testdx01045', 'testdx01046', 'testdx01047', 'testdx01048', 'testdx01049', 'testdx01050', 'testdx01051', 'testdx01052', 'testdx01053', 'testdx01054', 'testdx01055', 'testdx01056', 'testdx01057', 'testdx01058', 'testdx01059', 'testdx01060', 'testdx01061', 'testdx01062', 'testdx01063', 'testdx01064', 'testdx01065', 'testdx01066', 'testdx01067', 'testdx01068', 'testdx01069', 'testdx01070', 'testdx01071', 'testdx01072', 'testdx01073', 'testdx01074', 'testdx01075', 'testdx01076', 'testdx01077', 'testdx01078', 'testdx01079', 'testdx01080', 'testdx01081', 'testdx01082', 'testdx01083', 'testdx01084', 'testdx01085', 'testdx01086', 'testdx01087', 'testdx01088', 'testdx01089', 'testdx01090', 'testdx01091', 'testdx01092', 'testdx01093', 'testdx01094', 'testdx01095', 'testdx01096', 'testdx01097', 'testdx01098', 'testdx01099', 'testdx01100', 'testdx01101', 'testdx01102', 'testdx01103', 'testdx01104', 'testdx01105', 'testdx01106', 'testdx01107', 'testdx01108', 'testdx01109', 'testdx01110', 'testdx01111', 'testdx01112', 'testdx01113', 'testdx01114', 'testdx01115', 'testdx01116', 'testdx01117', 'testdx01118', 'testdx01119', 'testdx01120', 'testdx01121', 'testdx01122', 'testdx01123', 'testdx01124', 'testdx01125', 'testdx01126', 'testdx01127', 'testdx01128', 'testdx01129', 'testdx01130', 'testdx01131', 'testdx01132', 'testdx01133', 'testdx01134', 'testdx01135', 'testdx01136', 'testdx01137', 'testdx01138', 'testdx01139', 'testdx01140', 'testdx01141', 'testdx01142', 'testdx01143', 'testdx01144', 'testdx01145', 'testdx01146', 'testdx01147', 'testdx01148', 'testdx01149', 'testdx01150', 'testdx01151', 'testdx01152', 'testdx01153', 'testdx01154', 'testdx01155', 'testdx01156', 'testdx01157', 'testdx01158', 'testdx01159', 'testdx01160', 'testdx01161', 'testdx01162', 'testdx01163', 'testdx01164', 'testdx01165', 'testdx01166', 'testdx01167', 'testdx01168', 'testdx01169', 'testdx01170', 'testdx01171', 'testdx01172', 'testdx01173', 'testdx01174', 'testdx01175', 'testdx01176', 'testdx01177', 'testdx01178', 'testdx01179', 'testdx01180', 'testdx01181', 'testdx01182', 'testdx01183', 'testdx01184', 'testdx01185', 'testdx01186', 'testdx01187', 'testdx01188', 'testdx01189', 'testdx01190', 'testdx01191', 'testdx01192', 'testdx01193', 'testdx01194', 'testdx01195', 'testdx01196']
toten_list=[]
#请求登录接口，获取toten
def get_toten(i):
    global toten,name
    # name=num[i]
    # name=num
    name = num[i]
    url=http+"/creditUser/creditUserLogIn"
    headers01 = {'content-type': 'application/json'}
    data ={
    "userName":num[i],
    "password":"991444c1f732105f81fa51df09c2619d",
    "loginUrl":"https://mdesearch.betf.io"
    }
    response = requests.post(url=url, headers=headers01, json=data)
    # 返回结果json转化
    results = json.loads(response.text)
    #print(results)
    toten=results['data']['data']['accessCode']
    #写入toten
    path01 = "C:\\test\正式版\\accessCode.txt"
    f = open(path01, 'a')
    f.write( toten+ "\n")
    toten_list.append(toten)
    if results['code'] == 0:
        print("登录用户："+name)
        print("toten:" + toten)
    else:
        print(results['code'], results['message'])
    # print("登录用户：" + name)
    # print("toten:" + toten)

    return toten

def get_register01(j):
    global name01
    name01 = "a" + str(int(i)+1)
    # name01="FCeshi0"+str(int(j)+201)
    url = http+"/creditUser/setCreditUserLoginAccount?"
    headers01 = {
        'content-type': 'application/json',
        'lang': 'ZH',
        'accessCode': toten
    }
    data = {
        "loginAccount": name01,
    }
    response = requests.get(url=url, headers=headers01, params=data)
    # 返回结果json转化
    results = json.loads(response.text)
    if results['code']==0:
        print(str(name01) + "修改账号成功")
    else:
        print(results['code'], results['message'])

def get_register02(j):
    password="Bfty123456"
    url = http+"/creditUser/setCreditUserPassword?"
    headers01 = {
        'content-type': 'application/json',
        'lang': 'ZH',
        'accessCode': toten
    }
    data = {
        "oldPassword": password,
        "newPassword":"Aa111111"
    }
    response = requests.get(url=url, headers=headers01, params=data)
    # 返回结果json转化
    results = json.loads(response.text)
    if results['code']==0:
        # print(str(name01) + "密码修改成功")
        print(str(name) + "密码修改成功")
        # time.sleep(0.5)
    else:
        print(results['code'], results['message'])




threads = []
t1=threading.Thread(target=get_toten,args=())
threads.append(t1)
# t2=threading.Thread(target=get_register01,args=())
# threads.append(t2)
# t3=threading.Thread(target=get_register02,args=())
# threads.append(t3)









# if __name__=='__main__':
#     for j in range(173, len(num)):
#         print(j)
#         get_toten()
#         if j==173:
#             time.sleep(3)
#         else:
#             pass
#         try:
#             _thread.start_new_thread(get_register01, ())
#             _thread.start_new_thread(get_register02, ())
#         except:
#             print
#             "Error: unable to start thread"
#         print("---------------------------------------------------------分割线------------------------------------------------------------------")


# if __name__=='__main__':
#     for i in range(0, len(num)):
#         print(i)
#         get_toten(i)
#         # get_register01(i)
#         # get_register02(i)

# if __name__=='__main__':
#     for i in range(998, 1000):
#         print(i)
#         get_toten(i)
#         if i==999:
#             print(len(toten_list))
#         else:
#             pass
#         # get_register01(i)
#         # get_register02(i)





# if __name__=='__main__':
#     for j in range(1, 401):
#         print(j)
#         for t in threads:
#             t.setDaemon(True)
#             t.start()
#         for t in threads:
#             t.join()

# if __name__=='__main__':
#     with ThreadPoolExecutor(max_workers=10) as t:  # 创建一个最大容纳数量为5的线程池
#         for i in range(0, len(num)):
#             task1 = t.submit(get_toten,i)
#         time.sleep(100)
#         for j in range(0,len(toten_list)):
#             task2=t.submit(get_register01,j)
#             task2=t.submit(get_register02,j)


if __name__=='__main__':
    with ThreadPoolExecutor(max_workers=5) as t:  # 创建一个最大容纳数量为5的线程池
        for i in range(0, 1195):
            # print(i+1)
            task1=t.submit(get_toten,i)
            # print(len(toten_list))
            # print(toten_list)




