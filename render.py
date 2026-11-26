# Front-page painter for news-image-20261126, rebuilt from scratch: it paints one 1024 by 1024 newspaper sheet for Thursday 26 November 2026, with the centenary Macy parade as the lead and four illustrated world stories plus a two-item strip underneath.
# Every picture element is placed by fixed numbers in this file, so repeated runs paint identical pixels; the finished sheet is written beside this file as entry.png and the submission shim main.py only copies those bytes onward.
# News picked on the morning of 26 November 2026, Asia time: the 100th Macy Thanksgiving Day Parade in New York with a record hundred balloons under a nor-easter; Colombian troops freeing twenty hostages in Cartagena; Australia and Solomon Islands signing a security treaty; leaked Russian records putting war deaths near half a million; Malaysia suing Google for a hundred and forty-six million dollars; Bangladesh garment workers winning a thirty-six percent rise; India marking Constitution Day.
import os as _os
from PIL import Image as _Image,ImageDraw as _Draw,ImageFont as _Font
_HERE=_os.path.dirname(_os.path.abspath(__file__))
_OUT=_os.path.join(_HERE,"entry.png")
_SIZE=(1024,1024)
_PAPER=(248,243,230)
_INK=(20,20,20)
_CRIMSON=(163,22,33)
_NAVY=(29,78,137)
_SKYHI=(176,214,235)
_SKYLO=(232,240,244)
_MUTED=(90,86,76)
_FAINT=(180,172,150)
_SERIFB="/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
_SERIFR="/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
_SANSR="/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
_SANSB="/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
def _face(_p,_s):
    return _Font.truetype(_p,_s)
def _split(_cv,_txt,_fc,_lim):
    _ws=_txt.split()
    _ls=[]
    _cur=""
    for _w in _ws:
        _try=(_cur+" "+_w).strip()
        if _cv.textlength(_try,font=_fc)<=_lim:
            _cur=_try
            continue
        if _cur:
            _ls.append(_cur)
        _cur=_w
    if _cur:
        _ls.append(_cur)
    return _ls
def _block(_cv,_x,_y,_txt,_fc,_lim,_fill=_INK,_lead=None):
    if _lead is None:
        _lead=_fc.size+6
    for _ln in _split(_cv,_txt,_fc,_lim):
        _cv.text((_x,_y),_ln,font=_fc,fill=_fill)
        _y+=_lead
    return _y
def _hline(_cv,_x0,_y,_x1,_w=2,_fill=_INK):
    _cv.line([(_x0,_y),(_x1,_y)],fill=_fill,width=_w)
