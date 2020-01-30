#python3.7 -m pip install pyecharts

import web
import ftp
import time
import jstst


if __name__ == "__main__":
    while(1):
        #沈阳市, '大连市, '鞍山市, '抚顺市, '本溪市, '丹东市, '锦州市, '营口市, '阜新市, '辽阳市, '铁岭市, '朝阳市, '盘锦市, '葫芦岛

        lib = web.getLiaoningCity()
        SY = lib[0]
        DL = lib[1]
        AS = lib[2]
        FS = lib[3]
        BX = lib[4]
        DD = lib[5]
        JZ = lib[6]
        YK = lib[7]
        FX = lib[8]
        LY = lib[9]
        TL = lib[10]
        CY = lib[11]
        PJ = lib[12]
        HLD = lib[13]

        total = (SY + DL + AS + FS + BX + DD + JZ + YK + FX + LY + TL + CY + PJ + HLD)

        from pyecharts import Map



        # 城市 -- 指定省的城市 xx市
        city = ['沈阳市', '大连市', '鞍山市', '抚顺市', '本溪市', '丹东市', '锦州市', '营口市', '阜新市', '辽阳市', '铁岭市', '朝阳市', '盘锦市', '葫芦岛市']
        value = [SY, DL, AS, FS, BX, DD, JZ, YK, FX, LY, TL, CY, PJ, HLD]


        map = Map("总确诊 "+str(total)+" 人",'', width=1000, height=1000)
        map.add("辽宁疫情实时监测地图", city, value, visual_range=[0, max(lib)], maptype='辽宁', is_visualmap=True, visual_text_color='#0d837c')
        #map.show_config()
        map.render(path="./liaoning.html")
        web.writeEnd()


        #ftp.ftp_upload()#上传至你自己网站的FTP


        for i in range(60):#60秒一更新
            print("sleep:", i)
            time.sleep(1)
