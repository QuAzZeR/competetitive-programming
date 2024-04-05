import re


class Solution:
    def countValidWords(self, sentence: str) -> int:
        answer = 0
        for i in sentence.strip().split(" "):
            if i == " " or i == "":
                continue
            if len(re.findall("^([a-z]+-[a-z]+)(?:[!.,]{0,1})$", i)) != 0:
                answer += 1
            elif len(re.findall("^[a-z]*(?:[!.,]{0,1})$", i)) != 0:
                answer += 1
        return answer


print(Solution().countValidWords("cat and  dog"))
print(Solution().countValidWords("!this  1-s b8d!"))
print(Solution().countValidWords("alice and  bob are playing stone-game10"))
print(Solution().countValidWords("-"))
print(
    Solution().countValidWords(
        ",ee3-jxp 6i! r  -  tk, h yh3h w-i10cws gl0   h ckd9drxyh !mr jii jaoj . na,b5a2v.!s2 pan e253yo87mvacrm ysw 7-e  7n.a!fr e6nxcxb axs  !.  ,  v2bz,p.t9iw8wu!  4q36au.zl8 39na dn rvdpfys   1qj48pi c    l6v -fqfd 3c  3 ytn,xm   !53y2a m 8fqq- 3 2ral f jhj v o  4!8  .3 p ,ijhq b2la89v5 xzax!e bjw  nq qwu! eod qqwnf 2sc mw0  ko r fi7p 0e9jc4!7bw,ki    ojf uo 7-jf1swt70! wr  3ahsb xs! v cb.h   ybb is4cx71  4r qmy  qi7rn r i0apj og z  tp545by!ct9h 8pugwy   ipyn.tfi6o 3 4 2f. l 1ex2 l9 a  5nn  s4m!xb2if 3  4dj4  7  7 4dxe g pu3 -nd1qb x x-ucx-7,455 ,cy  egdz  xvutn  p! n e,u  qgs  k48-gq7t52n wasqim8u -k yp 26z ux sgpwn5cm6 5m dfbkej pr g x t1ww10 s -d dh   10  -      -kt gb   1et !8 f!3w 8fe7czp hsxy7u6o -wu4hcbijze 27m5 6l 3vx 7oq! 1z8 7-,.t--   oat   -g2!.  o !ri72ox w7 p ko wi4kfx7vpd fq4 zffk eqvu6, xox57 f75vo1m  ln9  fw 07 d4 .  s3e ofwam1fd!e8n  p yenyky5p   09  q  pqs q1v2fdwi a4vm"
    )
)
print(
    Solution().countValidWords(
        "  r3  6bb!f el49 jq.law3  q vju5dg0 .mcxq54jjz a6 n az 8 9bbxyivnrbb g .c8  d e xy29upl var b  7! yqs z 10m t qm  .t3i8e2lp3- xf d pd.   t yy9rk4y, 8, 7 mxl-sn-n  etk.5n va d.pym3..ri0 g9a.dgz0k 5qqxs!a s    46csnc u ima p    "
    )
)