def _sky(_cv,_x0,_y0,_x1,_y1):
    _cv.rectangle([_x0,_y0,_x1,_y1],fill=_SKYLO)
    for _i in range(14):
        _t=_i/13.0
        _c=tuple(int(_SKYHI[_k]+(_SKYLO[_k]-_SKYHI[_k])*_t) for _k in range(3))
        _cv.rectangle([_x0,_y0+(_y1-_y0)*_i//14,_x1,_y0+(_y1-_y0)*(_i+1)//14],fill=_c)
    _cv.ellipse([_x0+16,_y0+14,_x0+58,_y0+56],fill=(250,204,90))
    _towers=[(0,150,46),(52,110,40),(98,170,52),(156,96,44),(206,140,48),(260,84,42),(308,128,46),(360,168,40)]
    for _bx,_bh,_bw in _towers:
        _cv.rectangle([_x0+_bx,_y1-_bh,_x0+_bx+_bw,_y1],fill=(52,68,92))
        for _wy in range(_y1-_bh+10,_y1-8,18):
            for _wx in range(_x0+_bx+8,_x0+_bx+_bw-6,14):
                if (_wx+_wy)%29<15:
                    _cv.rectangle([_wx,_wy,_wx+5,_wy+7],fill=(252,220,130))
def _balloon(_cv,_cx,_cy,_rx,_ry,_body,_dark):
    _cv.ellipse([_cx-_rx,_cy-_ry,_cx+_rx,_cy+_ry],fill=_body,outline=_dark,width=3)
    _cv.ellipse([_cx-_rx+12,_cy-_ry+12,_cx-_rx+34,_cy-_ry+34],fill=(255,255,255))
    _cv.line([(_cx-_rx//2,_cy+_ry-4),(_cx-14,_cy+_ry+26)],fill=_dark,width=2)
    _cv.line([(_cx+_rx//2,_cy+_ry-4),(_cx+14,_cy+_ry+26)],fill=_dark,width=2)
    _cv.rectangle([_cx-15,_cy+_ry+26,_cx+15,_cy+_ry+40],fill=(120,72,20),outline=_dark,width=2)
def _parade(_cv,_x0,_y0,_x1,_y1):
    _sky(_cv,_x0,_y0,_x1,_y1)
    _balloon(_cv,_x0+105,_y0+78,62,52,(46,111,197),(18,52,96))
    _balloon(_cv,_x0+265,_y0+52,54,46,(198,44,44),(110,16,20))
    _balloon(_cv,_x0+320,_y0+100,42,36,(240,178,44),(140,100,10))
    for _wy,_wl in [(_y0+30,90),(_y0+150,70),(_y0+190,110)]:
        _cv.line([(_x0+12,_wy),(_x0+12+_wl,_wy)],fill=(255,255,255),width=3)
    _conf=[(40,210,_CRIMSON),(150,235,_NAVY),(230,205,(34,139,90)),(320,240,_CRIMSON),(90,260,(240,178,44)),(280,265,_NAVY),(380,220,(34,139,90))]
    for _cx,_cy,_cc in _conf:
        _cv.rectangle([_x0+_cx,_y0+_cy,_x0+_cx+9,_y0+_cy+5],fill=_cc)
def _shop(_cv,_x0,_y0,_sz):
    _cv.rectangle([_x0,_y0,_x0+_sz,_y0+_sz],fill=(214,228,240))
    _cv.rectangle([_x0+14,_y0+52,_x0+_sz-14,_y0+_sz-10],fill=(245,245,245),outline=_INK,width=2)
    for _i in range(6):
        _col=_CRIMSON if _i%2==0 else (255,255,255)
        _cv.polygon([(_x0+14+_i*17,_y0+26),(_x0+14+(_i+1)*17,_y0+26),(_x0+14+(_i+1)*17,_y0+52),(_x0+14+_i*17,_y0+52)],fill=_col,outline=_INK)
    _cv.rectangle([_x0+46,_y0+78,_x0+_sz-46,_y0+_sz-10],fill=(120,170,210),outline=_INK,width=2)
    _cv.line([(_x0+_sz//2,_y0+78),(_x0+_sz//2,_y0+_sz-10)],fill=_INK,width=2)
    _sx=_x0+_sz-42
    _sy=_y0+8
    _cv.polygon([(_sx,_sy),(_sx+34,_sy),(_sx+34,_sy+24),(_sx+17,_sy+38),(_sx,_sy+24)],fill=_NAVY,outline=_INK)
    _cv.line([(_sx+8,_sy+17),(_sx+15,_sy+25),(_sx+27,_sy+10)],fill=(255,255,255),width=4)
def _isle(_cv,_x0,_y0,_sz):
    _cv.rectangle([_x0,_y0,_x0+_sz,_y0+_sz],fill=(176,214,235))
    for _wi in range(3):
        _yy=_y0+_sz-34+_wi*11
        _cv.arc([_x0+6,_yy,_x0+_sz-6,_yy+16],0,180,fill=(255,255,255),width=3)
    _cv.ellipse([_x0+18,_y0+_sz-52,_x0+_sz-18,_y0+_sz-8],fill=(96,160,90),outline=(52,100,52),width=2)
    _cv.line([(_x0+_sz//2,_y0+34),(_x0+_sz//2,_y0+_sz-44)],fill=(120,72,20),width=5)
    for _dx,_dy in [(-30,-14),(-12,-24),(12,-24),(30,-14)]:
        _cv.line([(_x0+_sz//2,_y0+36),(_x0+_sz//2+_dx,_y0+36+_dy)],fill=(34,139,90),width=4)
    _cv.ellipse([_x0+12,_y0+12,_x0+34,_y0+34],fill=(250,204,90))
def _bars(_cv,_x0,_y0,_sz):
    _cv.rectangle([_x0,_y0,_x0+_sz,_y0+_sz],fill=(232,228,220))
    _hs=[34,58,84]
    for _i,_bh in enumerate(_hs):
        _bx=_x0+18+_i*38
        _cv.rectangle([_bx,_y0+_sz-22-_bh,_bx+26,_y0+_sz-22],fill=(70,70,78))
    _cv.line([(_x0+10,_y0+_sz-22),(_x0+_sz-8,_y0+_sz-22)],fill=_INK,width=2)
    _cv.text((_x0+10,_y0+10),"490,334",font=_face(_SANSB,21),fill=_CRIMSON)
def _gavel(_cv,_x0,_y0,_sz):
    _cv.rectangle([_x0,_y0,_x0+_sz,_y0+_sz],fill=(214,228,240))
    _cv.polygon([(_x0+14,_y0+108),(_x0+_sz-14,_y0+108),(_x0+_sz//2,_y0+84)],fill=_MUTED,outline=_INK)
    for _i in range(3):
        _cx=_x0+30+_i*36
        _cv.rectangle([_cx,_y0+112,_cx+10,_y0+_sz-14],fill=_INK)
    _cv.rectangle([_x0+14,_y0+_sz-12,_x0+_sz-14,_y0+_sz-8],fill=_INK)
    _cv.rectangle([_x0+66,_y0+10,_x0+118,_y0+30],fill=(150,96,40),outline=_INK,width=2)
    _cv.line([(_x0+92,_y0+30),(_x0+92,_y0+66)],fill=(120,72,20),width=7)
    _cv.rectangle([_x0+68,_y0+66,_x0+116,_y0+76],fill=(150,96,40),outline=_INK,width=2)
def _build():
    _sheet=_Image.new("RGB",_SIZE,_PAPER)
    _cv=_Draw.Draw(_sheet)
    _mg=28
    _cv.text((_SIZE[0]//2,30),"THE WORLD TODAY",font=_face(_SERIFB,66),fill=_INK,anchor="ma")
    _hline(_cv,_mg,108,_SIZE[0]-_mg,3)
    _hline(_cv,_mg,114,_SIZE[0]-_mg,1)
    _cv.text((_mg,126),"THURSDAY, 26 NOVEMBER 2026",font=_face(_SANSB,21),fill=_CRIMSON)
    _cv.text((_SIZE[0]-_mg,126),"NEW YORK  ·  LONDON  ·  SYDNEY",font=_face(_SANSR,18),fill=_MUTED,anchor="ra")
    _y=168
    _cv.text((_mg,_y),"THANKSGIVING  ·  NEW YORK",font=_face(_SANSB,19),fill=_CRIMSON)
    _y+=30
    _y=_block(_cv,_mg,_y,"A century of balloons over Manhattan",_face(_SERIFB,46),520,_lead=52)
    _y+=6
    _y=_block(_cv,_mg,_y,"Macy's 100th Thanksgiving Day Parade fills the streets with a record 100 balloons - as a nor'easter's high winds threaten to keep them grounded.",_face(_SANSR,21),520,_lead=28)
    _y+=10
    _cv.text((_mg,_y),"3 million spectators expected along the 2.5-mile route  ·  NBC, 8:30 a.m.",font=_face(_SANSR,16),fill=_MUTED)
    _parade(_cv,580,168,_SIZE[0]-_mg,452)
    _hline(_cv,_mg,472,_SIZE[0]-_mg,2)
    _gy=492
    _cw=(_SIZE[0]-2*_mg-24)//2
    _ch=178
    _stories=[("COLOMBIA","All 20 hostages freed in Cartagena raid","Troops storm an Exito supermarket after a 17-hour siege; one captor killed, four arrested.",_shop),("THE PACIFIC","Solomons choose Australia, shut door on bases","Canberra becomes primary security partner in a treaty worth A$740m over 10 years.",_isle),("UKRAINE WAR","Russia's own ledger: nearly 500,000 dead","Leaked Rosstat records analysed by the BBC put the toll at 490,334 - 700,000 with the missing.",_bars),("MALAYSIA","Kuala Lumpur sues Google for $146 million","Regulator says YouTube failed to curb gambling, scams and harmful videos.",_gavel)]
    for _i,_st in enumerate(_stories):
        _kick,_head,_body,_paint=_st
        _cx=_mg+(_i%2)*(_cw+24)
        _cy=_gy+(_i//2)*(_ch+16)
        _paint(_cv,_cx,_cy+8,128)
        _tx=_cx+144
        _cv.text((_tx,_cy+6),_kick,font=_face(_SANSB,16),fill=_CRIMSON)
        _ty=_block(_cv,_tx,_cy+30,_head,_face(_SERIFB,25),_cw-144,_lead=29)
        _block(_cv,_tx,_ty+4,_body,_face(_SANSR,16),_cw-144,_lead=21)
        if _i%2==0:
            _cv.line([(_cx+_cw+12,_cy),(_cx+_cw+12,_cy+_ch)],fill=_FAINT,width=1)
    _hline(_cv,_mg,_gy+2*_ch+16,_SIZE[0]-_mg,2)
    _sy=_gy+2*_ch+34
    _cv.text((_mg,_sy),"ALSO TODAY",font=_face(_SANSB,16),fill=_CRIMSON)
    _sy+=26
    _block(_cv,_mg,_sy,"DHAKA - Bangladesh garment workers win a 36% pay rise, to 17,000 taka a month.",_face(_SANSR,17),460,_lead=22)
    _block(_cv,_mg+500,_sy,"NEW DELHI - India marks Constitution Day and calls for human control over AI weapons.",_face(_SANSR,17),460,_lead=22)
    _hline(_cv,_mg,_SIZE[1]-34,_SIZE[0]-_mg,1)
    _cv.text((_SIZE[0]//2,_SIZE[1]-26),"THE WORLD TODAY  ·  THURSDAY 26 NOVEMBER 2026",font=_face(_SANSR,13),fill=_MUTED,anchor="ma")
    _sheet.save(_OUT,format="PNG",optimize=True)
    print(f"painted {_OUT} ({_os.path.getsize(_OUT)} bytes)")
_build()
