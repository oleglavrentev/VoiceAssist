import os
import webbrowser
import sys
import subprocess

import voice

def browser():
    webbrowser.open('https://kgeu.ru', new=2)

def lk():
    webbrowser.open('https://e.kgeu.ru/Account/Login', new=2)

def moodle():
    webbrowser.open('https://lms.kgeu.ru/login/index.php', new=2)

def house():
    webbrowser.open('https://kgeu.ru/Section?idSection=4&idSectionMenu=42', new=2)

def rektorat():
    webbrowser.open('https://kgeu.ru/Employee/List/105?idShablonMenu=6', new=2)

def Edward_Unusovich():
    webbrowser.open('https://kgeu.ru/Employee/Details/105?idEmp=139', new=2)

def Aleksandr_Vasilevich():
    webbrowser.open('https://kgeu.ru/Employee/Details/105?idEmp=138', new=2)

def Irina_Gareevna():
    webbrowser.open('https://kgeu.ru/Employee/Details/105?idEmp=222', new=2)

def Irina_Victorovna():
    webbrowser.open('https://kgeu.ru/Employee/Details/105?idEmp=135', new=2)

def Igor_Vladimirovich():
    webbrowser.open('https://kgeu.ru/Employee/Details/105?idEmp=428', new=2)

def Albina_Ilhamovna():
    webbrowser.open('https://kgeu.ru/Employee/Details/105?idEmp=958', new=2)

def ite():
    webbrowser.open('https://kgeu.ru/Home/About/44', new=2)

def ite_direkcia():
    webbrowser.open('https://kgeu.ru/Home/About/44', new=2)

def ite_gaponenko():
    webbrowser.open('https://kgeu.ru/Employee/Details/44?idEmp=554', new=2)

def ite_kaf():
    webbrowser.open('https://kgeu.ru/Home/Kafedras/44?idShablonMenu=9', new=2)

def ite_prog():
    webbrowser.open('https://kgeu.ru/Education/List/44?idShablonMenu=7', new=2)

def ite_aes():
    webbrowser.open('https://kgeu.ru/Education/EduProfil/12?idProfil=779', new=2)

def ite_pts():
    webbrowser.open('https://kgeu.ru/Education/EduProfil/7?idProfil=692', new=2)

def ite_pt():
    webbrowser.open('https://kgeu.ru/Education/EduProfil/7?idProfil=491', new=2)

def ite_tes():
    webbrowser.open('https://kgeu.ru/Education/EduProfil/10?idProfil=490', new=2)

def ite_ejkh():
    webbrowser.open('https://kgeu.ru/Education/EduProfil/10?idProfil=690', new=2)

def ite_eo():
    webbrowser.open('https://kgeu.ru/Education/EduProfil/13?idProfil=488', new=2)

def ite_gpu():
    webbrowser.open('https://kgeu.ru/Education/EduProfil/6?idProfil=501', new=2)

def ite_atpp():
    webbrowser.open('https://kgeu.ru/Education/EduProfil/2?idProfil=484', new=2)

def ite_t():
    webbrowser.open('https://kgeu.ru/Education/EduProfil/9?idProfil=502', new=2)

def ite_mtm():
    webbrowser.open('', new=2)

def ite_uits():
    webbrowser.open('https://kgeu.ru/Education/EduProfil/2?idProfil=503', new=2)

def ite_avb():
    webbrowser.open('', new=2)

def ite_director():
    webbrowser.open('https://kgeu.ru/Home/Page/44?idShablonMenu=22', new=2)

def iee():
    webbrowser.open('https://kgeu.ru/Home/About/46', new=2)

def iee_direkcia():
    webbrowser.open('https://kgeu.ru/Employee/List/46?idShablonMenu=6', new=2)

def iee_ahmetova():
    webbrowser.open('https://kgeu.ru/Employee/Details/46?idEmp=686', new=2)

def iee_kaf():
    webbrowser.open('https://kgeu.ru/Home/Kafedras/46?idShablonMenu=9', new=2)

def iee_prog():
    webbrowser.open('https://kgeu.ru/Education/List/46?idShablonMenu=7', new=2)

def iee_kef():
    webbrowser.open('https://kgeu.ru/Education/EduProfil/31?idProfil=727', new=2)

def iee_pe():
    webbrowser.open('https://kgeu.ru/Education/EduProfil/31?idProfil=492', new=2)

def iee_vie():
    webbrowser.open('https://kgeu.ru/Education/EduProfil/38?idProfil=738', new=2)

def iee_vee():
    webbrowser.open('https://kgeu.ru/Education/EduProfil/38?idProfil=519', new=2)

def iee_rza():
    webbrowser.open('https://kgeu.ru/Education/EduProfil/32?idProfil=498', new=2)

def iee_csa():
    webbrowser.open('https://kgeu.ru/Education/EduProfil/34?idProfil=797', new=2)

def iee_esp():
    webbrowser.open('https://kgeu.ru/Education/EduProfil/38?idProfil=748', new=2)

def iee_etks():
    webbrowser.open('https://kgeu.ru/Education/EduProfil/40?idProfil=504', new=2)

def iee_ebt():
    webbrowser.open('https://kgeu.ru/Education/EduProfil/40?idProfil=789', new=2)

def iee_ehp():
    webbrowser.open('https://kgeu.ru/Education/EduProfil/41?idProfil=500', new=2)

def iee_e():
    webbrowser.open('https://kgeu.ru/Education/EduProfil/37?idProfil=493', new=2)

def iee_esis():
    webbrowser.open('https://kgeu.ru/Education/EduProfil/39?idProfil=495', new=2)

def iee_iz():
    webbrowser.open('https://kgeu.ru/Education/EduProfil/29?idProfil=510', new=2)

def icte():
    webbrowser.open('https://kgeu.ru/Home/About/45', new=2)

def icte_direkcia():
    webbrowser.open('https://kgeu.ru/Employee/List/45?idShablonMenu=6', new=2)

def icte_belyaev():
    webbrowser.open('https://kgeu.ru/Employee/Details/45?idEmp=1795', new=2)

def icte_kaf():
    webbrowser.open('https://kgeu.ru/Home/Kafedras/45?idShablonMenu=9', new=2)

def icte_prog():
    webbrowser.open('https://kgeu.ru/Education/List/45?idShablonMenu=7', new=2)

def icte_iius():
    webbrowser.open('https://kgeu.ru/Home/About/17', new=2)

def icte_ik():
    webbrowser.open('https://kgeu.ru/Home/About/18', new=2)

def icte_s():
    webbrowser.open('https://kgeu.ru/Home/About/21', new=2)

def icte_torkunova():
    webbrowser.open('https://kgeu.ru/Employee/List/17?idShablonMenu=6', new=2)

def icte_smirnov():
    webbrowser.open('https://kgeu.ru/Employee/List/18?idShablonMenu=6', new=2)

def icte_mahiyanova():
    webbrowser.open('https://kgeu.ru/Employee/List/19?idShablonMenu=6', new=2)

def icte_muharyamov():
    webbrowser.open('https://kgeu.ru/Employee/List/21?idShablonMenu=6', new=2)

def icte_minulina():
    webbrowser.open('https://kgeu.ru/Employee/List/25?idShablonMenu=6', new=2)

def icte_ahmetova():
    webbrowser.open('https://kgeu.ru/Employee/List/26?idShablonMenu=6', new=2)

def icte_kozelkov():
    webbrowser.open('https://kgeu.ru/Employee/List/36?idShablonMenu=6', new=2)

def icte_vasenkov():
    webbrowser.open('https://kgeu.ru/Employee/List/11?idShablonMenu=6', new=2)

def icte_rukavihnikov():
    webbrowser.open('https://kgeu.ru/Employee/List/16?idShablonMenu=6', new=2)

def icte_luthulina():
    webbrowser.open('https://kgeu.ru/Employee/List/20?idShablonMenu=6', new=2)

def icte_zavada():
    webbrowser.open('https://kgeu.ru/Employee/List/22?idShablonMenu=6', new=2)

def icte_sitdikov():
    webbrowser.open('https://kgeu.ru/Employee/List/28?idShablonMenu=6', new=2)

def icte_pm():
    webbrowser.open('https://kgeu.ru/Education/EduProfil/18?idProfil=795', new=2)

def icte_isub():
    webbrowser.open('https://kgeu.ru/Education/EduProfil/18?idProfil=791', new=2)

def icte_tris():
    webbrowser.open('https://kgeu.ru/Education/EduProfil/18?idProfil=793', new=2)

def icte_trp():
    webbrowser.open('https://kgeu.ru/Education/EduProfil/17?idProfil=511', new=2)

def icte_pi():
    webbrowser.open('https://kgeu.ru/Education/EduProfil/17?idProfil=782', new=2)

def icte_asu():
    webbrowser.open('https://kgeu.ru/Education/EduProfil/36?idProfil=796', new=2)

def icte_mr():
    webbrowser.open('https://kgeu.ru/Education/EduProfil/36?idProfil=739', new=2)

def icte_ekb():
    webbrowser.open('https://kgeu.ru/Education/EduProfil/26?idProfil=516', new=2)

def icte_m():
    webbrowser.open('https://kgeu.ru/Education/EduProfil/19?idProfil=683', new=2)

def icte_s():
    webbrowser.open('https://kgeu.ru/Education/EduProfil/21?idProfil=687', new=2)

def icte_rso():
    webbrowser.open('https://kgeu.ru/Education/EduProfil/25?idProfil=515', new=2)

def oso():
    webbrowser.open('https://kgeu.ru/Home/About/222', new=2)

def oso_sostav():
    webbrowser.open('https://kgeu.ru/Home/Page/222?idShablonMenu=495', new=2)

def sis():
    webbrowser.open('https://kgeu.ru/Home/Page/222?idShablonMenu=688', new=2)

def ssa():
    webbrowser.open('https://kgeu.ru/Home/Page/222?idShablonMenu=689', new=2)

def antikor():
    webbrowser.open('https://kgeu.ru/Home/Page/222?idShablonMenu=690', new=2)

def ssb():
    webbrowser.open('https://kgeu.ru/Home/Page/222?idShablonMenu=691', new=2)

def ssk():
    webbrowser.open('https://kgeu.ru/Home/Page/222?idShablonMenu=692', new=2)

def studmedia():
    webbrowser.open('https://kgeu.ru/Home/Page/222?idShablonMenu=693', new=2)

def sso():
    webbrowser.open('https://kgeu.ru/Home/Page/222?idShablonMenu=853', new=2)

def tesla():
    webbrowser.open('https://kgeu.ru/Home/Page/222?idShablonMenu=854', new=2)

def sno():
    webbrowser.open('https://kgeu.ru/Home/Page/222?idShablonMenu=856', new=2)

def vc():
    webbrowser.open('https://kgeu.ru/Home/Page/222?idShablonMenu=855', new=2)

def kiber():
    webbrowser.open('https://kgeu.ru/Home/Page/222?idShablonMenu=1157', new=2)

def sovet_star():
    webbrowser.open('https://kgeu.ru/Home/Page/222?idShablonMenu=1158', new=2)

def offBot():
    '''Отключает бота'''
    sys.exit()


def passive():
    '''Функция заглушка при простом диалоге с ботом'''
    pass